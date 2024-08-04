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
from tables.tableview_yfinance import YFinanceTableView




class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('yfinance test')

        table = YFinanceTableView()
        self.setCentralWidget(table)

        ticker = yf.Ticker('^DJI')
        df = ticker.history(period='1mo')
        index_name = df.index.name
        if index_name != '':
            table.setUpperLeftCornerTitle(index_name)
        model = YFinanceModel(df)
        table.setModel(model)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
