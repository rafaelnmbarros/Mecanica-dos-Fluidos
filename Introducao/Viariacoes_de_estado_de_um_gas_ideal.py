# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 11:04:25 2022

@author: Rafael Nascimento
"""

nome=['Ar','Dióxido de carbono','Helio','Hidrogênio','Metano',
      'Monóxido de carbono','Nitrogênio','Oxigênio','Vapor d’água']
R=[286.9,188.9,2077,4124,518.3,296.8,296.8,259.8,461.4]
k=[1.4,1.29,1.66,1.41,1.31,1.4,1.4,1.4,1.3,]

#=====================================================================
#Exemplo - processo isotérmico
#=====================================================================
T=30+273 #Temperatura constante (K)
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6,5))
for gas in range(len(nome)):
    p=[]
    rho=[]
    for pressao in range(1000,100000, 2000):
        p.append(pressao)
        rho.append(pressao/(R[gas]*T))
    ax.plot(rho, p, label=nome[gas], marker='x')
ax.set_title('Variação da densidade e função da pressão em \n um Processo ISOTÉRMICO a T = %s°C' % round(float(T-273),2))
ax.set_ylabel('Pressão (Pa)')
ax.set_xlabel('Densidade (kg/m3)')
ax.set_ylim(0,100000)
ax.set_xlim(0,2)
ax.grid(linestyle='--')
ax.legend()

#=====================================================================
#Exemplo - processo isobárico
#=====================================================================
p=100000 #Pressão constante (Pa)
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6,5))
for gas in range(len(nome)):
    T=[]
    rho=[]
    for temp in range(-200, 200,20):
        T.append(temp)
        rho.append(p/(R[gas]*(temp+273)))
    ax.plot(T, rho, label=nome[gas], marker='*')
ax.set_title('Variação da densidade e função da temperatura em \n um Processo ISOBÁRICO a p = %s kPa' % (p/1000))
ax.set_xlabel('Temperatura (°C)')
ax.set_ylabel('Densidade (kg/m3)')
ax.set_xlim(-200,200)
ax.set_ylim(0,5)
ax.grid(linestyle='--')
ax.legend()

#=====================================================================
#Exemplo - processo adiabático
#=====================================================================
Q=30000 #Pressão constante (Pa)
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6,5))
for gas in range(len(nome)):
    p=[]
    rho=[]
    for pressao in range(1000,100000, 2000):
        p.append(pressao)
        rho.append((pressao/Q)**(1/k[gas]))
    ax.plot(rho, p, label=nome[gas], marker='x')
ax.set_title('Variação da densidade e função da pressão em \n um Processo ADIABÁTICO com Q = %s kJ' % str(Q/1000))
ax.set_ylabel('Pressão (Pa)')
ax.set_xlabel('Densidade (kg/m3)')
ax.set_ylim(0,100000)
ax.set_xlim(0,3)
ax.grid(linestyle='--')
ax.legend()
    

    

