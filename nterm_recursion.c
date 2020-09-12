// finding out nth term by recursion (basic of recursion)

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.
// n>3

int find_nth_term(int n, int a, int b, int c) {
    int sum;  
    if(n==3)
    {  
        return c;
    }
    else 
    {
    sum=find_nth_term(n-1,b,c,a+b+c);
    
    }
    return sum;
}

int main() {
    int n, a, b, c;
  
    scanf("%d %d %d %d", &n, &a, &b, &c);
    int ans = find_nth_term(n, a, b, c);
 
    printf("%d", ans); 
    return 0;
}

