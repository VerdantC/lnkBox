
import shutil
import os

def swap_folders(folder1, folder2):
    # 创建临时文件夹
    temp_folder = "temp_swap_folder"
    if os.path.exists(temp_folder):
        shutil.rmtree(temp_folder)
    # 创建新的临时文件夹
    os.makedirs(temp_folder)
    # os.makedirs(temp_folder, exist_ok=True)
    
    # 将folder1移动到临时文件夹
    move_dir_files(folder1, temp_folder)
    
    # 将folder2移动到folder1的位置
    move_dir_files(folder2, folder1)
    
    # 将临时文件夹移动到folder2的位置
    move_dir_files(temp_folder, folder2)
    
    # 删除临时文件夹
    shutil.rmtree(temp_folder)

def move_dir_files(source_dir, destination_dir):
    # 创建目标目录（如果不存在）
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # 遍历源目录中的所有内容
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        destination_item = os.path.join(destination_dir, item)

        # 移动文件或目录到目标目录
        if os.path.isdir(source_item):
            shutil.move(source_item, destination_item)
        else:
            shutil.move(source_item, destination_dir)


def is_chinese(char):
    """判断字符是否为中文"""
    return '\u4e00' <= char <= '\u9fff'

def write_file_content(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False
    

def file_content(file_path):



    with open(file_path, 'r') as file:
        content = file.read()

    

    return content




# original_file_path ="asd.txt"
# new_file_path = "asdd.txt"
# def replace_text_in_files(original_file_path, new_file_path):
def replace_file_text2another(original_file_path, new_file_path):
    """
    将原始文件中的内容替换为新文件中的内容。

    Parameters:
        original_file_path (str): 原始文件路径。
        new_file_path (str): 新文件路径。

    Returns:
        None
    """
    # 打开原始文件并读取内容
    with open(original_file_path, 'r') as original_file:
        original_content = original_file.read()

    # 打开新文件并读取内容
    with open(new_file_path, 'r') as new_file:
        new_content = new_file.read()

    # 将原始文件内容替换为新文件内容
    replaced_content = original_content.replace(original_content, new_content)

    # 将替换后的内容写入原始文件
    with open(original_file_path, 'w') as original_file:
        original_file.write(replaced_content)

    print(f"文件内容已从 {new_file_path} 复制到 {original_file_path}。")




def replace_folder_content(destination_folder, source_folder):
    # 删除目标文件夹内的所有内容
    shutil.rmtree(destination_folder)
    # 复制源文件夹到目标文件夹
    shutil.copytree(source_folder, destination_folder)













