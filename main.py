from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QGridLayout,
    QGroupBox,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QApplication
)

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.x = ''
        self.y = ''
        self.operator = None
        self.left_operand = True
        self.result_shown = False
        self.result = 0
        self.setWindowTitle('Calculator')
        self.resize(230, 300)
        self.setFixedSize(self.size())
        self.createGridLayout()

        layout = QVBoxLayout()
        self.input = QLineEdit()
        self.input.setStyleSheet("height: 30px; font-size: 16px")
        self.input.setReadOnly(True)
        layout.addWidget(self.input)
        layout.addWidget(self.group)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def createGridLayout(self) -> QGridLayout:
        self.group = QGroupBox()
        layout = QGridLayout()
        layout.setColumnStretch(1, 1)

        self.one = QPushButton('1')
        self.two = QPushButton('2')
        self.three = QPushButton('3')
        self.four = QPushButton('4')
        self.five = QPushButton('5')
        self.six = QPushButton('6')
        self.seven = QPushButton('7')
        self.eight = QPushButton('8')
        self.nine = QPushButton('9')
        self.zero = QPushButton('0')
        self.plus = QPushButton('+')
        self.minus = QPushButton('-')
        self.mul = QPushButton('x')
        self.div = QPushButton('/')
        self.monolog = QPushButton('%')
        self.clear = QPushButton('C')
        self.equal = QPushButton('=')
        self.power = QPushButton('x2')

        layout.addWidget(self.one, 0, 0)
        layout.addWidget(self.two, 0, 1)
        layout.addWidget(self.plus, 0, 2)

        layout.addWidget(self.three, 1, 0)
        layout.addWidget(self.four, 1, 1)
        layout.addWidget(self.minus, 1, 2)

        layout.addWidget(self.five, 2, 0)
        layout.addWidget(self.six, 2, 1)
        layout.addWidget(self.mul, 2, 2)

        layout.addWidget(self.seven, 3, 0)
        layout.addWidget(self.eight, 3, 1)
        layout.addWidget(self.div, 3, 2)

        layout.addWidget(self.nine, 4, 0)
        layout.addWidget(self.zero, 4, 1)
        layout.addWidget(self.monolog, 4, 2)

        layout.addWidget(self.clear, 5, 2)
        layout.addWidget(self.equal, 5, 1)
        layout.addWidget(self.power, 5, 0)

        self.one.clicked.connect(self.click_1)
        self.two.clicked.connect(self.click_2)
        self.three.clicked.connect(self.click_3)
        self.four.clicked.connect(self.click_4)
        self.five.clicked.connect(self.click_5)
        self.six.clicked.connect(self.click_6)
        self.seven.clicked.connect(self.click_7)
        self.eight.clicked.connect(self.click_8)
        self.nine.clicked.connect(self.click_9)
        self.zero.clicked.connect(self.click_0)

        # Add
        self.plus.clicked.connect(self.click_plus)
        
        # Substract
        self.minus.clicked.connect(self.click_minus)

        # Multiply
        self.mul.clicked.connect(self.click_mul)

        # Divide
        self.div.clicked.connect(self.click_div)

        # Show remaining
        self.monolog.clicked.connect(self.click_monolog)

        # Raise power
        self.power.clicked.connect(self.click_double)

        # Show result
        self.equal.clicked.connect(self.show_result)
        
        # Clear input
        self.clear.clicked.connect(self.clear_input)

        self.group.setLayout(layout)


    def keyPressEvent(self, e) -> None:
        key = e.key()
        self.result_done()
        # Number key check
        if key in range(48, 58):
            if self.left_operand:
                if not self.operator:
                    self.x += str(e.text())
                    self.input.setText(self.x)
            else:
                self.y += str(e.text())
                output = f'{self.x} {self.operator} {self.y}'
                self.input.setText(output)

        # Operator check
        if key in [36, 42, 43, 45, 47]:
            self.left_operand = False
            if not self.x:
                self.left_operand = True
            else:
                self.operator = e.text()
                output = f'{self.x} {self.operator} {self.y}'
                self.input.setText(output)

        # Enter key
        if key == 16777221:
            self.show_result()


    def is_preceeding_zero(self):
        # Make sure x or y is not preceeding by 0
        if self.x and self.x[:1] == '0' or self.y and self.y[:1] == '0':
            self.x = self.y = ''
            self.input.setText('0')

        return


    def result_done(self) -> None:
        if self.result_shown:
            self.x = self.y = ''
            self.operator = None
            self.left_operand = True
            self.input.setText('')
        self.result_shown = False


    def clear_input(self):
        self.x = self.y = ''
        self.left_operand = True
        self.input.setText('')
        self.input.setFocus()


    def click_1(self):
        self.result_done()
        if self.left_operand:
            self.x += self.one.text()
            self.input.setText(self.x)
        else:
            self.y += self.one.text()
            output = f'{self.x} {self.operator} {self.y}'
            self.input.setText(output)

        self.is_preceeding_zero()

    
    def click_2(self):
        if self.left_operand:
            self.x += self.two.text()
            self.input.setText(self.x)
        else:
            self.y += self.two.text()
            output = f'{self.x} {self.operator} {self.y}'
            self.input.setText(output)

        self.is_preceeding_zero()


    def click_3(self):
        if self.left_operand:
            self.x += self.three.text()
            self.input.setText(self.x)
        else:
            self.y += self.three.text()
            output = f'{self.x} {self.operator} {self.y}'
            self.input.setText(output)

        self.is_preceeding_zero()


    def click_4(self):
        if self.left_operand:
            self.x += self.four.text()
            self.input.setText(self.x)
        else:
            self.y += self.four.text()
            output = f'{self.x} {self.operator} {self.y}'
            self.input.setText(output)

        self.is_preceeding_zero()


    def click_5(self):
        if self.left_operand:
            self.x += self.five.text()
            self.input.setText(self.x)
        else:
            self.y += self.five.text()
            output = f'{self.x} {self.operator} {self.y}'
            self.input.setText(output)

        self.is_preceeding_zero()


    def click_6(self):
        if self.left_operand:
            self.x += self.six.text()
            self.input.setText(self.x)
        else:
            self.y += self.six.text()
            output = f'{self.x} {self.operator} {self.y}'
            self.input.setText(output)

        self.is_preceeding_zero()


    def click_7(self):
        if self.left_operand:
            self.x += self.seven.text()
            self.input.setText(self.x)
        else:
            self.y += self.seven.text()
            output = f'{self.x} {self.operator} {self.y}'
            self.input.setText(output)

        self.is_preceeding_zero()


    def click_8(self):
        if self.left_operand:
            self.x += self.eight.text()
            self.input.setText(self.x)
        else:
            self.y += self.eight.text()
            output = f'{self.x} {self.operator} {self.y}'
            self.input.setText(output)

        self.is_preceeding_zero()


    def click_9(self):
        if self.left_operand:
            self.x += self.nine.text()
            self.input.setText(self.x)
        else:
            self.y += self.nine.text()
            output = f'{self.x} {self.operator} {self.y}'
            self.input.setText(output)

        self.is_preceeding_zero()


    def click_0(self):
        if self.left_operand:
            self.x += self.zero.text()
            self.input.setText(self.x)
        else:
            self.y += self.zero.text()
            output = f'{self.x} {self.operator} {self.y}'
            self.input.setText(output)


    def click_plus(self) -> None:
        self.left_operand = False
        if self.x:
            self.operator = self.plus.text()
            output = f'{self.x} {self.operator} {self.y}'
            self.input.setText(output)


    def click_minus(self) -> None:
        self.left_operand = False
        if self.x:
            self.operator = self.minus.text()
            output = f'{self.x} {self.operator} {self.y}'
            self.input.setText(output)

    
    def click_mul(self) -> None:
        self.left_operand = False
        if self.x:
            self.operator = self.mul.text()
            output = f'{self.x} {self.operator} {self.y}'
            self.input.setText(output)

    
    def click_div(self) -> None:
        self.left_operand = False
        if self.x:
            self.operator = self.div.text()
            output = f'{self.x} {self.operator} {self.y}'
            self.input.setText(output)


    def click_monolog(self) -> None:
        self.left_operand = False
        if self.x:
            self.operator = self.monolog.text()
            output = f'{self.x} {self.operator} {self.y}'
            self.input.setText(output)


    def click_double(self) -> None:
        try:
            if self.x and not self.operator and not self.y:
                output = float(self.x)**2
                self.x = str(output)
                self.input.setText(self.x)

            if self.result:
                self.result = self.result ** 2
                self.input.setText(str(self.result))
        except (OverflowError) as e:
            QMessageBox.critical(None, 'OverflowError', str(e))

    def add(self, x: float, y: float) -> float:
        return x + y
        

    def substract(self, x: float, y: float) -> float:
        return x - y


    def multiply(self, x: float, y: float) -> float:
        return x * y


    def divide(self, x: float, y: float) -> float:
        z = 0
        try:
            z = x / y
        except (ZeroDivisionError):
            QMessageBox.critical(None, 'Zerro Division Error', 'Zero cannot be divided')
        return z


    def mono(self, x: float, y: float) -> float:
        return x % y


    def show_result(self) -> None:
        if not self.x or not self.y or not self.operator: return

        x = float(self.x)
        y = float(self.y)
        output = ''
        if self.operator == '+':
            output = self.add(x, y)

        if self.operator == '-':
            output = self.substract(x, y)

        if self.operator == 'x':
            output = self.multiply(x, y)

        if self.operator == '/':
            output = self.divide(x, y)

        if self.operator == '%':
            output = self.mono(x, y)

        self.input.setText(str(output))
        self.result = output
        self.result_shown = True


if __name__ == '__main__':
    import sys

    app = QApplication([])
    cal = Calculator()
    cal.show()
    sys.exit(app.exec())
