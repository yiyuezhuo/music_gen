# 用户指南,第二章 音符

记谱音乐(Notated music)，就像它的名字所显示的一样，由一系列音符所组成
，在五线谱(on staff)上，它们一个在另一个后面或在一起。当然还有一些其他
东西，如谱号(clef)，调号(key signatures)，连音线(slur)等。但是音乐的核心
是音符，所以为了使用music21，你需要知道它的思路以及如何操作音符。

打开IDLE或者输入"python" 于命令行(对于Mac是Terminal或者对于Windows是
"run:cmd")来做好准备。

## 创建与操作音符

music21里标准音符的概念以 `Note` 对象表示，其可以在 `note` 模块中找到。

__对于Python新手请阅读这个__(_其他人可以跳过_)： 注意模块名与对象名的不同。
模块，其可以包含0个或数个对象，其总是以小写字母开头。Music21的对象则总是
以大写字母开头。所以 `Note` 对象可以在 `note` 模块里找到。而Python是对大小写
敏感的，如果你输入一个对象的名字以错误的方式它将不知道你要做什么，也不会给你
任何关于区分它们的帮助信息。

在　`note` 模块，还有一些除了 `note.Note` 以外的类，其最重要的是 `note.Rest`
正如你想像的它表示休止符。如果我们以下面的方式载入music21

		from music21 import *
		
则你讲可以用 `note` 命令访问 `note` 模块

		>>> note
		<module 'music21.note' from 'D:\music21files\music21\note.pyc'>
		
如果你得到类似这样的信息则你已经访问到了music21

对于你输入 `"note"` 访问的 `note`  模块，文件名 "from 'D:\music21files...'" 会与你的有区别，
它会显示出你安装music21的地方(如果你忘记了你在哪装的music21这会是有帮助的)。
另外它以 `note.pyc` 还是 `note.py` 结尾是没影响的。

如果你想要知道 `note` 模块除了 Note与Rest对象外还包含什么你可以输入 "`dir(note)`" 
来查看:

		dir(note)
	
		 ['GeneralNote',
		  'Lyric',
		  'LyricException',
		  'NotRest',
		  'NotRestException',
		  'Note',
		  'NoteException',
		  'Rest',
		  'SlottedObject',
		  'SpacerRest',
		  'Test',
		  'TestExternal',
		  'Unpitched',
		  '_DOC_ORDER',
		  '_MOD',
		  '__builtins__',
		  '__cached__',
		  '__doc__',
		  '__file__',
		  '__loader__',
		  '__name__',
		  '__package__',
		  '__spec__',
		  'base',
		  'beam',
		  'common',
		  'copy',
		  'duration',
		  'editorial',
		  'environLocal',
		  'environment',
		  'exceptions21',
		  'expressions',
		  'interval',
		  'noteheadTypeNames',
		  'pitch',
		  'stemDirectionNames',
		  'tie',
		  'unittest',
		  'volume']

它们中的一些是音符类型-以大写开头的那些。那些类我们之后会接触到，比如 `Lyric` 
对象。(顺带一提:这些对象可以从完整文档中找到相关解释。你可以在之后阅读它们
如果你好奇，困惑或者在回放Mad Men，不过你现在不需要了解这些。)

## (高级题外话)

如果你十分了解Python，并且你恐惧污染你的命名空间，作为输入"`from music21 import *`"
你可以输入 

		import music21
		
从而在所有需要用到 `note` 的场合，你可以以 `music21.note` 来调用它

		>>> music21.note 
		<module 'music21.note' from 'D:\music21files\music21\note.pyc'>

如果你是一个Python大师，你将知道这个。可能如果你不知道这个，但是你听说过
"污染你的命名空间"，你有一个Python大师朋友而他对此尖叫"永远不要使用 `import *`!"
起码在这个教程相信我，这么做将会更简便，如果你可以无视你的朋友。到最后，你将
知道遵从什么建议才是对你来说最自然的。

_(从题外话中的题外话中返回正文)_

很好，所以现在你知道了关于模块和对象的知识。让我们创建一个 `note.Note` 对象。
它是高音谱号里的一个F:

		f=note.Note("F5")
		
我们使用传统记法，中央C是C4，比它高一个八度的是C5,以此类推（译:即从大字组1开始推
数字无视小字组那些混乱记法的方法）。

现在，你有了一个音符。它在哪？它存在变量 `f` 中。你可以通过输入 `f` 来查询它:

		f
		
		 <music21.note.Note F>
		 
你可以看到它的确是一个F并且它具有5的八度，这可以通过访问 `.name`与`.octave`
属性于 `Note` 对象，`f` :

		f.name
		
		 'F'
		
		f.octave
		
		 5
		
还有一个叫 `.pitch` 的属性，其返回另一个对象

		f.pitch
		
		 <music21.pitch.Pitch F5>
		
