"""
 * Project name(项目名称)：Python_readline函数和readlines函数
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 12:58
 * Version(版本): 1.0
 * Description(描述)： readlines()函数
readlines() 函数用于读取文件中的所有行，它和调用不指定 size 参数的 read() 函数类似，只不过该函数返回是一个字符串列表，其中每个元素为文件中的一行内容。
 """

if __name__ == '__main__':
    file = open("test2.py", "r", encoding="utf-8")
    fileStr = file.readlines()
    file.close()
    print(fileStr)
    print("---------------------")
    for i in fileStr:
        print(i, end="")
    print("---------------------")
    print("一共", len(fileStr), "行")
