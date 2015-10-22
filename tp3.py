#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
TP3 de Matthieu Caron et de Armand Bour


Pour les tests fonction de (10,7,7,3) = 11
               fonction de (10,7,5,3) = 15

'''

import numpy as np
import math

def calculePrec(liste):
    '''
        ici on veut connaitre le score du coup précédent comme dans la question 2
    '''
    val = liste[0]
    print liste
    print type(val)
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
            if(iElement > val and iElement < 0) :
                val = iElement
        #Return a different value depending the min and max values
        if (val == 0) :
            return 1
        elif (val > 0) :
            return (-1*val - 1)
        else :
            return (-1*val + 1)
        
    

# def naif(m,n,i,j) :
#     barre = []
#     # si qu'un seul carré
#     if(m==n==1) :
#         return 0
#     #toutes les possibilités de découpages
#     else :
#         #on coupe la gauche
#         for k in xrange(1,i+1):
#             barre.append(naif(m-k,n,i-k,j))
#         #on coupe le haut
#         for k in xrange(1,j+1):
#             barre.append(naif(m,n-k,i,j-k))
#         #on coupe la droite
#         for k in xrange(1,m-i):
#             barre.append(naif(m-k,n,i,j))
#         #on coupe le bas
#         for k in xrange(1,n-j):
#             barre.append(naif(m,n-k,i,j))
#     return calculePrec(barre)


def naif(m,n,i,j) :
    positif = []
    negatif = []
    # si qu'un seul carré
    if(m==n==1) :
        return 0
    #toutes les possibilités de découpages
    else :
        #on coupe la gauche
        for k in xrange(1,i+1):
            res = (naif(m-k,n,i-k,j))
            if(res>0) :
                positif.append(res)
            else :
                negatif.append(res)
        #on coupe le haut
        for k in xrange(1,j+1):
            res = (naif(m,n-k,i,j-k))
            if(res>0) :
                positif.append(res)
            else :
                negatif.append(res)
        #on coupe la droite
        for k in xrange(1,m-i):
            res = (naif(m-k,n,i,j))
            if(res>0) :
                positif.append(res)
            else :
                negatif.append(res)
        #on coupe le bas
        for k in xrange(1,n-j):
            res = (naif(m,n-k,i,j))
            if(res>0) :
                positif.append(res)
            else :
                negatif.append(res)
        if(negatif == []):
            return -(max(positif)+1)
        else :
            return -(max(negatif))+1



def dynamic(m,n,i,j) :
    global tableau 
    tableau = np.ndarray(shape=(m+1,n+1,i+1,j+1))
    for a in range(m+1) :
        for b in xrange(n+1):
            for c in xrange(i+1):
                for d in xrange(j+1):
                    tableau[a][b][c][d] = None
    for k in xrange(m+1):
        tableau[k][1][0][0] = 1
    for k in xrange(n+1):
        tableau[1][k][0][0] = 1
    tableau[1][1][0][0] = 0
    return dynamic_rec(m,n,i,j)


def dynamic_rec(m,n,i,j):
    if not math.isnan(tableau[m][n][i][j]) :
        return tableau[m][n][i][j]
    else :
        positif = []
        negatif = []
        #on coupe la gauche
        for k in xrange(1,i+1):
            res = (dynamic_rec(m-k,n,i-k,j))
            if(res>0) :
                positif.append(res)
            else :
                negatif.append(res)
        #on coupe le haut
        for k in xrange(1,j+1):
            res = (dynamic_rec(m,n-k,i,j-k))
            if(res>0) :
                positif.append(res)
            else :
                negatif.append(res)
        #on coupe la droite
        for k in xrange(1,m-i):
            res = (dynamic_rec(m-k,n,i,j))
            if(res>0) :
                positif.append(res)
            else :
                negatif.append(res)
        #on coupe le bas
        for k in xrange(1,n-j):
            res = (dynamic_rec(m,n-k,i,j))
            if(res>0) :
                positif.append(res)
            else :
                negatif.append(res)
        if(negatif == []):
            res = -(max(positif)+1)
            tableau[m][n][i][j] = res
            return res
        else :
            res = -(max(negatif))+1
            tableau[m][n][i][j] = res
            return res

#test
#print naif(10,7,7,3)
#print naif(10,7,5,3)
# dynamic(10,7,7,3)
#print dynamic(3,2,2,0)
print dynamic(10,7,7,3)
print dynamic(10,7,5,3)