/*

*/

import java.util.*;

public class ProjectEuler9 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            int b,c;
            long prod=-1;
            for(int a=1;a<=n/3; a++){
                b=(n*n - 2*n*a)/(2*n - 2*a);
                c=n-a-b;
                if(c*c == a*a + b*b)
                    if(a*b*c > prod)
                        prod=a*b*c;
            }
            System.out.println(prod);
        }
        in.close();
    }
}