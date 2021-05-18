__author__ = 'Ankit Pant'
__email__ = "maven7@tutanota.com"
__status__ = "alpha"

# imports
from dearpygui.core import *
from dearpygui.simple import *


# TODO: Fix background color of menu bar items in Aurora when going back from light theme

def setTheme():
    """ 
    Method that is responsible to set themes and add specific colours to certain elements
    """
    
    selectedTheme = get_value("Theme")
    if (selectedTheme != "Aurora"):
        set_theme_item(item=mvGuiCol_Button, r=18, g=228, b=180, a=150)
        set_theme_item(item=mvGuiCol_ButtonHovered, r=74, g=183, b=230, a=255)
        set_theme(selectedTheme)
        

    else:
    
        # Window, frame, properties
        set_style_window_title_align(0.5,0.5)
        set_style_window_padding(9.00, 6.00)
        set_style_frame_padding(5.00, 2.00)
        set_style_item_spacing(9.00, 2.00)
        set_style_item_inner_spacing(5.00, 4.00)
        set_style_touch_extra_padding(0.00, 0.00)
        set_style_indent_spacing(21.00)
        set_style_scrollbar_size(10.00)
        set_style_grab_min_size(12.00)
        set_style_window_border_size(1.00)
        set_style_child_border_size(1.00)
        set_style_popup_border_size(1.00)
        set_style_frame_border_size(0.00)
        set_style_tab_border_size(0.00)
        set_style_window_rounding(8.00)
        set_style_child_rounding(0.00)
        set_style_frame_rounding(5.00)
        set_style_popup_rounding(0.00)
        set_style_scrollbar_rounding(9.00)
        set_style_grab_rounding(5.00)
        set_style_tab_rounding(4.00)
        set_style_window_menu_button_position(mvDir_Left)
        set_style_color_button_position(mvDir_Right)
        set_style_button_text_align(0.50, 0.50)
        set_style_selectable_text_align(0.00, 0.00)
        set_style_display_safe_area_padding(3.00, 3.00)
        set_style_global_alpha(1.00)
        set_style_antialiased_lines(True)
        set_style_antialiased_fill(True)
        set_style_curve_tessellation_tolerance(1.25)
        set_style_circle_segment_max_error(1.60)
        
    

        # General Colors
        set_theme_item(mvGuiCol_WindowBg, 18, 22, 26, 230)
        set_theme_item(mvGuiCol_ChildBg, 27, 37, 58, 201)
        set_theme_item(mvGuiCol_Border, 212, 175, 55, 255)
        set_theme_item(mvGuiCol_BorderShadow, 1, 162, 140, 255)
        set_theme_item(mvGuiCol_FrameBg, 0, 74, 122, 138)
        set_theme_item(mvGuiCol_TitleBg, 59, 89, 164, 255)
        set_theme_item(mvGuiCol_TitleBgActive, 41, 205, 122, 255)
        set_theme_item(mvGuiCol_TitleBgCollapsed, 44, 75, 151, 130)
        set_theme_item(mvGuiCol_MenuBarBg, 37, 40, 113, 139)
        set_theme_item(mvGuiCol_CheckMark, 17, 254, 31, 255)
        set_theme_item(mvGuiCol_Button, 18, 228, 180, 140)
        set_theme_item(mvGuiCol_ButtonHovered, 74, 183, 230, 255)
        set_theme_item(mvGuiCol_Text, 255, 255, 255, 255)
        set_theme_item(mvGuiCol_PopupBg, 29, 54, 32, 224)

        # Specific Colors
        set_item_color("To Do", mvGuiCol_TitleBg, [185,30,10,125])
        set_item_color("To Do", mvGuiCol_WindowBg, [185,30,10,10])
        set_item_color("In Progress", mvGuiCol_TitleBg, [155,190,90,125])
        set_item_color("In Progress", mvGuiCol_WindowBg, [155,190,90,10])
        set_item_color("Done", mvGuiCol_TitleBg, [25,220,10,125])
        set_item_color("Done", mvGuiCol_WindowBg, [25,220,10,10])

        allElements = get_all_items()
        for element in allElements:
            if "delete" in element:
                set_item_color(element, mvGuiCol_Button, [205, 0, 0, 150])
                set_item_color(element, mvGuiCol_ButtonHovered, [205, 0, 80, 180])
            if "Add" in element:
                set_item_color(element, mvGuiCol_Button, [0, 205, 0, 150])
                set_item_color(element, mvGuiCol_ButtonHovered, [0, 205, 30, 180])
            if "archives" in element:
                set_item_color(element, mvGuiCol_Button, [180, 125, 0, 150])
                set_item_color(element, mvGuiCol_ButtonHovered, [190, 155, 30, 170])

