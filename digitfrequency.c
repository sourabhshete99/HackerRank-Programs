// calculate the frequency of each digit how many times each digit has occured in given string

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    char s[1000];
    scanf("%s", s);

    int cnt,l=strlen(s);
    for(int j=0;j<10;j++)
    {   cnt=0;

        for(int i=0;i<l;i++)
        {   
           if(s[i]>='0' && s[i]<='9')
            {   if((s[i]-'0')==j)
                {   cnt++;  }
            }   
        }

        printf("%d ",cnt);    
    }
    return 0;
}

