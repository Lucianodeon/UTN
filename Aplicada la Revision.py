# -*- coding: utf-8 -*-
"""
Created on Sun May  5 14:39:01 2019

@author: pablo
"""

import numpy as np
import math
from matplotlib import pyplot as plt

NACA2415=np.loadtxt('NACA 2415.txt')
top_density=np.loadtxt('density top.txt')
top_density=top_density[top_density[:,0].argsort()]
buttom_density=np.loadtxt('density bottom.txt')
buttom_density=buttom_density[buttom_density[:,0].argsort()]
top_pressure=np.loadtxt('pressure top.txt')
top_pressure=top_pressure[top_pressure[:,0].argsort()]
buttom_pressure=np.loadtxt('pressure bottom.txt')
buttom_pressure=buttom_pressure[buttom_pressure[:,0].argsort()]
NACA2415top=np.loadtxt('NACA 2415 top.txt')
NACA2415top=NACA2415top[NACA2415top[:,0].argsort()]
NACA2415buttom=np.loadtxt('NACA 2415 buttom.txt')
NACA2415buttom=NACA2415buttom[NACA2415buttom[:,0].argsort()]

#Toma de datos
#print('Numero de mach?')
M=0.5#float(input())
#print('R del gas?')
R=287#float(input())
#print('K del gas?')
K=1.4#float(input())
#print('temperatura del gas?')
T0=288#float(input())
#print('presion del infinito')
P0=101325#float(input())
#print('angulo de ataque')
alpha=5
#Calculos

#C del infinito
C=np.sqrt(K*T0*R)
#velocidad del infinito
V0=M*C
den0=P0/(R*T0)
print('velocidad del infinito:',V0)
Cte=(K/(K-1))*(P0/den0)+V0**2*0.5 #float(1004*T0+V0*V0*0.5)
print(Cte)
plt.figure(figsize=(10.24, 2.56))
plt.title("NACA2415") 
plt.xlabel("x") 
plt.ylabel("y") 
plt.plot(NACA2415[:,0],NACA2415[:,1]) 
plt.show()

#Punto A

#Calculo del modulo de la velocidad superior
vsup=np.zeros((len(top_pressure), 2))
vsup[:,0]=top_pressure[:,0]
i=0
while i<len(vsup):
    vsup[i,1]=np.sqrt(2*(Cte-((K/(K-1))*top_pressure[i,1]/(top_density[i,1]))))
    i+=1
#plt.title("velocidad sobre extrados") 
#plt.plot(vsup[:,0],vsup[:,1])
#plt.show()

#Calculo del modulo de la velocidad inferior
vinf=np.zeros((len(buttom_pressure), 2))
vinf[:,0]=buttom_pressure[:,0]


i=0
while i<len(buttom_pressure):
    if (Cte-((K/(K-1))*buttom_pressure[i,1]/(buttom_density[i,1])))<0 :
        vinf[i,1]=0
        i+=1
    else:
        vinf[i,1]=np.sqrt(2*(Cte-((K/(K-1))*buttom_pressure[i,1]/(buttom_density[i,1]))))
        i+=1
        
#plt.title("velocidad sobre intrados") 
#plt.plot(vinf[:,0],vinf[:,1])
#plt.show()


plt.figure(figsize=(10,10))

#leyendas del ploteo
plt.title("Velocidades sobre el perfil") 
plt.xlabel("posicion sobre cuerda (m)") 
plt.ylabel("velocidad (m/s)")
#ploteo del perfil
plt.plot(NACA2415[:,0],NACA2415[:,1]*500) 
#ploteo de campo de velocidades superios
l1=plt.plot(vsup[:,0],vsup[:,1],'r',label='velocidad de extrados')
#ploteo de campo de velocidades inferior
l2=plt.plot(vinf[:,0],vinf[:,1],'g',label='velocidad de intrados')
plt.legend(loc='upper right')
#configuracion del ploteo
plt.axes().set_aspect( 'auto')
plt.savefig('01-a.png')
plt.show()

#Punto B
den0=P0/(R*T0)

#Cp superior
Cpsup=np.zeros((len(top_pressure),2))
Cpsup[:,0]=top_pressure[:,0]
Cpsup[:,1]=(top_pressure[:,1]-P0)/((1/2)*den0*V0**2)

