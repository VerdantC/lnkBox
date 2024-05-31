from z3.var import *
import os

############################################################1
init_page_path = r"page_item00\page_item19\page_item19"
init_pre_page_path = r"page_item00\page_item19"

def makedir_from(root_path):

    os.makedirs(root_path)
    absolute_path = os.path.abspath(root_path)
    print(absolute_path)
    
    with open(os.path.join(root_path, "final_page_path_.txt"), "w") as file:
        file.write(init_page_path)
    with open(os.path.join(root_path, "pre_page_path_.txt"), "w") as file:
        file.write(init_pre_page_path)

    subfolder = "page_item00"
    path = os.path.join(root_path, subfolder)
    os.makedirs(path)

    makedir_list3(path)


    init_text(root_path)



def makedir_list3(page_path):
    with open(os.path.join(page_path, "text.txt"), "w") as file:
        file.write("")
    with open(os.path.join(page_path, "color.txt"), "w") as file:
        file.write("None")

    subfolders = [f"page_item{i:02}" for i in range(20)]
    for subfolder in subfolders:
        path = os.path.join(page_path, subfolder)
        os.makedirs(path)

        makedir_list2(path)

def makedir_list2(page_path):
    with open(os.path.join(page_path, "text.txt"), "w") as file:
        file.write("")
    with open(os.path.join(page_path, "color.txt"), "w") as file:
        file.write("None")

    subfolders = [f"page_item{i:02}" for i in range(20)]
    for subfolder in subfolders:
        path = os.path.join(page_path, subfolder)
        os.makedirs(path)

        makedir_list1(path)

def makedir_list1(page_path):
    with open(os.path.join(page_path, "text.txt"), "w") as file:
        file.write("")
    with open(os.path.join(page_path, "color.txt"), "w") as file:
        file.write("None")
# 不同处
    subfolders = [f"item{i:02}" for i in range(20)]
    for subfolder in subfolders:
        path = os.path.join(page_path, subfolder)
        os.makedirs(path)

        makedir_item(path)


def makedir_item(page_path):
    with open(os.path.join(page_path, "text.txt"), "w") as file:
        file.write("")
    with open(os.path.join(page_path, "color.txt"), "w") as file:
        file.write("None")
    with open(os.path.join(page_path, "link.txt"), "w") as file:
        file.write("None")


############################################################
def init_text(root_path):
    # path = os.path.join(root_path, init_page_path, "item19")
    
    # with open(os.path.join(path, "text.txt"), "w") as file:
    #         file.write("start")

    for index in range(20):
        path = os.path.join(root_path, f"page_item00\page_item{index:02}\page_item19")
        path1 = os.path.join(root_path, f"page_item00\page_item{index:02}\page_item19", "item19")

        
        with open(os.path.join(path, "text.txt"), "w") as file:
            file.write("start\n...")
        with open(os.path.join(path1, "text.txt"), "w") as file:
            file.write("start")

############################################################1