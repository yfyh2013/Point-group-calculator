clc;
clear;
%�����Ⱥ����Լ��ʾ���Զ�����Լ����ϵ��
%�����Ⱥ��������Ӧ���������ͼ򲢶�
disp('Ŀǰ֧�����µ�Ⱥ�ļ���(c3v oh td d2h d4h)')
[Chart1,Dege1,ReRe1]=Return_point_group();
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
%�жϼ������ϵ���Ƿ�Ϊ������������������˵������Ŀ�Լ��ʾ������flag�����������ִ���
i=1;flag=1;
while i<=length(Y);
	if rem(Y(i),1)~=0
        fprintf('��Լ��ʾ�����޷�����');
        flag=0;
        break;
    end
    i=i+1;
end
%��flag�����ж��Ƿ�������
%��ʽ������������ϵ������Ӧ�Ĳ���Լ��ʾ���
i=1;
while i<=length(Y)&&flag==1;
    if Y(i)~=0
        fprintf('%1.0f%s',Y(i),ReRe1{i});
        fprintf('   ');
    end
    i=i+1;
end
