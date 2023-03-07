import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QMdiArea, QMdiSubWindow
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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = 'Web Browser'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # 다중 창 레이아웃
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        # 새 창 열기 버튼
        new_window_action = QAction(QIcon('new_window.png'), 'New Window', self)
        new_window_action.setShortcut('Ctrl+N')
        new_window_action.triggered.connect(self.new_window)
        toolbar = self.addToolBar('New Window')
        toolbar.addAction(new_window_action)

        # 로드 버튼
        load_action = QAction(QIcon('load.png'), 'Load', self)
        load_action.setShortcut('Ctrl+L')
        load_action.triggered.connect(self.load_url)
        toolbar = self.addToolBar('Load')
        toolbar.addAction(load_action)

        # 리로드 버튼
        reload_action = QAction(QIcon('reload.png'), 'Reload', self)
        reload_action.setShortcut('Ctrl+R')
        reload_action.triggered.connect(self.reload_page)
        toolbar.addAction(reload_action)

        self.show()
    
    def new_window(self):
        sub_window = QMdiSubWindow()
        sub_window.setWidget(WebPage())
        sub_window.setWindowTitle('New Window')
        sub_window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()

    def load_url(self):
        active_window = self.mdi_area.activeSubWindow()
        if active_window:
            active_window.widget().load_url()

    def reload_page(self):
        active_window = self.mdi_area.activeSubWindow()
        if active_window:
            active_window.widget().web_view.reload()

    def keyPressEvent(self, event):
        if event.modifiers() == QtCore.Qt.ControlModifier and event.key() == QtCore.Qt.Key_R:
            self.reload_page()
        else:
            super().keyPressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

