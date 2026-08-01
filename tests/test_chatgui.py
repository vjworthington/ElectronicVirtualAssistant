# tests/test_chatgui.py
from unittest.mock import MagicMock, patch

from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtGui import QFontMetrics, QPainter

from chatgui import (
    USER_EVA,
    USER_ME,
    MainWindow,
    MessageDelegate,
    MessageModel,
)


class TestMessageDelegate:
    """Tests for chat message rendering delegate."""

    def setup_method(self):
        self.delegate = MessageDelegate()
        self.painter = MagicMock(spec=QPainter)
        self.option = MagicMock()
        self.option.rect = QRect(0, 0, 400, 100)

    def _make_index(self, user, text):
        index = MagicMock()
        index.model().data.return_value = (user, text)
        return index

    def test_paint_user_message(self):
        index = self._make_index(USER_ME, "Hello")

        self.delegate.paint(self.painter, self.option, index)

        self.painter.setPen.assert_any_call(Qt.NoPen)
        self.painter.setBrush.assert_called()
        self.painter.drawRoundedRect.assert_called()
        self.painter.drawPolygon.assert_called()
        self.painter.drawText.assert_called()

    def test_paint_eva_message(self):
        index = self._make_index(USER_EVA, "Hi there")

        self.delegate.paint(self.painter, self.option, index)

        self.painter.setPen.assert_any_call(Qt.NoPen)
        self.painter.setBrush.assert_called()
        self.painter.drawRoundedRect.assert_called()
        self.painter.drawPolygon.assert_called()
        self.painter.drawText.assert_called()

    def test_paint_empty_text(self):
        index = self._make_index(USER_ME, "")

        self.delegate.paint(self.painter, self.option, index)

        self.painter.drawRoundedRect.assert_called()
        self.painter.drawPolygon.assert_called()

    def test_size_hint_returns_size(self):
        index = self._make_index(USER_ME, "Test message")

        with patch("chatgui.QApplication") as mock_app:
            mock_metrics = MagicMock(spec=QFontMetrics)
            mock_metrics.boundingRect.return_value = QRect(0, 0, 200, 50)
            mock_app.fontMetrics.return_value = mock_metrics

            size = self.delegate.sizeHint(self.option, index)

        assert isinstance(size, QSize)
        assert size.width() > 0
        assert size.height() > 0


class TestMessageModel:
    """Tests for message data model."""

    def setup_method(self):
        self.model = MessageModel()

    def test_initial_empty(self):
        assert self.model.rowCount(None) == 0

    def test_add_message_user(self):
        self.model.add_message(USER_ME, "Hello")
        assert self.model.rowCount(None) == 1
        assert self.model.data(self.model.index(0), Qt.DisplayRole) == (USER_ME, "Hello")

    def test_add_message_eva(self):
        self.model.add_message(USER_EVA, "Hi there")
        assert self.model.rowCount(None) == 1
        assert self.model.data(self.model.index(0), Qt.DisplayRole) == (USER_EVA, "Hi there")

    def test_add_empty_message_ignored(self):
        self.model.add_message(USER_ME, "")
        self.model.add_message(USER_ME, None)
        assert self.model.rowCount(None) == 0

    def test_multiple_messages_order(self):
        self.model.add_message(USER_ME, "First")
        self.model.add_message(USER_EVA, "Second")
        self.model.add_message(USER_ME, "Third")
        assert self.model.rowCount(None) == 3
        assert self.model.data(self.model.index(0), Qt.DisplayRole)[1] == "First"
        assert self.model.data(self.model.index(2), Qt.DisplayRole)[1] == "Third"

    def test_layout_changed_emitted(self, qtbot):
        """Verify layoutChanged signal emits on add_message."""
        with qtbot.waitSignal(self.model.layoutChanged, timeout=100):
            self.model.add_message(USER_ME, "Test")


class TestMainWindow:
    """Tests for main chat window."""

    def test_window_creation(self, qtbot):
        """Verify MainWindow constructs without error."""
        window = MainWindow()
        qtbot.addWidget(window)

        assert window.windowTitle() == ""  # No title set
        assert window.centralWidget() is not None

    def test_message_input_exists(self, qtbot):
        window = MainWindow()
        qtbot.addWidget(window)

        assert hasattr(window, "message_input")
        assert window.message_input.placeholderText() == ""

    def test_send_buttons_exist(self, qtbot):
        window = MainWindow()
        qtbot.addWidget(window)

        assert hasattr(window, "btn1")
        assert hasattr(window, "btn2")
        assert window.btn1.text() == "user"
        assert window.btn2.text() == "eva"

    def test_message_list_view_exists(self, qtbot):
        window = MainWindow()
        qtbot.addWidget(window)

        assert hasattr(window, "messages")
        assert window.messages.itemDelegate() is not None
        assert isinstance(window.messages.itemDelegate(), MessageDelegate)

    def test_model_connected(self, qtbot):
        window = MainWindow()
        qtbot.addWidget(window)

        assert window.messages.model() is window.model
        assert isinstance(window.model, MessageModel)

    def test_message_to_adds_user_message(self, qtbot):
        window = MainWindow()
        qtbot.addWidget(window)

        window.message_input.setText("Hello")
        window.message_to()

        assert window.model.rowCount(None) == 1
        assert window.model.data(window.model.index(0), Qt.DisplayRole) == (USER_ME, "Hello")

    def test_message_from_adds_eva_message(self, qtbot):
        window = MainWindow()
        qtbot.addWidget(window)

        window.message_input.setText("Hi")
        window.message_from()

        assert window.model.rowCount(None) == 1
        assert window.model.data(window.model.index(0), Qt.DisplayRole) == (USER_EVA, "Hi")

    def test_buttons_connected_to_slots(self, qtbot):
        """Verify button signals connect to correct slots."""
        window = MainWindow()
        qtbot.addWidget(window)

        # btn1 -> message_to
        window.message_input.setText("Test")
        qtbot.mouseClick(window.btn1, Qt.LeftButton)
        assert window.model.rowCount(None) == 1

        # btn2 -> message_from
        window.message_input.setText("Reply")
        qtbot.mouseClick(window.btn2, Qt.LeftButton)
        assert window.model.rowCount(None) == 2
