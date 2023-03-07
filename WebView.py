import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout

class WebSurf(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Web Surfing'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 150
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # URL 입력 필드
        self.url_input = QLineEdit(self)
        self.url_input.move(20, 20)
        self.url_input.resize(260, 30)

        # 검색 버튼
        self.search_button = QPushButton('Search', self)
        self.search_button.move(290, 20)
        self.search_button.resize(80, 30)
        self.search_button.clicked.connect(self.search)

        # 구글 검색 버튼
        self.google_button = QPushButton('Google', self)
        self.google_button.move(20, 60)
        self.google_button.resize(80, 30)
        self.google_button.clicked.connect(self.google_search)

        # 네이버 검색 버튼
        self.naver_button = QPushButton('Naver', self)
        self.naver_button.move(110, 60)
        self.naver_button.resize(80, 30)
        self.naver_button.clicked.connect(self.naver_search)

        # 다음 검색 버튼
        self.daum_button = QPushButton('Daum', self)
        self.daum_button.move(200, 60)
        self.daum_button.resize(80, 30)
        self.daum_button.clicked.connect(self.daum_search)

        self.show()

    def search(self):
        url = self.url_input.text()
        webbrowser.open(url)

    def google_search(self):
        keyword = self.url_input.text()
        url = 'https://www.google.com/search?q=' + keyword
        webbrowser.open(url)

    def naver_search(self):
        keyword = self.url_input.text()
        url = 'https://search.naver.com/search.naver?query=' + keyword
        webbrowser.open(url)

    def daum_search(self):
        keyword = self.url_input.text()
        url = 'https://search.daum.net/search?q=' + keyword
        webbrowser.open(url)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WebSurf()
    sys.exit(app.exec_())
