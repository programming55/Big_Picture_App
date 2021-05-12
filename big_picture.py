# imports
from dearpygui.core import *
from dearpygui.simple import *

# font and other window settings
add_additional_font("./fonts/CascadiaCodePL-Regular.otf", 20)
set_main_window_title("The Big Picture")
set_main_window_resizable(False)
set_main_window_pos(100,30)



# set whole Application Theme
def setTheme(sender, data):
    set_theme(sender)


# reposition and resize windows
def resizeWindows(sender, data):
    mainWindowWidth = get_main_window_size()[0]
    mainWindowHeight = get_main_window_size()[1]

    heightTopPanel = int(mainWindowHeight * 0.1)
    heightMiddlePanels = int(mainWindowHeight * 0.70)
    heightBottomPanel = int(mainWindowHeight * 0.6)

    widthMiddlePanels = int(mainWindowWidth * 0.32)
    widthTopPanel = int(mainWindowWidth * 0.97)
    widthBottomPanel = int(mainWindowWidth * 0.97)

    yPosTopPanel = int(mainWindowHeight * 0.03)
    yPosMiddlePanels = int(mainWindowHeight * 0.20)
    yPosBottomPanel = int(mainWindowHeight * 0.15)

    xPosTopPanel = int(mainWindowWidth * 0.009)
    xPosLeftPanel = int(mainWindowWidth * 0.008)
    xPosMiddlePanel = int(mainWindowWidth * 0.0073 + xPosLeftPanel + widthMiddlePanels)
    xPosRightPanel = int(mainWindowWidth * 0.0073 + xPosMiddlePanel + widthMiddlePanels)
    xPosBottomPanel = int(mainWindowWidth * 0.009)

    # Assigning dimensions to various windows

    # Top Panel
    set_window_pos("Top Panel", x=xPosTopPanel, y=yPosTopPanel)
    set_item_width("Top Panel", width=widthTopPanel)
    set_item_height("Top Panel", height=heightTopPanel)

    # Left Panel
    set_window_pos("To Do", x=xPosLeftPanel, y=yPosMiddlePanels)
    set_item_width("To Do", width=widthMiddlePanels)
    set_item_height("To Do", height=heightMiddlePanels)

    # Middle Panel
    set_window_pos("In Progress", x=xPosMiddlePanel, y=yPosMiddlePanels)
    set_item_width("In Progress", width=widthMiddlePanels)
    set_item_height("In Progress", height=heightMiddlePanels)

    # Right Panel
    set_window_pos("Done", x=xPosRightPanel, y=yPosMiddlePanels)
    set_item_width("Done", width=widthMiddlePanels)
    set_item_height("Done", height=heightMiddlePanels)

    # Bottom Panel
    set_window_pos("Archives", x=xPosBottomPanel, y=yPosBottomPanel)
    set_item_width("Archives", width=widthBottomPanel)
    set_item_height("Archives", height=heightBottomPanel)


def moveToArchive(sender,data):
    print("Moving task to Archive")
    grandParent = get_item_parent(get_item_parent(sender))
    move_item(item=grandParent, parent="Archives")
    for elem in data:
        hide_item(elem)

def deleteTaskItem(sender,data):
    print("Deleting Item")
    grandParent = get_item_parent(get_item_parent(sender))
    delete_item(grandParent)

def moveTaskItemLeft(sender, data):
    print("Moving Task to left")
    oldParent = get_item_parent(sender)
    grandParent = get_item_parent(oldParent)
    greatGrandParent = get_item_parent(grandParent)
    print(oldParent,grandParent,greatGrandParent)
    if greatGrandParent == "Done":
        move_item(item=grandParent, parent="In Progress")
        show_item(data)
    elif greatGrandParent == "In Progress":
        move_item(item=grandParent, parent="To Do")
        show_item(data)
        hide_item(sender)

def moveTaskItemRight(sender, data):
    print("Moving Task to right")
    oldParent = get_item_parent(sender)
    grandParent = get_item_parent(oldParent)
    greatGrandParent = get_item_parent(grandParent)
    print(oldParent,grandParent,greatGrandParent)
    if greatGrandParent == "To Do":
        move_item(item=grandParent, parent="In Progress")
        show_item(data)
    elif greatGrandParent == "In Progress":
        move_item(item=grandParent, parent="Done")
        show_item(data)
        hide_item(sender)

def moveTaskItemUp(sender, data):
    print("Moving Task to up")
    parent = get_item_parent(sender)
    move_item_up(parent)

def moveTaskItemDown(sender, data):
    print("Moving Task to down")
    parent = get_item_parent(sender)
    move_item_down(parent)

def changeTaskItemText(sender,data):
    print("Change to Project Title")

