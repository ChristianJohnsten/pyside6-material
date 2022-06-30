# pyside6-material
Material design for PySide6 (forked from asztalosdani/pyqt4-material and updated to PySide6)

##Example.py
###Light Mode
[![Light Mode](https://github.com/chrisddr77/pyside6-material/blob/master/img/example_1.jpg?raw=true "Light Mode")](https://github.com/chrisddr77/pyside6-material/blob/master/img/example_1.jpg "Light Mode")

###Dark Mode
[![Dark Mode](https://github.com/chrisddr77/pyside6-material/blob/master/img/example_2.jpg?raw=true "Dark Mode")](https://github.com/chrisddr77/pyside6-material/blob/master/img/example_2.jpg "Dark Mode")



#Usage
##Standard
```python
import sys
from PySide6 import QtGui, QtCore, QtWidgets

from pyside6_material import material as mt
from pyside6_material.material_shadow import MaterialShadowEffect
from pyside6_material.shadow import CustomShadowEffect

class Example(mt.MainWindow):
    def __init__(self):
        mt.MainWindow.__init__(self)

        main_layout = QtWidgets.QVBoxLayout()

        main_layout.addWidget(mt.RaisedButton('BUTTON 1'))
        main_layout.addWidget(mt.RaisedButton('BUTTON 2'))
        main_layout.addWidget(mt.RaisedButton('BUTTON 3'))

        main_widget = QtWidgets.QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    QtGui.QFontDatabase.addApplicationFont(r'.\Roboto\Roboto.ttf')
    font = QtGui.QFont("Roboto")
    font.setBold(True)
    app.setFont(font)
    app.setProperty(mt.PROPERTY_THEME, mt.THEME_LIGHT)
	#app.setProperty(mt.PROPERTY_THEME, mt.THEME_DARK)
    app.setProperty(mt.PROPERTY_PRIMARY_COLOR, "#2196f3")
    app.setProperty(mt.PROPERTY_SECONDARY_COLOR, "#68efad")

    window = Example()  # Your class that inherits mt.MainWindow
    window.show()

    sys.exit(app.exec())
```

## Bare-minimum
```python
import sys
from PySide6 import QtGui, QtCore, QtWidgets

from pyside6_material import material as mt
from pyside6_material.material_shadow import MaterialShadowEffect
from pyside6_material.shadow import CustomShadowEffect

class Example(mt.MainWindow):
    def __init__(self):
        mt.MainWindow.__init__(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    app.setProperty(mt.PROPERTY_THEME, mt.THEME_LIGHT)
    app.setProperty(mt.PROPERTY_PRIMARY_COLOR, "#2196f3")
    app.setProperty(mt.PROPERTY_SECONDARY_COLOR, "#68efad")

    window = Example()  # Your class that inherits mt.MainWindow
    window.show()

    sys.exit(app.exec())
```


#
