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
        self.Result = []
        self.h = 0

    def calculator(self):

        # 获取点群数据
        self.Chart, self.Dege, self.IrReRe = Get_point_group.get_point_group()

        # 获取可约表示
        self.ReRe = list(input('请输入可约表示（数与数之间逗号隔开）\n'))
        if len(self.ReRe) != len(self.IrReRe):
            print('输入的可约表示不正确')

        # 计算h 总操作数
        i = 0
        # 总操作数转为浮点型（系数实际不为整数的答案应该是错误的，但由于python整数除法默认结果也为整数，将导致错误）
        self.h = 0.0
        while i <= len(self.ReRe) - 1:
            self.h += self.Dege[i, i]
            i += 1

        # 计算可约表示系数
        i = 0
        # 复位Result，否则答案会保持在第一个计算的结果
        self.Result = []
        while i <= len(self.ReRe) - 1:
            self.Result.append(numpy.dot(numpy.dot(self.Chart[i], self.Dege), self.ReRe) * 1 / self.h)
            i += 1

        # 判断答案是否正确，包含非整数、负数均表示答案出错
        i = 0
        flag = 0
        while i <= len(self.Result) - 1:
            if self.Result[i] % 1 != 0.0 or self.Result[i] < 0:
                print('可约表示错误，无法化简')
                flag = 1
                break
            i += 1

        # 格式化输出
        i = 0
        while i <= len(self.Result) - 1 and flag == 0:
            if self.Result[i] != 0:
                print('%1.0f%s ' % (self.Result[i], self.IrReRe[i]), end='')
            i += 1
        print('')


if __name__ == '__main__':
    GP = GroupPointCalculator()
    print('目前支持如下点群的计算(C3v D3h Oh Td)')
    while 1:
        try:
            GP.calculator()
        except StandardError as e:
            print('输入错误,请检查')
        finally:
            print('------')
