# Instructions

- Decide the 50 indices for the subset
```
python3 random_idx.py -m 1012 -s 50 > test_rand_idx.txt
```

- Extract from the full set
```
python3 random_idx_select.py -ps test_full.txt -pi test_rand_idx.txt > test_rand_50.txt
```

- Segment the Japanese sentences for char-level BLEU
```
cat test_hyp.txt | python3 char_seg.py > test_hyp_char.txt
```
