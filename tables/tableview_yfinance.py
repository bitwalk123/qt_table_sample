from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableView, QAbstractButton, QVBoxLayout, QLabel


def add_label(but: QAbstractButton):
    layout = QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    but.setLayout(layout)
    label = QLabel()
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(label)
    return label


class YFinanceTableView(QTableView):
    __version__ = '0.0.1'

    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QTableView{
                font-family: monospace;
            }
            QTableCornerButton::section{
                border-width: 1px;
                border-color: #BABABA;
                border-style: outset;
            }
        """)
        but = self.findChild(QAbstractButton, '')
        if type(but) is QAbstractButton:
            self.label = add_label(but)
        else:
            self.label = None

    def setUpperLeftCornerTitle(self, title: str):
        if self.label is not None:
            self.label.setText(title)
