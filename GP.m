clc;
clear;
%�����Ⱥ����Լ��ʾ���Զ�����Լ����ϵ��
%�����Ⱥ��������Ӧ���������ͼ򲢶�
[Chart1,Dege1]=Return_point_group();
%�����Լ��ʾ���������Ϊ����
X0=input('�������Լ��ʾ��������֮���ÿո������','s');
X=strread(X0,'%d');
%�����ܲ�����h
i=1;h=0;
while i<=length(Dege1(1,:))
    h=h+Dege1(i,i);
    i=i+1;
end
%�ֱ������Լ��ʾԼ����ĸ���ϵ��
i=1;
while i<=length(X);
    Y(i)=1/h*Chart1(i,:)*Dege1*X;
    i=i+1;
end
disp(Y')

