def head(size=int, text=str):
    if 0 < int(size) <= 6:
        t = "#" * size + " " + text
    elif int(size) < 0:
        t = "# " + text
    elif int(size) > 6:
        t = "#" * 6 + " " + text
    return t


def para(text=str):
    t = text + "\n"
    return t


def line(text=str):
    t = text + "<br>"
    return t


def bold(text=str):
    t = "**" + text + "**"
    return t


def italic(text=str):
    t = "*" + text + "*"
    return t


def bold_and_italic(text=str):
    t = "***" + text + "***"
    return t


def cite(text=list):
    t = ""
    for i in range(0, len(text)):
        if isinstance(text[i], str):  # 元素是字符串
            if text[i] == "":  # 字符串为空
                t += ">"
            else:
                t += "> %s" % text[i]
        else:  # 元素不是字符串
            for i_ in range(0, len(text[i])):
                t += ">> %s" % text[i][i_]
    return t


def ordered_list(text=list):
    t = ""
    for i in range(0, len(list)):
        if isinstance(text[i], str):  # 元素是字符串
            t += "%d. %s" % (i+1, text[i])
        else:  # 元素是列表
            for i_ in range(0, len(text[i])):
                t += "  %d. %s" % (i_+1, text[i][i_])
    return t


def unordered_list(text=list):
    t = ""
    for i in range(0, len(text)):
        if isinstance(text[i], str):  # 元素是字符串
            t += "- %s" % text[i]
        else:  # 元素是列表
            for i_ in range(0, len(text[i])):
                t += "  - %s" % text[i][i_]
    return t


def code(text=str):  # 代码
    t = "'" + text + "'"
    return t


def code_block(text=str):  # 代码块
    t = "   " + text
    return t


def fence_code(text=str, lauguage=""):  # 围栏代码块
    t = ""
    if lauguage != "":
        t += "'''\n" + text + "'''\n"
    else:
        t += "'''" + lauguage + "\n" + text + "'''\n"
    return t


def separation():  # 分隔线
    t = "***\n"
    return t


def link(display=str, path=str, title=str):  # 超链接
    if title != "":
        t = "[%s](%s \"%s\")" % (display, path, title)
    else:
        t = "[%s](%s)" % (display, path)
    return t


def web(text=str):  # 网址
    t = "<%s>" % text
    return t


def picture(alt=str, path=str, title=str):  # 图片
    t = "![%s](%s \"%s\")" % (alt, path, title)
    return t


def change(text=str):  # 转义
    if text[0:3] == "***":
        t = "\\" + text[0] + "\\" + text[1] + "\\" + text
    elif text[0:2] == "**":
        t = "\\" + text[0] + "\\" + text
    else:
        t = "\\" + text
    return t


def form(title=list, element=list, align=""):  # 列表
    """
    element参数排列方式应该是一行一行，而不是一列一列

    """
    t = ""
    # 绘制标题
    for i in range(0, len(title)):
        t += "|" + title[i]
    t += "|\n"
    # 绘制对齐栏
    for i in range(0, len(title)):
        if align[i] == "":
            t += "|" + "---"
        elif align[i] == "left":
            t += "|" + ":---"
        elif align[i] == "middle":
            t += "|" + ":---:"
        elif align[i] == "right":
            t += "|" + "---:"
    t += "|\n"
    # 绘制列表
    for i in range(0, len(element)):
        for i_ in range(0, len(element[i])):
            t += "|" + element[i][i_]
        t += "|\n"
    return t


def definition(text=list):  # 定义列表
    t = ""
    for i in range(0, len(text)):
        for i_ in range(0, len(text[i])):
            if i_ == 0:
                t += text[i][0] + "\n"
            else:
                t += ": " + text[i][i_] + "\n"
        t += "\n"
    return t


def deletion(text=str):  # 删除线
    t = "~~" + text + "~~"
    return t


def task_list(choose=list, text=list):  # 任务列表
    t = ""
    for i in range(0, len(choose)):
        if choose[i]:
            t += "- [x] " + text[i] + "\n"
        else:
            t += "- [] " + text[i] + "\n"
    return t
