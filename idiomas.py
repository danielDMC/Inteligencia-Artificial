# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 15:17:06 2016

@author: AlbantaMusic
"""
entr =[[4,6,7,8,9,13],
[4,5,6,8],
[1,2,3,8,10,12],
[1,2,3,5,6,8,12],
[4,9,10,11]]

listact =[]
dicc ={}

long =len(entr)
cont = 0
for i in entr:
   dicc[cont]=i
   cont+=1

#print dicc

totidiomas=0
trad = 0

for i in entr:
    if (len(i))>totidiomas:
        totidiomas = (len(i))
        trad = i
        listaact =[i]
        
print "Traductor con mas idiomas: "+str(len(trad))
print listaact

        
      
       

    





