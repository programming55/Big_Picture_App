# imports
from dearpygui.core import *
from dearpygui.simple import *

# font and other window settings
add_additional_font("./fonts/CascadiaCodePL-Regular.otf", 20)


# set whole Application Theme
def setTheme(sender, data):
    set_theme(sender)


# reposition and resize windows
def resizeWindows(sender, data):
    mainWindowWidth = get_main_window_size()[0]
    mainWindowHeight = get_main_window_size()[1]

    heightTopPanel = int(mainWindowHeight * 0.1)
    heightMiddlePanels = int(mainWindowHeight * 0.70)
    heightBottomPanel = int(mainWindowHeight * 0.09)

    widthMiddlePanels = int(mainWindowWidth * 0.32)
    widthTopPanel = int(mainWindowWidth * 0.97)
    widthBottomPanel = int(mainWindowWidth * 0.97)

    yPosTopPanel = int(mainWindowHeight * 0.03)
    yPosMiddlePanels = int(mainWindowHeight * 0.15)
    yPosBottomPanel = int(mainWindowHeight * 0.86)

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


with window("Top Panel", autosize=False, no_title_bar=True, no_scrollbar=False, no_close=True, collapsed=False, no_collapse=True, no_resize=False, no_move=False, no_background=False, horizontal_scrollbar=True):
    add_text("This is Top Window")

with window("Archives", autosize=False, no_title_bar=False, no_scrollbar=False, no_close=True, collapsed=True, no_collapse=False, no_resize=False, no_move=False, no_background=False, horizontal_scrollbar=True):
    add_text("This is Bottom Window")

with window("To Do", autosize=False, no_title_bar=False, no_scrollbar=False, no_close=True, collapsed=False, no_collapse=True, no_resize=False, no_move=False, no_background=False, horizontal_scrollbar=True):
    add_text("This is Left Window")

with window("In Progress", autosize=False, no_title_bar=False, no_scrollbar=False, no_close=True, collapsed=False, no_collapse=True, no_resize=False, no_move=False, no_background=False, horizontal_scrollbar=True):
    add_text("This is Middle Window")

with window("Done", autosize=False, no_title_bar=False, no_scrollbar=False, no_close=True, collapsed=False, no_collapse=True, no_resize=False, no_move=False, no_background=False, horizontal_scrollbar=True):
    add_text("This is Right Window")

with window("Main"):
    set_theme("Gold")
    set_style_window_title_align(0.5,0.5)
    with menu_bar('Main Menu'):
        with menu("Themes"):
            add_menu_item("Gold", callback=setTheme)
            add_menu_item("Dark", callback=setTheme)
            add_menu_item("Classic", callback=setTheme)
        with menu("Layout"):
            add_menu_item("Reset to Default Layout", callback=resizeWindows)

    


set_start_callback(resizeWindows)
set_resize_callback(resizeWindows)

# ! For Theming
# show_style_editor() 

start_dearpygui(primary_window="Main")

stop_dearpygui()



