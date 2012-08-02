#!/usr/bin/env vroom

from vroom import *

# Functions

def clearPoints():
   Global.points = point_list()

# vroom callbacks

def init():
   addMainMenuItem('clear', clearPoints)
   Global.points = point_list()

def draw():
   material(green)
   Global.points.for_each(sphere, 1.0, style='solid')

def button_press(pos, button):
   print ' -- button_press (pos={}, button={})'.format(pos, button)
   Global.points.append(pos)

