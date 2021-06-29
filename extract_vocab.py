#!/usr/bin/python

import csv

def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

with open('color_attribute_score.csv', 'r') as f:
  r=csv.reader(f)
  l=[[i[0], i[5]] for i in r]

l=list(map(lambda x:",".join(x), get_unique_list(l)))
print('\n'.join(l), file=open('color_attribute_score_vocab.csv', 'w'))
