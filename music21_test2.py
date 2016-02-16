# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:22:41 2016

@author: Administrator
"""

'''
MuseScore一些配置与music21默认的不一致，就是正常装了（我笔记本还不能正常装
只能用绿色版的）也不能直接用，上stackoverflow才找到解决方法，改配置。
http://stackoverflow.com/questions/25879764/creating-images-of-notes-in-music21
'''
import music21
from music21 import environment,corpus,note
import numpy as np
import matplotlib.pyplot as plt

exe_path="C:\\Program Files (x86)\\MuseScore 2\\bin\\MuseScore.exe"

environment.set("musescoreDirectPNGPath",exe_path)
environment.set("musicxmlPath",exe_path)

s = corpus.parse('bach/bwv65.2.xml')
s.analyze('key')
s.show()


fl=[]
fd={}
fk=[]
ft=[]
for octave in range(1,8):
    for name in 'CDEFGAB':
        key=name+str(octave)
        note1=music21.note.Note(key)
        f=note1.pitch.frequency
        fl.append(f)
        fd[key]=f
        fk.append(key)
        ft.append((key,note1.pitch.pitchClass,note1.pitch.pitchClassString))
        