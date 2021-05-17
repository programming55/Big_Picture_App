


# imports
import datetime
import _pickle as pickle
from pathlib import Path
from dearpygui.core import *
from dearpygui.simple import *
from core_files import projectsDS as pds
from core_files import bpUtils



# font and other window settings
add_additional_font("./fonts/CascadiaCodePL-Regular.otf", 20)
set_main_window_title("The Big Picture")
set_main_window_resizable(False)
set_main_window_pos(100,30)



# set whole Application Theme
def setTheme(sender, data):
    """
    Uses the set_theme internal function of dearpygui to set the theme of the window
    """

    set_theme(sender)


# reposition and resize windows
def resizeWindows(sender, data):
    """
    Method that is used to resize and position windows in the manner originally intended. Called during startup of the GUI as well as on clicking Reset to Default Layout.
    """

    mainWindowWidth = get_main_window_size()[0]
    mainWindowHeight = get_main_window_size()[1]

    heightTopPanel = int(mainWindowHeight * 0.05)
    heightMiddlePanels = int(mainWindowHeight * 0.70)
    heightArchivePanel = int(mainWindowHeight * 0.6)
    heightBottomPanels = int(mainWindowHeight * 0.09)

    widthMiddlePanels = int(mainWindowWidth * 0.32)
    widthTopPanel = int(mainWindowWidth * 0.97)
    widthArchivePanel = int(mainWindowWidth * 0.97)

    yPosTopPanel = int(mainWindowHeight * 0.03)
    yPosMiddlePanels = int(mainWindowHeight * 0.15)
    yPosArchivePanel = int(mainWindowHeight * 0.1)
    yposBottomPanels = int(mainWindowHeight * 0.85)

    xPosTopPanel = int(mainWindowWidth * 0.009)
    xPosLeftPanel = int(mainWindowWidth * 0.008)
    xPosMiddlePanel = int(mainWindowWidth * 0.0073 + xPosLeftPanel + widthMiddlePanels)
    xPosRightPanel = int(mainWindowWidth * 0.0073 + xPosMiddlePanel + widthMiddlePanels)
    xPosArchivePanel = int(mainWindowWidth * 0.009)

    # Assigning dimensions to various windows

    # Top Panel
    set_window_pos("Top Panel", x=xPosTopPanel, y=yPosTopPanel)
    set_item_width("Top Panel", width=widthTopPanel)
    set_item_height("Top Panel", height=heightTopPanel)

    # To Do Panel
    set_window_pos("To Do", x=xPosLeftPanel, y=yPosMiddlePanels)
    set_item_width("To Do", width=widthMiddlePanels)
    set_item_height("To Do", height=heightMiddlePanels)

    # In Progress Panel
    set_window_pos("In Progress", x=xPosMiddlePanel, y=yPosMiddlePanels)
    set_item_width("In Progress", width=widthMiddlePanels)
    set_item_height("In Progress", height=heightMiddlePanels)

    # Done Panel
    set_window_pos("Done", x=xPosRightPanel, y=yPosMiddlePanels)
    set_item_width("Done", width=widthMiddlePanels)
    set_item_height("Done", height=heightMiddlePanels)

    # Archives Panel
    set_window_pos("Archives", x=xPosArchivePanel, y=yPosArchivePanel)
    set_item_width("Archives", width=widthArchivePanel)
    set_item_height("Archives", height=heightArchivePanel)

    # To Do Status Panel
    set_window_pos("Status To Do", x=xPosLeftPanel, y=yposBottomPanels)
    set_item_width("Status To Do", width=widthMiddlePanels)
    set_item_height("Status To Do", height=heightBottomPanels)

    # In Progress Status Panel
    set_window_pos("Status In Progress", x=xPosMiddlePanel, y=yposBottomPanels)
    set_item_width("Status In Progress", width=widthMiddlePanels)
    set_item_height("Status In Progress", height=heightBottomPanels)

    # Done Status Panel
    set_window_pos("Status Done", x=xPosRightPanel, y=yposBottomPanels)
    set_item_width("Status Done", width=widthMiddlePanels)
    set_item_height("Status Done", height=heightBottomPanels)


with window("Top Panel", autosize=False, no_title_bar=True, no_scrollbar=False, no_close=True, collapsed=False, no_collapse=True, no_resize=True, no_move=True, no_background=False, horizontal_scrollbar=True):
    set_item_style_var("Top Panel", mvGuiStyleVar_WindowBorderSize, [0])
    week = datetime.date.today().strftime("%W")
    today = datetime.datetime.now().strftime("%A, %d %B %Y")
    thisWeek = "Week: " + week
    add_text(thisWeek)
    add_same_line()
    add_text("\t\t\t\t\t\t\t\t\t\t")
    add_same_line()
    add_text(today)
   

with window("Archives", autosize=False, no_title_bar=False, no_scrollbar=False, no_close=True, collapsed=True, no_collapse=False, no_resize=False, no_move=False, no_background=False, horizontal_scrollbar=True):
    pass

