"""
使用python语法编辑.md文件

以下是一些函数：
1.head(size=int, text=str)  # 标题
2.para(text=str)  # 段落
3.line(text=str)  # 换行
4.bold(text=str)  # 粗体
5.italic(text=str)  # 斜体
6.bold_and_italic(text=str)  # 粗体和斜体
7.cite(text=list)  # 引用
8.ordered_list(text=list)  # 有序列表
9.unordered_list(text=list)  # 无序列表
10.code(text=str)  # 代码
11.code_block(text=str)  # 代码块
12.fence_code(text=str, lauguage="")  # 围栏代码块
13.separation()  # 分隔线
14.link(display=str, path=str, title=str)  # 超链接
15.web(text=str)  # 网址
16.picture(alt=str, path=str, title=str)  # 图片
17.change(text=str)  # 转义
18.form(title=list, align="", element=list)  # 列表
19.definition(text=list)  # 定义列表
20.deletion(text=str)  # 删除线
21.task_list(choose=list, text=list)  # 任务列表

cite(引用)示例：
1.
代码：
lst = ["Markython", "", ["A good module to make markdown file."]]
print(cite(text=lst))
结果：
>Markython
>
>>A good module to make markdown file.
2.
代码：
lst = [bold("Markython"), "", ["A good module to make" + bold_and_italic("markdown") + "file."]]
print(cite(text=lst))
结果：
>**Markython
>
>A good module to make ***markdown*** file.

ordered_list(有序列表)示例：
1.
代码：
lst = ["Python", "Java", "C", "C++", "C#"]
print(ordered_list(text=lst))
结果：
1. Python
2. Java
3. C
4. C++
5. C#
2.
代码：
lst = ["Python", "Java", ["C", "C", "C++", "C#"], "html"]
print(ordered_list(lst))
结果：
1. Python
2. Java
3. C
    1. C
    2. C++
    3. C#
4. html
3.
代码：
lst = ["Python", "Java", cite("C"), bold("html")]
print(ordered_list(lst))
结果：
1. Python
2. Java
    > C
3. **html**

unordered_list(无序列表)示例：
1.
代码：
lst = ["Python", "Java", "C"]
print(unordered_list(lst))
结果：
- Python
- Java
- C

"""
