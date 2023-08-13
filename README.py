from markython import *


form_function_title = ["函数", "参数"]
form_function_align = ["left", "left"]
form_function_element = [
    ["head()", "size=int, text=str"],
    ["para()", "text=str"],
    ["line()", "text=str"],
    ["bold()", "text=str"],
    ["italic()", "text=str"],
    ["bold_and_italic()", "text=str"],
    ["cite()", "text=list"],
    ["ordered_list()", "text=list"],
    ["unordered_list()", "text=list"],
    ["code()", "text=str"],
    ["code_block()", "text=str"],
    ["fence_code()", "text=str, lauguage=\"\""],
    ["separation()", "\/"],
    ["link()", "display=str, path=str, title=str"],
    ["web()", "text=str"],
    ["picture()", "alt=str, path=str, title=str"],
    ["change()", "text=str"],
    ["form()", "title=list, align=\"\", element=list"],
    ["definition()", "text=list"],
    ["deletion()", "text=str"],
    ["task_list()", "text=list"]
]


text_list = [
    head(1, "markython"),
    "\n",
    head(2, "markython模块介绍"),
    "\n",
    line("Markython是一个能让你使用纯Python语法写Markdown标记语言的模块，与其配套的编写程序为MarkythonEditor，你可以上我的Github仓库寻找MarkythonEditor寻找源代码进行学习和使用。"),
    "\n",
    head(2, "markython实现原理"),
    "\n",
    line("markython通过一些函数将你输入的文本转化为markdown文本，并返回结果为字符串值。"),
    line("比如说你想要写一个Markdown表格，你就只需要调用模块内的函数form(title=list, element=list, align=list)，填写好相关参数，函数就能将你输入的内容智能转化为markdown语言并返回结果。"),
    line("实现原理就是通过处理输入的参数，将他们处理转化为markdown语言。"),
    "\n",
    head(2, "markython的所有函数"),
    "\n",
    form(title=form_function_title, align=form_function_align, element=form_function_element),
    "\n",
    head(2, "markython安装教程"),
    "\n",
    line("要安装markython到你的python并在你的python文件中直接调用，你需要下载markython.py并存放到你python安装目录下的.Lib内."),
    line("或者你也可以再终端输入\"pip install markython\"来进行安装(当前不可用)。"),
    line("安装好后你就可以在Python文件内通过\"import markython\"或者\"from markython import *\"使用markython。"),
    "\n",
    head(2, "markython鸣谢"),
    "\n",
    line("感谢Lonely-Pea的编写！"),
    line("感谢各位使用者的支持！"),
    line("可以的话能点个star吗？"),
    "\n"
]


if __name__ == "__main__":
    # 写入文件
    with open("README.md", "w", encoding="utf-8") as f:
        text = ""
        for i in range(0, len(text_list)):
            text += text_list[i]
        f.write(text)
