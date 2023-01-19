import argparse
#import sacrebleu
#from sacrebleu.metrics import BLEU
#import sacrebleu.tokenizers.tokenizer_zh as tokenizer_zh
#import sacrebleu.tokenizers.tokenizer_char as tokenizer_char
#import sacrebleu.tokenizers.tokenizer_base as tokenizer_base
import numpy as np

    
def select_by(path_src, path_idx):
    f1 = open(path_src, 'r', encoding='utf-8')
    src = f1.readlines()
    f1.close()
    with open(path_idx, 'r', encoding='utf-8') as f:
        for line in f:
            idx = int(line.strip())
            print(src[idx].strip())
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path-src', '-ps', type=str, required=True, help='input file directory')
    parser.add_argument('--path-idx', '-pi', type=str, required=True, help='output file directory')
    args = parser.parse_args()
    path_src = args.path_src
    path_idx = args.path_idx
    select_by(path_src, path_idx)
