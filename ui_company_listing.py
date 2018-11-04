from PyQt5 import QtCore, QtGui, QtWidgets

class CompanyListing(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CompanyListing, self).__init__(parent)
        self.setObjectName("Form")
        self.resize(400, 83)
        self.setMinimumSize(QtCore.QSize(400, 0))
        self.setMaximumSize(QtCore.QSize(400, 16777215))
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 40))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.companyLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.companyLabel.setFont(font)
        self.companyLabel.setObjectName("companyLabel")
        self.horizontalLayout.addWidget(self.companyLabel)
        self.priceLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.priceLabel.setFont(font)
        self.priceLabel.setObjectName("priceLabel")
        self.horizontalLayout.addWidget(self.priceLabel)
        self.percentChangeLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.percentChangeLabel.setObjectName("percentChangeLabel")
        self.horizontalLayout.addWidget(self.percentChangeLabel)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 40, 401, 42))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.highLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.highLabel.setObjectName("highLabel")
        self.gridLayout.addWidget(self.highLabel, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)
        self.openLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.openLabel.setObjectName("openLabel")
        self.gridLayout.addWidget(self.openLabel, 1, 0, 1, 1)
        self.volumeLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.volumeLabel.setObjectName("volumeLabel")
        self.gridLayout.addWidget(self.volumeLabel, 1, 4, 1, 1)
        self.closeLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.closeLabel.setObjectName("closeLabel")
        self.gridLayout.addWidget(self.closeLabel, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 1)
        self.lowLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lowLabel.setObjectName("lowLabel")
        self.gridLayout.addWidget(self.lowLabel, 1, 2, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.companyLabel.setText(_translate("Form", "AAPL"))
        self.priceLabel.setText(_translate("Form", "0"))
        self.percentChangeLabel.setText(_translate("Form", "0"))
        self.label_3.setText(_translate("Form", "Close"))
        self.label_2.setText(_translate("Form", "High"))
        self.highLabel.setText(_translate("Form", "0"))
        self.label_4.setText(_translate("Form", "Volume"))
        self.openLabel.setText(_translate("Form", "0"))
        self.volumeLabel.setText(_translate("Form", "0"))
        self.closeLabel.setText(_translate("Form", "0"))
        self.label.setText(_translate("Form", "Open"))
        self.label_9.setText(_translate("Form", "Low"))
        self.lowLabel.setText(_translate("Form", "0"))
