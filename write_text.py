# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:38:36 2015

@author: polsztyn
"""
import matplotlib.pyplot as plt

def addFigText(x,y,message,fontsize=14,ha='left',va='top',spaceAbove=None,spaceBelow=None,percentBelow=0.2,fontweight='normal'):
  fig = plt.gcf()
  r = fig.canvas.get_renderer()
  canvasWidth,canvasHeight = r.get_canvas_width_height()
  print canvasWidth,canvasHeight
  sp1 = 0.0
  sp2 = 0.0
  if spaceAbove:
    sp1 = r.points_to_pixels(spaceAbove)
    print sp1
    y = y - sp1 / canvasHeight
  if spaceBelow is None:
    spaceBelow = fontsize * percentBelow
  if spaceBelow:
    sp2 = r.points_to_pixels(spaceBelow)
  t = fig.text(x,y,message,fontsize=fontsize,ha=ha,va=va,fontweight=fontweight)
  plt.draw()
  bb = t.get_window_extent(renderer=r)
  dy = (bb.height + sp1 + sp2) / canvasHeight
  ## dx = (bb.width) / canvasWidth
  return dy
  
if __name__ == "__main__":
    
    fig=plt.figure(figsize=(12,8))
    dummyAxes = fig.add_axes((0, 0, 1, 1))
    dummyAxes.patch.set_visible(False)
    dummyAxes.axis('off')

    #addFigText(0,0,"(0,0)")

    #addFigText(.25,.25,"(.25,.25)")    
    #addFigText(.5,.5,"(.5,.5)")   
    #addFigText(.75,75,"(.75,.75)")   
    addFigText(1.0,1.0,"(1,1)")  
    addFigText(.5,.5,"(.5,.5)")  
    addFigText(0,0,"(0,0)") 
    addFigText(0,.5,"A spaceBelow = .5",spaceBelow = 320) 
    fig.show()