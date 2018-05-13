import hou
import sys

def node_changed(node, **kwargs):
    #print kwargs["event_type"]
    #print kwargs["change_type"]
    print node.name()
    print '\n  '.join(['%s = %s' % (k,w) for (k,w) in kwargs.items()])
    
    if len(hou.selectedNodes())==0:
         return

    if kwargs["event_type"] == hou.nodeEventType.AppearanceChanged and kwargs["change_type"] == hou.appearanceChangeType.Pick:
        auto_help_show_Browser(hou.selectedNodes()[0])

def auto_help_show_Browser(selectedNode):
    desktop = hou.ui.curDesktop()
    help_browser = desktop.paneTabOfType(hou.paneTabType.HelpBrowser)
    if help_browser is None:
        help_browser = desktop.displaySideHelp()
    if len(help_browser.url())>0 and selectedNode.type().defaultHelpUrl()!=None and \
        len(selectedNode.type().defaultHelpUrl())>1 and \
        'Invalid' not in selectedNode.type().defaultHelpUrl() and \
        help_browser.url().split("/")[-1]!=selectedNode.type().defaultHelpUrl().split("/")[-1]:
        print selectedNode.type().defaultHelpUrl()
        print help_browser.url()
        help_browser.displayHelp(selectedNode.type())

def auto_help_is_on():
    return hou.node("/").userData("h2c_auto_show_help") == "1" if hou.node("/").userData("h2c_auto_show_help")!=None else False 

def add_auto_help(node, iterateChildren = True):
    print "Adding event to node: "+node.name()
    node.addEventCallback((hou.nodeEventType.AppearanceChanged,), node_changed)

    if iterateChildren and len(node.allSubChildren())>0:
        auto_help_iterate_children(node, False)

def remove_auto_help(node):
    try:
        print "Removing from node: "+node.name()
        node.removeAllEventCallbacks() #(hou.nodeEventType.AppearanceChanged,), node_changed seems not working
    except hou.OperationFailed,hou.AttributeError:
        pass

def auto_help_iterate_children(rootNode = None, removeRootEvent = True):
    autoShowHelp = int(hou.node("/").userData("h2c_auto_show_help")) if hou.node("/").userData("h2c_auto_show_help")!=None else 0
            
    hou.ui.setStatusMessage("H2C: enabling auto help display") if autoShowHelp == 1 else hou.ui.setStatusMessage("H2C: disabling auto help display")

    parentNode = (hou.node("/") if rootNode == None else rootNode)
   
    if removeRootEvent and rootNode != None:
        remove_auto_help(parentNode)
 
    #iterate all children
    for node in parentNode.allSubChildren():

        remove_auto_help(node)

        if autoShowHelp == 1: #add           
            add_auto_help(node, False)

def main():
    if len(sys.argv)>=2:
        choice = int(sys.argv[1])

        if choice == 0:# enable/disable auto display help on node selection

            if hou.node("/").userData("h2c_auto_show_help") == None:
                hou.node("/").setUserData("h2c_auto_show_help", str(1)) #store setting
            else:
                hou.node("/").setUserData("h2c_auto_show_help", str(1) if hou.node("/").userData("h2c_auto_show_help")=="0" else str(0))

            auto_help_iterate_children()

            if len(hou.selectedNodes())>0 and int(hou.node("/").userData("h2c_auto_show_help"))==1:
                auto_help_show_Browser(hou.selectedNodes()[0])

    #elif kwargs["node"] != None:
    #    kwargs["node"].addEventCallback(hou.nodeEventType.AppearanceChanged, name_changed)
   
main()