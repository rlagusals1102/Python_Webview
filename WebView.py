import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Web Page Viewer'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # 웹 페이지 뷰어
        self.web_view = QWebEngineView(self)
        self.web_view.load(QUrl('https://www.google.com'))
        self.setCentralWidget(self.web_view)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WebPage()
    sys.exit(app.exec_())
