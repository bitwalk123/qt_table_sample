import sys
import yfinance as yf
from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QAbstractButton,
    QApplication,
    QLabel,
    QMainWindow,
    QTableView,
    QVBoxLayout,
)

from models.model_yfinance import YFinanceModel


def add_label(but: QAbstractButton):
    layout = QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    but.setLayout(layout)
    label = QLabel()
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    layout.addWidget(label)
    return label


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('yfinance test')

        table = QTableView()
        table.setStyleSheet("""
            QTableView{
                font-family: monospace;
            }
            QTableCornerButton::section{
                border-width: 1px;
                border-color: #BABABA;
                border-style: outset;
            }
        """)
        but = table.findChild(QAbstractButton, '')
        if type(but) is QAbstractButton:
            label = add_label(but)
        else:
            label = None
        self.setCentralWidget(table)

        ticker = yf.Ticker('^DJI')
        df = ticker.history(period='1mo')
        index_name = df.index.name
        if index_name != '':
            if label is not None:
                label.setText(index_name)
        model = YFinanceModel(df)
        table.setModel(model)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
