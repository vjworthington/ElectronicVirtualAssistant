from PyQt5.QtCore import QAbstractListModel, QMargins, QPoint, QSize, Qt
from PyQt5.QtGui import QColor, QFontMetrics
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
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
        # calc dim
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

          l = QVBoxLayout()

          self.message_input = QLineEdit("Enter message: ")

          self.btn1 = QPushButton("user")
          self.btn2 = QPushButton("eva")

          self.messages = QListView()
          self.messages.setItemDelegate(MessageDelegate())

          self.model = MessageModel()
          self.messages.setModel(self.model)

          self.btn1.pressed.connect(self.message_to)
          self.btn2.pressed.connect(self.message_from)

          l.addWidget(self.messages)
          l.addWidget(self.message_input)
          l.addWidget(self.btn1)
          l.addWidget(self.btn2)

          self.w = QWidget()
          self.w.setLayout(l)
          self.setCentralWidget(self.w)
    
    def message_to(self):
        self.model.add_message(USER_ME, self.message_input.text())


    def message_from(self):
        self.model.add_message(USER_EVA, self.message_input.text())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()