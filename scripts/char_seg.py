#-*- encoding: utf-8 -*-
#!/usr/bin/env python

# By wxjiao: 2020-06-29

import json
import sys
#import requests

def char_segmenter(sentence):
    phrase_list = sentence.strip('\n').split()    # remove '\n' and ' '
    sent = "".join(phrase_list)
    char_list = list(sent)
    data = " ".join(char_list)
    return data

if __name__ == '__main__':
    start = 0
    if len(sys.argv) > 1:
        start = int(sys.argv[1])
    cnt = 0
    for line in sys.stdin:
        if cnt<start:
            cnt+=1
            continue
        line = line.strip()
        print(char_segmenter(line))
