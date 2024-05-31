from z3.header import *

from PyQt6.QtGui import QInputMethod

class QListWidgetItem1(QListWidgetItem):
    
    def __init__(self):
        super().__init__()

        self.setTextAlignment(Qt.AlignmentFlag.AlignAbsolute)
        self.setFlags(self.flags() | Qt.ItemFlag.ItemIsEditable)


class QPlainTextEdit1(QPlainTextEdit):
    def __init__(self, parent, QListWidget1):
        super().__init__(parent)


        self.setStyleSheet("""
            QPlainTextEdit1{
                background-color: #e5f3ff;
            font-family: Terminal;
            font-size: 9pt;
            }
        """)


        self.QListWidget1 = QListWidget1
        self.QListWidget1.itemEditing = True

        
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        

    def __del__(self):
        self.QListWidget1.itemEditing = False


    def mousePressEvent(self, event):
        cursor_width = 1
        self.setCursorWidth(cursor_width)

        super().mousePressEvent(event)


    def keyPressEvent1(self):
        cursor_width = 1
        self.setCursorWidth(cursor_width)

    def keyPressEvent(self, event):
        
        # if event.key() == Qt.Key.Key_Alt:
        #     self.close()
        
        if event.key() == Qt.Key.Key_Tab:
            spaces = ' ' * 4 * 2  
            spaces = ' ' * 3 * 2  
            self.insertPlainText(spaces)
            return
        
        if event.key() == Qt.Key.Key_Escape:
            self.close()
            return
        
            
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter or event.key() == Qt.Key.Key_Down:
            cursor = self.textCursor()
            current_line = cursor.blockNumber() + 1  
            line_limit = 7
            if current_line == line_limit:
                return
            
        if event.key() == Qt.Key.Key_Down or event.key() == Qt.Key.Key_Up or event.key() == Qt.Key.Key_Left or event.key() == Qt.Key.Key_Right:
            cursor_width = 1
            self.setCursorWidth(cursor_width)

        super().keyPressEvent(event)

    def wheelEvent(self, event):
        event.ignore()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key.Key_Alt:
            self.close()



class QStyledItemDelegate1(QStyledItemDelegate):

    def __init__(self, QListWidget1):
        
        super().__init__(QListWidget1)
        self.QListWidget1 = QListWidget1




    def createEditor(self, parent, option, index):
        editor = QPlainTextEdit1(parent, self.QListWidget1)

        return editor


    def setEditorData(self, editor, index):
        value = index.model().data(index, QtCore.Qt.ItemDataRole.EditRole)


        if value is None:
            value = ""

        value = decode_text(value)
        cursor_flag = False
# 折算行数
        num1 = 0
        num2 = 0
        for char in value:
            if char == "\n":
                num2 += 1
                num1 = 0
            else:
                if is_chinese(char):
                    num1 += 2
                else:
                    num1 += 1

                if num1 >= 14:
                    cursor_flag = True
                    num2 += 1
                    num1 = 0
        line_limit = 7 -1
        if num2 >= line_limit:
            pass
        else:
            value += "\n" * (line_limit - num2)


        editor.setPlainText(value)

        cursor = editor.textCursor()

        third_line_block = editor.document().findBlockByLineNumber(2)

# 有过长行，不重设cursor
        
        if cursor_flag:
            pass
        else:
            cursor.setPosition(third_line_block.position() + third_line_block.length() - 1)
        
        # cursor.setPosition(third_line_block.position() + third_line_block.length() - 1)
        
        editor.setCursorWidth(0)
        editor.setTextCursor(cursor)

        editor.textChanged.connect(editor.keyPressEvent1)

    # def cursorPosition(self, text)

    def setModelData(self, editor, model, index):

        text_content = editor.toPlainText()
        text_content = encode_text(text_content)

        truncated_text = text_content.rstrip('\n')
        
        

        model.setData(index, truncated_text, QtCore.Qt.ItemDataRole.EditRole)

    def updateEditorGeometry(self, editor, option, index):

        x, y, p, q = option.rect.getRect()
        editor.setGeometry(option.rect)
        editor.setGeometry(x -2,y-5,p,q)
        editor.setGeometry(x -2,y-5,p,q + 20)
        editor.setGeometry(x -1,y-4,p,q + 20)
        
        editor.setGeometry(x -1,y-4,p + 2,q +3)
        editor.setGeometry(x -1,y-4,p + 2,q +4)




    def eventFilter(self, editor, event):
        
        # input_method = QInputMethod()
        # input_method.reset()
        
        
        if event.type() == QtCore.QEvent.Type.Close:

            # self.QListWidget1.inputMethod().reset()

            self.commitData.emit(editor)
            self.closeEditor.emit(editor, QStyledItemDelegate.EndEditHint.NoHint)

            return True
        return False
    


class QToolBar1(QToolBar):
    def __init__(self, foo):
        super().__init__()

# sad
        self.setMinimumWidth(30)

        self.setMinimumWidth(40)
        self.setMinimumWidth(35)
        self.setMinimumWidth(38)
        # self.setMinimumWidth(60)

# 圆角后
        self.setMinimumWidth(0)


        self.setIconSize(QSize(24,24))


        self.setFloatable(True)

                
        self.setStyleSheet("""
            QToolBar QToolButton:hover {
                background-color: rgba(255, 255, 255, 0);
            }
        """)
        
        self.setOrientation(Qt.Orientation.Vertical)
