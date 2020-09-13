/*
The sum of the squares of the first ten natural numbers is, 385.
The square of the sum of the first ten natural numbers is, 3025.
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640.
Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.
t is the number of test cases.
*/
import java.util.*;

public class ProjectEuler6 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            long n = in.nextInt();
            double sqsum=Math.pow((n*(n+1))/2,2);
            double sumsq=(n*(n+1)*((2*n)+1))/6;
            System.out.println((long)(sqsum-sumsq));
        }
        in.close();
    }
}
