//To calculate sum of digits of a given int number

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    scanf("%d", &n);
    int a,ans=0;
    do
    {   a=(n%10);
        ans=ans+a;
        n=n/10;
    }while (n>=10);
    ans=ans+n;

    printf("%d",ans);

    return 0;
}
