from z2.mkdir import *
from z3.var import *
from z3.header import *
from z2.mainWindow import *
from PyQt6.QtCore import QLocale


def main():
    if __name__ == "__main__":

        args = sys.argv[1:]  # 第一个参数是脚本名称，因此从第二个参数开始获取
    

        global root_path
        global main_folder

        if args:
            main_folder = args[0]  # 将第一个参数赋值给全局变量root_path
        
            root_path = main_folder + "\\.inkBox\\"

        if os.path.exists(root_path):
            pass
        else:
            makedir_from(root_path)


        app = QApplication(sys.argv)


        
        window = MainWindow(root_path)
        sys.exit(app.exec())

main()