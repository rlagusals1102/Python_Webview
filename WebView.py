import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore

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
        self.web_view.load(QUrl('https://www.google.com/?hl=ko'))

        # URL 입력 필드
        self.url_input = QLineEdit()
        self.url_input.returnPressed.connect(self.load_url)
        self.url_input.setFixedHeight(30)

        # 로드 버튼
        self.load_button = QPushButton('Load', self)
        self.load_button.setStyleSheet('''
            QPushButton {
                border: none;
                background-color: transparent;
            }
            QPushButton:hover {
                background-color: #F5F5F5;
            }
        ''')
        self.load_button.clicked.connect(self.load_url)
        toolbar = QToolBar('Load')
        toolbar.addWidget(self.load_button)

        # 새 창 버튼
        self.new_window_button = QPushButton('New Window', self)
        self.new_window_button.setStyleSheet('''
            QPushButton {
                border: none;
                background-color: transparent;
            }
            QPushButton:hover {
                background-color: #F5F5F5;
            }
        ''')
        self.new_window_button.clicked.connect(self.new_window)
        toolbar.addWidget(self.new_window_button)

        # 전체 레이아웃
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.url_input)
        hbox.addWidget(toolbar)
        vbox.addLayout(hbox)
        vbox.addWidget(self.web_view)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.show()

    def load_url(self):
        url = self.url_input.text()
        self.web_view.load(QUrl(url))

    def keyPressEvent(self, event):
        if event.modifiers() == QtCore.Qt.ControlModifier and event.key() == QtCore.Qt.Key_R:
            self.web_view.reload()
        else:
            super().keyPressEvent(event)

    def new_window(self):
        new_window = WebPage()
        new_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WebPage()
    sys.exit(app.exec_())
