# -*- coding: utf-8 -*-
import codecs
import sys
import gensim
import gen_fsa as fsa
import argparse

def is_chinese(word):
  if word >= u'\u4e00' and word <= u'\u9f5a':
    return True
  else:
    return False

parser = argparse.ArgumentParser()
parser.add_argument("-m","--mode", type = int, default=0, help="rhym mode selection -m/--mode=0(1,2)")
parser.add_argument("-ln","--linenum", type = int, default=4,  help="line number selection -ln/--linenum")
parser.add_argument("-wn","--wordnum", type = int, default=7, help="word number in one line selection -wn/--wordnum")
parser.add_argument("-al","--alli", type = int, default=0, help="enable lliteration or not -al/--alli 0(1)")
parser.add_argument("-d","--doublerhyme", type = int, default=0, help="enable double rhyme or not -d/--doublerhyme 0(1)")
parser.add_argument("-t","--topic", default='默认', help="specify the topic word -t/--topic")
parser.add_argument("-o","--filename", default='rap.fsa',  help="specify the fsa output file -o/-filename filename")
args = parser.parse_args()

if __name__=='__main__':
  vocab_l = []
  #f = codecs.open('test_fsa.txt', 'r', encoding='utf-8')
  word = args.topic
  print 'topic: '+word
  model = gensim.models.Word2Vec.load('../../model/wiki.zh.model')
  #print 'model load successfully! ...'
  result = model.most_similar(args.topic.decode('utf-8'),[],1000)
  for x in result:
    if (x[0].strip() != '') and (is_chinese(x[0])):
      vocab_l.append(x[0].strip().encode('utf-8'))
  #print vocab_l
  fsa.gen_fsa(vocab_l, args.filename, args.mode, args.linenum, args.wordnum, args.alli, args.doublerhyme)
