/*By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the nth prime number?
t is the number of test cases.*/

import java.util.*;

public class ProjectEuler7 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        int[] prime = new int[10000];
        prime[0]=2;
        int k=1;
        int i=3;
        int count =1;
        while(count<10000){
             boolean flag = true;
            for(int j=3;j<i/2;j++){
                if(i%j==0){
                    flag = false;
                    break; 
                }
            }
            if(flag==true){
                prime[k]=i;
                count++;
                k++;  
            }
            i=i+2;
        } 
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            System.out.println(prime[n-1]);
        }
        in.close();
    }
}