import sys
import yfinance as yf

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableView,
)

from models.model_pandas import PandasModel


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('df test')

        table = QTableView()
        self.setCentralWidget(table)

        ticker = yf.Ticker('^N225')
        df = ticker.history(period='1mo')
        model = PandasModel(df)
        table.setModel(model)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
