from z3.header import *
from z1.list1 import *
from z1.list2 import *
from z1.list3 import *


def setCurrentRow_(self):
    
    index = self.pre_page_path[-2:]
    index = int(index)

    self.page.setCurrentRow(index)


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

def switch_pre_page(self):
    page_num = page_num1(self)
    target_num = page_num + 1
    if(target_num > 19):
        return
    
    prefix = self.cur_page_path[:-2]
    path = prefix + f"{target_num:02}"
    self.switch_page(path)
    


def switch_nxt_page(self):
    page_num = page_num1(self)
    target_num = page_num - 1
    if(target_num < 0):
        return

    prefix = self.cur_page_path[:-2]
    path = prefix + f"{target_num:02}"
    self.switch_page(path)


def page_num1(self):
    num = self.cur_page_path[-2:]
    num = int(num)

    return num


############################################################
def path2page(self, path):

    level = level_in_path(path)  

    if (level == 1):
        page = QListWidget1(self, path)
    elif (level == 2):
        page = QListWidget2(self, path)
    elif (level == 3):
        page = QListWidget3(self, path)

    return page

############################################################
def update_page_state(self, path):
    flag = False

    level_path = level_in_path(path)  
    level_cur_path = level_in_path(self.cur_page_path)  
    if (level_path != level_cur_path):
        self.pre_page_path = self.cur_page_path
# 保证pre和cur,path在不同层级
        if (level_path > level_cur_path):

            flag = True
# 高层，切换时，重置低层path
    elif (level_path == level_cur_path):    
        level_pre_path = level_in_path(self.pre_page_path)
        if (level_cur_path > level_pre_path):
            print(self.pre_page_path)
            # if (level_cur_path == 3):
            new_pre_path = path + "//page_item04"

        # 此处设置为 04页面
            # elif (level_cur_path == 2):
            #     new_pre_path = path + "//item19"
            self.pre_page_path = new_pre_path

    self.cur_page_path = path

    return flag

def save_page_state2file(self):
# 替换pre
    final_page_path_ = final_page_path_1()
    pre_page_path_ = pre_page_path_1()



# 更新final
    write_file_content(final_page_path_, self.cur_page_path)
    write_file_content(pre_page_path_, self.pre_page_path)



def remove_current_page(self):
        self.page.saveItem()

        self.page.close()
        self.page.deleteLater()
        self.grid.removeWidget(self.page)


############################################################
def final_page_path():
    file_path = final_page_path_1()

    return file_content(file_path)


def pre_page_path():
    file_path = pre_page_path_1()

    return file_content(file_path)

def final_page_path_1():
    final_page_path_ = f"{rot_path}\\final_page_path_.txt"


    return final_page_path_

def pre_page_path_1():
    pre_page_path_ = f"{rot_path}\\pre_page_path_.txt"
    return pre_page_path_





















