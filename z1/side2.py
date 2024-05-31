from z3.header import *
from z1.side0 import *


def reload_item_from_index(self, index):
    path = item_path(self.path, index)
    text = read_text(path)
    # text = encode_text(text)

    # link = read_link(path)


    item = self.item(index)

    item.setText(text)

    # item.setData(256,link)


    str = read_color(path)
    if (str != "None"):
        color = str_marks2marks[str]
        item.setBackground(color)
    else:
        refresh_color(item)
    

def item_info(self, item):
    index = self.row(item)

    text = item.text()
    color = item.background().color().name()
    path = item_path(self.path, self.row(item))

    return index, text, color, path

def is_cur_level_path(path):
    if(level_in_path(path) == 1):
        return True
    return False


def detect4list3(selfpath):

    # text = read_text(selfpath)
    # if (text != ""):
    #     return
#   判定是否已生成过，时间文本

    return_text = ""
    # for index in range(0,20):
    #     path = item_path(selfpath,index)

    #     text = read_text(path)
    #     if (text != "" and text[:5] != "start"):
    #         current_time = datetime.now()
    #         time_string = current_time.strftime("%Y-%m-%d")
    #         time_string = current_time.strftime("%d-%m-%Y")
    #         # time_string = current_time.strftime("%Y-%m-%d-%Hh")
            
    #         return_text = "\n\n" + time_string
    #         break
    for index in range(0,20):
        path = item_path(selfpath, index)

        text = read_text(path)
        if (text != "" and text[:5] != "start"):
            return_text = text + "..."
            break
# 优先第四格
    path = item_path(selfpath, 4)

    text = read_text(path)
    if (text != ""):
        return_text = text + "..."
# 
    
    write_text(selfpath, return_text)
# diff：

def item_path(selfpath,index):
    path = \
        selfpath + f"\\page_item{index:02}"
    
    # print("item_path")
    # print(path)
    # print(level_in_path(path))
    
    return path


def refresh_color(item):
    item_text = item.text()
    if(item_text.isspace() or item_text == ""):
        item.setBackground(Color_blank2)
    else:
        item.setBackground(Color_route)










def level_in_path(path):
    # 使用os.path.split()将路径拆分为目录和基本名称
    folders = []
    while True:
        path, folder = os.path.split(path)
        if folder != "" and folder != ".":
            folders.append(folder)
        else:
            if path != "":
                folders.append(path)
            break
    # 返回文件夹数量（减去根目录）
    a = len(folders) 
    return 4 - a

