# 用户指导.第一部分，安装与使用 `music21`

如果你希望使用 `music21` ，你需要拥有一份它的拷贝与Python在你的电脑上。
不同的电脑上的实现方式略有不同，所以请按照下面的链接做。对于大多数人来
说，安装是一系列步骤中最困难的一步。

Mac 用户: [Installing Music21 on Mac](http://music21.readthedocs.org/en/latest/installing/installMac.html#installmac)

Windows 用户（包括安装Python） [Installing Music21 in Windows](http://music21.readthedocs.org/en/latest/installing/installWindows.html#installwindows)

Unix/Linux 用户或者Mac用户也许需要: [Installing Music21 on GNU/Linux](http://music21.readthedocs.org/en/latest/installing/installLinux.html#installlinux)

当新版的 `music21` 被发布，你可以通过与上面所述一样的安装方法去更新它。

如果你希望看到是否值得安装它，请先阅读 [说明](http://music21.readthedocs.org/en/latest/usersGuide/usersGuide_02_notes.html#usersguide-02-notes)
在安装之前，但是如果你已经安装完了，你可以比说明上提到的做的更多。

## `music21` 初步

我们来看看music21是否安装好了。打开Terminal(Mac)或者IDLE(Windows)。
在Mac输入"python" (不包括引号)并且按回车。

为了载入music21输入这个

	from music21 import *
	
你可能会得到一些警告你缺失了一些可选模块。这没问题。如果你得到警告
"no module named music21"则上面的的过程可能出了一些问题。尝试再一次
按照安装指南一步一步操作，确保没有跳过任何步骤。99%的安装错误都是
因为跳过了某些步骤。如果你仍然没有解决问题，请Google"installation
 problem music21" 或者 "installation problem mac python module"
 看看有没有类似的情况。如果所有尝试都失败了，请在Google Group
 联系music21list以寻求帮助。
 
 如果你没有碰上问题，这是一般的情况，则 `music21` 就可以运转了。
 输入下列命令你可以得到一个乐谱(score)从曲库(corpus)中。
 
	s=corpus.parse('bach/bwv65.2.xml')
	
现在 `s` 表示J.S.Bach的一个完整赞美诗乐谱(chorale)。输入
" `s.analyse('key')` " 查看music21对其调的最优猜测:

	s.analyse('key')
	
	<music21.key.Key of a minor>
	
现在看看你是否可以用music21显示乐谱。如果不行，你可以跳到
[第8章:安装MusicXML读取器](http://music21.readthedocs.org/en/latest/usersGuide/usersGuide_08_installingMusicXML.html#usersguide-08-installingmusicxml)
或者不看乐谱的完成教程直到那里。输入 `s.show()` 假如你的安装与配置没问题的话，
你的MusicXML读取器应该打开并且显示出这个赞美诗。正如我们下面看到的那样

	s.show()
	
一个乐谱的图

你那边应该是这个样子的

一个截图

又一次，如果你没有 `MusicXML` 没有显示出来，不要绝望。我们将在之后几章
里给出更清晰的指导。现在，让我们进入 [第2章:音符](http://music21.readthedocs.org/en/latest/usersGuide/usersGuide_02_notes.html#usersguide-02-notes)