#Cp inferior
Cpinf=np.zeros((len(buttom_pressure),2))
Cpinf[:,0]=buttom_pressure[:,0]
Cpinf[:,1]=(buttom_pressure[:,1]-P0)/((1/2)*den0*V0**2)

#Ploteo

plt.figure(figsize=(10,10))
#leyendas del ploteo
plt.title("Coeficientes de presion") 
plt.xlabel("posicion sobre cuerda (m)") 
plt.ylabel("Cp en(J/kgK)")
#ploteo del perfil
#plt.plot(NACA2415[:,0],NACA2415[:,1]) 
#ploteo de Cp superior
l1=plt.plot(Cpsup[:,0],Cpsup[:,1],'r',label='Cp extrados')
#ploteo de Cp inferior
l2=plt.plot(Cpinf[:,0],Cpinf[:,1],'g',label='Cp intrados')
plt.legend(loc='upper right')
#configuracion del ploteo
plt.axes().set_aspect( 'auto')
plt.savefig('01-b.png')
plt.show()

#Punto c

#calculo del area de los paneles por producto vectorial
Asup=np.zeros((len(NACA2415top)-1,3))
i=0
k=[0,0,-1]
while i<len(NACA2415top)-1:
    Asup[i,0]=NACA2415top[i+1,0]-NACA2415top[i,0]
    Asup[i,1]=NACA2415top[i+1,1]-NACA2415top[i,1]
    Asup[i,:]=np.cross(Asup[i,:],k)
    i+=1
    
Ainf=np.zeros((len(NACA2415buttom)-1,3))
i=0
k=[0,0,-1]
while i<len(NACA2415buttom)-1:
    Ainf[i,0]=NACA2415buttom[i+1,0]-NACA2415buttom[i,0]
    Ainf[i,1]=NACA2415buttom[i+1,1]-NACA2415buttom[i,1]
    Ainf[i,:]=np.cross(Ainf[i,:],k)
    i+=1

#calculo del promedio de presiones superior por paneles
    
presion_promedio_superior=np.zeros((len(NACA2415top)-1))
dummy=np.zeros((len(top_pressure)))
i=0
j=0

while j<len(NACA2415top)-1:
    dummy[:]=0
    while i<len(top_pressure):
        if NACA2415top[j,0]<top_pressure[i,0]<NACA2415top[j+1,0]:
            dummy[i]=top_pressure[i,1]
            i+=1
        else:
            i+=1
    presion_promedio_superior[j]=np.average(np.trim_zeros(dummy))
    j+=1
    i=0

#calculo del promedio de presiones inferior por paneles

presion_promedio_inferior=np.zeros((len(NACA2415buttom)-1))
dummy=np.zeros((len(buttom_pressure)))
i=0
j=0

while j<len(NACA2415buttom)-1:
    dummy[:]=0
    while i<len(buttom_pressure):
        if NACA2415buttom[j,0]<buttom_pressure[i,0]<NACA2415buttom[j+1,0]:
            dummy[i]=buttom_pressure[i,1]
            i+=1
        else:
            i+=1
    presion_promedio_inferior[j]=np.average(np.trim_zeros(dummy))
    j+=1
    i=0


#fuerzas superior
Fsup=np.zeros((len(NACA2415top)-1,3))
Fsup[:,0]=(-presion_promedio_superior[:]+P0)*Asup[:,0]
Fsup[:,1]=(-presion_promedio_superior[:]+P0)*Asup[:,1]

#fuerzas inferior
Finf=np.zeros((len(NACA2415top)-1,3))
Finf[:,0]=(presion_promedio_inferior[:]-P0)*Ainf[:,0]
Finf[:,1]=(presion_promedio_inferior[:]-P0)*Ainf[:,1]



#calculo de resultante de fuerzas

F=np.zeros((1,2))
F[0,0]=np.sum(Fsup[:,0])+np.sum(Finf[:,0])
F[0,1]=np.sum(Fsup[:,1])+np.sum(Finf[:,1])

theta = np.radians(alpha)
c, s = np.cos(theta), np.sin(theta)
rotation = np.array(((c,-s), (s, c)))


D=np.dot(F,rotation)[0,0]
L=np.dot(F,rotation)[0,1]

print('La sustentacion es %.2f N y la resistencia %.2f N '%(L,D))

Cl=L/(0.5*den0*V0**2)
Cd=D/(0.5*den0*V0**2)

