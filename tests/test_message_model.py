# tests/test_message_model.py
from PyQt5.QtCore import Qt

from start import USER_EVA, USER_ME, MessageModel


class TestMessageModel:
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

    def test_multiple_messages(self):
        self.model.add_message(USER_ME, "First")
        self.model.add_message(USER_EVA, "Second")
        self.model.add_message(USER_ME, "Third")
        assert self.model.rowCount(None) == 3
        assert self.model.data(self.model.index(0), Qt.DisplayRole)[1] == "First"
        assert self.model.data(self.model.index(2), Qt.DisplayRole)[1] == "Third"
