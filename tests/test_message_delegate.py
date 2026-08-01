# tests/test_message_delegate.py
from unittest.mock import MagicMock, patch

from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtGui import QFontMetrics, QPainter

from start import (
    USER_EVA,
    USER_ME,
    MessageDelegate,
)


class TestMessageDelegate:
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

        # Verify bubble drawing calls
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

        # Should still draw bubble but no text
        self.painter.drawRoundedRect.assert_called()
        self.painter.drawPolygon.assert_called()

    def test_size_hint_returns_size(self):
        index = self._make_index(USER_ME, "Test message")

        # Mock QApplication.fontMetrics
        with patch("start.QApplication") as mock_app:
            mock_metrics = MagicMock(spec=QFontMetrics)
            mock_metrics.boundingRect.return_value = QRect(0, 0, 200, 50)
            mock_app.fontMetrics.return_value = mock_metrics

            size = self.delegate.sizeHint(self.option, index)

        assert isinstance(size, QSize)
        assert size.width() > 0
        assert size.height() > 0

    def test_size_hint_empty_text(self):
        index = self._make_index(USER_ME, "")

        with patch("start.QApplication") as mock_app:
            mock_metrics = MagicMock(spec=QFontMetrics)
            mock_metrics.boundingRect.return_value = QRect(0, 0, 0, 0)
            mock_app.fontMetrics.return_value = mock_metrics

            size = self.delegate.sizeHint(self.option, index)

        assert isinstance(size, QSize)
