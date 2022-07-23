# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    #initializing variables
    permutation_list = []
    simplified_word_list = []
    hold_out_character_list = []
    
    #changing string to list to mutate later
    word_as_list = list(sequence)

    #base case for recursion
    if len(sequence) == 1:
        permutation_list.append(sequence)
    
    #recursive case
    else:
        
        #holding out characters and adding that character to a list
        for character in word_as_list:
            hold_out_character_list.append(character)

            #copying list to prevent mutation
            word_as_list_copy_one = word_as_list.copy()
            word_as_list_copy_one.remove(character)
            
            #getting the partial words and adding them to a list
            simplified_word = "".join(word_as_list_copy_one)
            simplified_word_list.append(simplified_word)


        #getting permutations of each partial word
        for index_one in range(len(simplified_word_list)):
            
            simplified_word = simplified_word_list[index_one]
            simplified_word_permutations = get_permutations(simplified_word) # recursion!

            #getting permutations of permutations
            for index_two in range(len(simplified_word_permutations)):
                
                permutation_string = simplified_word_permutations[index_two]
                permutation_as_list = list(permutation_string)              
                permutation_as_list.insert(0, hold_out_character_list[index_one])
                permutation = "".join(permutation_as_list)

                if permutation not in permutation_list:
                    permutation_list.append(permutation)

    return sorted(permutation_list)


if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
   
#   Put three example test cases here (for your sanity, limit your inputs
#   to be three characters or fewer as you will have n! permutations for a 
#   sequence of length n)

#Example 1
    example_input = 'bca'
    print("Input:", example_input)
    print("Expected Output:", ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print("Actual Output:", get_permutations(example_input))
    print("")

#Example 2
    example_input = 'ab'
    print("Input:", example_input)
    print("Expected Output:", ['ab', 'ba'])
    print("Actual Output:", get_permutations(example_input))
    print("")

#Example 3
    example_input = 'efg'
    print("Input:", example_input)
    print("Expected Output:", ['efg', 'egf', 'feg', 'fge', 'gef', 'gfe'])
    print("Actual Output:", get_permutations(example_input))
    print("")


