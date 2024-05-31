# 总行数：2673

from z3.header import *

class QListWidget0(QListWidget):



    def __init__(self, mainWindow, path):
        super().__init__()
        
        self.set_name(mainWindow, path)


        self.set_attr()


    def set_name(self, mainWindow, path):

        self.path = path
        self.mainWindow = mainWindow

        self.setFont(font)
        
        # self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        # self.customContextMenuRequested.connect(self.openFile)
        
        #1 delegate = QStyledItemDelegate1(self)
        # self.setItemDelegate(delegate)
        # self.delegate = delegate
        

        self.copy_shortcut = QShortcut(PyQt6.QtGui.QKeySequence.StandardKey.Copy, self)
        self.copy_shortcut.activated.connect(self.copy_selected_item)

        self.paste_shortcut = QShortcut(PyQt6.QtGui.QKeySequence.StandardKey.Paste, self)
        self.paste_shortcut.activated.connect(self.paste_text)

    # def contextMenuEvent(self, event):
    #     # 禁用默认的上下文菜单事件
    #     event.ignore()

    def set_attr(self):
#
        #2 self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.itemEditing = False 

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.setFlow(self.Flow.LeftToRight)
        self.setWrapping(True)
        
        
        self.setWordWrap(True)
        

        self.setSpacing(1)
        
        self.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

    def mousePressEvent(self, event):

        super().mousePressEvent(event)
        if event.button() == Qt.MouseButton.RightButton:
            self.openFile()
            

    def keyPressEvent(self, event):


        
        key = event.key()





        if event.key() == Qt.Key.Key_Q and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            self.stain_item("Color_mark1")
            return
        if event.key() == Qt.Key.Key_W and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            self.stain_item("Color_mark2")
            return
        if event.key() == Qt.Key.Key_E and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            self.stain_item("Color_mark3")
            return
        if event.key() == Qt.Key.Key_R and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            self.stain_item("Color_mark4")
            return
        

        if event.key() == Qt.Key.Key_Space:
            self.openFile()
        
        if event.key() == Qt.Key.Key_X and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            self.cut_selected_item()
            return
            
        # if event.key() == Qt.Key.Key_Alt:
        #     if self.itemEditing == True:
        #         event.ignore()
        #         return
        #     if self.selectedItems():
        #         self.editItem(self.selectedItems()[0])
        #     return
        #1 if Qt.Key.Key_0 <= key <= Qt.Key.Key_9 or Qt.Key.Key_A <= key <= Qt.Key.Key_Z or key == (Qt.Key.Key_Return or Qt.Key.Key_F2):

        #     if self.selectedItems():
        #         self.editItem(self.selectedItems()[0])
        #         event.ignore()
        #     return

        if event.key() == Qt.Key.Key_Delete and event.modifiers() == Qt.KeyboardModifier.ShiftModifier:
            
            self.clearItem()
            return

        if \
            Qt.Key.Key_Delete == key\
            or\
            Qt.Key.Key_Backspace == key\
            :
            
            self.deleteItem()
            return



        super().keyPressEvent(event)




    def stain_item(self,str_marks):
        raise NotImplementedError("Subclasses must implement clearItem method.")

                 

    def openFile(self):
        raise NotImplementedError("Subclasses must implement clearItem method.")


    def cut_selected_item(self):
        raise NotImplementedError("Subclasses must implement clearItem method.")

    def copy_selected_item(self):
        raise NotImplementedError("Subclasses must implement clearItem method.")

    def paste_text(self):
        raise NotImplementedError("Subclasses must implement clearItem method.")


    def clearItem(self):
        raise NotImplementedError("Subclasses must implement clearItem method.")
    
    def deleteItem(self):
        raise NotImplementedError("Subclasses must implement clearItem method.")
    



    def wheelEvent(self, event):
        event.ignore()


# 大纲


    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            super().mouseMoveEvent(event)





    def dragLeaveEvent(self, event):
        print(1)
        event.ignore()  # 取消事件
        # 好像没用，不知道为什么能在vscode上释放
        return