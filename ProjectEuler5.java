/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is divisible by all of the numbers from 1 to n?
*/

import java.util.*;

public class ProjectEuler5 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            for(int result = n;result<800000;result++ ){
                int counter=0;
                for(int i=1;i<=n;i++){
                    if(result%i==0){
                        counter++;
                    }
                }
                if(counter==n){
                    System.out.println(result);
                    break ;
                }
            }
        }
        in.close();
    }
}