很好，可是这并没有告诉你任何你还不知道的东西！让我们看看其他属性来告诉你一些你
不知道的东西。它们中的一些是子属性，就是说它们有两个点来用来访问。这里有一个
`pitch` 的子属性，这里把它看成一个对象的属性，叫  `.frequency` :

		f.pitch.frequency
		
		 698.456462866008
		 
另一个子属性叫 `pitch.pitchClassString`

		f.pitch.pitchClassString`
		
		 '5'
		 
这非常好！所以一个f是698hz(如果A4是440hz),并且它的音高是第五类（以C=0,C#=Db=1
开始推F所具有的八度内的音高编号。）

有一系列你需要注意的东西。

* 1.你的 `frequency` 可能有很长的数字位而不是"..."。对于我来说，它返回了 
"698.456462866008".在这个文档，我们有时写成"..."而不写完（对于字符串也是如此）。
这样做一部分原因是为了保存空间，也因为长数字的最后几位根据计算机，32位/64位
，Mac还是PC乃至季节会取到不同的数。而我不知道你的电脑具体情况，如果只是略微
的差别请不要担心。
* 2.由单引号为围起来输出（像`f.name` 返回的 `'F'`，而 `f.octave` 返回 `5` 则并
非如此）。引号意味着这个属性返回的是一个字符串（由字符数字符号组成）。
而没有引号则意味着其返回的是一个数字（要么是一个整数要么如果它有一个小数点，
则被称为 `float` 浮点数）。你可以完全把浮点数当成小数。

(也许会有一个寂寞的计算机科学家在一场聚会上对 `floats` 以长篇大论的形式对你做出
解释，无论如何我们只需要知道使用浮点数比使用小数对于计算机更快即可)

字符串 `5` 与数字5的区别有别要记住。在Python中（像大多数现代编程语言一样）我们
使用双等号（==）来询问这两个东西是否相同，像这样：

		f.octave==5
		
		True
		
这是我们期待的，但是如果尝试

		f.pitch.pitchClassString==5`
		
		False
		
这是因为 `5=='5'` 结果是 `False` .(有一些可爱的编程语言如JavaScript与Perl会的得到
`True` ;但Python并不是它们中的一员。这起初看起来是一个麻烦，但之后你也许会发现
这样做有好处的)。所以为了查看是否 `f.pitchClassString` 的值是 `'5'` 我们需要创建一个
`'5'`字符串通过用引号包住它:

		f.pitch.pitchClassString == "5"
		
		True
		
在Python它对于你使用单引号还是双引号进行包围无所谓:

		f.pitch.pitchClassString == '5'
		
		True
		
`pitchClassString` 这个名称暗示了你它返回一个字符串。而如果使用 `.pitch.pitchClass`
它就会返回一个数字

		f.pitch.pitchClass
		
		5
		
对于音符"F"它们的结果是类似的（除了一个是字符串另一个是整数以外），但是对于
B-flat（B-flat。sharp # 升调，flat b/- 降调 ）, `.pitchClass` 结果是10而 `.pitchClassString`
结果是"A"，这种情况就有区别。

让我们继续创建B-flat音符。在 `music21` 中，sharps是用"#"表示，正如你期望的
。但是flats是用"-"表示。这是因为难以说明Note `b` （在这个例子中你可以写成
大写或小写）与符号 `flat`。所以让我们创建B-flat音符：

		bflat=note.Note("B-2")
		
我这里将其赋给变量"`bflat`"。你可以使用`Bb`，也可以使用"`b_flat`"，但是不能是
"`b-flat`"，因为减号不能用作变量名。

		b-flat = note.Note("B-2")
		
		  File "<ipython-input-17-d519b3e88921>", line 1
			b-flat = note.Note("B-2")
									 ^
		SyntaxError: can't assign to operator

这个符号有一个变调符号（accidental），你可以通过使用 `.pitch.accidental` 取得它。

		bflat.pitch.accidental
		
		<accidental flat>
		
这里我们有一个不是数字也没有引号包围的形式。这一般意味着它是一个对象，由
`.accidental` 返回的另一个对象-在这个例子是一个 `Accidental` 对象。正如我们上面
看到的，对象有一些属性，`Accidental` 对象也不例外。所以让我们创建一个新变量
让其保存 `bflat` 的变调符号:

		acc=bflat.pitch.accidental
		
我们稍后介绍 `Accidental` 对象的全部属性。但在这里我们介绍两个: `.alter` 与 
`displayLocation` 。第一个可以显示这个 `Accidental` 从 `Note` 微调了多少：

		acc.alter
		
		-1.0
		
因为这个`Accidental` 是降调，这个 `.alter` 是一个负数。注意到它并不是一个整型，而
是一个浮点数。这暗示着music21支持四分音，在这个例子中无所谓这个。

