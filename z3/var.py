
from PyQt6.QtGui import  QFont, QColor

from PyQt6.QtCore import QSize

"""
#dceaf6
#f0f0f0
#e4e4e4

"""
color_list2 = """
#eaeaea
""".strip()
color_list3 = """
#313131
""".strip()
Color_blank2 = QColor(f"{color_list2}")
Color_blank3 = QColor(f"{color_list3}")


copy_mark = ""

back_Color = """
#313131
""".strip()

y = 94
x = y
size = QSize(x,y)

font = QFont("Terminal", 9);font.setHintingPreference(QFont.HintingPreference.PreferFullHinting)

icon_lnk = "conf\\images\\inks.ico"

icon_empty = "conf\\images\\empty.png"

icon_grid = "conf\\images\\grid.png"
icon_trash = "conf\\images\\trash.png"
icon_undo = "conf\\images\\undo.png"



main_folder = "conf\\default\\"

root_path = main_folder + ".inkBox\\"

rot_path = "."


color0 = """
#ffffff
""".strip()
color1 = """
#d5eceb
""".strip()
color12 = """
#fff0c8
""".strip()
"""
#d5c6f5
#e0d3fa
"""
color13 = """
#e8defd
""".strip()
color2 = """
#f8f6ea
""".strip()


color3 = """
#b1e6e4
""".strip()
color3 = """
#98dae2
""".strip()
color3 = """
#8cd8a6
""".strip()

color4 = """
#ed7161
""".strip()
color5 = """
#8db9f8
""".strip()

color6 = """
#ccffcc
""".strip()
############################################################4
Color_blank = QColor(f"{color0}")

Color_link = QColor(f"{color1}")
Color_link2 = QColor(f"{color12}")
# 文件夹
Color_link3 = QColor(f"{color13}")
# 文件

Color_route = QColor(f"{color2}")


# qwer
Color_mark1 = QColor(f"{color3}")
Color_mark2 = QColor(f"{color4}")
Color_mark3 = QColor(f"{color5}")
Color_mark4 = QColor(f"{color6}")

Color_marks = [
    Color_mark1,
    Color_mark2,
    Color_mark3,
    Color_mark4,
]

# save
str_color2str_marks = {
    f"{color3}":"Color_mark1",
    f"{color4}":"Color_mark2",
    f"{color5}":"Color_mark3",
    f"{color6}":"Color_mark4",
}
# read
str_marks2str_color = \
{v: k for k, v in str_color2str_marks.items()}

str_marks2marks = {
    "Color_mark1":Color_mark1,
    "Color_mark2":Color_mark2,
    "Color_mark3":Color_mark3,
    "Color_mark4":Color_mark4,
}


list1_item_default = {
    "text":"",
    "color":"None"
}


item_default = {
    "text":"",
    "link":"None",
    "color":"None"
}