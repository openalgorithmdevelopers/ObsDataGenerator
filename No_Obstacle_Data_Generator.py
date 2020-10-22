# -*- coding: utf-8 -*-
"""
Created on Sun May 12 11:10:43 2019

@author: bhupendra.singh
"""
#def no_obstacle_data(Nd, Da, Dx, Di, Alpha, SD):
def no_obstacle_data(Nd):
### define inputs
    Alpha = 96
    SD = 1.5
    Da = 80
    Dx = 20 # in %
    Di = 30 # in %

    import random
    from random import randint
    Qn = list(range(0, Nd))

    Rd_Dxa = int(Da*(100+Dx)/100)
    Rd_Dia = int(Da*(100-Di)/100)
    Et = int(Nd*Da*(100-Alpha)/100)
    Er = Et
    loopCounter = Nd
    print(loopCounter)
    while loopCounter > 0:
        Re_Exa = Da + Er
        Re_Eia = Da - Er
    
        if(Rd_Dxa > Re_Exa):
            Rd_Dxa = Re_Exa
        if(Rd_Dia < Re_Eia):
            Rd_Dia = Re_Eia
        if(Er < 1):
            Qn.append(Da)
    #Di = randint(Rd_Dia, Rd_Dxa)
    # https://stackoverflow.com/questions/16471763/generating-numbers-with-gaussian-function-in-a-range-using-python
        Di = int(min(Rd_Dxa, max(Rd_Dia, random.gauss(Da, SD))))
        Qn[loopCounter - 1] = Di
        Ec = abs(Da - Di)
        Er = Er - Ec
        loopCounter = loopCounter - 1
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
    return(Qn)