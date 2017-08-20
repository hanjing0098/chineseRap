# -*- coding: utf-8 -*-
import thulac	
thu1 = thulac.thulac(seg_only=True)  #只进行分词，不进行词性标注
thu1.cut_f("wiki.zh.text.jian", "wiki.zh.seg.text")  #对input.txt文件内容进行分词，输出到output.txt
