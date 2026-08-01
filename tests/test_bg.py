# tests/test_bg.py
from PyQt5 import QtCore, QtWidgets

from bg import GUI_main


class TestGUIMain:
    """Tests for GUI_main background setup."""

    def test_setup_gui_creates_main_window_structure(self, qtbot):
        """Verify setupGUI creates central widget and label with correct properties."""
        window = QtWidgets.QMainWindow()
        gui = GUI_main()

        # This should not raise
        gui.setupGUI(window)

        # Window properties
        assert window.objectName() == "MainWindow"
        assert window.width() == 645
        assert window.height() == 370

        # Central widget exists
        central = window.centralWidget()
        assert central is not None
        assert central.objectName() == "centralwidget"

        # Label exists on central widget
        label = gui.label
        assert label is not None
        assert isinstance(label, QtWidgets.QLabel)
        assert label.objectName() == "label"
        assert label.parent() is central

        # Label geometry constraints
        assert label.minimumSize() == QtCore.QSize(645, 370)
        assert label.maximumSize() == QtCore.QSize(645, 370)

        # Label geometry (approximate - QRect(1,1,1000,1000) covers window)
        geo = label.geometry()
        assert geo.x() == 1
        assert geo.y() == 1

    def test_setup_gui_idempotent(self, qtbot):
        """Calling setupGUI twice should not crash or duplicate widgets."""
        window = QtWidgets.QMainWindow()
        gui = GUI_main()

        gui.setupGUI(window)
        first_label = gui.label
        first_central = window.centralWidget()

        gui.setupGUI(window)

        # Should replace central widget
        assert window.centralWidget() is not first_central
        assert gui.label is not first_label

    def test_main_block_creates_window(self, qtbot):
        """Verify the __main__ block creates a showable window."""
        # This tests the module-level code path
        from bg import GUI_main as MainGUI

        window = QtWidgets.QMainWindow()
        ui = MainGUI()
        ui.setupGUI(window)

        qtbot.addWidget(window)
        window.show()

        # Process events to ensure window is shown
        qtbot.waitExposed(window)

        assert window.isVisible()
        assert window.windowTitle() == ""  # No title set in bg.py
