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

    tuple_list= []
    for i, word in enumerate(text_list[:-1]):
        words_tuple = (text_list[i],text_list[i+1])
        tuple_list.append(words_tuple)

    for idx, k in enumerate(tuple_list[:-1]):
        next_word = tuple_list[idx+1][1]
        values = chains.setdefault(k,[])
        values.append(next_word)
    # print(chains)
    #     if k == keys_list[idx]:
    #         chains[k].append(keys_list[idx+1][0])
    #     idx += 1    
    # print(keys_list)
  

    # print(len(chains))
    # print(chains)
    their_answer = {('a', 'fox?'): ['Would'],
 ('Sam', 'I'): ['am?'],
 ('could', 'you'): ['in', 'with', 'in', 'with'],
 ('you', 'with'): ['a', 'a'],
 ('box?', 'Would'): ['you'],
 ('ham?', 'Would'): ['you'],
 ('you', 'in'): ['a', 'a'],
 ('a', 'house?'): ['Would'],
 ('like', 'green'): ['eggs'],
 ('like', 'them,'): ['Sam'],
 ('and', 'ham?'): ['Would'],
 ('Would', 'you'): ['could', 'could', 'could', 'could', 'like', 'like'],
 ('you', 'could'): ['you', 'you', 'you', 'you'],
 ('a', 'mouse?'): ['Would'],
 ('them,', 'Sam'): ['I'],
 ('in', 'a'): ['house?', 'box?'],
 ('with', 'a'): ['mouse?', 'fox?'],
 ('house?', 'Would'): ['you'],
 ('a', 'box?'): ['Would'],
 ('green', 'eggs'): ['and'],
 ('you', 'like'): ['green', 'them,'],
 ('mouse?', 'Would'): ['you'],
 ('fox?', 'Would'): ['you'],
 ('eggs', 'and'): ['ham?']
}
    # if chains == their_answer:
    #     print(True)
    # else:
    #     print(False)

    return chains


# make_chains(new_string)

def make_text(chains):
    """Return text from chains."""
    chains_keys = list(chains.keys())
    
    words = []

    random_keys = choice(chains_keys)
    phrase_list = chains[random_keys] 
    random_word = choice(phrase_list)

    words = [random_word]

    random_keys = (random_keys[1], random_word)

    while random_keys != chains['Sam','I']:
        words.append(random_keys)
        words.append(random_word)


    print(words)

    # your code goes here

    # return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

# print(random_text)
