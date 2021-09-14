import java.util.Scanner;
public class C {
        public static void main(String args[]){
                Scanner entrada = new Scanner(System.in);
                int n = Integer.parseInt(entrada.nextLine());
                int soma = 0;
                int idade[] = new int[1000];
                int i=0;
                for(;i<=n-1;i++){
                     idade[i] = Integer.parseInt(entrada.nextLine());
                     soma+=idade[i];    
                }
                idade[i] = Integer.parseInt(entrada.nextLine());
                int soma2 = 0;
                int n2 = i;
                for(i=0;i<=n2;i++){
                     soma2+=idade[i]; 
                }
                double media = (double)soma/n;
                double media2 = (double)soma2/(n2+1);
                
                if(media2 > media) {
                     double diferenca = media2 - media;
                     if(diferenca > 1)
                       System.out.println("Media das idades aumenta em mais de 1 ano");
                     else     
                         System.out.println("Media das idades aumenta em menos de 1 ano");
                } else {
                     double diferenca = media - media2;
                     if(diferenca > 1)
                        System.out.println("Media das idades diminui em mais de 1 ano");
                     else
                        System.out.println("Media das idades diminui em menos de 1 ano");                                                                  
                    }
        }
}