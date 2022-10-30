import math
import string

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import lyricsgenius
import config

genius = lyricsgenius.Genius(config.GENIUS_TOKEN)

artist = genius.search_artist("Gloomcatcher", sort="title")

print(len(artist.songs))
with open('gloomcatcher.txt', 'w', encoding='utf-8') as f:
    f.write(artist.songs[0].lyrics)
for item in artist.songs[1:]:
    with open('gloomcatcher.txt', 'a',encoding='utf-8') as f:
        f.write('\n')
        f.write(item.lyrics)
input_files = [
  'falling_up.txt', 'gloomcatcher.txt', 'the_river_empires.txt'
]

input_data = []
labels = []
initial = {}
first={}
second={}

def add2dict(d,k,v):
    if k not in d:
        d[k]=[]
    d[k].append(v)
def remove_punctuation(s):
    return s.translate(str.maketrans('','',string.punctuation))

for doc in input_files:

    for line in open(doc,encoding='utf-8'):
        tokens = line.rstrip().lower().split()

        T = len(tokens)
        for i in range(T):
            t = tokens[i]
            if i == 0:
                # measure the distribution of the first word
                initial[t] = initial.get(t, 0.) + 1
            else:
                t_1 = tokens[i-1]
                if i == T - 1:
                    # measure probability of ending the line
                    add2dict(second, (t_1, t), 'END')
                if i == 1:
                    # measure distribution of second word
                    # given only first word
                    add2dict(first, t_1, t)
                else:
                    t_2 = tokens[i-2]
                    add2dict(second, (t_2, t_1), t)

initial_total=sum(initial.values())
for t, c in initial.items():
    initial[t]= c/initial_total

def list2dict(list_words):
    init_dict={}
    n = len(list_words)
    for word in list_words:
        init_dict[word] = init_dict.get(word, 0) + 1
    for w, count in init_dict.items():
        init_dict[w] = init_dict[w] / n
    return init_dict

for t_1, tl in first.items():
    first[t_1] = list2dict(tl)

for t_1_2, tl in second.items():
    second[t_1_2] = list2dict(tl)

def generate_word(prob_dict):
    p0 = np.random.random()
    accumulator = 0
    for w, p in prob_dict.items():
        accumulator += p
        if p0 < accumulator:
            return w

def generate(number_of_lines):
    for i in range(number_of_lines):
        line = []
        first_word = generate_word(initial)
        line.append(first_word)
        second_word = generate_word(first[first_word])
        line.append(second_word)
        while True:
            next_word = generate_word(second[(first_word,second_word)])
            if next_word == "END":
                break
            else:
                first_word = second_word
                second_word = next_word
                line.append(next_word)
        print(" ".join(line))



