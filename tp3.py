#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
TP3 de Matthieu Caron et de Armand Bour


Pour les tests fonction de (10,7,7,3) = 11
               fonction de (10,7,5,3) = 15

'''

import numpy as np
import math


def naif(m, n, i, j):
    positif = []
    negatif = []
    # Si qu'un seul carré
    if m == n == 1:
        return 0
    # Toutes les possibilités de découpages
    else:
        # On coupe la gauche
        for k in xrange(1, i + 1):
            res = (naif(m-k, n, i-k, j))
            if res > 0:
                positif.append(res)
            else:
                negatif.append(res)

        # On coupe le haut
        for k in xrange(1, j + 1):
            res = naif(m, n - k, i, j - k)
            if res > 0:
                positif.append(res)
            else:
                negatif.append(res)

        # On coupe la droite
        for k in xrange(1, m - i):
            res = naif(m - k, n, i, j)
            if res > 0:
                positif.append(res)
            else:
                negatif.append(res)

        # On coupe le bas
        for k in xrange(1,n-j):
            res = naif(m, n - k, i, j)
            if res > 0:
                positif.append(res)
            else:
                negatif.append(res)

        # On retourne le résulat
        if negatif == []:
            return -(max(positif) + 1)
        else:
            return -(max(negatif)) + 1


def dynamic(m, n, i, j) :
    global tableau 
    tableau = np.ndarray(shape=(m+1, n+1, i+1, j+1))
    print 'Initialisation du tableau de pré-calcul...'
    for a in xrange(m+1) :
        for b in xrange(n+1):
            for c in xrange(i+1):
                for d in xrange(j+1):
                    tableau[a][b][c][d] = None

    for k in xrange(m+1):
        tableau[k][1][0][0] = 1

    for k in xrange(n+1):
        tableau[1][k][0][0] = 1

    # Superstition
    for k in xrange(m+1):
        tableau[k][0][0][0] = 1
    for k in xrange(n+1):
        tableau[0][k][0][0] = 1
    tableau[1][1][0][0] = 0

    print 'Tableau initialisé. Calcul des possibilités...'
    return dynamic_rec(m, n, i, j)


def dynamic_rec(m, n, i, j):
    print (m, n, i, j)
    if not math.isnan(tableau[m][n][i][j]) :
        return tableau[m][n][i][j]
    else :
        positif = []
        negatif = []
        # On coupe la gauche
        for k in xrange(1, i+1):
            res = dynamic_rec(m-k, n, i-k, j)
            if res > 0:
                positif.append(res)
            else :
                negatif.append(res)
        # On coupe le haut
        for k in xrange(1, j+1):
            res = dynamic_rec(m,n-k,i,j-k)
            if res > 0:
                positif.append(res)
            else :
                negatif.append(res)
        # On coupe la droite
        for k in xrange(1, m - i):
            res = dynamic_rec(m - k, n, i, j)
            if res > 0:
                positif.append(res)
            else :
                negatif.append(res)
        # On coupe le bas
        for k in xrange(1, n-j):
            res = dynamic_rec(m, n-k, i, j)
            if res > 0:
                positif.append(res)
            else :
                negatif.append(res)
        if(negatif == []):
            res = -(max(positif) + 1)
            tableau[m][n][i][j] = res
            return res
        else :
            res = -(max(negatif)) + 1
            tableau[m][n][i][j] = res
            return res

# Fonction pour trouver les couples (i, j) pour la valeur 127
def find127():
    res = []

    for i in xrange(0, 128):
        for j in xrange(0, 128):
            val = dynamic(127, 127, i, j)
            if val == 127:
                res.append((i, j))

    print res

# Test

def test_naif():
    print "** Naïf **"
    print("Résultat pour (10,7,7,3): {res}".format(res=naif(10, 7, 7, 3))) #4m 47s
    #print("Résultat pour (10,7,5,3): {res}".format(res=naif(10,7,5,3) #10m 24s

def test_dynamic():
    print "** Dynamique **"
    #print("Résultat pour (10,7,7,3): {res}".format(res=dynamic(10, 7, 7, 3))) # 0,4s
    #print("Résultat pour (10,7,5,3): {res}".format(res=dynamic(10, 7, 5, 3))) # 0,1s
    print("Résultat pour (100,100,50,50): {res}".format(res=dynamic(100, 100, 50, 50)))


# test_naif()
# test_dynamic()
find127()
