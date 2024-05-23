# -*- coding: utf-8 -*-
from API import Delta2D_API
import time
Delta2D = Delta2D_API('reel')
Delta2D.Initialiser()
Delta2D.ModeXY()
posy=350
while posy>250:
    Delta2D.PositionXY(-35,posy, 1)
    time.sleep(1)
    posy=posy-10
    I2 =Delta2D.LireVariable("i2")
    I1 =Delta2D.LireVariable("i1")
    A1=Delta2D.LireVariable("alpha1")
    A2=Delta2D.LireVariable("alpha2")
    print(posy,I1,A1,I2,A2)
Delta2D.Terminer()

