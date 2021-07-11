import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
 
import Ui_Webp_to_Gif_Converter
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Webp_to_Gif_Converter.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
