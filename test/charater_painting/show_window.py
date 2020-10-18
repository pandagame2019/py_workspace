from window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog
from PyQt5 import QtGui
import sys
import _thread
import time



class Main(QMainWindow ,Ui_MainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)
        # 开启自动填充背景
        self.centralWidget().setAutoFillBackground(True)
        palette=QtGui.QPalette() #调色板类
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(
            QtGui.QPixmap('img/cat.png')
        ))#设置背景图片
        self.centralWidget().setPalette(palette) # 设置调色板

        input_img=QtGui.QPixmap('img/input_test.png') #打开位图
        self.input_img.setPixmap(input_img) #设置位图

        export_img=QtGui.QPixmap('img/output_test.png')  #打开位图
        self.export_img.setPixmap(export_img) #设置位图


if __name__=='__main__':
    app=QApplication(sys.argv)  #创建GUI对象
    main=Main()  #创建主窗体UI类对象
    main.show() #显示主窗体
    sys.exit(app.exec_()) # 除非退出程序关闭窗体，否则一直运行























