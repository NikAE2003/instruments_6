from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from matrix import Matrix

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.connections()

    def initUI(self):

        self.resize(800, 600)

        self.centralWidget = QWidget(self)
        self.mainLayout = QVBoxLayout(self.centralWidget)
        self.setCentralWidget(self.centralWidget)

        self.formLayout = QFormLayout()
        self.formLayout.setContentsMargins(0,0,0,0)

        self.A_label = QLabel('A', self.centralWidget)
        self.A_field = QSpinBox(self.centralWidget)
        self.A_field.setButtonSymbols(QSpinBox.NoButtons)

        self.P_label = QLabel('П', self.centralWidget)
        self.P_field = QSpinBox(self.centralWidget)
        self.P_field.setButtonSymbols(QSpinBox.NoButtons)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.A_label)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.A_field)
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.P_label)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.P_field)
        
        self.mainLayout.addLayout(self.formLayout)

        self.mainTable = QTableWidget(self.centralWidget)
        self.mainTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.mainLayout.addWidget(self.mainTable)

        self.q_table = QTableWidget(self.centralWidget)
        self.q_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.mainLayout.addWidget(self.q_table)

        self.gm_formLayout = QFormLayout()
        self.gm_formLayout.setContentsMargins(0,0,0,0)

        self.gourviz_label = QLabel('Константа для метода Гурвица',self.centralWidget)
        self.gourviz_field = QSpinBox(self.centralWidget)
        self.gourviz_field.setButtonSymbols(QSpinBox.NoButtons)

        self.gm_formLayout.setWidget(0, QFormLayout.LabelRole, self.gourviz_label)
        self.gm_formLayout.setWidget(0, QFormLayout.FieldRole, self.gourviz_field)
        
        self.mainLayout.addLayout(self.gm_formLayout)

        self.getResult_button = QPushButton(self.centralWidget)
        
        self.mainLayout.addWidget(self.getResult_button)

        self.res_label = QLabel('Результаты:', self.centralWidget)
        self.res_field = QLineEdit(self.centralWidget)

        self.mainLayout.addWidget(self.res_label)
        self.mainLayout.addWidget(self.res_field)

    def connections(self):
        self.A_field.valueChanged.connect(self.changeRowCount)
        self.P_field.valueChanged.connect(self.columnCountChange)
        self.getResult_button.pressed.connect(self.getResult)
    
    def changeRowCount(self, value):
        self.mainTable.setRowCount(value)
        self.mainTable.setVerticalHeaderLabels([f'A{i + 1}' for i in range(value)])
        self.q_table.setRowCount(1)
    
    def columnCountChange(self, value):
        self.mainTable.setColumnCount(value)
        self.q_table.setColumnCount(value)
        self.mainTable.setHorizontalHeaderLabels([f'П{i+1}' for i in range(value)])
        self.q_table.setHorizontalHeaderLabels([f'Q{i+1}' for i in range(value)])

    def getResult(self):
        self.matrix = Matrix(self.mainTable)
        self.matrix.calculateRisk()
