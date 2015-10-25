#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
TP3 de Matthieu Caron et de Armand Bour


Pour les tests fonction de (10,7,7,3) = 11
               fonction de (10,7,5,3) = 15

'''

import numpy as np
import math


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
    #superstition
    for k in xrange(m+1):
        tableau[k][0][0][0] = 1
    for k in xrange(n+1):
        tableau[0][k][0][0] = 1
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

def dynamic_symetric(m,n,i,j) :
    global tableau 
    tableau = np.ndarray(shape=(m+1,n+1,i+1,j+1))
    global longueur
    longueur = m+1
    global hauteur
    hauteur = n+1
    global glob_i
    glob_i = i + 1
    global glob_j
    glob_j = j + 1
    for a in range(m+1) :
        for b in xrange(n+1):
            for c in xrange(i+1):
                for d in xrange(j+1):
                    tableau[a][b][c][d] = None
    for k in xrange(m+1):
        tableau[k][1][0][0] = 1
    for k in xrange(n+1):
        tableau[1][k][0][0] = 1
    #superstition
    for k in xrange(m+1):
        tableau[k][0][0][0] = 1
    for k in xrange(n+1):
        tableau[0][k][0][0] = 1
    tableau[1][1][0][0] = 0
    return dynamic_rec_symetric(m,n,i,j)

def ajoute8cas(m,n,i,j,res) :
    m1 = n
    n1 = m
    i1 = j
    j1 = i
    # cas 1
    tableau[m][n][i][j] = res
    # cas 2
    if not(n-j-1 >= glob_j) :
        tableau[m][n][i][n-j-1] = res
    # cas 3
    if not(m-i-1 >= glob_i) :
        tableau[m][n][m-i-1][j] = res
    # cas 4
    if not(n-j-1 >= glob_j) and not(m-i-1 >= glob_i) :
        tableau[m][n][m-i-1][n-j-1] = res
    # les cas pivotés
        # cas 5
    if not(m1 >= longueur) and not(n1>=hauteur) and not(i1>= glob_i) and not(j1 >= glob_j):
        tableau[m1][n1][i1][j1] = res
        # cas 6
    if not(m1 >= longueur) and not(n1>=hauteur) and not(i1>= glob_i) and not(n1-j1-1 >= glob_j) and not(n1-j1-1 < 0):
        tableau[m1][n1][i1][n1-j1-1] = res
        # cas 7
    if not(m1 >= longueur) and not(n1>=hauteur) and not(m1-i1-1>= glob_i) and not(j1 >= glob_j) and not(m1-i1-1 < 0):
        tableau[m1][n1][m1-i1-1][j1] = res
        # cas 8
    if not(m1 >= longueur) and not(n1>=hauteur) and not(m1-i1-1>= glob_i) and not(n1-j1-1 >= glob_j)and not(m1-i1-1 < 0) and not(n1-j1-1 < 0):
        tableau[m1][n1][m1-i1-1][n1-j1-1] = res

def dynamic_rec_symetric(m,n,i,j):
    if not math.isnan(tableau[m][n][i][j]) :
        return tableau[m][n][i][j]
    else :
        positif = []
        negatif = []
        #on coupe la gauche
        for k in xrange(1,i+1):
            res = (dynamic_rec_symetric(m-k,n,i-k,j))
            if(res>0) :
                positif.append(res)
            else :
                negatif.append(res)
        #on coupe le haut
        for k in xrange(1,j+1):
            res = (dynamic_rec_symetric(m,n-k,i,j-k))
            if(res>0) :
                positif.append(res)
            else :
                negatif.append(res)
        #on coupe la droite
        for k in xrange(1,m-i):
            res = (dynamic_rec_symetric(m-k,n,i,j))
            if(res>0) :
                positif.append(res)
            else :
                negatif.append(res)
        #on coupe le bas
        for k in xrange(1,n-j):
            res = (dynamic_rec_symetric(m,n-k,i,j))
            if(res>0) :
                positif.append(res)
            else :
                negatif.append(res)
        if(negatif == []):
            res = -(max(positif)+1)
            ajoute8cas(m,n,i,j,res)
            return res
        else :
            res = -(max(negatif))+1
            ajoute8cas(m,n,i,j,res)
            return res



#test
# print naif(10,7,7,3)
# print naif(10,7,5,3)
# print dynamic(3,2,2,0)
# print dynamic(10,7,7,3)
# print dynamic(10,7,5,3)
# print dynamic(100,100,50,50) # res = -198.0
# print dynamic_symetric(10,7,7,3)
# print dynamic_symetric(10,7,5,3)
# print dynamic(30,30,10,8)
print dynamic_symetric(30,30,10,8)