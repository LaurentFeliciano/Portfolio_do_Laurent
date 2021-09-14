import java.util.Scanner;
public class E {
        public static void main(String args[]){
            Scanner entrada = new Scanner(System.in);
            int n = Integer.parseInt(entrada.nextLine());
            int X[] = new int[1000];
            for(int i=0;i<=n-1;i++) {   
               int Y = Integer.parseInt(entrada.nextLine());
               int A = Integer.parseInt(entrada.nextLine());
               X[i] = Math.abs(Y - A) + 2;
            }
              for(int i=0;i<=n-1;i++)
                System.out.println(String.format("%C",X[i]) );    
        }
}