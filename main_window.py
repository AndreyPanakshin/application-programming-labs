import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget, QSizePolicy, QMessageBox
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap

from Iterator import Iterator
class ImageViewer(QMainWindow):
    """
    Конструктор класса Image Viewer
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.setFixedSize(QSize(1280,700))
        self.move(100,100)
        self.init_ui()
        self.path_to_csv = None
        self.iterator_image = None
        self.load_button=None
        self.next_button=None
        self.cur_img=None

    def init_ui(self):
        '''
        создаем и настраиваем графический интерфейс(GUI)
        '''
        c_widget = QWidget(self)
        self.setCentralWidget(c_widget)
        layout = QVBoxLayout()
        c_widget.setLayout(layout)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.load_button = QPushButton("load file csv")
        self.load_button.clicked.connect(self.load_csv)

        self.next_button = QPushButton("Next image")
        self.next_button.clicked.connect(self.next_image)

        layout.addWidget(self.label)
        layout.addWidget(self.next_button)
        layout.addWidget(self.load_button)

    def load_csv(self):
        '''
        получаем путь к csv файлу
        '''
        path_to_csv, _ = QFileDialog.getOpenFileName(self, "Select CSV-file", "", "CSV file (*.csv)")
        if path_to_csv:
            self.path_to_csv = path_to_csv
            self.iterator_image = iter(Iterator(self.path_to_csv))
            self.next_image()

    def next_image(self):
        '''
        получаем следующий путь к изображению из итератора
        '''
        try:
           img = next(self.iterator_image)
           self.cur_img = img[0]
           self.show_image(self.cur_img)
        except StopIteration:
            self.label.setText("No more images")
            self.next_button.setEnabled(False)

    def show_image(self, img):
        '''
        Выводим изображение по полученной директории на экран в нашем окне
        :param img: путь к изображению
        '''
        try:
            pixmap = QPixmap(img)
            if pixmap.isNull():
                QMessageBox.critical(self, "Error", "Error file.")

            self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error load image: {str(e)}")



def main():
    try:
        app = QApplication(sys.argv)
        window = ImageViewer()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"mistake:{e}")

if __name__ == "__main__":
    main()


