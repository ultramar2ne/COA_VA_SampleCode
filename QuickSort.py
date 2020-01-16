import random

def outPut(num): #출력함수
    for i in range(0,12):
        print(num[i] , end=" ")

def Swap(num , L , R): #두개의 수 비교후 저장
    ex = num[L]
    num[L] = num[R]
    num[R] = ex

def comPare(num,left,right): #정리를 위한 함수
    L = left
    R = right
    pnum = int((L+R)/2)
    pivot = num[pnum]

    while(L <= R):
        while(num[L] < pivot):
            L+ = 1
        while(num[R] > pivot):
            R- = 1

        if(L <= R):
            if(L != R):
                Swap(num,L,R)
            L = L+1
            R = R-1

    if(left < R):
        comPare(num,left,R)
    if(L < right):
        comPare(num,L,right)
    outPut(num)
    print("\n")


print("퀵 정렬 프로그램 \n")

num = list()

for i in range(1,13):
    num.append(i)
    random.shuffle(num)

outPut(num)
print("\n\n퀵 정렬")
comPare(num,0,11)
outPut(num)
