// converting a number in binary and find out maximum number of consecutive 1's in that binary number

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
    private static final Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int rem,s=0,t=0;
        while(n>0)
        {   rem=n%2;
            n=n/2;

            if(rem==1)
            {   s++;
                if(s>=t)
                {   
                    t=s;
                }
            }
            else
            {   s=0;
            }
        }
        System.out.print(t);
    }
}
