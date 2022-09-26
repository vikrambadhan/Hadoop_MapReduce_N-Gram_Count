#!/usr/bin/env python
"""An advanced Mapper, using Python iterators and generators."""

import sys
import re

def read_input(input):
    t=0
    for line in input:
        # spliting the line to words inorder to keep returning each word

        line=line.lower()
        # replacing all words not in [a-z0-9]with blank space
        line=re.sub("[^a-z0-9]"," ",line).split()
        l=len(line)
        if l < 3:
            continue
        # Putting all all 2 or 3 word inputs into single string by using commas
        for x in range(l-1):
            t=line[x]+','+line[x+1]
            line.append(t)
            
        for x in range(l-2):
            t=line[x]+','+line[x+1]+','+line[x+2]
            line.append(t)

        
        yield line   
        
        


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    data=list(data)
    count=0
    
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in words:
            
            print('%s%s%d' % (word, separator, 1))
            

# how to test locally in bash/linus: cat <input> | python mapper.py
if __name__ == "__main__":
    main()
