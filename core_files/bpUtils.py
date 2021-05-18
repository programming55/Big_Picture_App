__author__ = 'Ankit Pant'
__email__ = "maven7@tutanota.com"
__status__ = "alpha"

# imports
import uuid
import _pickle as pickle
from pathlib import Path
from dearpygui.core import *
from dearpygui.simple import *
from core_files import projectsDS as pds

# dictionary to store each project item with its unique id as key
projects = {}

# Status Codes are used to describe the current stage of a particular project item
statusCodes = {"To Do": "INI", "In Progress": "INP", "Done": "COM", "Archives": "ARC"}
inverseStatusCodes = {"INI": "To Do", "INP": "In Progress", "COM": "Done", "ARC":"Archives"}

def incrementTaskItemCount(taskItem, totalInc = True):
    """
    Used to increment the count of project items in a particular stage as well as total project items being tracked.
    If parameter totalInc is true, the value of count of total project is also incremented as is in the case of creating a new project task.
    If parameter totalInc is false, the value of only the current stage items to which the project item belongs is incremented as is in the case of moving a task from one stage to another.
    """
    
    if totalInc:
        totalCurrentTasks = int(get_value("Total Current Task Items"))
        totalCurrentTasks += 1
        set_value("Total Current Task Items", str(totalCurrentTasks))
    itemToIncrement = taskItem + " Task Items"
    taskCounter = int(get_value(itemToIncrement))
    taskCounter += 1
    set_value(itemToIncrement, taskCounter)

def decrementTaskItemCount(taskItem, totalDec = True):
    """
    Used to decrement the count of project items in a particular stage as well as total project items being tracked.
    If parameter totalInc is true, the value of count of total project is also decremented as is in the case of moving the project task to archives.
    If parameter totalInc is false, the value of only the current stage items to which the project item belongs is decremented as is in the case of moving a task from one stage to another.
    """

    if totalDec:
        totalCurrentTasks = int(get_value("Total Current Task Items"))
        totalCurrentTasks -= 1
        set_value("Total Current Task Items", str(totalCurrentTasks))
    itemToIncrement = taskItem + " Task Items"
    taskCounter = int(get_value(itemToIncrement))
    taskCounter -= 1
    set_value(itemToIncrement, taskCounter)

def moveToArchive(sender,data):
    """
    Moves the project item from the current stage to Archives.
    """

    print("Moving task to Archive")
    widget = get_item_parent(get_item_parent(get_item_parent(sender)))
    stage = get_item_parent(widget)
    decrementTaskItemCount(stage)
    move_item(item=widget, parent="Archives")
    for elem in data:
        hide_item(elem)
    elementId = widget[2:34]
    status = statusCodes["Archives"]
    currentProject = projects[elementId]
    currentProject.updateStatus(status)

def deleteProjectItem(sender,data):
    """
    Deletes the particular project item (widget) from which it is called
    """

    print("Deleting Item")
    widget = get_item_parent(get_item_parent(get_item_parent(sender)))
    stage = get_item_parent(widget)
    if stage != "Archives":
        decrementTaskItemCount(stage)
    delete_item(widget)
    elementId = widget[2:34]
    del projects[elementId]

def moveProjectItemLeft(sender, data):
    """
    Moves the current project item to the left stage. 
    From Done to In Progress or form In Progress to To Do
    """

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
    """
    Moves the current project item to the right stage. 
    From To Do to In Progress or form In Progress to Done
    """

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
    """
    Moves the project item up (before any other project item if it exits) as a way to represent priority.
    The items at the top of the stage are implied to be having higher priority.
    """

    print("Moving Task to up")
    parent = get_item_parent(sender)
    grandParent = get_item_parent(parent)
    if grandParent != "Archives":
        move_item_up(grandParent)
    else:
        move_item_up(parent)

def moveProjectItemDown(sender, data):
    """
    Moves the project item down (after any other project item if it exits) as a way to represent priority.
    The items at the bottom of the stage are implied to be having lower priority.
    """

    print("Moving Task to down")
    parent = get_item_parent(sender)
    grandParent = get_item_parent(parent)
    if grandParent != "Archives":
        move_item_down(grandParent)
    else:
        move_item_down(parent)

def changeProjectItemText(sender,data):
    """
    Callback function that tracks and saves (in memory) the changes made to project item names (titles).
    This method is called once the project name is changed and enter(return) key is pressed to confirm the new name.
    """

    print("Change to Project Title")
    widgetName = data[0]
    elementId = widgetName[2:34]
    currentProject = projects[elementId]
    newTitle = get_value(sender)
    currentProject.updateTitle(newTitle)

def addWidget(parent, groupName, childName, pName):
    """
    Adds a project item widget to one of the stages (defined by parent) or the Archives. The widget consists of one unit comprising of all GUI elements that are associated with one project item.
    """

    add_group(name=groupName, parent=parent)
    add_spacing(count=7, parent=groupName)
    add_child(name=childName, parent=groupName, autosize_x=True, autosize_y=False, height=80, horizontal_scrollbar=True)
    with menu_bar(childName+"menu"):
        add_button(childName+"left", direction=get_value("Left Arrow"), arrow=True, callback=moveProjectItemLeft, callback_data=childName+"right")
        if parent=="To Do" or parent=="Archives":
            hide_item(childName+"left")
        add_input_text(childName+"s1", width=1)
        add_button(childName+"archives", label="Move to Archives", callback=moveToArchive, callback_data=[childName+"left", childName+"right", childName+"archives"])
        if parent == "Archives":
            hide_item(childName+"archives")
        add_button(childName+"delete", label="Delete", callback=deleteProjectItem)
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
    """
    Callback method that is invoked once the user clicks on Add Task button in either of the stages.
    This creates a new unique id for the project item and then calls addWidget method to create a widget for the new project item.
    """

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
    """
    Method that extracts information about the project items stored in the file and then calls addWidget method to create a widget for the exisinng project item.
    """

    groupName = "##" + projectItem.projectId + "_group_"
    childName = "##" + projectItem.projectId + "_child_"
    pName = projectItem.projectName
    status = projectItem.projectStatus
    parent =inverseStatusCodes[status]
    if parent != "Archives":
        incrementTaskItemCount(parent)
    addWidget(parent, groupName, childName, pName)

def writeToFile():
    """
    Method that writes the project items' information from the memory to the disk so that the project items created persist and can be loaded on reopeining the app.
    """

    filePath = Path("./storedProjects")
    with open(filePath, 'wb') as outFile:
        global projects
        # print(projects)
        outFile.write(pickle.dumps(projects))

def initialiseProjectsList(storedProjects):
    """
    Method that takes the project item object as input and uses to information to call methods to create project item widgets for the already existing project items that are read from persistent storage.
    """

    global projects
    projects = storedProjects
    for key in projects:
        addExistingProjectItems(projects[key])