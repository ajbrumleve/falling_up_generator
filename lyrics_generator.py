import string

import numpy as np

import genius_scrape
class lyric_model:
    def __init__(self):


        pass
    def run_generator(self,file_list):
        input_files = file_list



        input_data = []
        labels = []
        self.initial = {}
        self.first={}
        self.second={}

        def add2dict(d,k,v):
            if k not in d:
                d[k]=[]
            d[k].append(v)
        def remove_punctuation(s):
            return s.translate(str.maketrans('','',string.punctuation))

        # TODO delete duplicate lines
        for doc in input_files:
            genius_scrape.lyrics_cleaning(doc)
            for line in open(doc,encoding='utf-8'):
                tokens = line.rstrip().lower().split()

                T = len(tokens)
                for i in range(T):
                    t = tokens[i]
                    if i == 0:
                        # measure the distribution of the first word
                        self.initial[t] = self.initial.get(t, 0.) + 1
                    else:
                        t_1 = tokens[i-1]
                        if i == T - 1:
                            # measure probability of ending the line
                            add2dict(self.second, (t_1, t), 'END')
                        if i == 1:
                            # measure distribution of second word
                            # given only first word
                            add2dict(self.first, t_1, t)
                        else:
                            t_2 = tokens[i-2]
                            add2dict(self.second, (t_2, t_1), t)

        initial_total=sum(self.initial.values())
        for t, c in self.initial.items():
            self.initial[t]= c/initial_total

        def list2dict(list_words):
            init_dict={}
            n = len(list_words)
            for word in list_words:
                init_dict[word] = init_dict.get(word, 0) + 1
            for w, count in init_dict.items():
                init_dict[w] = init_dict[w] / n
            return init_dict

        for t_1, tl in self.first.items():
            self.first[t_1] = list2dict(tl)

        for t_1_2, tl in self.second.items():
            self.second[t_1_2] = list2dict(tl)


    def generate_word(self,prob_dict):
        p0 = np.random.random()
        accumulator = 0
        for w, p in prob_dict.items():
            accumulator += p
            if p0 < accumulator:
                return w

    def generate(self,number_of_lines):
        for i in range(number_of_lines):
            line = []
            first_word = self.generate_word(self.initial)
            line.append(first_word)
            second_word = self.generate_word(self.first[first_word])
            line.append(second_word)
            while True:
                next_word = self.generate_word(self.second[(first_word,second_word)])
                if next_word == "END":
                    break
                else:
                    first_word = second_word
                    second_word = next_word
                    line.append(next_word)
            print(" ".join(line))



