import hou
import locale
import os.path
import os
import sys
import zipfile

sys.path.append(os.environ['HFS']+"/houdini/scripts/h2c/".replace("/",os.sep))
from HelpToCommentGoogleTranslate import translate

ZIPFOLDER = os.environ['HFS']+"/houdini/help/nodes.zip".replace("/",os.sep)
ARCHIVE = zipfile.ZipFile(ZIPFOLDER, 'r')

#sys.path.append(os.environ['HFS']+"/houdini/scripts/h2c/".replace("/",os.sep))
#from HelpToCommentTranslateUtils import translateText

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

def translateText(text, checkAutoTranslate = False, promptForLanguageSelection = True):
    
    if hou.node("/").userData("h2c_translate_language") == None and promptForLanguageSelection:
        changeTranslateLanguage()
        
    language = hou.node("/").userData("h2c_translate_language")

    if checkAutoTranslate:
         if hou.node("/").userData("h2c_auto_translate_language") == None or int(hou.node("/").userData("h2c_auto_translate_language")) == 0:
            language = "en"

    #print "Tranlate text: "+language

    return text if language == None or language == "en" else translate(text,language)

def changeTranslateLanguage():
    languageInfo = hou.ui.readInput("Translation language (en, it, fr, es, ru...):")

    if languageInfo[1] and len(languageInfo[1])==2:
        hou.node("/").setUserData("h2c_translate_language", languageInfo[1]) #store setting
    else:
        hou.node("/").setUserData("h2c_translate_language", "en")

    hou.ui.setStatusMessage("H2C: translation language set to: "+hou.node("/").userData("h2c_translate_language"))

      
def main():
    
    if len(sys.argv)>=2:
        choice = int(sys.argv[1])

        if choice == 0:
            #translate nodes
            for node in hou.selectedNodes():
                try:
                    node.setComment(translateText(getHeader(node.type().defaultHelpUrl())))
                    node.setGenericFlag(hou.nodeFlag.DisplayComment,True)
                except:
                    pass

            if len(hou.selectedNodes())==0:
                hou.ui.setStatusMessage("H2C: select at least a node.")
            elif hou.node("/").userData("h2c_translate_language") != None:
                hou.ui.setStatusMessage("H2C: node/s content translated to: " + hou.node("/").userData("h2c_translate_language"))

        elif choice == 1:
            #auto translate new nodes
            if hou.node("/").userData("h2c_auto_translate_language") == None or int(hou.node("/").userData("h2c_auto_translate_language")) == 0:
                hou.node("/").setUserData("h2c_auto_translate_language", str(1))
                hou.ui.setStatusMessage("H2C: auto-translate new nodes ON.")

            else:
                hou.node("/").setUserData("h2c_auto_translate_language", str(0))
                hou.ui.setStatusMessage("H2C: auto-translate new nodes OFF.")
        elif choice == 2:
            changeTranslateLanguage()
        
main()