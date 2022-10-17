#include "omp.h"
#include "stdio.h"
#include "string.h"
#define TAM 40

int longitud;
int inicio=0,
int fin;
char plin [TAM];                      
int main(void){
  
  printf("Ingresar palabra : ");
  scanf("%s",palindromo);
  longitud=strlen(palindromo);

        #pragma omp parallel
        {
    int x = omp_get_thread_num();
              if(x != 1){
                printf("Hilo %d\n", x);
        }
              
    #pragma omp critical
        {
    for(fin=longitud-1; plin[fin]==plin[inicio] && fin>=0; inicio++,fin--);
    { if(x == 1){
       if(inicio==longitud){
        printf("Hilo %d Verdadero\n", x);
     }  else { printf ("Hilo %d  Falso\n", x);
       } 
    }}
        }
        }
                         
  return 0;
}