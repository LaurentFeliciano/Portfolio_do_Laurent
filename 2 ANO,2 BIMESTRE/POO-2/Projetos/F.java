import java.util.Scanner;
public class F {
        public static void main(String args[]){
            Scanner entrada = new Scanner(System.in);
            int n = Integer.parseInt(entrada.nextLine());
            String C[] = new String[1000];
            double D[] = new double[1000];
            n++;
            for(int i=0;i<=n-1;i++){
                 C[i] = entrada.nextLine();
                 D[i] = Double.parseDouble(entrada.nextLine());
            }
            boolean parar = false;
            double aux_C=0;
            String aux_D=""; 
            while(!parar){
                 parar = true;
                 for(int i=0;i<=n-2;i++){
                      if(D[i] > D[i+1]) {
                        aux_C = D[i];
                        D[i] = D[i+1];
                        D[i+1] = aux_C;
                        
                        aux_D = C[i];
                        C[i] = C[i+1];
                        C[i+1] = aux_D; 
                        parar = false;
                      }
                 }
            }
            
            for(int i=1;i<=3;i++)
               System.out.println(String.format("%s %2.2f",C[i],D[i]));
            
           
        }
}