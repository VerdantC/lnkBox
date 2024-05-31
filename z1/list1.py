from z3.header import *
from z1.side1 import *
from z1.zzz import *
from z1.list0 import *


class QListWidget1(QListWidget0):



    def __init__(self, mainWindow, path):
        super().__init__(mainWindow, path)
        
        

        delegate = QStyledItemDelegate1(self)
        self.setItemDelegate(delegate)
        self.delegate = delegate



# windowIconTextChanged
# currentTextChanged


        self.addItem_()

    def keyPressEvent(self, event):

        super().keyPressEvent(event)

        key = event.key()

    def keyPressEvent(self, event):

        super().keyPressEvent(event)

        key = event.key()
        print(key)

        if event.modifiers() is not Qt.KeyboardModifier.NoModifier:
            return
    #否则会染色时，出问题 

        # if Qt.Key.Key_0 <= key <= Qt.Key.Key_9 or Qt.Key.Key_A <= key <= Qt.Key.Key_Z or key == (Qt.Key.Key_Return or Qt.Key.Key_F2):
        #     if self.selectedItems():
        #         self.editItem(self.selectedItems()[0])
        #         event.ignore()
        #     return
    # 关闭输入

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key.Key_Alt:
            if self.itemEditing == True:
                event.ignore()
                return
            if self.selectedItems():
                self.editItem(self.selectedItems()[0])
            return


    def addItem_(self):


        for i in range(0,20):
            list_item = QListWidgetItem1()
            self.addItem(list_item)
        
            list_item.setBackground(Color_blank)
            
            list_item.setSizeHint(size)

            list_item.setData(256,"None")
    
        
        


        for index in range(0,20):
            path = item_path(self.path, index)

        

            text = read_text(path)
            text = encode_text(text)

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


############################################################1
    def openFile(self):
        selected_items = self.selectedItems()
        if not selected_items:
            return
        
        item = selected_items[0]
        if (item.data(256) == "None"):
            return
        filePath1 = item.data(256)

        # item18\\ + EsdfhisNEMT.png.lnk
        filePath2 = os.path.join(f"item{self.row(item):02}", filePath1)
        
        print("self.path")
        print(self.path)
        filePath = os.path.join(self.path, filePath2)
        try:
            # Use QDesktopServices to open the file
            url = PyQt6.QtCore.QUrl.fromLocalFile(filePath)
            print("url")
            print(url)



            PyQt6.QtGui.QDesktopServices.openUrl(url)
        except Exception as e:
            print(f"Error opening file: {e}")
############################################################

    def cut_selected_item(self):
        selected_items = self.selectedItems()
        if not selected_items:
            return
        
        if (selected_items[0].data(256) == ""):

            selected_text = selected_items[0].text()
            selected_text = decode_text(selected_text)
            selected_items[0].setText("")
            
            clipboard = QApplication.clipboard()
            clipboard.setText(selected_text)
        
        else:
            item = selected_items[0]
            item.setText("")
            item.setBackground(Color_blank)

            self.copy_selected_item_withlink()


    def copy_selected_item_withlink(self):

        selected_items = self.selectedItems()
        if selected_items:
            item = selected_items[0]

            _, _, _, path = item_info(self, item)


            clipboard = QApplication.clipboard()

            clipboard.setText(path)


    def copy_selected_item(self):
        selected_items = self.selectedItems()
        if selected_items:

            if (selected_items[0].data(256) == "None"):
                pass
            else:
                print(selected_items[0].data(256))
                self.copy_selected_item_withlink()
                return
            

            selected_text = selected_items[0].text()
            selected_text = decode_text(selected_text)

            clipboard = QApplication.clipboard()
            global copy_mark
            copy_mark = selected_text

            selected_text = selected_text.lstrip('\n')
            selected_text = selected_text.rstrip('\n')
            clipboard.setText(selected_text)
  
#   不支持跨页面剪切，（会清空
    def paste_text_withlink(self):
        clipboard = QApplication.clipboard()
        path = clipboard.text()

        selected_items = self.selectedItems()
        if selected_items:
            item = selected_items[0]
            index, _, _, cur_item_path = item_info(self, item)

            if is_cur_level_path(path):

                replace_folder_content(cur_item_path,path)

                reload_item_from_index(self, index)
   
    def paste_text(self):
        clipboard = QApplication.clipboard()
        text_to_paste = clipboard.text()

        if (text_to_paste[:3] == r".\\"):
            self.paste_text_withlink()
            return
        else:
            print(text_to_paste[:3])
            print("asdasd")
            


        selected_items = self.selectedItems()
        if selected_items:
            global copy_mark
            copy_mark1 = copy_mark.lstrip('\n')
            copy_mark1 = copy_mark1.rstrip('\n')
            if copy_mark1 == text_to_paste:
                text_to_paste = copy_mark
            else:
                # 小型文本
                text_to_paste = pure_and_small_text(text_to_paste)


            text_to_paste = encode_text(text_to_paste)
            selected_items[0].setText(text_to_paste)
            print(ascii(text_to_paste))

