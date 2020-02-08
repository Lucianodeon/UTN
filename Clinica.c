#include<stdio.h>
main(){
int n,i,numhc[500],cv[500],k,nhc,cap,x,c,aux,aux1,nv[500],g;
float valc[500],ia[500],aux3,aux2,j,f;
printf("ingrese la cantidad de pacientes a atender\n");scanf("%d",&n);
for (i=0;i<n;i++){
    printf("\nIngrese:\nNumero de Historia clinica:\t");scanf("%d",&numhc[i]);
    printf("\nValor de Cuota:\t");scanf("%f",&valc[i]);
    printf("\nCoutas vencidas:\t");scanf("%d",&cv[i]);
    ia[i]=valc[i]*cv[i];
    printf("\nImporte adeudado:\t%f\n",ia[i]);}
printf("\nIngrese Historia Clinica a Actualizar:\t");scanf("%d",&nhc);
while(nhc!=0){
    k=0;i=0;
    while (k==0&&i<n){
        if (nhc==numhc[i]) k=1;
        else i++;}
    if (k==0){
        printf("\nNo se encontro Historia Clinica");}
    else {
        printf("\nNumero de Historia clinica:\t%d",numhc[i]);
        printf("\nValor de Cuota:\t%f",valc[i]);
        printf("\nCoutas vencidas:\t%d",cv[i]);
        printf("\nImporte adeudado:\t%f",ia[i]);
        printf("\nCantidad de cuotas a pagar:\t");
        scanf("%d",&cap);
        cv[i]-=cap;
        j=valc[i];
        f=cap;
        ia[i]-=j*f;
        system("cls");
        printf("\nNumero de Historia clinica:\t%d",numhc[i]);
        printf("\nValor de Cuota:\t%f",valc[i]);
        printf("\nCoutas vencidas:\t%d",cv[i]);
        printf("\nImporte adeudado:\t%f\n",ia[i]);
        system("pause");
        system("cls");}
    printf("\nIngrese Historia Clinica a Actualizar:\n");
    scanf("%d",&nhc);}
c=0;
for (i=0;i<n;i++){
    if (cv[i]>5)
        {nv[c]=numhc[i];c++;}
    else;}
if (c==0)
    printf("No hay Historias Clinicas con mas de 5 cuotas vencidas\n");
else{printf("Las Historias Clinicas con mas de 5 cuotas vencidas son:\n");
    for(i=0;i<c;i++) printf("%d\n",nv[i]);}
k=0;x=n;
while (k==0){
    k=1;x--;
    for(i=0;i<x;i++){
        if (numhc[i]>numhc[i+1]){
        k=0;
        aux=numhc[i];numhc[i]=numhc[i+1];numhc[i+1]=aux;
        aux1=cv[i];cv[i]=cv[i+1];cv[i+1]=aux1;
        aux2=valc[i];valc[i]=valc[i+1];valc[i+1]=aux2;
        aux3=ia[i];ia[i]=ia[i+1];ia[i+1]=aux3;}
        ;}}
for(i=0;i<n;i++){printf("\nNumero de Historia clinica:\t%d",numhc[i]);
        printf("\nValor de Cuota:\t%f",valc[i]);
        printf("\nCoutas vencidas:\t%d",cv[i]);
        printf("\nImporte adeudado:\t%f\n",ia[i]);}
system("pause");}






