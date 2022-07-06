#1000
# a, b =map(int, input().split())
# print(a+b)

#1001
# a, b =map(int, input().split())
# print(a-b)

#1008
# a, b =map(int, input().split())
# print(a/b)

#1271 엄청난 부자2
# n,m = map(int, input().split())
# print(n//m)
# print(n%m)


#1330
# a,b=map(int, input().split())
# if(a>b):
#     print(">")
# elif(a<b):
#     print("<")
# else:
#     print("==")

#2338
# a,b=int(input()), int(input())
# print(a+b)
# print(a-b)
# print(a*b)

#2420
# a,b=map(int, input().split())
# print(abs(a-b))

#2438
# a = int(input())
# for i in range(1,a+1):
#     print("*"*i)

#2475
# a,b,c,d,e = map(int, input().split())
# result = (pow(a,2)+pow(b,2)+pow(c,2)+pow(d,2)+pow(e,2))%10
# print(result)

#2557
# print("Hello World!")

#2558
# a, b =int(input()), int(input())
# print(a+b)

#2738
# n,m=map(int, input().split())
# a=[]
# b=[]

# for j in range(n):
#     a.append(list(map(int, input().split())))
# for j in range(n):
#     b.append(list(map(int, input().split())))

# for i in range(n):
#     for j in range(m):
#         print(a[i][j] + b[i][j], end=" ")  
#     print()

#2739
# n = int(input())
# for i in range(1,10):
#     print(str(n)+" * "+str(i)+" = "+str(n*i))

#2741
# n = int(input())
# for i in range(1,n+1):
#     print(i)

#2743
# a = input()
# print(len(a))

#2744
# s = input()
# print(s.swapcase())

#2753 - 정답1
# year = int(input())
# if year%4==0 and (year%100!=0 or year%400==0) :
#     print(1)
# else :
#     print(0)

#2753 - 정답2
# year = int(input())
# print(1 if year%4==0 and (year%100!=0 or year%400==0) else 0)

#2754-정답1
# grade = input()
# point = {'A+':4.3,'A0':4.0,'A-':3.7,'B+':3.3,'B0':3.0,'B-':2.7,
# 'C+':2.3,'C0':2.0,'C-':1.7,'D+':1.3,'D0':1.0,'D-':0.7,'F':0.0}
# print(point[grade.upper()])

#2754-정답2
# grade = input()
# match grade.upper():
#     case 'A+':
#         print(4.3)
#     case 'A0':
#         print(4.0)
#     case 'A-':
#         print(3.7)
#     case 'B+':
#         print(3.3)
#     case 'B0':
#         print(3.0)
#     case 'B-':
#         print(2.7)
#     case 'C+':
#         print(2.3)
#     case 'C0':
#         print(2.0)
#     case 'C-':
#         print(1.7)
#     case 'D+':
#         print(1.3)
#     case 'D0':
#         print(1.0)
#     case 'D-':
#         print(0.7)
#     case 'F':
#         print(0.0)

#3003
# chess = [1,1,2,2,2,8]#체스판 말 수 
# a=list(map(int,input().split()))#입력값
# dif=[]#chess - a 값 저장할 리스트
# for i in range(6):
#     dif.append(chess[i]-a[i])#차이 값 저장
# for i in dif:
#     print(i, end=" ")

#4101
numlist = []
while(True):
    a,b =map(int,input().split())
    if(a==0 and b==0):
        for i in range(len(numlist)):
            if(numlist[i][0]>numlist[i][1]):
                print('Yes')
            else:
                print('No')
        break
    else:
        numlist.append(list(map(int,(a,b))))







