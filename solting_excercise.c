// 파일명: solting_excercise
// 학  번: CHOI JINWOOK
// 이메일: jinsrobot@naver.com
// 작성일: 2020/01/10
// 수정일: 2020/01/10

#include <stdio.h>
#include <time.h>

#define _CRT_SECURE_NO_WARNINGS
#define SWAP(a,b) {int j = a; a = b; b = j;}
#define nMax 10     //Maximum value of randNum array

main()
{
    int selNum;
    int randNum[nMax];

    setRand(randNum);

    while (1) {
      selNum = 0;
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

      }else if{
          printf("오케이~ 바이~ \n");
          break;

      } else {
          printf("It's wrong select, plz select again. \n\n");
          startMessage(selNum);  //need some loop expression
      }

    }
}
