from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from QPoint3DF import *

class InputDialog(QDialog):

    def __init__(self, *args, **kwargs):
        """Constructs QDialog window."""
        super().__init__(*args, **kwargs)
        # Initialize necessary objects
        self.setWindowTitle("Contour Properties")
        self.dmin = QLineEdit(self)
        self.alpha = QLineEdit(self)
        self.beta = QLineEdit(self)
        self.gamma = QLineEdit(self)
        self.lam = QLineEdit(self)
        self.iters = QLineEdit(self)
        self.ok_button = QPushButton("Ok", self)
        self.cancel_button = QPushButton("Cancel", self)
        # Create layout
        layout = QFormLayout(self)
        layout.addRow("Minimum distance [m] (default=100)", self.dmin)
        layout.addRow("Alpha coefficient (default=0.3)", self.alpha)
        layout.addRow("Beta coefficient (default=1000)", self.beta)
        layout.addRow("Gamma coefficient (default=1000)", self.gamma)
        layout.addRow("Lambda coefficient (default=20)", self.lam)
        layout.addRow("Number of iterations (default=500)", self.iters)
        layout.addRow(self.ok_button)
        layout.addRow(self.cancel_button)
        # Connect signals to slots
        self.ok_button.clicked.connect(self.okButtonClicked)
        self.cancel_button.clicked.connect(self.cancelButtonClicked)

    def okButtonClicked(self):
        """Emits accept signal on button click."""
        self.accept()

    def cancelButtonClicked(self):
        """Emits reject signal on button click."""
        self.reject()

    def getInputs(self):
        """Returns input values."""
        return self.dmin.text(), self.alpha.text(), self.beta.text(), self.gamma.text(), self.lam.text(), self.iters.text()