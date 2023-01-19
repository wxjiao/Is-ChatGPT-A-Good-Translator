import argparse
#import sacrebleu
#from sacrebleu.metrics import BLEU
#import sacrebleu.tokenizers.tokenizer_zh as tokenizer_zh
#import sacrebleu.tokenizers.tokenizer_char as tokenizer_char
#import sacrebleu.tokenizers.tokenizer_base as tokenizer_base
import numpy as np

    
def select_by_random(max_, k):
    np.random.seed(1)
    rand_ = np.random.choice(max_, k, replace=False)
    rand_sorted = sorted(rand_)
    for i in rand_sorted:
        print(i)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--max', '-m', type=int, required=True, help='max num')
    parser.add_argument('--select', '-s', type=int, required=True, help='select num')
    args = parser.parse_args()
    max_num = args.max
    sel_num = args.select
    select_by_random(max_num, sel_num)
