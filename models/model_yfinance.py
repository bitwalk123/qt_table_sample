from typing import Any, Union

import numpy as np
import pandas as pd
from PySide6.QtCore import (
    QModelIndex,
    QPersistentModelIndex,
    Qt,
)

from models.model_pandas import PandasModel


class YFinanceModel(PandasModel):
    __version__ = '0.0.1'

    def __init__(self, df: pd.DataFrame):
        super().__init__(df)

    def data(self, index: Union[QModelIndex, QPersistentModelIndex], role: int = ...) -> Any:
        if not index.isValid():
            return None

        row = index.row()
        col = index.column()
        value = self._df.iloc[row, col]

        if role == Qt.ItemDataRole.DisplayRole:
            if (type(value) is np.int64) | (type(value) is np.float64):
                return '%.2f' % value
            else:
                return str(value)

        if role == Qt.ItemDataRole.TextAlignmentRole:
            if (type(value) is np.int64) | (type(value) is np.float64):
                flag = Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
            else:
                flag = Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
            return flag
