#!/usr/bin/python
#TILE: HOUDINI HELP TO COMMENT CHILDREN HIDE
#AUTHOR: eng. ANDREA LEGANZA
#HOUDINI VERSION: TESTED ON HOUDINI 16.0 AND 16.5
#SCRIPT VERSION: 1.0
#DESCRIPTION:
#This script hides comment of all node children
#INSTALLATION:
#Place script inside $houdini/scripts folder

import hou

def iterateChildren(node):
     for child in node.children():
 
        child.setGenericFlag(hou.nodeFlag.DisplayComment,False)
            
        if child.isLockedHDA(): 
            #hou.ui.displayMessage("LOCKED: "+child.name())
            return
        elif child.children()>0 :
            iterateChildren(child)
                
    

def main(kwargs):
    #node = kwargs["node"]

    for node in hou.selectedNodes():
        if len(node.children())>0:
            iterateChildren(node)
            hou.ui.setStatusMessage("H2C: Comment hidden from all children.")
        else:
            hou.ui.setStatusMessage("H2C: Node has no children.")

main(kwargs)