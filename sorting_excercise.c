// 파일명: sorting_excercise
// 이  름: CHOI JINWOOK
// 이메일: jinsrobot@naver.com
// 작성일: 2020/01/10
// 수정일: 2020/01/30

#define _CRT_SECURE_NO_WARNINGS
#define SWAP(a,b) {temp = a; a = b; b = temp;}
#define nMax 10     //Maximum value of randNum array

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef enum {       //bool 타입 구현
	true = 1,
	false = 0
} bool;

void printArray(int Array[], bool mode);
void arraySorting(int Array[], int mode);
void setRand(int randNum[]);

int main()
{
	int selNum;
	int randNum[nMax];

    char sortMode[][10] = {"0","Bubble","Selection","Insertion","Quick"};

	while (1)
    {
		selNum = 0;
		setRand(randNum);

        printf("\nSorting Exercise\n");
        printf("\nRandom number >>\n");
        printArray(randNum, true);
        printf("Select sorting method\n");
		printf("(1)Bubble (2)Selection (3)Insertion (4)exit >> ");
		scanf("%d", &selNum);

        if (selNum == 4){
            printf("The end the program. Thank you.\n");
            break;
        } else if (selNum == 1 || selNum == 2 || selNum == 3){
			arraySorting(randNum,selNum);
            printf("\n%s Sorting Completed >>\n",sortMode[selNum]);
      		printArray(randNum,true);
        }else{
            printf("\nNumber what you choose is not correct\n");
            printf("Plz select correct number! \n");
        }
        
	}
	return 0;
}

void printArray(int Array[], bool mode){
	int count = 0;
	int i;

	for (i = 0; i < nMax; i++) {
		printf("%2d ", Array[i]);       //두자리수 출력
		if (mode == 1 && count++>3) {   //조건 만족 시 5개씩 출력
			printf("\n");
			count = 0;
		}
	}
	printf("\n");
}

void setRand(int randNum[]) { //난수 생성
	srand((unsigned int)time(NULL));
	int i, j;
	for (i = 0; i < nMax; i++) {       // sizeof(array)/sizeof(int) -> array.length
		randNum[i] = rand() % (nMax + 1);
		for (j = 0; j<i; j++) {
			if (randNum[j] == randNum[i])
			{
				i--;
			}
		}
	}
}


void arraySorting(int array[], int mode){
    //if mode 1 is bubble, 2 selection, 3 insertion sort Algorithm
    int i,j,temp;
	
	switch (mode)
    {
    case 1:         //bubble
        for(i = 0 ; i < nMax-1 ; i++){
            for(j = nMax-1 ; j > i ; j--){
                if(array[j-1] > array[j]){
                    SWAP(array[j-1],array[j]);
                    printArray(array,false);
                }
            }
        }
        break;

    case 2:         //selection
		for(i=0; i<nMax-1; i++){
    		temp= i;
    		for(j=i+1; j<nMax; j++){
      			if(array[j]<array[temp])
        			temp = j;
    		}
    		if(i!= temp){
				//SWAP(array[i], array[temp]);// 메크로 함수가 잘 작동하지 않음...
				j = array[i];
				array[i] = array[temp];
				array[temp] = j;
    		}
            printArray(array,false);
 		}
        break;

    case 3:       //Insertions
        for (i = 1 ; i < nMax ; i++) {
            temp = array[i];
            for(j = i ; j > 0 && array[j-1] > temp ; j--){
                array[j] = array[j-1];
            }
            array[j] = temp;	
            printArray(array,false);	
        }
        break;

    default:
        break;
    }
}
