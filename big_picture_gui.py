


# imports
import datetime
import uuid
import _pickle as pickle
from dearpygui.core import *
from dearpygui.simple import *
from core_files import projectsDS as pds


projects = {}

statusCodes = {"To Do": "INI", "In Progress": "INP", "Done": "COM", "Archives": "ARC"}
inverseStatusCodes = {"INI": "To Do", "INP": "In Progress", "COM": "Done", "ARC":"Archives"}

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


def incrementTaskItemCount(taskItem, totalInc = True):
    # Set Task counts
    if totalInc:
        totalCurrentTasks = int(get_value("Total Current Task Items"))
        totalCurrentTasks += 1
        set_value("Total Current Task Items", str(totalCurrentTasks))
    itemToIncrement = taskItem + " Task Items"
    taskCounter = int(get_value(itemToIncrement))
    taskCounter += 1
    set_value(itemToIncrement, taskCounter)

def decrementTaskItemCount(taskItem, totalDec = True):
    if totalDec:
        totalCurrentTasks = int(get_value("Total Current Task Items"))
        totalCurrentTasks -= 1
        set_value("Total Current Task Items", str(totalCurrentTasks))
    itemToIncrement = taskItem + " Task Items"
    taskCounter = int(get_value(itemToIncrement))
    taskCounter -= 1
    set_value(itemToIncrement, taskCounter)


def moveToArchive(sender,data):
    print("Moving task to Archive")
    widget = data[0]
    stage = data[1]
    elements = data[2:-1]
    decrementTaskItemCount(stage)
    move_item(item=widget, parent="Archives")
    for elem in elements:
        hide_item(elem)
    elementId = widget[2:34]
    status = statusCodes["Archives"]
    currentProject = projects[elementId]
    currentProject.updateStatus(status)

def deleteProjectItem(sender,data):
    print("Deleting Item")
    widget = data[0]
    stage = data[1]
    if stage != "Archives":
        decrementTaskItemCount(stage)
    delete_item(widget)
    elementId = widget[2:34]
    del projects[elementId]

def moveProjectItemLeft(sender, data):
    print("Moving Task to left")
    widget = get_item_parent(get_item_parent(get_item_parent(sender)))
    stage = get_item_parent(widget)
    arrowButton = data
    elementId = widget[2:34]
    currentProject = projects[elementId]

    if stage == "Done":
        move_item(item=widget, parent="In Progress")
        show_item(arrowButton)
        decrementTaskItemCount("Done", False)
        incrementTaskItemCount("In Progress", False)
        status = statusCodes["In Progress"]
        currentProject.updateStatus(status)

    elif stage == "In Progress":
        move_item(item=widget, parent="To Do")
        show_item(arrowButton)
        hide_item(sender)
        decrementTaskItemCount("In Progress", False)
        incrementTaskItemCount("To Do", False)
        status = statusCodes["To Do"]
        currentProject.updateStatus(status)

def moveProjectItemRight(sender, data):
    print("Moving Task to right")
    widget = get_item_parent(get_item_parent(get_item_parent(sender)))
    stage = get_item_parent(widget)
    arrowButton = data
    elementId = widget[2:34]
    currentProject = projects[elementId]
    if stage == "To Do":
        move_item(item=widget, parent="In Progress")
        show_item(arrowButton)
        decrementTaskItemCount("To Do", False)
        incrementTaskItemCount("In Progress", False)
        status = statusCodes["In Progress"]
        currentProject.updateStatus(status)

    elif stage == "In Progress":
        move_item(item=widget, parent="Done")
        show_item(arrowButton)
        hide_item(sender)
        decrementTaskItemCount("In Progress", False)
        incrementTaskItemCount("Done", False)
        status = statusCodes["Done"]
        currentProject.updateStatus(status)

def moveProjectItemUp(sender, data):
    print("Moving Task to up")
    parent = get_item_parent(sender)
    grandParent = get_item_parent(parent)
    if grandParent != "Archives":
        move_item_up(grandParent)
    else:
        move_item_up(parent)

def moveProjectItemDown(sender, data):
    print("Moving Task to down")
    parent = get_item_parent(sender)
    grandParent = get_item_parent(parent)
    if grandParent != "Archives":
        move_item_down(grandParent)
    else:
        move_item_down(parent)

def changeProjectItemText(sender,data):
    print("Change to Project Title")
    widgetName = data[0]
    elementId = widgetName[2:34]
    currentProject = projects[elementId]
    newTitle = get_value(sender)
    currentProject.updateTitle(newTitle)


