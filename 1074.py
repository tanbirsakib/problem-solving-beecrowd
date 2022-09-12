i = int(input())

for j in range(i):
    num = int(input())
    if num>0 :
        if num%2==0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    if num<0: 
        if num%2 == 0:
            print('EVEN NEGATIVE')
        else:
            print("ODD NEGATIVE")
    if num == 0:
        print('NULL')