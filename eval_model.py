#!/usr/bin/python -u

from gensim.models import Word2Vec, KeyedVectors
import sys
import csv
import os


p=print
if len(sys.argv) != 2:
  raise ValueError('arg arity is wrong, expect 1, got {}'.format(len(sys.argv)-1))

mname = sys.argv[1]
p('loading model: ', mname)

if not os.path.exists(mname):
  raise FileExistsError(mname)

try:
  model = Word2Vec.load(mname)
except Exception:
  pass
try:
  model = KeyedVectors.load_word2vec_format(mname, unicode_errors='ignore')
except Exception:
  pass
try:
  model = KeyedVectors.load_word2vec_format(mname, binary=True, unicode_errors='ignore')
except Exception:
  raise ValueError('cannot load')
p('model:', model)

r=csv.reader(open('color_attribute_score_vocab.csv', 'r'))
next(r) #header
vs=[i for i in r]
vs_exists=[i for i in vs if i[0] in model or i[1] in model]
ls=(len(vs_exists), len(vs),)
p('{}/{}'.format(*ls))
p((ls[0]/ls[1])*100.0,"%")
