from z3.header import *
from z2.side import *
from z2.side_tool import *
from PyQt6.QtGui import QPainter


class MainWindow(QWidget):
    def __init__(self, root_path):
        super().__init__()

        self.copy_mark = ""
        self.copy_path = ""

# list2 copy

        self.root_path = root_path

        self.set_name()
        self.set_attr()
        
        self.init_process()

    def set_name(self):
        self.cur_page_path = ""
        self.pre_page_path = ""


        global icon_lnk
        self.icon_lnk = QIcon(f"{icon_lnk}")



        global icon_grid 
        absolute_path = os.path.abspath(icon_grid)
        print(absolute_path)
        self.icon_grid = QIcon(f"{icon_grid}")
        global icon_trash 
        self.icon_trash = QIcon(f"{icon_trash}")
        global icon_undo 
        self.icon_undo = QIcon(f"{icon_undo}")

        global icon_empty 
        self.icon_empty = QIcon(f"{icon_empty}")



# 切换为相对路径，防止重命名文件夹后链接失效
        global root_path
        os.chdir(f"{self.root_path}")
        root_path = ".\\"



    def set_attr(self):

        
        shortcut = PyQt6.QtGui.QShortcut(QtGui.QKeySequence(Qt.Key.Key_Tab), self)
        shortcut.activated.connect(self.return_page)

        global x
        offset = 39
        self.resize(offset + 5 * x + 29 + 11, offset + 4 * y - 9)

        self.resize(offset + 5 * x + 29 +9, offset + 4 * y - 9)
# 圆角后
        self.resize(offset + 5 * x + 29, offset + 4 * y - 10)
        
        self.setWindowIcon(self.icon_grid)  # 替换'icon.png'为你的图标文件路径
        self.setWindowIcon(self.icon_lnk)  # 替换'icon.png'为你的图标文件路径
        self.setWindowTitle("lnkBox")

        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        border_style = f"""
        background-color: {back_Color};
        border-radius: 5000px;
        """ 
        self.setStyleSheet(border_style)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
   
    # def do_something(self):
        # self.over_view.trigger()

# 圆角后
    def paintEvent(self, ev):
        # return
        painter = QPainter(self)
        # painter.begin(self)
        # gradient = QLinearGradient(QRectF(self.rect()).topLeft(), QRectF(self.rect()).bottomLeft())
        # gradient.setColorAt(0.0, Qt.GlobalColor.black)
        # gradient.setColorAt(0.4, Qt.GlobalColor.gray)
        # gradient.setColorAt(0.7, Qt.GlobalColor.black)
        # painter.setBrush(gradient)
        custom_color = QColor(f"{back_Color}")
        painter.setBrush(custom_color)
        painter.drawRoundedRect(self.rect(), 20.0, 20.0)
        painter.drawRoundedRect(self.rect(), 10.0, 10.0)
        # painter.drawRoundedRect(self.rect(), 15.0, 15.0)
        # painter.end()



    def init_process(self):
        
        self.grid = QGridLayout()

        self.init_grid()


        self.setLayout(self.grid)

        self.show()

    def init_grid(self):
        
        
        self.init_page_state()


        createToolBar(self)
        self.setup_page(self.cur_page_path)

    def init_page_state(self):
        self.cur_page_path = final_page_path()
        self.pre_page_path = pre_page_path()


    def setup_page(self, path):
# page-listWidget
        self.page = path2page(self, path)

        path2action(self, path)

        self.grid.addWidget(self.page, 0, 1)

        #setcurrent的格子 


############################################################
    def switch_page(self, path):
        is_switch_higher_level = update_page_state(self, path)
#       换了层次
        remove_current_page(self)

        self.setup_page(path)

        if(is_switch_higher_level is True):
            setCurrentRow_(self)




        

    def closeEvent(self, event):
        super().closeEvent(event)
        self.page.saveItem()

        save_page_state2file(self)


############################################################
    def wheelEvent(self, event):
        if isinstance(self.page, QListWidget3):
            return

        if event.angleDelta().y() > 0:
            switch_pre_page(self)
        else:
            switch_nxt_page(self)


        

    def clearItem(self):
        self.page.clearItem()
        return
    



    def keyPressEvent(self, event):        
        key = event.key()
        
        
        
        if event.key() == Qt.Key.Key_Escape:
            if self.page.itemEditing == True:
                event.ignore()
                return
            self.close()
        else:
            super().keyPressEvent(event)

    
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        delta = PyQt6.QtCore.QPoint(event.globalPosition().toPoint() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPosition().toPoint()
############################################################
    def return_page(self):

        path = self.pre_page_path
        self.switch_page(path)
        
    def enter_3_page(self):
        path = f"{root_path}\\page_item00"
        self.switch_page(path)