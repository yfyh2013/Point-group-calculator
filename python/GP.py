# coding:utf-8
from __future__ import print_function
import numpy
import Get_point_group


class GroupPointCalculator:

    def __init__(self):
        self.Chart = ''
        self.Dege = ''
        self.IrReRe = ''
        self.ReRe = ''
        self.ReRe_input = ''
        self.Result = []
        self.h = 0

    def calculator(self):

        # 获取点群数据
        self.Chart, self.Dege, self.IrReRe = Get_point_group.get_point_group()

        # 获取可约表示
        print('请输入可约表示（数与数之间逗号隔开）')
        self.ReRe_input = raw_input()
        # 输入的字符串转为列表
        self.ReRe = list(eval(self.ReRe_input))
        if len(self.ReRe) != len(self.IrReRe):
            print('输入的可约表示不正确')

        # 计算h 总操作数
        i = 0
        while i <= len(self.ReRe) - 1:
            self.h += self.Dege[i, i]
            i += 1

        # 计算可约表示系数
        i = 0
        while i <= len(self.ReRe) - 1:
            self.Result.append(numpy.dot(numpy.dot(self.Chart[i], self.Dege), self.ReRe) * 1 / self.h)
            i += 1

        # 判断答案是否正确
        i = 0
        flag = ''
        while i <= len(self.Result) - 1:
            if self.Result[i] % 1 != 0 or self.Result[i] < 0:
                print('可约表示错误，无法化简')
                flag = 1
                break
            i += 1

        # 格式化输出
        i = 0
        while i <= len(self.Result) - 1 and flag == '':
            if self.Result[i] != 0:
                print('%1.0f%s ' % (self.Result[i], self.IrReRe[i]), end='')
            i += 1
        print('')


if __name__ == '__main__':
    GP = GroupPointCalculator()
    print('目前支持如下点群的计算(c3v oh td)')
    while 1:
        try:
            GP.calculator()
        except StandardError as e:
            print('输入错误,请检查')
        finally:
            print('------')
