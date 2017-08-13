# -*- coding: utf-8 -*-
import sys
import random
import word_rhyme as rhyme

def vocb2word(vocb_l):
  word_dict = {}
  v_cnt     = 0
  for v in vocb_l:
    key = 'W%0d'%v_cnt
    word_dict[key]=str(v)
    v_cnt = v_cnt + 1
  return word_dict

def find_rhyme(rhym_vocb, line_num):
  max_length = 0
  lkeys=[key for key in rhym_vocb.keys() if len(rhym_vocb[key])> line_num] 
  if len(lkeys) == 0:
    for key in rhym_vocb.keys():
      if (len(rhym_vocb[key]) > max_length):
        max_key    = key
        max_length = len(rhym_vocb[key])
    key_select = max_key
  else:
    key_select = random.choice(lkeys)  
  return rhym_vocb[key_select] 

def state_trans_print(src_state,tar_state,word):
  print '(%s (%s %s))'%(src_state,tar_state,word)

def index2str(index):
  if (index > 9):
    index_str = '0' + str(index)
  else:
    index_str = '0' + str(index)
  
  return index_str

def normal_state_trans(vocb_l,line_index_str,word_index):
  for trans_word in vocb_l:
    state_trans_print('L%sW%s'%(line_index_str,index2str(word_index-1)),'L%sW%s'%(line_index_str,index2str(word_index)),str(trans_word))

def line_process(vocb_l, rhym_l, line_index_str, word_num_line, alliter_en, dbet_en):
  #gen each word in line
  for word_index in range(word_num_line):
    word_index_str = index2str(word_index)
    if (word_index == 0):
      if (alliter_en == 1):
        for trans_word in rhym_l:
          if (word_num_line == 1):
            state_trans_print('L%sSTART'%line_index_str,'L%sEND0',line_index_str,str(trans_word))
          elif not ((dbet_en == 1) and (word_num_line == 2)):
            state_trans_print('L%sSTART'%line_index_str,'L%sW00',line_index_str,str(trans_word))
      else:
        for trans_word in vocb_l:
          if (word_num_line == 1):
            state_trans_print('L%sSTART'%line_index_str,'L%sEND0'%line_index_str,str(trans_word))
          else:
            state_trans_print('L%sSTART'%line_index_str,'L%sW00'%line_index_str,str(trans_word))
    elif (word_index == (word_num_line - 2)):
      if (dbet_en == 0):
        normal_state_trans(vocb_l,line_index_str,word_index)
      else:
        for trans_word in rhym_l:
          if (word_num_line == 2):
            state_trans_print('L%sSTART'%line_index_str,'L%sEND1'%line_index_str,str(trans_word))
          else: 
            state_trans_print('L%sW%s'%(line_index_str,index2str(word_index-1)),'L%sEND1'%line_index_str,str(trans_word))
    elif (word_index == (word_num_line - 1)):
      #if (word_num_line == 2):
      #  for trans_word in rhym_l:
      #    state_trans_print('L%sSTART'%line_index_str,'L%sEND0'%line_index_str,str(trans_word))
      #else:
      if (dbet_en == 0):
        for trans_word in rhym_l:
          state_trans_print('L%sW%s'%(line_index_str,index2str(word_index-1)),'L%sEND0'%line_index_str,str(trans_word))
      else:
        for trans_word in rhym_l:
          state_trans_print('L%sEND1'%line_index_str,'L%sEND0'%line_index_str,str(trans_word))
    else: 
      normal_state_trans(vocb_l,line_index_str,word_index)
        
def gen_fsa(vocb_l, line_num=4, word_num=7, variance=2, alliter_en=0, dbet_en=0):
  #get rhym list
  rhym_vocb = rhyme.word_rhyme(vocb_l)
  rhym_l    = find_rhyme(rhym_vocb,line_num) 
  #gen end state
  print 'END'
  #START -> L00START
  state_trans_print('START','L00START','Rap:')
  #gen each line
  for line_index in range(line_num):
    line_index_str = index2str(line_index)
    word_num_line = random.randint(word_num-variance,word_num+variance)
    line_process(vocb_l, rhym_l, line_index_str, word_num_line, alliter_en, dbet_en)
    #line->line
    if (line_index == (line_num - 1)):
      state_trans_print('L%sEND0'%line_index_str,'END','.')
    else:
      state_trans_print('L%sEND0'%line_index_str,'L%sSTART'%index2str(line_index+1),';')
      
if __name__=='__main__':
  l = ['你','喜','哈','笑'] 
  gen_fsa(l,2,5,1)
         
        
        
   
  

