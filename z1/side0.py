from z3.header import *
from z3.util import *
from z3.var import *


############################################################
def read_color(path):
    append = "//color.txt"
    path = path + append

    return file_content(path)
def read_text(path):
    append = "//text.txt"
    path = path + append

    return file_content(path)
def read_link(path):
    append = "//link.txt"
    path = path + append

    return file_content(path)
############################################################1
def write_text(path, content):
    append = "//text.txt"
    path = path + append

    return write_file_content(path, content)
def write_link(path, content):
    append = "//link.txt"
    path = path + append

    return write_file_content(path, content)

def write_color(path, content):
# 由颜色#asd转译
    append = "//color.txt"
    path = path + append


    if(content in str_color2str_marks):
        content = str_color2str_marks[content]
    else:
        content = "None"

    write_file_content(path, content)
    return 
############################################################2

def is_linked(item):
    if item.data(256) != "None":
        return True
    return False

############################################################

def reset_list3_item(path):

    reset_color(path)
    reset_text(path)
    for index in range(20):
        path1 = path + f"\\page_item{index:02}"
        
        reset_list2_item(path1)

def reset_list2_item(path):

    reset_color(path)
    reset_text(path)
    for index in range(20):
        path1 = path + f"\\page_item{index:02}"
        
        reset_list1_item(path1)

def reset_list1_item(path):
    
    reset_color(path)
    reset_text(path)
    for index in range(20):
        path1 = path + f"\\item{index:02}"

        reset_item(path1)
############################################################
def reset_item(path):
        reset_text(path)
        reset_color(path)
        reset_link(path)

def reset_link(path):
    write_link(path, "None")

def reset_text(path):
    write_text(path, "")

def reset_color(path):
    write_color(path, "None")

########################################################################################################################3

def encode_text(text):
        new_text = ""        
        num1 = 0
        for char in text:
            if char == "\n":
                num1 = 0
            else:
                if is_chinese(char):
                    num1 += 2
                else:
                    num1 += 1
# 16前加空格
                if num1 >= 16:
                    if num1 == 16:
                        num1 = 0
                        new_text += char
                        new_text += " "
                        continue
                    if num1 == 17:
                        num1 = 0
                        new_text += " "
                        new_text += char
                        continue
            new_text += char

        return new_text

def decode_text(text):
        new_text = ""        
        num1 = 0
        for char in text:
            if char == "\n":
                num1 = 0
            else:
                if is_chinese(char):
                    num1 += 2
                else:
                    num1 += 1

                if num1 >= 17:
                    if num1 == 17:
                        num1 = 0
                        continue
                    if num1 == 18:
                        num1 = 0
                        new_text = new_text[:-1]
                        new_text += char
                        continue
            new_text += char

        return new_text














