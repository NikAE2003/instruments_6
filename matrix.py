from msilib.schema import tables
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtCore import QObject, pyqtSignal

class sender(QObject):
    send = pyqtSignal(list)

class Matrix():
    def __init__(self, table:QTableWidget):
        self._table = table
        self._rowCount = self._table.rowCount()
        self._ColumnCount = self._table.columnCount()
        self._capital = [[int(self._table.item(j,i).text()) for i in range(self._ColumnCount)] for j in range(self._rowCount)]

    def calculateRisk(self):
        transposed = transpose(self._capital.copy())
        maximums = [max(row) for row in transposed]

        self._risk = [[maximums[i] - elem for i, elem in enumerate(row)] for row in enumerate(self._capital)]
        

def transpose(matrix: list):
    for i in range(len(matrix[0])):
        yield [matrix[j][i] for j in range(len(matrix))]

