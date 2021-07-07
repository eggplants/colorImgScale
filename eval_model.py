#!/usr/bin/python -u

from gensim.models import Word2Vec, KeyedVectors
import sys
import csv
import os
import inspect
# Usage: python eval_model.py ../test/aozora_week210625.kv.bin

if len(sys.argv) != 2:
  raise ValueError('arg arity is wrong, expect 1, got {}'.format(len(sys.argv)-1))
mname = sys.argv[1]

l=open(mname.split('/')[-1]+'.log', 'w')
def p(*args):
  print(*args, file=l)
  print(*args)

p('loading model: ', mname)

if not os.path.exists(mname):
  raise FileExistsError(mname)

try:
  p('[1]Word2Vec.load')
  model = Word2Vec.load(mname).wv
except Exception as e:
  p('=> failed:', e)
  p(''.join([i[4][0]
    for i in inspect.getinnerframes(e.__traceback__)]))
  input('[OK]')
try:
  p('[2]KeyedVectors.load2vec_format(binary=False)')
  model = KeyedVectors.load_word2vec_format(mname, binary=False, unicode_errors='ignore')
except Exception as e:
  p('=> failed:', e)
  p(''.join([i[4][0]
    for i in inspect.getinnerframes(e.__traceback__)]))
  input('[OK]')
  p('[3]KeyedVectors.load2vec_format(binary=True)')
  model = KeyedVectors.load_word2vec_format(mname, binary=True, unicode_errors='ignore')

p('model:', model)
p('vocab size:', len(model.index_to_key))

r=csv.reader(open('color_attribute_score_vocab.csv', 'r'))
next(r) #header
vs=set(tuple(i) for i in r)
vs_exists=set(tuple(i) for i in vs if i[0] in model or i[1] in model)
ls=(len(vs_exists), len(vs),)
p('{}/{}'.format(*ls))
p((ls[0]/ls[1])*100.0,"%")
p('exists:    ', vs_exists)
p('not exists:', vs-vs_exists)
