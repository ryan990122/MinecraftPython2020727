# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:33:03 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

x,y,z=mc.player.getTilePos()

y=y+100
mc.player.setTilePos(x,y,z)
time.sleep(5)

y=y+100
mc.player.setTilePos(x,y,z)
time.sleep(5)

y=y+100
mc.player.setTilePos(x,y,z)
