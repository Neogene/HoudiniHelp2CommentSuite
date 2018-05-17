import hou
import sys
      
def main():
    
    if len(sys.argv)>=2:
        choice = int(sys.argv[1])

        if choice == 0:
            #disable Geometry file generation
            if hou.node("/").userData("h2c_destroy_geometry_file_creation") == None or int(hou.node("/").userData("h2c_destroy_geometry_file_creation")) == 0:
                hou.node("/").setUserData("h2c_destroy_geometry_file_creation", str(1))
                hou.ui.setStatusMessage("H2C: destroy file geometry in geometry ON.")
            else:
                hou.node("/").setUserData("h2c_destroy_geometry_file_creation", str(0))
                hou.ui.setStatusMessage("H2C: destroy file geometry in geometry OFF.")
        
main()