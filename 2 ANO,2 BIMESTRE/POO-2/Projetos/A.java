import java.util.Scanner;
public class A {
        public static void main(String args[]){
                Scanner entrada = new Scanner(System.in);
                int n = Integer.parseInt(entrada.nextLine());
                double custo_cerca[] = new double[n];
                for(int i=0;i<=n-1;i++) {
                   double x = Double.parseDouble(entrada.nextLine());
                   double y = Double.parseDouble(entrada.nextLine());
                   double v = Double.parseDouble(entrada.nextLine());
                   double lado = (x*x) - (y*y);
                   double p1 = Math.sqrt(lado);
                   double P = p1 + x + y;
                   custo_cerca[i] = P * v;        
                }  
                for(int i=0;i<=n-1;i++)   
                    System.out.println(String.format("R$ %2.2f",custo_cerca[i]));
                  
        }
}