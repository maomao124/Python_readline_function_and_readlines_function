"""
 * Project name(项目名称)：Python_readline函数和readlines函数
 * Package(包名):
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30
 * Time(创建时间)： 12:53
 * Version(版本): 1.0
 * Description(描述)： readline()函数
readline() 函数用于读取文件中的一行，包含最后的换行符“\n”。
file.readline([size])
其中，file 为打开的文件对象；size 为可选参数，用于指定读取每一行时，一次最多读取的字符（字节）数。
 """

if __name__ == '__main__':
    file = open("test1.py", "r", encoding="utf-8")
    print(file.readable())
    print(file.writable())
    print(file.readline(), end="")
    print(file.readline(), end="")
    print(file.readline(), end="")
    print(file.readline(), end="")
    print(file.readline(), end="")
    print(file.readline(), end="")
    print(file.readline(), end="")
    print(file.readline(5), end="")
    print(file.readline(5), end="")
    print(file.readline(5), end="")
    print(file.readline(5), end="")
    print(file.readline(5), end="")
    print(file.readline(5), end="")
    print(file.readline(5), end="")
