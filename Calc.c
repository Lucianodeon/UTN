#include<stdio.h>
int producto(int z, int t){
int m,i,n;
if (z==0||t==0)
    z=0;
else{
    if (t>0){
        m=z;
        for(i=0;i<t-1;i++){
            z+=m;}}
    else {
        if (z>0){
            m=z;n=t;n-=(t+t);t=n;
            for(i=0;i<t-1;i++){z+=m;}
            m=z;z-=(m+m);}
        else{ m=z;z-=(m+m);m=z;n=t;n-=(t+t);t=n;
        for(i=0;i<t-1;i++){z+=m;}}}}
return z;}
void division (int x, int y , int *z , int *j){
int b=0,r=0,k=0,v=0,flag=0,aux;
if (x<0&&y<0){
    aux=x;x-=(aux+aux);
    aux=y;y-=(aux+aux);
    flag=1;}
else {
    if (x>0&&y<0){
        aux=y;y-=(aux+aux);v=1;}
    else{
        if (x<0&&y>0){
            aux=x;x-=(aux+aux);v=1;flag=1;}
        else;}}
if(x==y){k=1;r=0;}
else
    {if (x<y){k=0;r=x;}
    else{
        while (b!=1)
            {x-=y; k++;
            if (x<y){r=x;b=1;}
            else{
                if (x==y){k++;r=0;b=1;}
                else;}}}}
if (v==1){aux=k;k-=(aux+aux);*j=k;}
else {*j=k;}
if (flag==1){aux=r;r-=(aux+aux);*z=r;}
else *z=r;}
main(){
int p,i,a,b,o,j,q;
j=0;q=0;
printf("Ingrese Cantidad de Pares de Numeros a Calcular\n"); scanf("%d",&p);
for (i=0;i<p;i++){
    printf("ingrese un par de numeros\n");
    scanf("%d%d",&a,&b);
    o=producto(a,b);
    printf("La multiplicacion es:%d\n",o);
    if(b==0)
    printf("Error al Dividir por CERO\n");
    else {division(a,b,&q,&j);
            printf("La Division es:%d\nEl resto es:%d\n",j,q);}
    }
system("pause");}
