#include<stdio.h>
#include<string.h>
main()

{
    float i,ca1=0,ca2=0,ap2=0,ca3=0,ca4=0,ce=0,b=0,peso,ppn,ta,pesopmin,ppnpmin;

    int ca,tpa;
    char mat[10],matpmin[10];
    printf("Ingrese Cantidad de Operaciones\n");

    scanf("%d",&ca);

    system("cls");

if (ca==0){

    printf("El día de hoy No Arribaran Aviones\n");;system("pause");}

    else{

    for ( i=1 ; i<=ca ; i++ )

    {

    printf("Ingrese Tipo de Avion\n");

    scanf("%d",&tpa);

    switch(tpa)

{

    case 1: ca1++;

    printf("Ingrese: Matricula, Peso y Promedio de Presiones de Neumaticos\n");

    scanf("%s",&mat);

    scanf("%f",&peso);

    scanf("%f",&ppn);

    while (ppn<1||ppn>1.5)

      {ce++;
      printf("Ingrese un Valor de Promedio de Presiones de Neumaticos Valido\n");
      scanf("%f",&ppn);}

    if(b==0)

       {pesopmin=peso;

        strcpy(matpmin,mat);

        ppnpmin=ppn;

        b=1;}

        else{

            if(ppn<ppnpmin){

                strcpy(matpmin,mat);

                pesopmin=peso;

                ppnpmin=ppn;}

                else{}}break;

    case 2:ca2++;

    printf("Ingrese: Matricula, Peso y Promedio de Presiones de Neumaticos\n");

    scanf("%s",&mat);

    scanf("%f",&peso);

    ap2+=peso;

    scanf("%f",&ppn);

    while (ppn<1||ppn>1.5)

      {ce++;

    printf("Ingrese un Valor de Promedio de Presiones de Neumaticos Valido\n");

    scanf("%f",&ppn);}

    break;

     case 3: ca3++;

    printf("Ingrese: Matricula, Peso y Promedio de Presiones de Neumaticos\n");

    scanf("%s",&mat);

    scanf("%f",&peso);

    scanf("%f",&ppn);

    while (ppn<1||ppn>1.5)

      {ce++;

    printf("Ingrese un Valor de Promedio de Presiones de Neumaticos Valido\n");

    scanf("%f",&ppn);}

    break;

      case 4: ca4++;

    printf("Ingrese: Matricula, Peso y Promedio de Presiones de Neumaticos\n");

    scanf("%s",&mat);

    scanf("%f",&peso);

    scanf("%f",&ppn);

    while (ppn<1||ppn>1.5)

      { ce++;

        printf("Ingrese un Valor de Promedio de Presiones de Neumaticos Valido\n");

        scanf("%f",&ppn);}

    break;

    default:printf("Ingrese un Tipo de Aeronave Valido\n");

    i--;}

    }

    if (ca2==0)

        printf("Hoy No Arribaron Embraer 170 o 175 (Tipo 2)\n");

    else

        printf("El Promedio de Pesos de los Aviones Embraer 170 o 175 es: %.2f  Kg \n",ap2/ca2);

    if (b==0)

        printf("Hoy No Arribaron Aviones Boeing 737-800 (Tipo 1)\n");

    else{

        printf("El Avión de ppn mínimo tiene un  Peso de %.2f,  PPN: %.2f Mpa y Matricula es %s \n",pesopmin,ppnpmin,matpmin);}

    if (ca3==0)

        printf("Hoy no Arribaron Aviones Airbus A330-800\n");

    else

        printf("Hoy Arribaron %.2f Aviones Airbus A330-800\n",ca3);

    printf("%.2f porciento de Errores V.S Operacionesn\n",ce*100/ca );

    if (b==0)

    {

        if (ca4==0)printf("Hoy No aterrizaron Boeing 737-800 Ni Aeronaves Pequeñas\n");

        else

        printf("Aterrizaron %.2f Aeronaves Pequeñas, pero no aterrizaron Boeing 737-800\n",ca4);

    }

    else

    {

        if(ca4==0)

         printf ("No aterrizaron Aviones Pequeños, pero aterrizaron %.2f Boeing 737-800\n",ca1);

         else printf ("Aterrizaron %.2f Aviones Pequeños cada Boeing 737-800\n",ca4/ca1);

        }}

system("pause");}
