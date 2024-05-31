from z3.header import *
from z2.side import *



def path2action(self, path):

    level = level_in_path(path)  

    action_disconnect(self)

    if (level == 1):
        createActions1(self)
    elif (level == 2):
        createActions2(self)
    elif (level == 3):
        createActions3(self)


def createToolBar(self):
    
    
    self.tool_bar = QToolBar1("Photo Editor Toolbar")
    


    self.over_view1 = QAction(self.icon_empty ,"")
    

    self.spacer1 = QAction(self.icon_empty ,"")


    self.over_view2 = QAction(self.icon_empty ,"")


    self.clear_act = QAction(self.icon_trash, "")
    self.clear_act.triggered.connect(self.clearItem)

    spacer = QWidget()
    spacer.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

    self.tool_bar.addAction(self.over_view1)
    # self.tool_bar.addAction(self.spacer1)
    self.tool_bar.addAction(self.over_view2)

    self.tool_bar.addWidget(spacer)

    self.tool_bar.addAction(self.clear_act)
    
    self.grid.addWidget(self.tool_bar, 0, 0)  


def createActions1(self):
    

    
    self.over_view1.setIcon(self.icon_grid)
    self.over_view1.triggered.connect(self.return_page)


    self.over_view2.setIcon(self.icon_empty)
    # self.over_view1.triggered.connect(self.hello)
    


def createActions2(self):
    
    
    self.over_view1.setIcon(self.icon_grid)
    self.over_view1.triggered.connect(self.enter_3_page)


    self.over_view2.setIcon(self.icon_undo)
    self.over_view2.triggered.connect(self.return_page)


def createActions3(self):
    
    
    self.over_view1.setIcon(self.icon_undo)
    self.over_view1.triggered.connect(self.return_page)


    self.over_view2.setIcon(self.icon_empty)
    # self.over_view1.triggered.connect(self.hello)
    



def action_disconnect(self):
    try: 
        self.over_view1.triggered.disconnect() 
    except Exception: 
        pass
    try: 
        self.over_view2.triggered.disconnect() 
    except Exception: 
        pass

