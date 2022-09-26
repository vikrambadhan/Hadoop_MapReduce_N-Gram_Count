#!/usr/bin/env python
"""An advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys
import re
import json

# receive the output of a mapper, (key, [value, value, ...])
def read_mapper_output(input, separator='\t'):
    for line in input:
        #  return each (key, [value, value, ...]) tuple, though there should only be one per line
        yield line.rstrip().split(separator, 1)


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    unigram_count = 0
    trigram_wordlist=[]
    unigram_wordlist=[]
    bigram_wordlist=[]
    # Harcoded in the mapper to create only one key with different values, each value being a different word
    print('unigram                                       bigram                                             trigram')
    
    for current_word, group in groupby(data, itemgetter(0)):
        try:    
            for current, w in group:
                
                w=json.loads(w)
                if len(re.findall(',',w[0]))==2:
                    trigram_wordlist.append(w)
                    
                    
                elif len(re.findall(',',w[0]))==1:
                    bigram_wordlist.append(w)
                    
                else:
                    unigram_wordlist.append(w)
                    unigram_count=int(w[1]) + unigram_count          
            # Finding the number of maximum ocuurence of trigrams.     
            maximum_len = max(len(trigram_wordlist), len(bigram_wordlist), len(unigram_wordlist))
            minimum_len = min(len(trigram_wordlist), len(bigram_wordlist), len(unigram_wordlist))
            diff= maximum_len-minimum_len
            val_add =["----","0"]
            # Printing the unigram , Bigram , Trigram
            for x in range(diff):
                unigram_wordlist.append(val_add)
                bigram_wordlist.append(val_add)
                trigram_wordlist.append(val_add)
            for x in range(maximum_len):
                print('%s%s%s%s%s%s%s%s%s%s%s' % (unigram_wordlist[x][0].replace(',',' '), separator, unigram_wordlist[x][1],separator,bigram_wordlist[x][0].replace(',',' '),separator,bigram_wordlist[x][1],separator,trigram_wordlist[x][0].replace(',',' '),separator,trigram_wordlist[x][1]))
                
        except ValueError:
            # count was not a number, so silently discard this item
            pass
           
    
if __name__ == "__main__":
    main()
