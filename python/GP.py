#coding:utf-8
from __future__ import print_function
import numpy
import Return_point_group

print ('目前支持如下点群的计算(c3v oh td)')
#获取点群数据
Chart,Dege,IrReRe = Return_point_group.point_group()
print ('请输入可约表示（数与数之间逗号隔开）')
ReRe_input = raw_input()
#输入的字符串转为列表
ReRe = list(eval(ReRe_input))
ReRe = numpy.array(ReRe)
if len(ReRe) != len(IrReRe):
    print ('输入的可约表示不正确')
#计算h 总操作数
i=0
h=0
while i<=len(ReRe)-1:
    h += Dege[i,i]
    i += 1
print ('h = %d'%h)
#计算可约表示系数
i=0
Result = []
while i<=len(ReRe)-1:
    Result.append(numpy.dot(numpy.dot(Chart[i],Dege),ReRe) *1/h)
    i += 1
#判断答案是否正确
i=0
flag = 1
while i<=len(Result)-1:
    if Result[i]%1 != 0:
        print ('可约表示错误，无法化简')
        flag = 0
        break
    i += 1
#格式化输出
i=0
while i<=len(Result)-1 and flag==1:
    if Result[i]!=0:
        print ('%1.0f%s '%(Result[i],IrReRe[i]),end='')
    i += 1
print ('')
print ('计算完成')
print ('')