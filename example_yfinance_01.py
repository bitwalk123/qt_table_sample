import sys
import yfinance as yf

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)

from models.model_yfinance import YFinanceModel
from tables.tableview_pandas import PandasTableView


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('yfinance test')

        tbl = PandasTableView()
        self.setCentralWidget(tbl)

        ticker = yf.Ticker('^DJI')
        df = ticker.history(period='1mo')

        name_index = df.index.name
        if name_index != '':
            tbl.setUpperLeftCornerTitle(name_index)

        model = YFinanceModel(df)
        tbl.setModel(model)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
