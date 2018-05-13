# HoudiniHelp2CommentSuite
A serie of python scripts which manage node(s) comment and add documentation to comment functionality.

## AUTHOR: ## 
eng. ANDREA LEGANZA

## TESTED VERSION/S: ## 
HOUDINI 16/16.5

## DESCRIPTION: ## 
When learning Houdini it may be hard to undestand the flow of nodes and to take a sneak peak on the purpose of a single node: a user has to select right click on node -> help and wait for Houdini internal browser to load the help page.

These scripts simplify this operations letting user automatically/manually populate node comment with proper text.

## RESULTS: ##
![Script result](https://github.com/Neogene/HoudiniHelp2CommentSuite/blob/master/result.png)

## INSTALLATION: ##
1. close Houdini
2. copy h2c folder inside  <$houdini>/scripts/ 
3. Add the content of file AddToOPmenu.xml into <$houdini>/OPMenu.xml, this is required to display menu on RMB. I placed after "Edit Comment" voice, but is up to you.
4. optional: copy OnUpdated.py inside <$houdini>/scripts/ : this script automatically adds help as comment for every new node
5. start Houdini
6. create a node (eg: geometry)
7. selecte node -> right mouse button -> Help to comment -> select proper menu voice

## RIGHT MOUSE BUTTON MENU VOICES ON NODE/S: ##
1. <b>Use help as comment</b>: populate node/selected nodes comment with online documentation headline
2. <b>Use help as comment for children</b>: populate node/selected nodes and its/theri children notes comment with online documentation headline
3. <b>Display node comment</b>: make node/selected nodes comment visible
4. <b>Hide node comment</b>: hides node/selected nodes comment
5. <b>Remove node comment</b>: removes node/selected nodes comment
6. <b>Display children comments</b>: make children nodes of node/selected nodes comment visible
7. <b>Hide children comments</b>: hides children nodes of node/selected nodes comment
8. <b>Remove children comments</b>: removes children nodes of node/selected nodes comment
9. <b>Translate comment</b>: translates comment using Google Translate service (it may take some seconds when using on multiple nodes)
10. <b>"Layout" submenu</b>: these options modify space between nodes to let user avoid comments overlap (if you select a single node and it has children it will lay out its children, otherwise it will layout selected nodes):
    1. <b>Lay out all increasing space</b>: lay out increasing space between nodes (+0.5)
    2. <b>Lay out all decreasing space</b>: lay out increasing space between nodes (-0.5)
    3. <b>Lay out all to x.y</b>: quick layout all to fixed space value
11. <b>"Settings" submenu</b>: these options let change auto-tranlsate settings: 
    1. <b>Auto translate new nodes comments</b>: translates online documentation headline comment when creating a new node, 
        NOTE: this options delays node creation depending on your network connection while requesting comment tranlsation to Google.
    2. <b>Set auto translate languate</b>: insert desidered language, eg: en (no translation), it, fr, es, ru etc

## NOTE: ## 
1. Scripts works when selecting a single node and with multiple nodes
2. Some nodes don't have headline or the whole documentation file.
3. Script should work on every OS due to OS path separator code, if fails fix/report please.
4. Scripts are separated to make them simpler to study and undertand. 

## CONTRIBUTING: ##
Please feel free to fix/optimize the scripts. 