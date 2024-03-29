# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("MIT OpenCourseware Intro to CompSci and Programming in Python\ps4\story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'MIT OpenCourseware Intro to CompSci and Programming in Python\ps4\words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
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

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        #initializing variables
        shift_dict = {}
        original_lower_case_letters = string.ascii_lowercase
        original_upper_case_letters = string.ascii_uppercase

        #letter shift
        for index in range(len(string.ascii_lowercase)):
            new_letter_index = shift + index
            
            #checking if out of range
            if new_letter_index >= 26:
                new_letter_index = abs(26-new_letter_index)

            #dict mapping
            shift_dict[original_lower_case_letters[index]] = original_lower_case_letters[new_letter_index]
            shift_dict[original_upper_case_letters[index]] = original_upper_case_letters[new_letter_index]
        
        return shift_dict
        

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        
        #initializing variables
        shift_dict = self.build_shift_dict(shift)
        mess = self.get_message_text()
        new_message_as_list = []
        special_characters = " !@#$%^&*()-_+={}[]|\:;'<>?,./\""

        #shifting letter
        for letter in mess:
            if letter in special_characters:
                new_message_as_list.append(letter)
            else:
                new_letter = shift_dict.get(letter)
                new_message_as_list.append(new_letter)

        #getting new word
        new_message = "".join(new_message_as_list)

        return new_message

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        og_encrypt_dict = self.encryption_dict
        copy_encrypt_dict = og_encrypt_dict.copy()

        return copy_encrypt_dict
        

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted


    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''

        if shift < 26:
            self.shift = shift
            self.encryption_dict = self.build_shift_dict(shift)
            self.message_text_encrypted = self.apply_shift(shift)
        
        elif shift < 0: 
            print("Shift too small.")
        
        else:
            print("Shift too large.")


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        #getting valid words list
        valid_words_list = self.get_valid_words()  

        #using dict to keep track of which shift_value is best
        shift_values_valid_words_dict = {}
        
        #finding out best shift_value
        for index in range(26):

            #resetting valid word counter
            valid_words = 0
            
            #applying shift
            og_message = self.apply_shift(index)
            message_word_list = og_message.split()

            #checking for valid words
            for item in message_word_list:
                if is_word(valid_words_list, item):
                    valid_words += 1  

            #mapping to dictionary shift_value:number of valid_words are in message  
            shift_values_valid_words_dict[index] = valid_words

        #decrypting message using best_shift value
        best_shift = max(shift_values_valid_words_dict, key=shift_values_valid_words_dict.get)
        decrypted_message = self.apply_shift(best_shift)  
        
        return (best_shift, decrypted_message)
            

if __name__ == '__main__':
    
#     #Example test case (PlaintextMessage)
    # plaintext = PlaintextMessage('hello', 2)
    # print('Expected Output: jgnnq')
    # print('Actual Output:', plaintext.get_message_text_encrypted())

#    #Example test case (CiphertextMessage)
#     ciphertext = CiphertextMessage('jgnnq')
#     print('Expected Output:', (24, 'hello'))
#     print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

    # Example test case 1 (PlaintextMessage)
    plaintext = PlaintextMessage("what's up", 2)
    print("Expected Output: yjcv'u wr")
    print('Actual Output:', plaintext.get_message_text_encrypted())

    # Example test case 2 (PlaintextMessage)
    plaintext = PlaintextMessage('Joe went outside.', 5)
    print('Expected Output: Otj bjsy tzyxnij.')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    # Example test case 1 (CiphertextMessage)
    ciphertext = CiphertextMessage('Otj bjsy tzyxnij.')
    print("Expected Output:", (21, "Joe went outside"))
    print('Actual Output:', ciphertext.decrypt_message())

    # Example test case 2 (CiphertextMessage)
    ciphertext = CiphertextMessage("ocp ku vtkrrkpi")
    print("Expected Output:", (24, "man is tripping"))
    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: best shift value and unencrypted story 

    story_message = CiphertextMessage(get_story_string())
    print(story_message.decrypt_message())
    # (12, 'Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. He has been registered for classes at MIT twice before, but has reportedly never passed a class. It has been the tradition of the residents of East Campus to become Jack Florey for a few nights each year to educate incoming students in the ways, means, and ethics of hacking.')
    

