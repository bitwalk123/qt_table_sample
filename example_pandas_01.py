import sys
import pandas as pd
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)

from models.model_pandas import PandasModel
from tables.tableview_pandas import PandasTableView


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('df test')

        tbl = PandasTableView()
        self.setCentralWidget(tbl)

        df = pd.DataFrame(
            [
                [1.2, 8.5, -2],
                [2.05, 0.1, -1.23],
                [3.21, 5, 2],
                [3, 3.0, 2],
                [5.2, 8.5, 9.87],
            ],
            columns=['A', 'B', 'C'],
            index=['Row 1', 'Row 2', 'Row 3', 'Row 4', 'Row 5']
        )

        name_index = df.index.name
        if name_index != '':
            tbl.setUpperLeftCornerTitle(name_index)

        model = PandasModel(df)
        tbl.setModel(model)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
