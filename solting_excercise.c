// 파일명: solting_excercise
// 이  름: CHOI JINWOOK
// 이메일: jinsrobot@naver.com
// 작성일: 2020/01/10
// 수정일: 2020/01/12

#include <stdio.h>
#include <time.h>

#define _CRT_SECURE_NO_WARNINGS
#define SWAP(a,b) {int j = a; a = b; b = j;}
#define nMax 10     //Maximum value of randNum array

typedef enum{       //bool 타입 구현
    true = 0,
    false = 1
} bool;

void printArray();
int setRand();

main()
{
    int selNum;
    int randNum[nMax];

    while (1) {

        selNum = 0;
        setRand(randNum);

        printf("Sample number : ");
        printArray(randNum,false);
        printf("What do you want to do..?\n");
        printf("\nplz select \n(1)Solting (2)Searching (3)Exit >> ");
        scanf("%d",&selNum);

        if (selNum == 1){
            printf("\nSolting Exercise\n");
            printf("Select sorting method\n");
            printf("(1)bubble (2)selection (3)insertion (4)Quick (5)exit >> ");
            scanf("%d", &selNum);
            //arraySorting(selNum);

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
            startMessage(selNum);  //need some loop expression
        }

    }
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
    return 0;
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
