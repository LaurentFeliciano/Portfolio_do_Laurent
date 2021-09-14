import java.util.Scanner;
public class D {
        public static void main(String args[]){
           Scanner entrada = new Scanner(System.in);
           int n = Integer.parseInt(entrada.nextLine());
           double valor_entrada[] = new double[1000]; 
           for(int i=0;i<=n-1;i++){   
              double v = Double.parseDouble(entrada.nextLine()); // Valor Imovel
              int x = Integer.parseInt(entrada.nextLine()); // N. Parcelas
              double y = Double.parseDouble(entrada.nextLine()); // Valor 2 parc.
              double z = Double.parseDouble(entrada.nextLine()); // Valor 4 parc.
              double fator = z / y;
              double q = Math.sqrt(fator);
              
              double a1 = y / q;
              double soma = 0;
              for(int j=1;j<=x;j++){
                   soma+= a1;
                   a1 = a1 * q;
              }
              valor_entrada[i] = v - soma;
           }   
              //System.out.println(soma);
              for(int i=0;i<=n-1;i++)
                System.out.println(String.format("%2.2f", valor_entrada[i]));
                            
        }
}