def add_task_item(sender, data):
    parent = data[0]
    itemNum = data[1]
    title = data[2]
    childName = "##" + parent + "_child_" + str(itemNum)
    beforeItem = "Spacer##"+parent
    
    add_child(name=childName, parent=parent,autosize_x=True, autosize_y=False, height=80, horizontal_scrollbar=True, before=beforeItem)
    with menu_bar(childName+"Menu"):
        add_button(childName+"left", direction=get_value("Left Arrow"), arrow=True, callback=moveTaskItemLeft, callback_data=childName+"right")
        if parent=="To Do" or parent=="Archives":
            hide_item(childName+"left")
        add_input_text(childName+"s1", width=1)
        add_button(childName+"archives", label="Move to Archives", callback=moveToArchive, callback_data=[childName+"left", childName+"right", childName+"archives"])
        if parent == "Archives":
            hide_item(childName+"archives")
        add_button(childName+"delete", label="Delete", callback=deleteTaskItem)
        add_input_text(childName+"s2", width=1)
        add_button(childName+"right", direction=get_value("Right Arrow"), arrow=True, callback=moveTaskItemRight, callback_data=childName+"left")
        if parent == "Done" or parent =="Archives":
            hide_item(childName+"right")
    # add_spacing(count=3)
    # add_separator()
    add_spacing(count=3)
    add_button(childName+"top", direction=get_value("Up Arrow"), arrow=True, callback=moveTaskItemUp)
    add_same_line()
    add_button(childName+"down", direction=get_value("Down Arrow"), arrow=True, callback=moveTaskItemDown)
    add_same_line()
    add_input_text(childName+"s3", width=1)
    add_same_line()
    add_input_text(childName+"Project", default_value=title, width=-1, callback=changeTaskItemText)
    end()
    # TODO: Add this spacing after figuring out drag events
    # add_spacing(count=15, parent=parent)
    

with window("Top Panel", autosize=False, no_title_bar=True, no_scrollbar=False, no_close=True, collapsed=False, no_collapse=True, no_resize=False, no_move=False, no_background=False, horizontal_scrollbar=True):
    add_text("This is Top Window")

with window("Archives", autosize=False, no_title_bar=False, no_scrollbar=False, no_close=True, collapsed=True, no_collapse=False, no_resize=False, no_move=False, no_background=False, horizontal_scrollbar=True):
    add_spacing(count=5)

with window("To Do", autosize=False, no_title_bar=False, no_scrollbar=False, no_close=True, collapsed=False, no_collapse=True, no_resize=False, no_move=False, no_background=False, horizontal_scrollbar=True):
    add_spacing(count=5)
    add_dummy(name="Spacer##To Do", parent="To Do")
    add_spacing(count=15)
    add_button("Add Task##To Do", parent="To Do", callback=add_task_item, callback_data=["To Do", 99, "New To Do"])
    
    

with window("In Progress", autosize=False, no_title_bar=False, no_scrollbar=False, no_close=True, collapsed=False, no_collapse=True, no_resize=False, no_move=False, no_background=False, horizontal_scrollbar=True):
    add_spacing(count=5)
    add_dummy(name="Spacer##In Progress", parent="In Progress")
    add_spacing(count=15)
    add_button("Add Task##In Progress", parent="In Progress", callback=add_task_item, callback_data=["In Progress", 99, "New In Progress"])

with window("Done", autosize=False, no_title_bar=False, no_scrollbar=False, no_close=True, collapsed=False, no_collapse=True, no_resize=False, no_move=False, no_background=False, horizontal_scrollbar=True):
    add_spacing(count=5)
    add_dummy(name="Spacer##Done", parent="Done")
    add_spacing(count=15)
    add_button("Add Task##Done", parent="Done", callback=add_task_item, callback_data=["Done", 99, "New Done"])
    

with window("Main", horizontal_scrollbar=True, no_scrollbar=False):
    set_theme("Gold")
    set_style_window_title_align(0.5,0.5)
    with menu_bar('Main Menu'):
        with menu("Themes"):
            add_menu_item("Gold", callback=setTheme)
            add_menu_item("Dark", callback=setTheme)
            add_menu_item("Classic", callback=setTheme)
        with menu("Layout"):
            add_menu_item("Reset to Default Layout", callback=resizeWindows)



if __name__ == '__main__':
    set_start_callback(resizeWindows)
    set_resize_callback(resizeWindows)
    add_value("Left Arrow", 0)
    add_value("Right Arrow", 1)
    add_value("Up Arrow", 2)
    add_value("Down Arrow", 3)
    add_value("Total tasks in archives", 0)
    # set_value("Right Arrow", 1)

    # ! For Theming
    # show_style_editor() 

   


    for i in range(0,2):
        add_task_item("To Do", ["To Do", i, "Todo Task"+str(i)])
        add_task_item("In Progress", ["In Progress", i, "In Progress Task "+str(i)])
        add_task_item("Done", ["Done", i, "Done Task"+str(i)])
    start_dearpygui(primary_window="Main")


    stop_dearpygui()



