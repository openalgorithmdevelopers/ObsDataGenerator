# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:38:24 2019

@author: bhupendra.singh
"""

#I/O: Sw, Ho, SR, Da, Vs, Nd
#O/P: Qn, array of Nd data points
#hardcoded values
def obstacle_ideal(Nd, Da, Alpha, SD, SR, Sw, Ho, W, Vs):
#def obstacle_ideal(Nd):
    Sw = 62.3
    Ho = 40
    SR = 195
    Da = 80
    Vs = 1
    W = Ho
    #Nd = 10

###### start the program

    D1 = Da
    Dlast = Da - Ho
    loopCounter = Nd
    total_obs_pts_available = SR*((Ho+W)/Sw)
    #print(total_obs_pts_available)
    Qn = list()

    samplingInterval = Sw/(SR*Vs)
    Di = D1
    while loopCounter > 0 :
        if( Di < Dlast ):
            break
        else:
            Di = Di - samplingInterval
            Di = round(Di, 2)
            Qn.append(round(Di))
        loopCounter = loopCounter - 1
    print("loopCounter=" + str(loopCounter)) 

    points_left = total_obs_pts_available - SR*(Ho/Sw)
    
    print(points_left)
    while loopCounter > 0:
        if( points_left > 0 ):
            Qn.append(Da - Ho)
            points_left -= 1
            loopCounter -= 1
            continue
        else:       
            Qn.append(D1)
        loopCounter = loopCounter - 1
    #print(Qn)
    return(Qn)