def addWidget(parent, groupName, childName, pName):
    add_group(name=groupName, parent=parent)
    add_spacing(count=7, parent=groupName)
    add_child(name=childName, parent=groupName, autosize_x=True, autosize_y=False, height=80, horizontal_scrollbar=True)
    with menu_bar(childName+"menu"):
        add_button(childName+"left", direction=get_value("Left Arrow"), arrow=True, callback=moveProjectItemLeft, callback_data=childName+"right")
        if parent=="To Do" or parent=="Archives":
            hide_item(childName+"left")
        add_input_text(childName+"s1", width=1)
        add_button(childName+"archives", label="Move to Archives", callback=moveToArchive, callback_data=[groupName, parent, childName+"left", childName+"right", childName+"archives"])
        if parent == "Archives":
            hide_item(childName+"archives")
        add_button(childName+"delete", label="Delete", callback=deleteProjectItem, callback_data=[groupName, parent])
        add_input_text(childName+"s2", width=1)
        add_button(childName+"right", direction=get_value("Right Arrow"), arrow=True, callback=moveProjectItemRight, callback_data=childName+"left")
        if parent == "Done" or parent =="Archives":
            hide_item(childName+"right")

    add_spacing(count=3)
    add_button(childName+"top", direction=get_value("Up Arrow"), arrow=True, callback=moveProjectItemUp)
    add_same_line()
    add_button(childName+"down", direction=get_value("Down Arrow"), arrow=True, callback=moveProjectItemDown)
    add_same_line()
    add_input_text(childName+"s3", width=1)
    add_same_line()
    add_input_text(childName+"Project", default_value=pName, width=-1, on_enter=True, callback=changeProjectItemText, callback_data=[groupName, parent])
    end()
    add_spacing(count=7, parent=groupName)
    end()

def addNewProjectItem(sender, data):
    parent = data
    status = statusCodes[parent]
    newTaskId = uuid.uuid4().hex
    taskItemCount = int(get_value(parent + " Task Items")) + 1
    pName = "New " + parent + " Project " + str(taskItemCount)
    newProject = pds.Project(newTaskId, pName, status)
    global projects
    projects[newTaskId] = newProject
    groupName = "##" + newTaskId + "_group_"
    childName = "##" + newTaskId + "_child_"

    incrementTaskItemCount(parent)

    addWidget(parent, groupName, childName, pName)
    

def addExistingProjectItems(projectItem):
    groupName = "##" + projectItem.projectId + "_group_"
    childName = "##" + projectItem.projectId + "_child_"
    pName = projectItem.projectName
    status = projectItem.projectStatus
    parent =inverseStatusCodes[status]
    incrementTaskItemCount(parent)
    addWidget(parent, groupName, childName, pName)

def writeToFile():
    with open("./storedProjects", 'wb') as outFile:
        global projects
        # print(projects)
        outFile.write(pickle.dumps(projects))

def initialiseProjectsList(storedProjects):
    global projects
    projects = storedProjects
    for key in projects:
        addExistingProjectItems(projects[key])

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
    add_button("Add Task##To Do", parent="Status To Do", callback=addNewProjectItem, callback_data="To Do")
    add_spacing(count=3)
    add_text("\t\tStatus: ")
    add_same_line()
    add_input_text(name="##TDo", source="To Do Task Items", width=50)
    add_same_line()
    add_text("/")
    add_same_line()
    add_input_text(name="##TCompleted", source="Total Current Task Items", width=50)
    add_same_line()
    

with window("Status In Progress", autosize=False, no_title_bar=True, no_scrollbar=False, no_move=True, no_resize=True):
    set_item_style_var("Status In Progress", mvGuiStyleVar_WindowBorderSize, [0])
    add_text("\t\t\t\t")
    add_same_line()
    add_button("Add Task##In Progress", parent="Status In Progress", callback=addNewProjectItem, callback_data="In Progress")
    add_spacing(count=3)
    add_text("\t\tStatus: ")
    add_same_line()
    add_input_text(name="##InP", source="In Progress Task Items", width=50)
    add_same_line()
    add_text("/")
    add_same_line()
    add_input_text(name="##ICompleted", source="Total Current Task Items", width=50)
    add_same_line()
    

with window("Status Done", autosize=False, no_title_bar=True, no_scrollbar=False, no_move=True, no_resize=True):
    set_item_style_var("Status Done", mvGuiStyleVar_WindowBorderSize, [0])
    add_text("\t\t\t\t")
    add_same_line()
    add_button("Add Task##Done", parent="Status Done", callback=addNewProjectItem, callback_data="Done")
    add_spacing(count=3)
    add_text("\t\tStatus: ")
    add_same_line()
    add_input_text(name="##Don", source="Done Task Items", width=50)
    add_same_line()
    add_text("/")
    add_same_line()
    add_input_text(name="##DCompleted", source="Total Current Task Items", width=50)
    add_same_line()
    


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
    set_value("Total Current Task Items", "0")
    set_value("To Do Task Items", "0")
    set_value("In Progress Task Items", "0")
    set_value("Done Task Items", "0")

    # ! For Theming
    # show_style_editor() 
    try:
        with open('storedProjects', 'rb') as inFile:
            try:
                storedProjects = pickle.load(inFile)
                print("Stored Projects (if any) loaded in memory!")
                initialiseProjectsList(storedProjects)
            
            except:
                print("No stored projects found!")
    except:
        with open('storedProjects', 'wb') as inFile:
            pass

    
    
    start_dearpygui(primary_window="Main")

    writeToFile()
    print("Projects persisted in memory... Exiting program")
    stop_dearpygui()



