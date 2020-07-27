# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:08:24 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x=100
y=100
z=100
mc.player.setPos(x,y,z)