'''
Décodage par ensemble d'information
Exo 18
SABIR ILYASS -FISE2
'''

import numpy as np
from random import random

def XOR(a: int, b : int):
    return (a+b) % 2

def trigonaliser_F2(H,S):
    """les coefficient des matrices d'entrée doivent égales suelement 0 ou 1"""
    dimension_H = H.shape
    for i in range(dimension_H[0] - 1):
        pivot = i
        for j in range(i, dimension_H[0]):
            if (H[j][i] == 1):
                pivot = j
                break
        L,M = H[pivot],S[pivot]
        H[pivot], S[pivot] = H[i], S[i]
        H[i], S[i] = L, M
        for k in range(i+1, dimension_H[0]):
            if (H[k][i] == 1):
                for l in range(dimension_H[1]):
                    H[k][l] = XOR(H[k][l], H[i][l])
                S[k][0] = XOR(S[k][0],S[i][0])

def pivot_de_Gauss_F2(H,S):
    dimension_H = H.shape
    trigonaliser_F2(H,S)
    for i in range(dimension_H[0] - 1):
        for k in range(i+1,dimension_H[0]):
            if (H[i][k] == 1):
                for l in range(dimension_H[1]):
                    H[i][l] = XOR(H[i][l], H[k][l])
                S[i][0] = XOR(S[k][0], S[i][0])

def choix_aleatoire_colonnes(H):
    L = []
    dimension = H.shape
    i = 0
    while(i < dimension[0]):
        rand = int(random() * (dimension[1]))
        while (rand in L):
            rand = int(random() * (dimension[1]))
        L.append(rand)
        i += 1
    s = dimension[0]
    for i in range(len(L)):
        for j in range(dimension[0]):
            m = H[j][L[i]]
            H[j][L[i]] = H[j][i]
            H[j][i] = m
    return L


def if_sous_matrice_inversible(H):
    dimension = H.shape[0]
    sous_matrice = np.zeros((dimension,dimension))
    for i in range(dimension):
        for j in range(dimension):
            sous_matrice[i][j] = H[i][j]
    det = np.linalg.det(sous_matrice)
    if (det != 0):
        return True
    else:
        return False

def IDS(H, S):
    dimension_H = H.shape
    # choix aléatoire des colonnes
    M = H
    L = choix_aleatoire_colonnes(H)
    while(not(if_sous_matrice_inversible(H))):
        H = M
        L = choix_aleatoire_colonnes(H)
    # on a pour l'instant un choix aléatoire de colonnes, où on est sûr que le pivot de gauss
    # va nous donner une matrice identité à gauche
    pivot_de_Gauss_F2(H,S)
    e = [0 for i in range(dimension_H[1])]
    for i in range(dimension_H[0]):
        if S[i][0] == 1:
            e[L[i]] = 1
    return e