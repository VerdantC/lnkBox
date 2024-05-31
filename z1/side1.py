from z3.header import *
from z1.side0 import *

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

def is_cur_level_path(path):
    if(level_in_path(path) == 0):
        return True
    return False

def reload_item_from_index(self, index):
    path = item_path(self.path, index)
    text = read_text(path)
    # text = encode_text(text)

    link = read_link(path)


    item = self.item(index)

    item.setText(text)

    item.setData(256,link)


    str = read_color(path)
    if (str != "None"):
        color = str_marks2marks[str]
        item.setBackground(color)
    else:
        refresh_color(self, item)

def item_info(self, item):
    index = self.row(item)

    text = item.text()
    color = item.background().color().name()
    path = item_path(self.path, self.row(item))

    return index, text, color, path

def item_path(selfpath,index):
    path = \
        selfpath + f"\\item{index:02}"
    
    # print("item_path")
    # print(path)
    # print(level_in_path(path))
    
    return path

############################################################
def set_background_by_data(self, item):

    data = item.data(256)
    tail = data[-4:]

    if tail == ".url":
        item.setBackground(Color_link)
    elif tail == ".lnk":
        # 更新的，  文件路径
        filePath = os.path.join(self.path,f"item{self.row(item):02}", data)
        # data = os.path.abspath(data)
        if is_folder(filePath):
            item.setBackground(Color_link2)
        else:
            item.setBackground(Color_link3)


# 4
def is_folder(lnk_file_path):
    # 测试示例
    shell = Dispatch("WScript.Shell")
    
    # lnk_file_path = convert_to_raw(lnk_file_path)
    shortcut = shell.CreateShortCut(lnk_file_path)
    path = shortcut.Targetpath

    return check_path(path)

    

def check_path(path):
    if os.path.isdir(path):
        return True
    return False

def convert_to_raw(path):
    raw_path = r"{}".format(path)
    return raw_path

# 4
# Example usage:
# lnk_file_path = "path/to/your.lnk"
# if is_folder(lnk_file_path):
#     print("LNK file points to a folder.")
# else:
#     print("LNK file points to a file.")
# # 

def pure_and_small_text(text):
    if '\n' not in text and len(text) < 30:
        text = "\n\n" + text
    return text
# Autism spectrum disorder (ASD
# 黑马程序员Java项目实战《苍穹外卖》，最适合新手的Sp


def detect4list2(selfpath): 
    return_text = ""
    for index in range(0,20):
        path = item_path(selfpath, index)

        text = read_text(path)
        if (text != ""):
            return_text = text + "\n..."
            break
    
    write_text(selfpath, return_text)

###################################

def item_path(selfpath, index):
    path = \
        selfpath + f"\\item{index:02}"
    
    return path

def pure_item_path(index):
    path = \
        f"item{index:02}"
    
    return path


def refresh_color(self, item):
    if (is_linked(item)):


        set_background_by_data(self, item)
    # blank
    else:
        item_text = item.text()
        if(item_text.isspace() or item_text == ""):
            item.setBackground(Color_blank)
        else:
            item.setBackground(Color_route)


############################################################1



def isFilePath(address):
    url = QUrl(address)
    if url.isValid() and url.isLocalFile():
        return True
    else:
        return False

def create_shortcut(target_file_path, generate_file_path):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(generate_file_path)
    shortcut.TargetPath = target_file_path
    shortcut.save()

def create_url_file(url, file_path):
    with open(file_path, 'w') as file:
        file.write('[InternetShortcut]\n')
        file.write('URL=' + url)


def clean_filename(filename):
    # 定义正则表达式来匹配不合法的文件名字符
    illegal_chars = r'[\\/:*?"<>|]'
    # 使用sub函数替换不合法字符为空字符串
    cleaned_filename = re.sub(illegal_chars, '', filename)
    # 删去后一半，避免过长
    cleaned_filename = cleaned_filename[:20]

    return cleaned_filename


def extract_filename(path):
    # 使用反斜杠分割路径
    parts = path.split('\\')
    # 返回最后一个部分（文件名）
    return parts[-1]


def event_position_item_path(self, event):
    drop_pos = event.position().toPoint()
    chip2 = self.itemAt(drop_pos)
    index = self.row(chip2)
    path = pure_item_path(index) 
    return path
