// 파일명: solting_excercise
// 이  름: CHOI JINWOOK
// 이메일: jinsrobot@naver.com
// 작성일: 2020/01/10
// 수정일: 2020/01/12
//***********************************************************
// 업데이트 내역 : Bubble Sort 알고리즘 구현 by Oaflias
//              : Selection Sort 그리고 Insertion Sort 알고리즘 구현 by Oaflias
// 최종 업데이트 날짜 2020/01/14
// **********************************************************


#include <stdio.h>
#include <time.h>

#define _CRT_SECURE_NO_WARNINGS
#define SWAP(type,a,b) do{type t=a;a=b;b=t;}while(0)
#define nMax 10     //Maximum value of randNum array

typedef enum{       //bool 타입 구현
    true = 0,
    false = 1
} bool;

void printArray();
int setRand();
void arraySorting(int randNum[],int input_Num);
void arraySearching(int randNum[],int input_Num);
int main()
{
    int selNum;
    int randNum[nMax];

    while (1) {

        selNum = 0;
        setRand(randNum);

        printf("\n Sample number : \n");
        printArray(randNum,false);
        printf("What do you want to do..?\n");
        printf("\nplz select \n(1)Sorting (2)Searching (3)Exit >> ");
        scanf("%d",&selNum);

        if (selNum == 1){
            printf("\nSorting Exercise\n");
            printf("Select sorting method\n");
            printf("(1)bubble (2)selection (3)insertion (4)Quick (5)exit >> ");
            scanf("%d", &selNum);
            arraySorting(randNum,selNum);

        }else if (selNum == 2) {
            printf("\nSearching Excercise\n");
            printf("Select searching method\n");
            printf("(1)binary (2)tree (3)exit >> ");
            scanf("%d", &selNum);
            //arraySearching(selNum);

        }else if (selNum == 3) {
            printf("오케이~ 바이~ \n");
            break;

        } else {
            printf("It's wrong select, plz select again. \n\n");
        }
    }
    return 0;
}

void printArray(int Array[], bool mode)
{
    int count = 0;
    int i;
    for (i = 0; i < nMax; i++){
        printf("%2d ",Array[i]);       //두자리수 출력
        if (mode == 1 && count++>3){   //조건 만족 시 5개씩 출력
            printf("\n");
            count = 0;
        }
    }
}

int setRand(int randNum[]){ //난수 생성
    srand((unsigned)time(NULL));
    int i,j;
    for(i = 0;i < nMax;i ++){       // sizeof(array)/sizeof(int) -> array.length
        randNum[i] = rand() % (nMax+1); 
        for(j = 0;j<i;j++){
            if (randNum[j] == randNum[i])
            {
                i--;
            }
        }
    }
    return randNum;
}

void arraySorting(int randNum[],int input_Num){
    while(input_Num!=5){
        if(input_Num==1){           //Bubble Sort
            for(int i=0;i<nMax-1;i++){
                for(int j=nMax-1;j>i;j--){
                    if(randNum[j-1]>randNum[j]){
                        SWAP(int,randNum[j-1],randNum[j]);
                    }
                }
            }
            printf("Bubble Sorting Completed\n");
            printArray(randNum,false);
            input_Num=5;    
            break;
        }
        else if(input_Num==2){
            //Selection Sort
            int index_min;
            for(int i=0;i<nMax-1;i++){
                index_min=i;
                for(int j=i+1;j<nMax;j++){
                    if(randNum[j]<randNum[index_min]){
                        index_min=j;
                    }
                }
                if (i != index_min){
                    SWAP(int,randNum[i],randNum[index_min]);
                }
                
            }
            printf("Selection Sorting Completed\n");
            printArray(randNum,false);
            input_Num=5;    
            break;
        }
        else if(input_Num==3){
            //Insertion Sort
            int temp,j;
            for(int i=1;i<nMax;i++){
                temp=randNum[i];
                for(j=i;j>0 && randNum[j-1]>temp;j--){
                    randNum[j]=randNum[j-1];
                }
                randNum[j]=temp;
            }
            printf("Insertion Sorting Completed\n");
            printArray(randNum,false);
            input_Num=5;    
            break;
        }
        else if(input_Num==4){
            //Quick Sort

        }
        else{
            printf("It's wrong select, plz select again. \n\n");
            printf("Select sorting method\n");
            printf("(1)bubble (2)selection (3)insertion (4)Quick (5)exit >> ");
            scanf("%d", &input_Num);
        }
    }
}

void arraySearching(int randNum[],int input_Num){
    while(input_Num!=3){
        if(input_Num==1){
            //Binary Search

        }
        else if(input_Num==2){
            //Tree Search

        }
        else{
            printf("\nSearching Excercise\n");
            printf("Select searching method\n");
            printf("(1)binary (2)tree (3)exit >> ");
            scanf("%d", &input_Num);
        }
    }
}
