from z3.header import *
from z1.side2 import *
from z1.zzz import *
from z1.list0 import *


class QListWidget2(QListWidget0):



    def __init__(self, mainWindow, path):


        print(2)
        super().__init__(mainWindow, path)
        

        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)



        self.addItem_()


    def keyPressEvent(self, event):

        super().keyPressEvent(event)



    def addItem_(self):


        for i in range(0,20):
            list_item = QListWidgetItem1()
            self.addItem(list_item)
        
            list_item.setBackground(Color_blank)
            
            list_item.setSizeHint(size)

            list_item.setData(256,"None")
    
        
        self.textDetect()

    def textDetect(self):



        for index in range(0,20):
            path = item_path(self.path, index)

        

            text = read_text(path)
            # text = encode_text(text)

            # link = read_link(path)



            item = self.item(index)

            item.setText(text)

            # item.setData(256,link)




            str = read_color(path)
            if (str != "None"):
                color = str_marks2marks[str]
                item.setBackground(color)
            else:
                refresh_color(item)



############################################################1
    def openFile(self):

        selected_items = self.selectedItems()
        if selected_items:
            
            index = self.row(selected_items[0])

            path = self.path + f"\\page_item{index:02}"
            
            self.mainWindow.switch_page(path)
############################################################

    def cut_selected_item(self):
        selected_items = self.selectedItems()
        if selected_items:
            item = selected_items[0]
            item.setText("")
            item.setBackground(Color_blank)

        self.copy_selected_item()

    def copy_selected_item(self):

        selected_items = self.selectedItems()
        if selected_items:
            item = selected_items[0]

            _, _, _, path = item_info(self, item)


            clipboard = QApplication.clipboard()

            clipboard.setText(path)

    def paste_text(self):
        clipboard = QApplication.clipboard()
        path = clipboard.text()

        selected_items = self.selectedItems()
        if selected_items:
            item = selected_items[0]
            index, _, _, cur_item_path = item_info(self, item)

            if is_cur_level_path(path):

                replace_folder_content(cur_item_path,path)

                reload_item_from_index(self, index)


############################################################


    def clearItem(self):
        item_count = self.count()
        for i in range(item_count):
            item = self.item(i)
            item.setText("")
            # item.setData(256, None)

            item.setBackground(Color_blank)

# 实际清空

        reset_list2_item(self.path)

    def deleteItem(self):
        # return
        selected_items = self.selectedItems()
        if not selected_items:
            return
        
        item = self.selectedItems()[0]
        item.setText("")
        # item.setData(256,None)
        # item.setBackground(Color0)
        # 
        refresh_color(item)

# 清空文件
        index = self.row(item)
        path = item_path(self.path, index)
        reset_list1_item(path)
# 


############################################################
    def saveItem(self):
        for index in range(0,20):

            path = item_path(self.path, index)
            item = self.item(index)
            
            item_text = item.text()
            # item_text = decode_text(item_text)
            
            # item_link = item.data(256)  
        
        

            if(item_text.isspace() or item_text == ""):
                pass
                # reset_list1_item(path)
                # 删除空格，但会出问题。。。。。。。。。。。。

            # write_text(path, item_text)
            # write_link(path, item_link)

            # write_color(path, item_color)
            item_color = item.background().color().name()
            if(item_text.isspace() or item_text == ""):
                # item_link = "None"
                item_color = f"{color0}"

            # write_text(path, item_text)
            # write_link(path, item_link)

            write_color(path, item_color)


        detect4list3(self.path)

        


    def stain_item(self,str_marks):
        color = str_marks2marks[str_marks]         
        
        if self.selectedItems():
            item = self.selectedItems()[0]
            
            item_color = item.background().color().name()

            if(item_color not in str_color2str_marks):
                item.setBackground(color)
            else:
                refresh_color(item)


    
    def dropEvent(self,event):

        chip = self.selectedItems()[0]
        
        drop_pos = event.position().toPoint()
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

      
      

        dir1 = item_path(self.path, row1)
        dir2 = item_path(self.path, row2)


        swap_folders(dir1, dir2)

