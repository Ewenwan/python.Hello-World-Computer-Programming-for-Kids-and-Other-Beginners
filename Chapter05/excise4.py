# -*- coding: cp936 -*-
length = float(raw_input("�����뷿��ĳ���"))
width = float(raw_input("�����뷿��Ŀ�"))
price = float(raw_input("������ÿƽ���ߵ�̺�ļ۸�"))
areaM = length * width
areaC = areaM * 9
totalPrice = areaC * price
print "�ܹ���Ҫ",areaM,"ƽ���׵�̺"
print "�ܹ���Ҫ",areaC,"ƽ���ߵ�̺"
print "��̺�ܼ۸�",totalPrice
