// 파일명: sorting_excercise
// 이  름: CHOI JINWOOK
// 이메일: jinsrobot@naver.com
// 작성일: 2020/01/10
// 수정일: 2020/01/23

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

void printArray();
void arraySorting();
void setRand();
void quick(int array[], int left, int right);

int main()
{
	int selNum;
	int randNum[nMax];

    char sortMode[][10] = {"0","Bubble","Selection","Insertion","Quick"};
    char searchMode[][10] = {"0","Binary","QUeQUe"};

	while (1)
    {
		selNum = 0;
		setRand(randNum);

		printf("\nshuffle >>\n");
		printArray(randNum, false);
		printf("\nWhat do you want to do..?");
		printf("\nplz select \n(1)Sorting (2)Searching (3)Exit >> ");
		scanf("%d", &selNum);


		if (selNum == 1)
    	{
			printf("\nSorting Exercise\n");
			printf("Select sorting method\n");
			printf("(1)Bubble (2)Selection (3)Insertion (4)Quick >> ");
			scanf("%d", &selNum);


      		printf("\n%s Sorting Completed >>\n",sortMode[selNum]);
			arraySorting(randNum,selNum);
      		printArray(randNum,false);
		}
		else if (selNum == 2)
    	{
			printf("\nSearching Excercise\n");
			printf("Select Searching method\n");
			printf("(1)binary (2)tree >> ");
			scanf("%d", &selNum);
			//arraySearching(selNum);


		}

		else if (selNum == 3)
    	{
			printf("Okay~ Bye~ \n");
			break;
		}
		else {
			printf("\nIt's wrong select, plz select again. \n\n");
		}
	}
	return 0;

}

void printArray(int Array[], bool mode)
{
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

void quick(int array[], int left, int right) {
	int L = left;
	int R = right;
	int pnum = (L + R) / 2;
	int pivot = array[pnum];
	int temp = 0;
	do {
		while (array[L] < pivot) {
			L++;
		}
		while (array[R] > pivot) {
			R--;
		}
		if (L <= R){
			SWAP(array[L], array[R]);
		}		
		L++;
		R--;
		if (left < R) {
			quick(array, left, R);
		}
		if (L < right) {
			quick(array, L, right);
		}
	} while (L <= R);
}

void arraySorting(int array[], int mode){
    //if mode 1 is bubble, 2 selection, 3 quick sort Algorithm

    int i,j,temp;
	

    switch (mode)
    {
    case 1:         //bubble
        for(i = 0 ; i < nMax-1 ; i++){
            for(j = nMax-1 ; j > i ; j--){
                if(array[j-1] > array[j]){
                    SWAP(array[j-1],array[j]);
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
 		}
        break;

    case 3:       //Insertions
        for (i = 1 ; i < nMax ; i++) {
            temp = array[i];
            for(j = i ; j > 0 && array[j-1] > temp ; j--){
                array[j] = array[j-1];
            }
            array[j] = temp;		
        }
        break;

    case 4:       //Quick
		quick(array, 0, nMax-1);
        break;

    default:
        break;
    }
}
