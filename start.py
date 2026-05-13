################################
# Electronic Virtual Assistant #
#        also known as         #
#            E V A             #
################################

from openai import OpenAI
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QAbstractListModel, QMargins, QPoint, QSize, Qt
from PyQt5.QtGui import QColor, QFontMetrics, QMovie, QPixmap
from PyQt5.QtWidgets import *
from paths import BACKGROUND_GIF
from paths import AVATAR_GIF
import time
import sys

USER_ME = 0
USER_EVA = 1

eva_color = QtGui.QColor(144,202,249) #90caf9
eva_color.setAlpha(128)
user_color = QtGui.QColor(164, 214, 167) #a5d6a7
user_color.setAlpha(128)

bubble_colors = {USER_ME: user_color, USER_EVA: eva_color}
bubble_padding = QMargins(15, 5, 15, 5)
text_padding = QMargins(25, 15, 25, 15)

# Your API: enter command below into terminal to set your OpenAI API key
#export OPENAI_API_KEY="your key"

# Create EVA
# OLD - client = OpenAI()
# read API key from file
try:
    #with open("config.txt", "r") as file:
    #    api_key = file.read().strip()

    #client = OpenAI(
    #api_key=api_key,
    #base_url="https://openrouter.ai/api/v1"
    #)

    def load_config():
        config = {}

        with open("config.txt", "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()

        return config


    config = load_config()

    API_KEY = config["API_KEY"]
    MODEL_NAME = config["MODEL"]
    
    client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
    )

except FileNotFoundError:
    print("config.txt not found")
    exit()

except Exception as e:
    print("Error loading API key:", e)
    exit()

def EVA(prompt):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "Helpful AI"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"An error occured: {str(e)}")
        return "Error. Please try again."

# draw messages
class MessageDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        # retrieve user, message
        user, text = index.model().data(index, Qt.DisplayRole)

        bubblerect = option.rect.marginsRemoved(bubble_padding)
        textrect = option.rect.marginsRemoved(text_padding)

        # draw bubble, send message
        painter.setPen(Qt.NoPen)
        color = QColor(bubble_colors[user])
        painter.setBrush(color)
        painter.drawRoundedRect(bubblerect, 10, 10)

        if user == USER_ME:
            p1 = bubblerect.topRight()
        else:
            p1 = bubblerect.topLeft()
        painter.drawPolygon(p1 + QPoint(-20, 0), p1 + QPoint(20, 0), p1 + QPoint(0, 20))

        # draw text
        painter.setPen(Qt.black)
        painter.drawText(textrect, Qt.TextWordWrap, text)

    def sizeHint(self, option, index):
        _, text = index.model().data(index, Qt.DisplayRole)
        # calc dimensions
        metrics = QApplication.fontMetrics()
        rect = option.rect.marginsRemoved(text_padding)
        rect = metrics.boundingRect(rect, Qt.TextWordWrap, text)
        rect = rect.marginsAdded(text_padding)
        return rect.size()
    
class MessageModel(QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super(MessageModel, self).__init__(*args, **kwargs)
        self.messages = []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.messages[index.row()]
    
    def rowCount(self, index):
        return len(self.messages)

    def add_message(self, who, text):
        if text:
            self.messages.append((who,text))
            self.layoutChanged.emit()

# Move API QThread to background to prevent Gif/Movie freezing
class Worker(QtCore.QThread):
    finished = QtCore.pyqtSignal(str)

    def __init__(self, prompt):
        super().__init__()
        self.prompt = prompt

    def run(self):
        response = EVA(self.prompt)
        self.finished.emit(response)

class MainWindow(QMainWindow):
    def __init__(self):
          super(MainWindow, self).__init__()
          self.initUI()

          # button and font colors
          self.message_input = QLineEdit("")
          self.btn1 = QPushButton("SEND")
          self.btn1.setStyleSheet("color: white;")

          self.messages = QListView()
          self.messages.setItemDelegate(MessageDelegate())

          self.model = MessageModel()
          self.messages.setModel(self.model)

          self.btn1.pressed.connect(self.message_to)
          self.btn1.pressed.connect(self.message_from)

          # add avatar
          self.avatar = QLabel(self)
          # movie = QtGui.QMovie('C:/Users/hexidigit/OneDrive/Desktop/shiny-slime-girl-allu.gif')
          movie = QtGui.QMovie(AVATAR_GIF)
          movie.setScaledSize(QSize(269, 200))
          self.avatar.setMovie(movie)
          movie.start()

          # add widgets
          # user_input / send
          user_input_box = QHBoxLayout()
          bottom_widget = QWidget()
          user_input_box.addWidget(self.message_input)
          self.message_input.setStyleSheet("""color: white; background-color: rgba(0, 0, 0, 0);""")
          user_input_box.addWidget(self.btn1)
          user_input_box.addWidget(self.btn1.setFixedWidth(50))
          bottom_widget.setLayout(user_input_box)

          # Chat window and user input / send
          vbox = QVBoxLayout()
          chat_widget = QWidget()
          vbox.addWidget(self.messages)
          self.messages.setStyleSheet("border :0px; background-color: rgba(0, 0, 0, 0)")
          vbox.addWidget(bottom_widget)
          chat_widget.setLayout(vbox)

          # avatar and chat
          hbox = QHBoxLayout()
          hbox.addWidget(self.avatar)
          hbox.addWidget(chat_widget)

          self.w = QWidget()
          self.w.setLayout(hbox)
          self.setCentralWidget(self.w)

    def message_to(self):
        self.model.add_message(USER_ME, self.message_input.text())

    def message_from(self):
        self.worker = Worker(self.message_input.text())
        self.worker.finished.connect(self.display_response)
        self.worker.start()

    def display_response(self, response):
        self.model.add_message(USER_EVA, response)

    # animated background
    def initUI(self):
        self.setGeometry(100, 100, 645, 370)
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, self.width(), self.height())
        self.movie = QMovie(BACKGROUND_GIF)
        self.label.setMovie(self.movie)
        self.movie.start()
        self.show()

# Main
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window = MainWindow()
    window.resize(645, 370)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
