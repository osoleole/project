#include<stdio.h>
#include<stdlib.h>

typedef struct point{
    int x;
    int y;
}POINT;

int main(int arg, char **args){
    printf("##########Memory allocation 1 ###########\n");
    int *ma;
    ma = malloc(1024);
    char c = 'B';
    ma[0] =  'A';
    ma[1] = 101;
    // Prints allocated cells
    printf("Allocated  characer %c allocated digit %d not allocated %d\n", ma[0], ma[1], ma[2]);
    free(ma);

    printf("##########Memory allocation 2 ###########\n");
    POINT **pa;
    pa = malloc(1024);
    POINT p1;
    p1.x = 3; 
    p1.y = 5;

}