with window("To Do", autosize=False, no_title_bar=False, no_scrollbar=False, no_close=True, collapsed=False, no_collapse=True, no_resize=True, no_move=True, no_background=False, horizontal_scrollbar=True):
    # add_group("mainGroup##To Do", parent="To Do")
    # add_dummy(name="Spacer##To Do", parent="mainGroup##To Do")
    # end()
    pass
    

with window("In Progress", autosize=False, no_title_bar=False, no_scrollbar=False, no_close=True, collapsed=False, no_collapse=True, no_resize=True, no_move=True, no_background=False, horizontal_scrollbar=True):
    # add_group("mainGroup##In Progress", parent="In Progress")
    # add_dummy(name="Spacer##In Progress", parent="mainGroup##In Progress")
    # end()
    pass

with window("Done", autosize=False, no_title_bar=False, no_scrollbar=False, no_close=True, collapsed=False, no_collapse=True, no_resize=True, no_move=True, no_background=False, horizontal_scrollbar=True):
    # add_group("mainGroup##Done", parent="Done")
    # add_dummy(name="Spacer##Done", parent="mainGroup##Done")
    # end()
    pass


with window("Status To Do", autosize=False, no_title_bar=True, no_scrollbar=False, no_move=True, no_resize=True):
    set_item_style_var("Status To Do", mvGuiStyleVar_WindowBorderSize, [0])
    add_text("\t\t\t\t")
    add_same_line()
    add_button("Add Task##To Do", parent="Status To Do", callback=bpUtils.addNewProjectItem, callback_data="To Do")
    add_spacing(count=3)
    add_text("\t\tStatus: ")
    add_same_line()
    add_input_text(name="##TDo", source="To Do Task Items", width=50, readonly=True)
    add_same_line()
    add_text("/")
    add_same_line()
    add_input_text(name="##TCompleted", source="Total Current Task Items", width=50, readonly=True)
    add_same_line()
    

with window("Status In Progress", autosize=False, no_title_bar=True, no_scrollbar=False, no_move=True, no_resize=True):
    set_item_style_var("Status In Progress", mvGuiStyleVar_WindowBorderSize, [0])
    add_text("\t\t\t\t")
    add_same_line()
    add_button("Add Task##In Progress", parent="Status In Progress", callback=bpUtils.addNewProjectItem, callback_data="In Progress")
    add_spacing(count=3)
    add_text("\t\tStatus: ")
    add_same_line()
    add_input_text(name="##InP", source="In Progress Task Items", width=50, readonly=True)
    add_same_line()
    add_text("/")
    add_same_line()
    add_input_text(name="##ICompleted", source="Total Current Task Items", width=50, readonly=True)
    add_same_line()
    

with window("Status Done", autosize=False, no_title_bar=True, no_scrollbar=False, no_move=True, no_resize=True):
    set_item_style_var("Status Done", mvGuiStyleVar_WindowBorderSize, [0])
    add_text("\t\t\t\t")
    add_same_line()
    add_button("Add Task##Done", parent="Status Done", callback=bpUtils.addNewProjectItem, callback_data="Done")
    add_spacing(count=3)
    add_text("\t\tStatus: ")
    add_same_line()
    add_input_text(name="##Don", source="Done Task Items", width=50, readonly=True)
    add_same_line()
    add_text("/")
    add_same_line()
    add_input_text(name="##DCompleted", source="Total Current Task Items", width=50, readonly=True)
    add_same_line()
    


with window("Main", horizontal_scrollbar=True, no_scrollbar=False):
    set_theme("Gold")
    set_style_window_title_align(0.5,0.5)
    with menu_bar('Main Menu'):
        with menu("File"):
            add_menu_item("Save", callback=bpUtils.writeToFile)
        with menu("Themes"):
            add_menu_item("Gold", callback=setTheme)
            add_menu_item("Dark", callback=setTheme)
            add_menu_item("Classic", callback=setTheme)
        with menu("Layout"):
            add_menu_item("Reset to Default Layout", callback=resizeWindows)
    

if __name__ == '__main__':
    """
    Main method that executes on running the python program. Constants and Shared Variables are declared and defined here. This method also reads for any existing stored Project Items as well as calls a method to write current Project Items to persistent storage on program exit
    """
    set_start_callback(resizeWindows)
    set_resize_callback(resizeWindows)
    add_value("Left Arrow", 0)
    add_value("Right Arrow", 1)
    add_value("Up Arrow", 2)
    add_value("Down Arrow", 3)
    set_value("Total Current Task Items", "0")
    set_value("To Do Task Items", "0")
    set_value("In Progress Task Items", "0")
    set_value("Done Task Items", "0")

    # ! For Theming
    # show_style_editor() 

    filePath = Path("./storedProjects")
    try:
        with open(filePath, 'rb') as inFile:
            try:
                storedProjects = pickle.load(inFile)
                print("Stored Projects (if any) loaded in memory!")
                bpUtils.initialiseProjectsList(storedProjects)
            
            except Exception as e:
                print(e)
                print("No stored projects found!")
    except:
        with open('storedProjects', 'wb') as inFile:
            pass

    
    
    start_dearpygui(primary_window="Main")

    bpUtils.writeToFile()
    print("Projects persisted in memory... Exiting program")
    stop_dearpygui()



