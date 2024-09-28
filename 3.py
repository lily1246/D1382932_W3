a=int(input('輸入數字:'))
result="偶數"*(a%2 ==0)+"奇數"*(a%2!=0)
print(f"{a}是{result}")