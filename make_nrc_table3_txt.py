#0 프로젝트 초기화
#Excel Read & Write Lib.
from openpyxl import load_workbook
from openpyxl import Workbook
import datetime
import os

f = open('NRC_TDP_case22.txt', mode='wt', encoding='utf-8')
 
#1 len(Byte) 입력
nByte = input(">> N-Byte = ")
nBit = 8*int(nByte)

#2 NRC AND 조건 입력 Byte[n];Bit[n];Value
tc_NRC = input(">> Test Condition (Byte[n];Bit[n];Value) : ")
list_NRC = []
list_NRC = tc_NRC.split(';')

#3-1 nBit 중 NRC 조건에 해당하는 Bit의 index 생성
p = 0
idx_cond = []
idx_value = []
#print(len(list_NRC)/3)
while ( p < int(len(list_NRC)/3) ):
    #print('p = %d' %p)
    idx_temp = (nBit-1) - (int(list_NRC[p*3])*8 + int(list_NRC[p*3+1]))
    idx_cond.append(idx_temp)
    idx_temp = int(list_NRC[p*3+2])
    idx_value.append(idx_temp)
    #print('idx_cond[%d] = %d' %(p,idx_cond[p]))
    #print('idx_value[%d] = %d' %(p,idx_value[p]))
    p = p+1

#3-2 nByte*8 경우의 수 생성
bn_i = []
tmp_i = []

n = 1

for i in range(0,pow(2,nBit)):
    hx_i = hex(int(i))
    hx_i = hx_i[2:]
    bn_i = bin(int(i))
    bn_i = bn_i[2:].zfill(nBit)

    for p in range(0,int(len(list_NRC)/3)):
        if str(idx_value[p]) in str(bn_i[int(idx_cond[p])]):
            #bn_i = bn_i
            if(p == int(len(list_NRC)/3) - 1):
                #print('==============================')
                #print('idx_cond[%d] = %d' %(p,idx_cond[p]))
                #print('idx_value[%d] = %d' %(p,idx_value[p]))
                #print('NRC : %s' %bn_i)
                f.write(hx_i)
                f.write('=')
                f.write(bn_i)
                f.write('\r\n')
                
        else:
            break

f.close()