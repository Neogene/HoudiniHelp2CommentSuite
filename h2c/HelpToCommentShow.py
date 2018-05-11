#!/usr/bin/python
#TILE: HOUDINI HELP TO COMMENT SHOW
#AUTHOR: eng. ANDREA LEGANZA
#HOUDINI VERSION: TESTED ON HOUDINI 16.0 AND 16.5
#SCRIPT VERSION: 1.0
#DESCRIPTION:
#This script show comment from selected node
#INSTALLATION:
#Place script inside $houdini/scripts/h2c folder

import hou

def main(kwargs):
    #node = kwargs["node"]
    
    for node in hou.selectedNodes():
        node.setGenericFlag(hou.nodeFlag.DisplayComment,True)
        hou.ui.setStatusMessage("H2C: Comment hidden from selected node.")

main(kwargs)