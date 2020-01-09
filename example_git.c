#include <stdio.h>
#include <stdlib.h>
#include <time.h> //난수 지정을 위함

#define _CRT_SECURE_NO_WARNINGS
#define SWAP(a,b) {int j = a; a = b; b = j;}
#define nMax 10     //Maximum value of randNum array

int startMessage(); 
int setRand();
int arraySorting();
void printArray();

void main()
{
    int selNum;
    int randNum[nMax];

    setRand(randNum);
    selNum=startMessage(selNum);
    

    if (selNum == 1){
        printf("\nSolting Algorithm\n");
        printf("Select sorting method\n");
        printf("안녕하세요 졸라 안녕못한 진욱이에요 죽겠네요");

    }else if (selNum == 2) {
        printf("Searching Algorithm");
    }else {
        printf("It's wrong select, plz select again. \n\n");
        startMessage(selNum);  //need some loop expression
    }

}

int startMessage(int selNum){

    printf("Hello world!\n");
    printf("What do you want to do..?\n");
    printf("\nplz select \n(1)cal (2)message (3)third..? >> ");
    scanf("%d",&selNum);

    return selNum;
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

void printArray(int Array[]){
    int count = 0;
    int i;
    for (i = 0; i < nMax; i++){
        printf("%2d ",Array[i]);       //두자리수 출력
        if (count++>3)                 //3개씩 출력 
        {
            printf("\n");
            count = 0;
        }        
    }
    return 0;
}

int arraySorting(int array[], int mode){
    //if mode 1 is bubble, 2 selection, 3 quick sort Algorithm

    int i,j;

    switch (mode)
    {
    case 1:         //bubble
        for (i = 1; i < nMax; i++){
           if (array[i-1] < array[i]){
               SWAP(array[i-1],array[i]);
               i = 1;
           } 
        }            
        break;

    case 2:         //selection
        for ( i = 0; i < nMax; i++){
            for (j =i; j < nMax; j++){
                if (array[i] < array[j]) SWAP(array[i],array[j]);               
            }
        }
        break;
        
    case 3:

        break;        

    default:
        break;
    }
}