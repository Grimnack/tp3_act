'''
TP3 de Matthieu Caron et de Armand Bour


Pour les tests fonction de (10,7,7,3) = 11
               fonction de (10,7,5,3) = 15

'''

import numpy as np

def calculePrec(liste):
'''
    ici on veut connaitre le score du coup précédent comme dans la question 2
'''    
val = liste[0]

for i in xrange(1,len(liste)):
    iElement = liste[i]
    if(val>0) :
        if(iElement > val) :
            val=iElement
    elif (iElement <= 0) :
        val=iElement
    elif (val ==0) :
        if (iElement < val) :
            val = iElement
    else :
        if(iElement > val && iElement < 0) :
            val = iElement
    #Return a different value depending the min and max values
    if (val == 0) :
        return 1
    elif (val > 0) :
        return -val - 1
    else :
        return -val + 1
    
    

def naif(m,n,i,j) :
    barre = []
    # si qu'un seul carré
    if(m==n==0) :
        return 0
    #toutes les possibilités de découpages
    else
        #on coupe la gauche
        for k in xrange(1,i):
            barre.append(naif(m-k,n,i-k,j))
        #on coupe le haut
        for k in xrange(1,j):
            barre.append(naif(m,n-k,i,j-k))
        #on coupe la droite
        for k in xrange(1,m-i):
            barre.append(naif(m-k,n,i,j))
        #on coupe le bas
        for k in xrange(1,n-j):
            barre.append(naif(m,n-k,i,j))
    return valPreviousPos(chocolateBar)