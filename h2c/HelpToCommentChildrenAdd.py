#!/usr/bin/python
# TILE: HOUDINI HELP TO COMMENT CHILDREN ADD
# AUTHOR: eng. ANDREA LEGANZA
# HOUDINI VERSION: TESTED ON HOUDINI 16.0 AND 16.5
# SCRIPT VERSION: 1.0
# DESCRIPTION:
# This script adds comment to all node children
# INSTALLATION:
# Place script inside $houdini/scripts/h2c folder

import hou
import os
import zipfile

ZIPFOLDER = os.environ['HFS']+"/houdini/help/nodes.zip".replace("/", os.sep)
ARCHIVE = zipfile.ZipFile(ZIPFOLDER, 'r')


def getHeader(path):
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


def iterateChildren(node):
    for child in node.children():

        description = getHeader(child.type().defaultHelpUrl())
        child.setComment(description)
        child.setGenericFlag(hou.nodeFlag.DisplayComment, True)

        if child.isLockedHDA():
            #hou.ui.displayMessage("LOCKED: "+child.name())
            return
        elif child.children() > 0:
            iterateChildren(child)


def main(kwargs):
    #node = kwargs["node"]

    for node in hou.selectedNodes():
        if len(node.children()) > 0:
            iterateChildren(node)
            hou.ui.setStatusMessage("H2C: Help comment added to all children.")
        else:
            hou.ui.setStatusMessage("H2C: Node has no children.")


main(kwargs)
