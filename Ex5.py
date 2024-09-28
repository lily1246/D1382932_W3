a=int(input('輸入一個三位數:'))
b=a//100
c=a//10%10
d=a%10
e=d*100+c*10+b
print('結果',e)