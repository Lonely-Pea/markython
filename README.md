# markython
## markython模块介绍
Markython是一个能让你使用纯Python语法写Markdown标记语言的模块，与其配套的编写程序为MarkythonEditor，你可以上我的Github仓库寻找MarkythonEditor寻找源代码进行学习和使用。<br>
## markython实现原理
markython通过一些函数将你输入的文本转化为markdown文本，并返回结果为字符串值。<br>比如说你想要写一个Markdown表格，你就只需要调用模块内的函数form(title=list, element=list, align=list)，填写好相关参数，函数就能将你输入的内容智能转化为markdown语言并返回结果。<br>实现原理就是通过处理输入的参数，将他们处理转化为markdown语言。<br>
## markython的所有函数
|函数|参数|
|:---|:---|
|head()|size=int, text=str|
|para()|text=str|
|line()|text=str|
|bold()|text=str|
|italic()|text=str|
|bold_and_italic()|text=str|
|cite()|text=list|
|ordered_list()|text=list|
|unordered_list()|text=list|
|code()|text=str|
|code_block()|text=str|
|fence_code()|text=str, lauguage=""|
|separation()|\/|
|link()|display=str, path=str, title=str|
|web()|text=str|
|picture()|alt=str, path=str, title=str|
|change()|text=str|
|form()|title=list, align="", element=list|
|definition()|text=list|
|deletion()|text=str|
|task_list()|text=list|

## markython安装教程
要安装markython到你的python并在你的python文件中直接调用，你需要下载markython.py并存放到你python安装目录下的.Lib内.<br>或者你也可以再终端输入"pip install markython"来进行安装(当前不可用)。<br>安装好后你就可以在Python文件内通过"import markython"或者"from markython import *"使用markython。<br>
## markython鸣谢
感谢Lonely-Pea的编写！<br>感谢各位使用者的支持！<br>可以的话能点个star吗？<br>