返回这两行， `acc=bflat.pitch.accidental` 与 `acc.alter`。我们设置 `acc` 为 `bflat.pitch`
的 `.accidental` 属性的值。然后我们从变量取得其 `.alter` 的值。我们甚至可以跳过第一步
直接"链式调用"最后的属性值:

		bflat.pitch.accidental.alter
		
		-1.0
		
		acc.displayLocation
		
		'normal'
		
很高兴我们得知我们设定了一个有意义的默认值。如果你希望变调符号显示在音符的上面，
你需要自己手动设定

		acc.displayLocation = 'above'
		acc.displayLocation
		
		'above'
		
我们的变量 `"acc"` 与`bflat` 的属性是_同一个_值。（以计算机的术语，`acc`是引用了）
`.accidental`）.所以现在如果我们查看`.displayLocation`从`bflat.pitch.accidental`中。我们
也会发现它被设置了愚蠢的"above"值。

		bflat.pitch.accidental.displayLocation
		
		'above'
		
Python是那一类可以动态增加属性的编程语言（一些人认为这会使得对象混乱，但是我
不介意这个）为了某些明显的原因，我Note对象没有属性 "`wasWrittenByStockhausen`".
所以如果你尝试访问，你将得到一个错误

		bflat.wasWrittenByStockhausen
		
		---------------------------------------------------------------------------

		AttributeError                            Traceback (most recent call last)

		<ipython-input-25-3e7bfdcb790a> in <module>()
		----> 1 bflat.wasWrittenByStockhausen


		AttributeError: 'Note' object has no attribute 'wasWrittenByStockhausen'

但是如果你想要设置这个可怕的值，你可以这样写:

		bflat.wasWrittenByStockhausen = True
		f.wasWrittenByStockhausen = False

然后你可以写 "if" 语句看看这是真还是假

		if bflat.wasWrittenByStockhausen == True:
			print("Hope you're enjoying Sirius!")

		 Hope you're enjoying Sirius!

注意在最后一行的"print"命令前面你应该加一个空格。Python使用空格来追踪哪些部分
在if语句（以及其他类似的语句）里面哪些不在。

(如果你没有找到上面有关Stockhausen的笑点，清查阅widipedia)。

而对于f来说，什么事都不会发生因为我们设置了其.wasWrittenByStockhausen为False

		if f.wasWrittenByStockhausen == True:
			print("I love Helicopters!")

到这个时间点你也许已经被编程语言搞烦了而只想看看或者演奏你那该死的音符！
如果你已经安装了MusicXML读取器像MuseScore,Finale,Sibelius或者Finale Notepad,你可
以输入:

		f.show()
		
(一张乐谱的图)

并且看到它。我们默认创建的是四分音符。我们将在一分钟内得到其他长度的音符。注意到
我们还设置了一个有意义的谱号。否则你不能知道它的确是 `F5` .

如果你想要听到它（并且你在Windows或Unix或者老Mac(10.5或更早)上），输入:

		f.show('midi')
		
你也许会需要等待几秒，如果你正在网上都这个文档，"大钢琴"声效江北载入，它有1M大小。

令人抓狂的是，Apple从OSX10.6(Snow Leopard)以及更后版本的的QuickTime(QuickTime X)
中移除了对MIDI的支持(包括Mountain Lion)。所以你需要获取更老的Quick Time7从
appleQuicktime中来让其能够执行。

当我们输入 `f.octave` 我们不用输入任何括号在其后。但是当我们调用 `f.show()` 
我们不用输入任何括号在其后。但是当我们调用总是需要在后面加上它。甚至如果
里面什么都没有(在这种情况下，我们将使用默认的.show格式，其一般是指musicxml)

`.show()` 是调用了 `Note` 对象的一个方法，而 `.octave` 则是访问了一个属性。
可以把方法当成动词("O Note:show thyself!")，而把属性当成对对象的修饰和描述。
调用任何方法需要括号在其后，而括号里面你可以放一些其他东西（“参数”），其
控制这个行为将如何具体实现。作为例子，让我们创建一个新音符，`D` 通过
从B-flat加一个大三度（"M3"）:

		d=bflat.transpose("M3")
		d
		
		<music21.note.Note D>
		
		bflat
		
		<music21.note.Note B->
		
取代在原音符处发生改变，`transpose()`方法返回一个新的 `note.Note` 对象，其表示
经过这个提升音调(或者下降，如果你传入"-M3")操作后得到的东西。

如果你想要改变tflat它本身，你可以增加一个"inPlace=True"给参数对于 `.transpose()`
通过用逗号分隔这两个参数。让我们让它自增一个全四度:

		bflat.transpose("P4", inPlace = True)
		bflat
		
		<music21.note.Note E->
		
