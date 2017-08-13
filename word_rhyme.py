# -*- coding: utf-8 -*-
import word2pinyin as pinyin

word_lib = './vocabulary_library/test.txt'
word_rhyme_dict = {}
def line_parse(line):
  word       = line.split('\t')[0].strip()
  py         = pinyin.word2pinyin(word)
  word_cnt   = len(py.split())
  last_py    = py.split()[-1].strip()
  if (last_py[0] in 'aoeiuv'):
    rhyme      = last_py[:-1] 
  else:
    rhyme      = last_py[2:-1] if last_py[:2] in 'zh,ch,sh' else last_py[1:-1]
  #print word
  return word,rhyme,word_cnt
def word_rhyme(debug_on=0):
  with open(word_lib) as wl:
    lines_1 = [x for x in wl.readlines()]
    lines_2 = lines_1
    for line_src in lines_1: 
      word_src, rhyme_src, word_cnt_src = line_parse(line_src)
      if (debug_on == 1):
        print 'word_src:%s, word_rhyme:%s, word_cnt:%d ' %(str(word_src),str(rhyme_src),word_cnt_src)
      word_rhyme_dict[str(word_src)]= []
      for line_tar in lines_2:
        word_tar, rhyme_tar, word_cnt_tar= line_parse(line_tar)
        if (debug_on == 1):
          print 'word_tar:%s, word_rhyme:%s ' %(str(word_tar),str(rhyme_tar))
        if rhyme_src == rhyme_tar and word_cnt_src == word_cnt_tar and word_src != word_tar:
          word_rhyme_dict[str(word_src)].append(word_tar)
      print '%s\t'%word_src,
      for i in word_rhyme_dict[str(word_src)]:
        print "%s"%i, 
      print '\n'

if __name__=='__main__':
  word_rhyme()
