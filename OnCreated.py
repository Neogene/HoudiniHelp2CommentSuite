#!/usr/bin/python
#TILE: HOUDINI HELP TO COMMENT
#AUTHOR: eng. ANDREA LEGANZA
#VERSION: HOUDINI 16.5
#DESCRIPTION:
# 1) place script inside  <$houdini>/scripts/ 
# 2) place <node_type>.json files into <$houdini>/scripts/nodes_help folder (create the folder)
# 3) restart Houdini
# 4) create a geometry node
# 5) inside it create any kind of node
# 6) script will add for any new node as comment the headline taken from online documentation
# NOTE: some scripts has not documentation 

import hou
import os
import zipfile

ZIPFOLDER = os.environ['HFS']+"/houdini/help/nodes.zip".replace("/",os.sep)
ARCHIVE = zipfile.ZipFile(ZIPFOLDER, 'r')
   
def getHeader(path):
    #print "Path"+path
    path = path.lower()
    path = path.replace("operator:","").replace("object/","obj/").split("?")[0]
   
    if "invalid" in path:
        return ""
    
    try:
        nodeHelpContent = ARCHIVE.read(path+".txt")
        splitted = nodeHelpContent.split("\"\"\"")
        return splitted[1] if len(splitted)>1 else "Not found"
    except:
        return "Not found"

def main(kwargs):

    node = kwargs["node"]

    if len(node.comment())==0 :
        description = getHeader(node.type().defaultHelpUrl())
        node.setComment(description)
        node.setGenericFlag(hou.nodeFlag.DisplayComment,True)
    
main(kwargs)