# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 18:34:47 2016

@author: yiyuezhuo
"""
import os
from  xml.dom import minidom

player_path='MidiAndMusicXmlPlayer.exe'
editor_path=u'C:/Users/yiyuezhuo/Desktop/temp_data/简五谱Overture/简五谱Overture.exe'.encode('gbk')

def play(path):
    os.system(player_path+' '+path)
    
def play_s(s,temp_path='temp.xml'):
    f=open(temp_path,'w')
    f.write(s)
    f.close()
    play(temp_path)
    
def edit(path):
    os.system(editor_path+' '+os.getcwd()+'\\'+path)
    
def edit_s(s,temp_path='temp.xml'):
    f=open(temp_path,'w')
    f.write(s)
    f.close()
    edit(temp_path)

    
template=minidom.parse('template.xml')

part=template.getElementsByTagName('part')[0]
measure=template.getElementsByTagName('measure')[0]
note=measure.getElementsByTagName('note')[0]

measure.removeChild(note)
part.removeChild(measure)

measure=measure.cloneNode(True)
note=note.cloneNode(True)
'''下面template和part是原始对象，而measure,note而是独立的模板'''
'''
      <note>
        <pitch>
          <step>C</step>
          <octave>5</octave>
        </pitch>
        <duration>384</duration>
        <type>quarter</type>
        <dot />
      </note>
'''

def Pair(name,text):
    obj=minidom.Element(name)
    _obj=minidom.Text()
    _obj.data=text
    obj.appendChild(_obj)
    return obj
def Dic(name,dom_list):
    obj=minidom.Element(name)
    for dom in dom_list:
        obj.appendChild(dom)
    return obj
    

class Note(object):
    def __init__(self,step='C',octave=5,duration=256,type='quarter',dot=0):
        self.step=step
        self.octave=str(octave)
        self.duration=str(duration)
        self.type=type
        self.dot=dot
        self.xml=None
    def to_xml(self):
        step=Pair('step',self.step)
        octave=Pair('octave',self.octave)
        pitch=Dic('pitch',[step,octave])
        duration=Pair('duration',self.duration)
        type=Pair('type',self.type)
        note=Dic('note',[pitch,duration,type])
        for i in range(int(self.dot)):
            dot=minidom.Element('dot')
            note.appendChild(dot)
        self.xml=note
        return self.xml
        
class Attributes(object):
    def __init__(self,divisions=256,fifths=0,beats=4,beat_type=4,sign='G',line=2):
        self.divisions=str(divisions)
        self.fifths=str(fifths)
        self.beats=str(beats)
        self.beat_type=str(beat_type)
        self.sign=sign
        self.line=str(line)
        self.xml=None
    def to_xml(self):
        divisions=Pair('divisions',self.divisions)
        fifths=Pair('fifths',self.fifths)
        key=Dic('key',[fifths])
        beats=Pair('beats',self.beats)
        beat_type=Pair('beat-type',self.beat_type)
        time=Dic('time',[beats,beat_type])
        sign=Pair('sign',self.sign)
        line=Pair('line',self.line)
        clef=Dic('clef',[sign,line])
        attributes=Dic('attributes',[divisions,key,time,clef])
        self.xml=attributes
        return self.xml
        
class Measure(object):
    def __init__(self,number,attributes=None,note_l=None):
        self.number=str(number)
        self.attributes=attributes
        self.note_l=note_l
        self.xml=None
    def set_attributes(self,attributes):
        self.attributes=attributes
    def append_note(self,note):
        self.note_l.append(note)
    def extend_notes(self,notes):
        for note in notes:
            self.append_note(note)
    def to_xml(self):
        measure=minidom.Element('measure')
        measure.setAttribute('number',self.number)
        if self.attributes:
            measure.appendChild(self.attributes.to_xml())
        for note in self.note_l:
            measure.appendChild(note.to_xml())
        self.xml=measure=measure
        return self.xml
        
class Part(object):
    def __init__(self,id="P1",measure_l=[]):
        self.id=id
        self.measure_l=measure_l
        self.xml=None
    def add_measure(self,measure):
        self.measure_l.append(measure)
    def to_xml(self):
        part=minidom.Element('part')
        part.setAttribute('id',self.id)
        for measurein in self.measure_l:
            part.appendChild(measure.to_xml())
        self.xml=part
        return self.xml
        
#默认attributes,即节拍，谱号那些
att=Attributes()
#第一小节
m1=Measure(1)
m1.attributes=att
#第一小节四个音符
n11=Note()
n12=Note(step='D')#D是一个八度里的一个符号
n13=Note(octave=4)#octabe 8度，第几个8度，大区间
n14=Note()
m1.note_l=[n11,n12,n13,n14]

part.appendChild(m1.to_xml())#这个part是引用的xml对象，而不是上面的Part封装

print template.toxml()