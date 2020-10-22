# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:48:35 2019

@author: bhupendra.singh
"""

#def obstacle_data(Nd, Da, D_mx, D_mn, Alpha, SD, SR, Sw, Ho, W, Vs):
def obstacle_data(Nd):
# obstacle_data(Number of points to generate,
#                Height above the surface,
#                Maximum distance expected
#                Minimum distance expected
#               Accuracy of the system,
#               Standard Dev. of the system,
#               Sampling rate,
#                walking speed,
#                Height of the obstacle,
#                Width of the obstacle flat surface
#                Visible part-- by default set it to 1)
    Alpha = 96
    SD = 4
    Da = 80
    D_mx = 94
    D_mn = 45
    SR = 195
    Ho = 40
    #Nd = 20
    Vs = 1
    Sw = 62.3
    W = 43

    from Obstacle_data_ideal_case import obstacle_ideal

    Dex = obstacle_ideal(Nd, Da, Alpha, SD, SR, Sw, Ho, W, Vs)
#Dex = [79,78,78,77,76,75,74,73,73,72]

    #print("Dex = " + str(Dex))
    Et = 0
    for i in range(0, len(Dex)):
    #print(i)
    #print(Dex[i])
        Et = Dex[i]*(100-Alpha)/100 + Et

    Et = int(Et)

    import random
    from random import randint
    Qn = list(range(0, Nd))


    Er = Et
    i = 0

    while i < (Nd):
    #print(Dex[i])
        Tx = round(round((Dex[i]*(100+D_mx)/100) , 2))
    #print(Tx)
        Ti = round(round((Dex[i]*(100-D_mn)/100), 2))
    #print("Tx = " + str(Tx) + " and Ti = " + str(Ti))
        Rd_Dxa = Tx
        Rd_Dia = Ti
    #print("Er = " + str(Er))
        Re_Exa = Dex[i] + Er
        Re_Eia = Dex[i] - Er
    
    #print("Rd_Dx = " + str(Rd_Dxa) + " Rd_Di" + str(Rd_Dia) + " Re_Ex" + str(Re_Exa) + " Re_Ei" + str(Re_Eia))
        if(Rd_Dxa > Re_Exa):
            Rd_Dxa = Re_Exa
        if(Rd_Dia < Re_Eia):
            Rd_Dia = Re_Eia
        if(Er < 1):
            Qn[i-1] = Dex[i]
       # print(Qn)
       # print("i = " + str(i))
            i = i + 1
            continue
    #Di = randint(Rd_Dia, Rd_Dxa)
    # https://stackoverflow.com/questions/16471763/generating-numbers-with-gaussian-function-in-a-range-using-python
        Di = int(min(Rd_Dxa, max(Rd_Dia, random.gauss(Dex[i], SD))))
    #print("Rd_Dx = " + str(Rd_Dxa) + " Rd_Di" + str(Rd_Dia) + " Re_Ex" + str(Re_Exa) + " Re_Ei" + str(Re_Eia) + " and Di = " + str(Di))
        Qn[i - 1] = Di
        Ec = abs(Dex[i] - Di)
        Er = Er - Ec
        i = i + 1
#print(Qn)
    #print("Er still remaining = " + str(Er))
    if(Er > 0):
        while(Er > 0):
            k = randint(0, Nd-1) 
            if( Qn[k] == Da):
                continue
            if( Qn[k] > Da):
                Qn[k] = Qn[k] + 1
            if( Qn[k] < Da):
                Qn[k] = Qn[k] - 1
                Er = Er - 1
    #print("Mean = " + str(np.mean(Qn)) + ",SD = " + str(np.std(Qn)) + ",Skewness = " + str(skew(Qn)) + ", Kurtosis = " + str(kurtosis(Qn)))
    #print("Generated Points = " + str(Qn))

        #res = [[1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']]
    return Qn