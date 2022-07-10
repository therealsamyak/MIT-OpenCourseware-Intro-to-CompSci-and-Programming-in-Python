# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "Problem Set 2 Words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
letters_guessed = []

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    # for char in secret_word:
    #   guessed = char in letters_guessed
    #   if not guessed:
    #     break

    # return guessed

    return all((char in letters_guessed) for char in secret_word)



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    guessing_string = ""
    for char in secret_word:
      if char in letters_guessed:
        guessing_string = guessing_string + (char + " ") 
      else:
        guessing_string = guessing_string + "_ "
   
    return guessing_string


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    not_yet_guessed = ""
    for char in string.ascii_lowercase:
      if char not in letters_guessed:
        not_yet_guessed = not_yet_guessed + (char + " ") 
  
    return not_yet_guessed


def valid_guess(player_guess):
  '''
  player_guess: string, player's guess of letter
  returns: boolean, whether guess is valid or not. 
  
  '''

  if player_guess in string.ascii_lowercase or player_guess == "*":
    validity = True
  else:
    validity = False

  return validity

def vowel_check(player_guess):
  '''
  player_guess: string, player's guess of letter
  returns: boolean, whether guess is vowel or not
  
  '''
  vowel_list = ["a","e","i","o","u"]
  if player_guess in vowel_list:
    vowel = True
  else:
    vowel = False

  return vowel

def total_score(secret_word, remaining_guesses):
  '''
  secret_word: string, word user is guessing
  remaining_guesses: int, number of guesses (lives) remaining
  returns: total score, remaining guesses * number of unique letters
  
  '''
  num_of_unique_letters = len(secret_word)
  for index in range(len(secret_word)):
    inx = index
    if secret_word[inx] in secret_word[(inx+1):len(secret_word)]:
      num_of_unique_letters -= 1

  total_score = remaining_guesses * num_of_unique_letters

  return total_score


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")

    remaining_guesses = 6
    warnings = 3
    while remaining_guesses > 0:
      print("---------------")
      print("You have " + str(remaining_guesses) + " guesses left.")

      available_letters = get_available_letters(letters_guessed)
      print("Available letters: " + available_letters)

      initial_player_guess = input("Please guess a letter: ")
      player_guess = str.lower(initial_player_guess)

      #guess manipulation
      if valid_guess(player_guess) and player_guess not in letters_guessed:
        letters_guessed.append(player_guess)

        if player_guess in secret_word:
          print("Good guess: " + get_guessed_word(secret_word,letters_guessed))
        else:
          print("Oops! That letter is not in my word: " + get_guessed_word(secret_word,letters_guessed))
          
          if vowel_check(player_guess):
            remaining_guesses -= 2
          else:
            remaining_guesses -= 1
      
      #checking for warnings
      
      else:
        warnings -= 1
        if warnings < 0:
          warnings = 0
          remaining_guesses -=1
        
        if player_guess in letters_guessed:
          print("Oops! You've already guessed that letter. You have " + str(warnings) + " warnings left: " + get_guessed_word(secret_word,letters_guessed))
        else:
          print("Oops! That is not a valid letter. You have " + str(warnings) + " warnings left: " + get_guessed_word(secret_word,letters_guessed))


      #check for completion
      if is_word_guessed(secret_word,letters_guessed):
        print("Congratulations! The word was " + secret_word + ".")

        #score
        print("Your total score for this game is: " + str(total_score(secret_word, remaining_guesses)) + ".")

        break

    #if all lives lost
    if remaining_guesses == 0:
      print("Too bad! The word was " + secret_word + ". Better luck next time.")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_without_space = ""
    my_word = (get_guessed_word(secret_word,letters_guessed))
    
    #removing spaces
    for char in my_word:
      if char != " ":
        word_without_space = word_without_space + char
    
    #checking to see if guessed word has same track as actual word
    for index in range(len(word_without_space)):
      if len(word_without_space) != len(other_word):
        matchingone = False
        break

      if word_without_space[index] == other_word[index] or word_without_space[index] == "_":
        matchingone = True
      
      else:
        matchingone = False
        break
  
    
    return matchingone

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    my_word = (get_guessed_word(secret_word,letters_guessed))
    matching_words = ""

    #checking if word in wordlist matches criteria
    for word in wordlist:

      list_word = list(word)
      
      #checking if match is legally playable
      for index in range(len(list_word)):
        if list_word[index] not in my_word and list_word[index] not in get_available_letters(letters_guessed):
          word = ""

    #adding word to string if matches criteria
      if match_with_gaps(my_word, word):
        matching_words = matching_words + word + " "

    if matching_words == "":
      matching_words = "No matches found."

    return matching_words



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")

    remaining_guesses = 6
    warnings = 3
    while remaining_guesses > 0:
      print("---------------")
      print("You have " + str(remaining_guesses) + " guesses left.")

      available_letters = get_available_letters(letters_guessed)
      print("Available letters: " + available_letters)

      initial_player_guess = input("Please guess a letter: ")
      player_guess = str.lower(initial_player_guess)

      #guess manipulation
      if valid_guess(player_guess) and player_guess not in letters_guessed and player_guess != "*":
        letters_guessed.append(player_guess)

        if player_guess in secret_word:
          print("Good guess: " + get_guessed_word(secret_word,letters_guessed))
        else:
          print("Oops! That letter is not in my word: " + get_guessed_word(secret_word,letters_guessed))
          
          if vowel_check(player_guess):
            remaining_guesses -= 2
          else:
            remaining_guesses -= 1


      elif player_guess == "*":
        my_word = (get_guessed_word(secret_word,letters_guessed))
        print("Possible word matches are:")
        print(show_possible_matches(my_word))

      
      #checking for warnings
      
      else:
        warnings -= 1
        if warnings < 0:
          warnings = 0
          remaining_guesses -=1
        
        if player_guess in letters_guessed:
          print("Oops! You've already guessed that letter. You have " + str(warnings) + " warnings left: " + get_guessed_word(secret_word,letters_guessed))
        elif player_guess not in letters_guessed and player_guess != "*":
          print("Oops! That is not a valid letter. You have " + str(warnings) + " warnings left: " + get_guessed_word(secret_word,letters_guessed))


      #check for completion
      if is_word_guessed(secret_word,letters_guessed):
        print("Congratulations! The word was " + secret_word + ".")

        #score
        print("Your total score for this game is: " + str(total_score(secret_word, remaining_guesses)) + ".")

        break

    #if all lives lost
    if remaining_guesses == 0:
      print("Too bad! The word was " + secret_word + ". Better luck next time.")





# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word) 

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = "apple"
    hangman_with_hints(secret_word)
