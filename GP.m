clc;
clear;
%输入点群及可约表示，自动计算约化的系数
%输入点群，返回相应的正交标表和简并度
disp('目前支持如下点群的计算(c3v oh td d2h d4h)')
[Chart1,Dege1,ReRe1]=Return_point_group();
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
%判断计算出的系数是否为整数，若有整数，则说明输入的可约表示有误，用flag参数表明出现错误
i=1;flag=1;
while i<=length(Y);
	if rem(Y(i),1)~=0
        fprintf('可约表示错误，无法化简');
        flag=0;
        break;
    end
    i=i+1;
end
%由flag阐述判断是否输出结果
%格式化输出结果，将系数与相应的不可约表示结合
i=1;
while i<=length(Y)&&flag==1;
    if Y(i)~=0
        fprintf('%1.0f%s',Y(i),ReRe1{i});
        fprintf('   ');
    end
    i=i+1;
end
