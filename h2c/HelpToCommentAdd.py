#!/usr/bin/python
# TILE: HOUDINI HELP TO COMMENT ADD
# AUTHOR: eng. ANDREA LEGANZA
# HOUDINI VERSION: TESTED ON HOUDINI 16.0 AND 16.5
# SCRIPT VERSION: 1.0
# DESCRIPTION:
# This script add node documentation headline as comment
# INSTALLATION:
# Place script inside $houdini/scripts/h2c folder

import hou
import os
import zipfile

ZIPFOLDER = os.environ['HFS']+"/houdini/help/nodes.zip".replace("/", os.sep)
ARCHIVE = zipfile.ZipFile(ZIPFOLDER, 'r')


def getHeader(path):
    #print "Path"+path
    path = path.lower()
    path = path.replace("operator:", "").replace(
        "object/", "obj/").split("?")[0]

    if "invalid" in path:
        return ""

    try:
        nodeHelpContent = ARCHIVE.read(path+".txt")
        splitted = nodeHelpContent.split("\"\"\"")
        return splitted[1] if len(splitted) > 1 else "Not found"
    except:
        return "Not found"


def main(kwargs):
    #node = kwargs["node"]

    for node in hou.selectedNodes():
        description = getHeader(node.type().defaultHelpUrl())
        node.setComment(description)
        node.setGenericFlag(hou.nodeFlag.DisplayComment, True)


main(kwargs)
