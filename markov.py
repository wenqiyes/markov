"""Generate Markov text from text files."""

from ast import For
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()

    return contents




def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    text_list = text_string.split()
    # for i in range(len(text_list)-1):
    #    if i == len(text_list)-2:
    #         chains[(text_list[i],text_list[i+1])] = [None]
    #    else:
    #          chains[(text_list[i],text_list[i+1])].append(text_list[i+2]) 

       
    # print(chains)

    for i in range(len(text_list)-1):
        key=(text_list[i],text_list [i +1])
        

        if i == len(text_list)-2:            
            value = None
        else:
            value= text_list[i+2]



        if key not in chains:
            chains[key]= []
        chains[key].append(value)
        
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    key = choice(list(chains.keys()))
    #value = choice(list(chains[key]))
    words=[key[0],key[1]]
    print(words)
    word=choice(chains[key])

    while True:
        key=(words[-2], word[-1])
        try:
            value= chains[key]
            words.append(choice(value))
        except:break





    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

print(chains)
# Produce random text
random_text = make_text(chains)

print(random_text)
