#!/usr/bin/python
#TILE: HOUDINI GRAPH UTILS
#AUTHOR: eng. ANDREA LEGANZA
#HOUDINI VERSION: TESTED ON HOUDINI 16.0 AND 16.5
#SCRIPT VERSION: 1.0
#DESCRIPTION:
#This script Increases/decreases nodes distance
#INSTALLATION:
#Place script inside $houdini/scripts/h2c folder

import sys
import hou

def getCurrentNetworkEditorPane():
    editors = [pane for pane in hou.ui.paneTabs() if isinstance(pane, hou.NetworkEditor) and pane.isCurrentTab()]
    return editors[-1]
    
def main(kwargs):

    if hou.node("/").userData("h2c_layout_delta") == None:
        hou.node("/").setUserData("h2c_layout_delta", str(1.0))
      
    h2cCurrentLayoutDelta = float(hou.node("/").userData("h2c_layout_delta"))

    delta = float(sys.argv[1])

    if delta==-1:#increment current/global layout delta and use instead of using presets
        if h2cCurrentLayoutDelta+0.5<=10.0:
            h2cCurrentLayoutDelta+=0.5
    elif delta == -2: #decrement current/global layout delta and use instead of using presets
        if h2cCurrentLayoutDelta-0.5>=0.5:
            h2cCurrentLayoutDelta-=0.5
    else:
        h2cCurrentLayoutDelta = delta

    editor = getCurrentNetworkEditorPane()

    node = kwargs["node"]
    
    if len(hou.selectedNodes()) == 1 and len(node.children())>0: #if selected one and has children lay out children   
        node.layoutChildren(node.children(), h2cCurrentLayoutDelta, h2cCurrentLayoutDelta)
        hou.ui.setStatusMessage("H2C: Lay out children nodes to "+str(h2cCurrentLayoutDelta)+".") #show current value
    elif len(hou.selectedNodes()) > 1: #if selected more than one lay out out selected nodes / all nodes
        editor.pwd().layoutChildren(hou.selectedNodes(), h2cCurrentLayoutDelta, h2cCurrentLayoutDelta)
        hou.ui.setStatusMessage("H2C: Lay out selected nodes to "+str(h2cCurrentLayoutDelta)+".") #show current value
    else:
         hou.ui.setStatusMessage("H2C: selected node has no children.")

    hou.node("/").setUserData("h2c_layout_delta", str(h2cCurrentLayoutDelta)) #store setting

main(kwargs)