############################################################


    def clearItem(self):
        item_count = self.count()
        for i in range(item_count):
            item = self.item(i)
            item.setText("")
            # item.setData(256, None)

            item.setBackground(Color_blank)

    def deleteItem(self):
        selected_items = self.selectedItems()
        if not selected_items:
            return
        
        item = self.selectedItems()[0]
        item.setText("")
        # item.setData(256,None)
        # item.setBackground(Color0)
        # 
        refresh_color(self, item)
# 

############################################################
    def saveItem(self):
        for index in range(0,20):

            path = item_path(self.path, index)
            item = self.item(index)
            
            item_text = item.text()
            item_text = decode_text(item_text)
            
            item_link = item.data(256)  
        
        
            item_color = item.background().color().name()

            if(item_text.isspace() or item_text == ""):
                item_link = "None"
                item_color = f"{color0}"

# 置空，防止某些
                item_text = ""

            write_text(path, item_text)
            write_link(path, item_link)

            write_color(path, item_color)



        detect4list2(self.path)
########################################################################################################################2

    def dragMoveEvent(self, event):

        # print(111)
        # mouse_pos = event.position()
        
        # # 获取窗口的边界
        # window_rect = self.geometry()
        
        # # 检查鼠标是否移出窗口
        # if not window_rect.contains(mouse_pos):
        #     event.ignore()  # 取消事件
        #     return
# 

        if event.mimeData().hasUrls():
            event.accept()
            return
        
        super().dragMoveEvent(event)

    def dragEnterEvent(self, event):

        if event.mimeData().hasUrls():
            event.accept()
            return
        
        super().dragEnterEvent(event)


    
    # def event(self, event):
    #     event_type_str = type(event).__name__
    #     print(f"Event type: {event_type_str}")
    #     return super().event(event)
    
    def dropEvent(self,event):

        # drop_pos = event.position().toPoint()
        # # 防止落点在外，或在不明位置
        # if(self.itemAt(drop_pos)):
        #     pass
        # else:
        #     return


        print(event.mimeData().urls())
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]

            # print("url")
            # # print(url.toLocalFile())
            # url = url.url()
            # print(url)
            # print("kkk")

            if isFilePath(url):
                file_path = url.toLocalFile()
                file_path = file_path.replace('/', '\\')
                file_path1 = clean_filename(file_path)
############################################################4
                generate_file_path = self.path\
                + file_path1 + ".lnk"

                item_path = event_position_item_path(self, event)
                # 改为相对于item位置的路径
                data_path = file_path1 + ".lnk"
                generate_file_path = os.path.join(item_path, data_path)

                generate_file_path = generate_file_path.replace('/', '\\')

                # 全路径，相对路径
                # print(generate_file_path)

                create_shortcut(file_path, os.path.join(self.path,generate_file_path))    

                name = file_path            
                name = extract_filename(name)
                        # 小型文本
                name = pure_and_small_text(name)
            else:
                url = url.url()

                url1 = clean_filename(url)
                # url = quote(url, safe="/:")

                generate_file_path = self.path\
                + url1 + ".url"
                
                item_path = event_position_item_path(self, event)
                # 改为相对于item位置的路径
                data_path = url1 + ".url"
                generate_file_path = os.path.join(item_path, data_path)
                
                create_url_file(url, os.path.join(self.path,generate_file_path))
                # asd
                name = url



            ######################################################################################
            drop_pos = event.position().toPoint()
            chip2 = self.itemAt(drop_pos)
            # chip2.setData(256, generate_file_path)
            chip2.setData(256, data_path)

            set_background_by_data(self, chip2)

            if chip2.text() == "":
                name = encode_text(name)
                chip2.setText(name)
            self.setCurrentItem(chip2)
            self.mainWindow.activateWindow()


        else:



            
            chip = self.selectedItems()[0]
            
            drop_pos = event.position().toPoint()
            # 防止落点在外，或在不明位置
            if(self.itemAt(drop_pos)):
                pass
            else:
                return
            
            chip2 = self.itemAt(drop_pos)
            row1 = self.row(chip)
            row2 = self.row(chip2)

            flag = False
            if(row1 < row2):
                flag = True
                row1, row2 = row2, row1
                chip, chip2 = chip2, chip
            self.takeItem(row1)
            self.takeItem(row2)
            self.insertItem(row2, chip)
            self.insertItem(row1, chip2)

            if flag:
                self.setCurrentItem(chip2)
            else:
                self.setCurrentItem(chip)

            #交换实际的，       对应文件夹，        防止链接文件出错

            path1 = os.path.join(self.path,f"item{row1:02}") 
            path2 = os.path.join(self.path,f"item{row2:02}") 
            print("path12")
            print(path1)
            print(path2)
            swap_folders(path1, path2)



        

    def stain_item(self,str_marks):
        color = str_marks2marks[str_marks]         
        
        if self.selectedItems():
            item = self.selectedItems()[0]
            
            item_color = item.background().color().name()

            if(item_color not in str_color2str_marks):
                item.setBackground(color)
            else:
                refresh_color(self, item)



        