clc;
clear;
%输入点群及可约表示，自动计算约化的系数
%输入点群，返回相应的正交标表和简并度
[Chart1,Dege1]=Return_point_group();
%输入可约表示，并将其存为矩阵
X0=input('请输入可约表示（数与数之间用空格隔开）','s');
X=strread(X0,'%d');
%计算总操作数h
i=1;h=0;
while i<=length(Dege1(1,:))
    h=h+Dege1(i,i);
    i=i+1;
end
%分别求出可约表示约化后的各个系数
i=1;
while i<=length(X);
    Y(i)=1/h*Chart1(i,:)*Dege1*X;
    i=i+1;
end
disp(Y')