当然现在 `bflat` 是一个差劲的名字来表示我们的这个变量。你可以输入 "`eflat=bflat`"
然后用eflat来表示它。但是你可能不需要不需要经常这么做。另一方面，music21有一些
奇怪的区间，所以让我们回到变量`d`上（这里 `d`没有受到bflat在原处变换的影响）
让我们给它加一个doubly-diminished sixth:

		whatNoteIsThis = d.transpose('dd6')
		whatNoteIsThis

		 <music21.note.Note B--->

B三减！很久没有看到这种东西了！让我们检查音符的 `.pitch.accidental.alter` 与它的
`.pitch.accidental.name` 。它们是子属性，意味着它们有三个点:

		whatNoteIsThis.pitch.accidental.alter

		 -3.0
		 
		whatNoteIsThis.pitch.accidental.name

		 'triple-flat'
		 
最后一件事:不是所有音符都有accidental。`d`对象就没有，所以它返回 `None`，
这是一个特殊值，不会产生任何输出值

		d.pitch.accidental
		
如果你想要确定它是 `None`，你可以尝试打印它

		print(d.pitch.accidental)

		None
		
当 `d.accidental` 是 `None` 是否意味着 `d.accidental.name` 也是 `None`

		d.pitch.accidental.name
		
		---------------------------------------------------------------------------

		AttributeError                            Traceback (most recent call last)

		<ipython-input-39-e15f6baf8e9d> in <module>()
		----> 1 d.pitch.accidental.name


		AttributeError: 'NoneType' object has no attribute 'name'

并不是！事实上它产生了一个错误（这里我们也称其为“抛出一个异常”）。这是因为
有别于获取 `Accidental` 对象从 `.accidental` 像我们之前做的那样。我们获取了一个
`NoneType` 对象（i.e.,`None`）。 `Accidental` 对象有一个叫 `name` 的属性，但是对象
`None` 没有（这就像之前尝试 `.wasWrittenByStockhausen` 在你定义出这个属性之前
那样）。

当你只是在IDLE或命令行中输入，抛出异常并没有什么大问题，但是当你在运行一个程序
异常将自动导致程序崩溃（停止运行）。所以我们尝试保证我们的 `Notes` 的确拥有
`accidentals` 属性在我们打印 `.accidental`的名称之前。于是我们像这样使用 `if` 语句:

		if d.pitch.accidental is not None:
			print(d.pitch.accidental.name)

这个方法比直接试图打印 `d.pitch.accidental.name` 要更安全。在 `d.pitch.accidental` 不是
`None` 的情况下它会正常工作，如果是 `None` Python将不会试图运行第二行。（如果运行
了将导致崩溃）

如果由于某些原因 `d` 没有 `.pitch`，我们将需要测试其是否是 `None` 在检查其子
属性 `.pitch.accidental` 之前。

这将成为一个好时机介绍休止符，首先让我们创建一个 `Rest` :

		r=note.Rest(type="whole")
		
确保输入了"()"(双括号)符号在 `note.Rest` 否则之后将发生一些奇怪的事情（技术的说
你取得了类 `note.Rest` 的引用，这种用法将在第十章时介绍，但不是现在）

		r.show()
		
(一个音符的图片)

...但是当你尝试以 `midi` 文件格式show它，不要期望有什么东西。

一个 `Rest` 是一个对象类型，其没有 `pitch` 属性在上面，所以自然地它也没有
`pitch.accidental`:

		r.pitch
		
		---------------------------------------------------------------------------

		AttributeError                            Traceback (most recent call last)

		<ipython-input-43-1b757368671c> in <module>()
		----> 1 r.pitch


		AttributeError: 'Rest' object has no attribute 'pitch'
		
最后一件事:注意我们永远不会使用像叫 `note` 的变量名来保存一个 `note.Note` 对象。
不要这么做，如果你像这样输入（不要这样输入如果你想就这样继续用户指南）:

		note=note.Note("C#3")
		
哦，现在你被困住了。你将你的 `Note` 对象存在 `note` 里，但是我们需要 `note` 模块
来产生新的 `Note` 对象，而现在你没有方法取得它了。（这是所谓的“污染命名空间”
问题，正如你的Python大师朋友告诉你的一样）。所以除非你是奥地利皇帝，并且
可以抱怨“音符太多了”。你也许还想要创建更多的 `note.Note` 对象在之后。
所以不要用 `note` 作为变量名字。(类似的观点可以用于, `pitch` , `scale` , `key` , 'clef' 
等等。你将看到我使用类似 `myNote` , `myClef` 之类的名字来避免这个问题）

很好，现在你已经了解了 `Note` 对象的基础知识。让我们前往
[第三章:音高和时长](http://music21.readthedocs.org/en/latest/usersGuide/usersGuide_03_pitches.html#usersguide-03-pitches)