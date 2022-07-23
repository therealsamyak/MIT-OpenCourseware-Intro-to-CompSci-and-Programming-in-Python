# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

from numpy import transpose
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'MIT OpenCourseware Intro to CompSci and Programming in Python\Problem Set 4\ps4\words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        valid_word_list = self.valid_words
        copy_list = valid_word_list.copy()

        return copy_list
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        #initializing variable
        transpose_dict = {}

        #mapping vowels
        for index in range(len(VOWELS_LOWER)):
            
            #using permutation
            new_vowel = vowels_permutation[index]
            new_vowel_lower = new_vowel.lower()
            new_vowel_upper = new_vowel.upper()
            
            transpose_dict[VOWELS_LOWER[index]] = new_vowel_lower
            transpose_dict[VOWELS_UPPER[index]] = new_vowel_upper
        
        #mapping consonents
        for index in range(len(CONSONANTS_LOWER)):
            transpose_dict[CONSONANTS_LOWER[index]] = CONSONANTS_LOWER[index]
            transpose_dict[CONSONANTS_UPPER[index]] = CONSONANTS_UPPER[index]      
        
        return transpose_dict

    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        #initializing variables
        message = self.get_message_text()
        new_message = ""

        #checking if letter can be transposed
        for letter in message:
            if letter in VOWELS_LOWER or letter in VOWELS_UPPER or letter in CONSONANTS_LOWER or letter in CONSONANTS_UPPER:
                letter = transpose_dict.get(letter)         

            new_message += letter
        
        return new_message
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        #initializing variables
        valid_words_list = self.get_valid_words()
        vowel_permutations = get_permutations("aeiou")
        vowel_permutations_valid_words_dict = {}
        
        #checking all permutations
        for permutation in vowel_permutations:
            
            #resetting valid_word counter
            valid_words = 0

            #applying transpose dict according to permutation
            transpose_dict = self.build_transpose_dict(permutation)
            decrypted_message = self.apply_transpose(transpose_dict)
            decrypted_message_as_word_list = decrypted_message.split()

            #checking for valid words
            for item in decrypted_message_as_word_list:
                if is_word(valid_words_list, item):
                    valid_words += 1
            
            #storing result to dictionary to check later
            vowel_permutations_valid_words_dict[permutation] = valid_words
        
        best_permutation = max(vowel_permutations_valid_words_dict, key=vowel_permutations_valid_words_dict.get)
        transpose_dict = self.build_transpose_dict(best_permutation)
        decrypted_message = self.apply_transpose(transpose_dict) 
        
        return decrypted_message 

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
