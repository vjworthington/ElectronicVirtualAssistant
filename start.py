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
import time
import sys

USER_ME = 0
USER_EVA = 1

user_color = QtGui.QColor(144,202,249) #90caf9
user_color.setAlpha(128)
eva_color = QtGui.QColor(164, 214, 167) #a5d6a7
eva_color.setAlpha(128)

bubble_colors = {USER_ME: user_color, USER_EVA: eva_color}
bubble_padding = QMargins(15, 5, 15, 5)
text_padding = QMargins(25, 15, 25, 15)

# Your API: enter command below into terminal to set your OpenAI API key
#export OPENAI_API_KEY="your key"

# Create EVA
client = OpenAI()
def EVA(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
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

class MainWindow(QMainWindow):
    def __init__(self):
          super(MainWindow, self).__init__()
          self.initUI()

          # button and font colors
          self.message_input = QLineEdit("")
          self.message_input.setStyleSheet("color: white;")
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
          movie = QtGui.QMovie('/home/hexidigit/Downloads/king_slime.gif')
          self.avatar.setMovie(movie)
          movie.start()

          # add widgets
          # user_input / send
          user_input_box = QHBoxLayout()
          bottom_widget = QWidget()
          user_input_box.addWidget(self.message_input)
          self.message_input.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
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
        response = EVA(self.message_input.text())
        self.model.add_message(USER_EVA, response)

    # animated background
    def initUI(self):
        self.setGeometry(100, 100, 645, 370)
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, self.width(), self.height())
        self.movie = QMovie("/home/hexidigit/background.gif")
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
