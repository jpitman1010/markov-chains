"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
   """
    contents = open(file_path).read()

    return contents


new_string = open_and_read_file(sys.argv[1])


def make_chains(text_string):
#     """Take input text as string; return dictionary of Markov chains.

#     A chain will be a key that consists of a tuple of (word1, word2)
#     and the value would be a list of the word(s) that follow those two
#     words in the input text.

#     For example:

#         >>> chains = make_chains("hi there mary hi there juanita")

#     Each bigram (except the last) will be a key in chains:

#         >>> sorted(chains.keys())
#         [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

#     Each item in chains is a list of all possible following words:

#         >>> chains[('hi', 'there')]
#         ['mary', 'juanita']
        
#         >>> chains[('there','juanita')]
#         [None]
#     """

#     chains = {}

#     # your code goes here
    chains = {}
    # for lines in text_string:
        # lines=lines.split("\n")
    text_list = text_string.split()
    print(text_list)

    # print(lines)
    for i in range(len(text_list)-2):
        words_tuple = (text_list[i],text_list[i+1])
        chains[words_tuple]=[]

    idx=0
    keys_list = list(chains.keys())
    keys_list.sort()
    for k,v in keys_list:
        print(k,v,s)
        if k == keys_list:
            chains[k].append(keys_list[idx+1][1])
        idx += 1    
    print(keys_list)
  

    print(len(chains))
    print(chains)

        # d.setdefault(k, [])
    #             # chains[words_tuple]= word.append(words[i+2])
    #     # for i in range(len(chains)-2):
    #     #     if words_tuple in chains[words_tuple]:
    #     #         chains[words_tuple] = word.append(words[i+2])
    #             # while word in chains[words_tuple]:
    #             #     word.append(words[i+2])
    #             if words_tuple in chains:
    #                 chains[words_tuple].append(words[i+2])

    #             else:
    #                 chains[words_tuple] = [words]
    

    # print(chains)
    # return chains
#     return chains
make_chains(new_string)

# def make_text(chains):
#     """Return text from chains."""

#     words = []

#     # your code goes here

#     return " ".join(words)


# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
