import sys
from  model import evaluateExpression

from PyQt5.QtWidgets import QApplication
from view import GUI

# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)

    model = evaluateExpression
    # Show the calculator's GUI
    view = GUI()
    view.show()

    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()