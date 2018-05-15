#!/usr/bin/python
#TILE: HOUDINI HELP TO COMMENT CHILDREN REMOVE
#AUTHOR: eng. ANDREA LEGANZA
#HOUDINI VERSION: TESTED ON HOUDINI 16.0 AND 16.5
#SCRIPT VERSION: 1.0
#DESCRIPTION:
#This script removes comment from all node children
#INSTALLATION:
#Place script inside $houdini/scripts folder

import hou

def iterateChildren(node):
     for child in node.children():
 
        try:
            child.setComment("")
        except:
            pass

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
            hou.ui.setStatusMessage("H2C: Comment removed from all children.")
        else:
            hou.ui.setStatusMessage("H2C: Node has no children.")

main(kwargs)