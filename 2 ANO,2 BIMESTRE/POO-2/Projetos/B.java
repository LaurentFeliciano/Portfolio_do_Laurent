import java.util.Scanner;
public class B {
        public static void main(String args[]){
            Scanner entrada = new Scanner(System.in);
               
               /*double mat1[][] = {{4, 5, 6},
                                 {9,  2, 1},
                                 {-1,  3, 9}};
                                 
               double mat2[][] = {{1,2},
                                  {0,1},
                                  {2,0}};  
                                  
                double mat3[][] = {{16,13},
                                  {11,20},
                                  {17,1}}; */
                                   
           
          /* System.out.println(mat3[1][0]);
           
           System.out.println(mat2[0][0]);
           System.out.println(mat2[0][1]);
           
           System.out.println(mat2[2][0]);
           System.out.println(mat2[2][1]);   */
           
           double mat1[][] = new double[3][3];
           double mat2[][] = new double[3][2];
           double mat3[][] = new double[3][2];
           
           for(int i=0;i<=2;i++){
               for(int j=0;j<=2;j++){
                     mat1[i][j] = Double.parseDouble(entrada.nextLine());                    
               }
           }
           
           for(int i=0;i<=2;i++){
               for(int j=0;j<=1;j++){
                     mat2[i][j] = Double.parseDouble(entrada.nextLine());                    
               }
           }  
           
            for(int i=0;i<=2;i++){
               for(int j=0;j<=1;j++){
                     mat3[i][j] = Double.parseDouble(entrada.nextLine());                    
               }
           }
           
                           
           double x = mat3[1][0]-(mat2[0][0]*mat2[0][1] + mat2[2][0]*mat2[2][1]);
           
           for(int i=0;i<=2;i++){
               for(int j=0;j<=2;j++){
                     if((i==1 && j == 0) || (i==2 && j == 2))
                         mat1[i][j] = x;
                         System.out.print(mat1[i][j]+" ");
                     
              }
                System.out.println();
            }
//           System.out.println(x);


        }
}