print('El Cl es:%f \nEl Cd es:%f'%(Cl,Cd))

    
#vector distancia superior

vec_dist_sup=np.zeros((len(NACA2415top)-1,3))

i=0
while i<len(NACA2415top)-1:
    vec_dist_sup[i,0]=-0.25+(NACA2415top[i+1,0]-NACA2415top[i,0])*0.5+NACA2415top[i,0]
    x=(NACA2415top[i+1,0]-NACA2415top[i,0])*0.5+NACA2415top[i,0]
    vec_dist_sup[i,1]=((NACA2415top[i+1,1]-NACA2415top[i,1])/(NACA2415top[i+1,0]-NACA2415top[i,0]))*(x-NACA2415top[i,0])+NACA2415top[i,1]
    i+=1

#vector distancia inferior

vec_dist_inf=np.zeros((len(NACA2415buttom)-1,3))

i=0
while i<len(NACA2415buttom)-1:
    vec_dist_inf[i,0]=-0.25+(NACA2415buttom[i+1,0]-NACA2415buttom[i,0])*0.5+NACA2415buttom[i,0]
    x=(NACA2415buttom[i+1,0]-NACA2415buttom[i,0])*0.5+NACA2415buttom[i,0]
    vec_dist_inf[i,1]=((NACA2415buttom[i+1,1]-NACA2415buttom[i,1])/(NACA2415buttom[i+1,0]-NACA2415buttom[i,0]))*(x-NACA2415buttom[i,0])+NACA2415buttom[i,1]
    i+=1
#grafico de fuerzas

plt.figure(figsize=(10,10))
plt.title("Fuerzas sobre paneles") 
plt.xlabel("x (m)") 
plt.ylabel("y (m)")
plt.plot(NACA2415[:,0],NACA2415[:,1]) 
plt.quiver(vec_dist_sup[:,0]+0.25,vec_dist_sup[:,1],Fsup[:,0]*7,Fsup[:,1]*7,width=0.001,scale=30000,headwidth=25,headlength=25)
plt.quiver(vec_dist_inf[:,0]+0.25,vec_dist_inf[:,1],Finf[:,0]*7,Finf[:,1]*7,width=0.001,scale=30000,pivot='tip',headwidth=25,headlength=25)
plt.axes().set_aspect('equal', 'datalim')
plt.savefig('01-c1.png')
plt.show()

#grafico de ayuda para visualizar los momentos

plt.figure(figsize=(10,10))
plt.title("NACA2415") 
plt.xlabel("x") 
plt.ylabel("y")
plt.plot(NACA2415[:,0],NACA2415[:,1]) 
plt.quiver(0.25,0,vec_dist_sup[:,0],vec_dist_sup[:,1],width=0.001,scale=1.1,headwidth=10,headlength=10)
plt.quiver(vec_dist_sup[:,0]+0.25,vec_dist_sup[:,1],Fsup[:,0],Fsup[:,1],width=0.001,scale=30000,headwidth=10,headlength=10)
plt.axes().set_aspect('equal', 'datalim')
plt.show()
   
plt.figure(figsize=(10,10))
plt.title("NACA2415") 
plt.xlabel("x") 
plt.ylabel("y")
plt.plot(NACA2415[:,0],NACA2415[:,1]) 
plt.quiver(0.25,0,vec_dist_inf[:,0],vec_dist_inf[:,1],width=0.001,scale=1.1,headwidth=10,headlength=10)
plt.quiver(vec_dist_inf[:,0]+0.25,vec_dist_inf[:,1],Finf[:,0],Finf[:,1],width=0.001,scale=30000,headwidth=10,headlength=10)
plt.axes().set_aspect('equal', 'datalim')
plt.show()

#Calculo de momentos superior
i=0
Msup=np.zeros((len(Fsup),3))
while i<len(Msup):
    Msup[i,:]=np.cross(vec_dist_sup[i,:],Fsup[i,:])
    i+=1

#Calculo de momentos inferior
i=0
Minf=np.zeros((len(Fsup),3))
while i<len(Minf):
    Minf[i,:]=np.cross(vec_dist_inf[i,:],Finf[i,:])
    i+=1

Moa=np.sum(Msup[:,2])+np.sum(Minf[:,2])
print('el momento aerodinamico es:%.2f'%Moa)

Cm=Moa/(0.5*den0*V0**2)
print('el coeficiente de momento es:%.4f'%Cm)