# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = { #added wildcard as '*'
    '*':0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "Problem Set 3 Words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    
    #making all letters lowercase
    actual_word = word.lower()
    
    #first component of word score
    word_score_part_one = 0

    for letter in actual_word:

        #checking letter scores and adding them up
        letter_score = SCRABBLE_LETTER_VALUES.get(letter, 0)
        word_score_part_one += letter_score
        
    #second component of word score
    word_score_part_two = (7 * len(word) - 3 * (n-len(word))) 
    
    #checking if 1 is greater
    if word_score_part_two < 1:
        word_score_part_two = 1
    
    #final word score
    word_score = word_score_part_one * word_score_part_two

    return word_score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    hand_as_string = ""
    for letter in hand.keys():
        for j in range(hand[letter]):
            #  print(letter, end=' ') # print all on the same line
             hand_as_string = hand_as_string + letter + " " #modified to help with output
    print()                              # print an empty line

    return hand_as_string

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    hand["*"] = hand.get("*", 0) + 1

    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    #initializing variables
    word = word.lower()
    frequency_word = get_frequency_dict(word)
    new_hand = {} # creating new_hand so original hand isn't modified

    # checking letters against word, and adding letters to new_hand 
    for letter in hand.keys():
        
        # if letters overlap between hand and word, get difference and update new_hand
        if hand.get(letter, 0) >= frequency_word.get(letter, 0):
            new_hand[letter] = hand.get(letter) - frequency_word.get(letter,0)

        # if difference < 0, set difference to 0 and update new_hand
        elif hand.get(letter,0) < frequency_word.get(letter,0):
            new_hand[letter] = 0

        #if no overlap between hand and word, add letter in hand to new hand with no change
        else:
            new_hand[letter] = hand.get(letter,0)
    
    return new_hand


#checks word to see if its in word_list (with wildcards!)
def word_check_with_wildcard(word, word_list):
    """
    Returns True if word (and word if wildcard is replaced with any vowel) is in word list. Otherwise returns False

    word: string
    returns: boolean, whether a word (including ones made when replacing a vowel with '*') is valid or not
    """

    #initializing variables
    word = word.lower()
    word_valid = False
    possible_word_list = []

    #since string isn't mutable, change word to list of characters
    word_as_list = list(word)

    #checking for wildcard
    for index in range(len(word_as_list)):

        if word_as_list[index] == "*":

            #replace wildcard with vowel, then add to possible_word_list; repeat for every vowel
            for vowel in VOWELS:
                word_as_list[index] = vowel
                possible_word_list.append("".join(word_as_list))

    #if word has no wildcards, add to possible_word_list anyway
    if "*" not in word_as_list:
        possible_word_list.append(word)

    #checking if possible words are valid (only one validity is needed for word to be valid)*
    for possible_word in possible_word_list:
        if possible_word in word_list:
            word_valid = True
            break

    return word_valid
            
#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    
    #initializing variables
    validity = True

    #getting word
    word = word.lower()
    frequency_word = get_frequency_dict(word)

    #check if word is in word list
    if word_check_with_wildcard(word, word_list):
        
        #check if hand can create word
        for letter in word:
                
            #checking if letters are sufficient to make word (includes wildcards!)
            
            if hand.get(letter, 0) < frequency_word.get(letter, 0) and hand.get(letter, 0) != "*":
                validity = False
                break
    
    else:
        validity = False

    return validity

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    hand_length = 0
    for letter in hand:
        hand_length += hand.get(letter,0)
    
    return hand_length

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    hand_score = 0


    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) > 0:
    
        # Display the hand
        print("Current hand: ", display_hand(hand))

        # Ask user for input
        word = input("Enter word, or '!!' to indicate that you are finished: ")

        # If the input is two exclamation points:
        if word == "!!":
            break
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(word, hand, word_list):

                # Tell the user how many points the word earned,
                # and the updated total score
                word_score = get_word_score(word, HAND_SIZE)
                hand_score += word_score
                print(word + " earned " + str(word_score) + " points. Total: " + str(hand_score) + " points")

            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print("That is not a valid word. Please choose another word.")

            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, word)          

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print()
    if calculate_handlen(hand) == 0:
        print("Ran out of letters. Total score for this hand: " + str(hand_score) + " points")
    
    else:
        print("Total score for this hand: " + str(hand_score) + " points")

    print("----------")
    # Return the total score as result of function
    return hand_score

#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    #creating list of invalid letters
    banned_letter_list = []
    for character in hand.keys():
        banned_letter_list.append(character)

    
    #picking out new letter
    all_letters_combined = VOWELS + CONSONANTS
    
    valid = False
    while not valid:
        new_letter = random.choice(all_letters_combined)
        if new_letter not in banned_letter_list:
            valid = True


    #getting updated hand without mutation :)
    new_hand = {}
    for character in hand.keys():
        if character == letter:
            new_hand[new_letter] = hand.get(character,0)
            new_hand[character] = 0
        else:
            new_hand[character] = hand.get(character,0)
    
    return new_hand

    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    #initializing variables
    replay = True
    substitute = True
    total_score = 0

    #total_hands check
    total_hands = int(input("Enter total number of hands: "))
    while total_hands > 0:
        
        #dealing hand
        hand = deal_hand(HAND_SIZE)
        
        #checking for substitute
        if substitute:
            print("Current hand: ", display_hand(hand))
            substitute_input = input("Would you like to substitute a letter? ")
            substitute_input = substitute_input.lower()

            if substitute_input == "yes":
                letter = input("Select a letter to replace: ")
                
                if letter in hand:
                    hand = substitute_hand(hand, letter)
                    substitute = False
                
                else:
                    print("Letter selected is not inside hand. Substitute Failed. ")
                
        #playing hand
        hand_score = play_hand(hand, word_list)

        #checking for replay
        if replay:
            replay_input = input("Would you like to replay this hand? ")
            replay_input = replay_input.lower()

            if replay_input == "yes":
                second_time_score = play_hand(hand, word_list)

                #checking to see which score is higher
                if second_time_score > hand_score:
                    total_score += second_time_score

                elif hand_score < second_time_score:
                    total_score += hand_score

                total_hands -= 1
                replay = False

            else:
                total_score += hand_score
                total_hands -= 1

        else:
            total_score += hand_score
            total_hands -= 1

    print ("Total score over all hands: " + str(total_score) + " points.")

        



    # print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
    # play_hand(hand, word_list)
