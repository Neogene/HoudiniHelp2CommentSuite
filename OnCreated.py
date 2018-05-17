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
# NOTE: some scripts don't have documentation 

import hou
import os
import zipfile
import sys
import re

ZIPFOLDER = os.environ['HFS']+"/houdini/help/nodes.zip".replace("/",os.sep)
ARCHIVE = zipfile.ZipFile(ZIPFOLDER, 'r')

sys.path.append(os.environ['HFS']+"/houdini/scripts/h2c/".replace("/",os.sep))
from HelpToCommentTranslateUtils import translateText
from HelpToCommentNodeInteractionUtils import auto_help_is_on,add_auto_help,auto_help_iterate_children,auto_help_show_Browser
   
def getHeader(path):
    #print "Path"+path
    path = path.lower()
    
    #print path
      
    path = path.replace("operator:","").replace("object/","obj/").split("?")[0]
   
    if "invalid" in path:
        return ""
    
    try:
        nodeHelpContent = ARCHIVE.read(path+".txt")

        if "\"\"\"" in nodeHelpContent:
            splitted = nodeHelpContent.split("\"\"\"")
            return splitted[1] if len(splitted)>1 else "Not found"
        elif "See the" in nodeHelpContent:
            if len(nodeHelpContent.split("See the"))>1:
                #print "Found see the"
          
                #See the [DOP Network Node|Node:obj/dopnet].
                m = re.search('(\w+)/(\w+)(?=])', nodeHelpContent, flags=re.I) #matches obj/dopnet
               
                if m:
                    path = m.group(0)

                    path = path.replace("operator:","").replace("object/","obj/").split("?")[0]

                    try:
                        nodeHelpContent = ARCHIVE.read(path+".txt")

                        if "\"\"\"" in nodeHelpContent:
                            splitted = nodeHelpContent.split("\"\"\"")
                            return splitted[1] if len(splitted)>1 else "Not found"

                    except Exception, error:
                       # print "EXCEPTION: "+str(error)
                        return "Not found"
                else:
                    #print "regex not found"
                    return "Not found"
            else:
                #print "See the not found..."
                return "Not found" 
            
    except Exception, error:
        #print "EXCEPTION: "+str(error)
        return "Not found"

def iterateChildren(node):
    for child in node.children():
        try:
            if len(child.comment()) == 0:
                description = getHeader(child.type().defaultHelpUrl())
                child.setComment(translateText(description,True,False))
                child.setGenericFlag(hou.nodeFlag.DisplayComment, True)
        except:
            pass #ignore

        if child.isLockedHDA() or not child.isEditable():
            #hou.ui.displayMessage("LOCKED: "+child.name())
            return
        elif len(child.children())>0:
            iterateChildren(child)

def main(kwargs):

    node = kwargs["node"]

    if node.type().name() == "geo" and len (node.children())==1:
        if hou.node("/").userData("h2c_destroy_geometry_file_creation") != None and int(hou.node("/").userData("h2c_destroy_geometry_file_creation")) == 1:
            print "Destroying 1st child of geo"
            node.children()[0].destroy()

    if auto_help_is_on():
        add_auto_help(node)
        auto_help_show_Browser(node)

    try:
        if len(node.comment()) == 0:
            description = getHeader(node.type().defaultHelpUrl())
            node.setComment(translateText(description,True,False))
            node.setGenericFlag(hou.nodeFlag.DisplayComment, True)  
    except:
        pass #ignore

    if len(node.children())>0:
        iterateChildren(node)

    
main(kwargs)