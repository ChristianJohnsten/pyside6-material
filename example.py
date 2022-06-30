import sys
from PySide6 import QtGui, QtCore, QtWidgets

import material
from material_shadow import MaterialShadowEffect
from shadow import CustomShadowEffect


class Example(material.MainWindow):
    def __init__(self):
        material.MainWindow.__init__(self)

        self._init_ui()
        self._create_menu()

    def _init_ui(self):
        tab = material.TabWidget()
        self.setCentralWidget(tab)

        tab.addTab(self._create_page1(), "Page1")
        tab.addTab(self._create_page2(), "Page2")
        tab.addTab(self._create_page3(), "Page3")
        tab.setCurrentIndex(0)

        self.setMinimumSize(300, 600)

    def _create_page1(self):
        main_layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("Tooltip here")
        label.setToolTip("This is a tooltip")
        main_layout.addWidget(label)

        dropdown_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(dropdown_layout)
        dropdown = material.Dropdown()
        dropdown.addItems(["Option{}".format(i + 1) for i in range(10)])
        dropdown_layout.addWidget(dropdown)
        dropdown_layout.addStretch()

        main_layout.addWidget(QtWidgets.QCheckBox('CheckBox'))
        text_field1 = material.TextField('Sajtoskorte')
        text_field2 = material.TextField('Disabled')
        text_field2.setDisabled(True)
        main_layout.addWidget(text_field1)
        main_layout.addWidget(text_field2)

        slider_h1 = material.Slider(QtCore.Qt.Horizontal)
        slider_h1.setValue(40)
        slider_h2 = material.Slider(QtCore.Qt.Horizontal)
        slider_h2.setValue(30)
        slider_h2.setDisabled(True)
        h_slider_layout = QtWidgets.QVBoxLayout()
        h_slider_layout.addWidget(slider_h1)
        h_slider_layout.addWidget(slider_h2)

        slider_v1 = material.Slider(QtCore.Qt.Vertical)
        slider_v1.setValue(100)
        slider_v2 = material.Slider(QtCore.Qt.Vertical)
        slider_v2.setValue(30)
        slider_v2.setDisabled(True)

        slider_layout = QtWidgets.QHBoxLayout()
        slider_layout.addLayout(h_slider_layout)
        slider_layout.addWidget(slider_v1)
        slider_layout.addWidget(slider_v2)
        slider_layout.addStretch()
        main_layout.addLayout(slider_layout)

        main_layout.addStretch()

        button_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(button_layout)

        button_layout.addStretch()
        button_layout.addWidget(material.RaisedButton('BUTTON1'))
        button2 = material.RaisedButton('BUTTON2')
        button2.setDisabled(True)
        button_layout.addWidget(button2)
        button_layout.addWidget(material.RaisedButton('BUTTON3'))

        button_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(button_layout)

        button_layout.addStretch()
        button_layout.addWidget(material.FlatButton('FLAT1'))
        button2 = material.FlatButton('FLAT2')
        button2.setDisabled(True)
        button_layout.addWidget(button2)

        page = QtWidgets.QWidget()
        page.setLayout(main_layout)
        return page

    def _create_page2(self):
        main_layout = QtWidgets.QVBoxLayout()

        table = material.TableView()
        main_layout.addWidget(table)
        table.setModel(ExampleTableModel())

        page = QtWidgets.QWidget()
        page.setLayout(main_layout)
        return page

    def _create_page3(self):
        main_layout = QtWidgets.QVBoxLayout()

        card1 = material.Card()
        main_layout.addWidget(card1)

        card1.add_title("Title goes here")
        card1.add_subtitle("Subtitle here")
        image = QtGui.QPixmap("test_image1.jpeg")
        card1.add_image(image.scaled(400, 500, QtCore.Qt.KeepAspectRatio))
        card1.add_supporting_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
        card1.add_actions([material.FlatButton("action 1"), material.FlatButton("action 2")])

        card2 = material.Card()
        main_layout.addWidget(card2)

        card2.add_title("Title goes here")
        card2.add_subtitle("Subtitle here")
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum leo id imperdiet porttitor. In cursus mauris vitae enim eleifend facilisis. Quisque eu ex sit amet elit rutrum facilisis non a tellus. Ut nulla leo, tristique in aliquam pulvinar, blandit vel ex. Morbi feugiat sem eu tortor facilisis commodo. Donec eu ullamcorper dui. Donec dictum diam non mauris vulputate, pellentesque lobortis turpis fringilla. Fusce vitae urna sapien. Aliquam aliquet tellus sapien. Suspendisse dapibus lectus tellus."
        card2.add_supporting_text(text)

        card3 = material.Card()
        main_layout.addWidget(card3)

        card3.add_title("Title goes here")
        card3.add_subtitle("Subtitle here")
        card3.add_actions([material.FlatButton("action 1"), material.FlatButton("action 2")], direction=material.Card.DIRECTION_VERTICAL)

        main_layout.addStretch()

        page = QtWidgets.QWidget()
        page.setLayout(main_layout)
        page.setMaximumWidth(400)
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setWidget(page)
        return scroll_area

    def _create_menu(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(QtGui.QAction('Option 1', self))
        file_menu.addAction(QtGui.QAction('Option 2', self))
        file_menu.addAction(QtGui.QAction('Option 3', self))

        sub_menu = file_menu.addMenu('Sub menu')
        sub_menu.addAction(QtGui.QAction('Sub Option 1', self))
        sub_menu.addAction(QtGui.QAction('Sub Option 2', self))
        sub_menu.addAction(QtGui.QAction('Sub Option 3', self))


class ExampleTableModel(QtCore.QAbstractTableModel):
    def rowCount(self, parent):
        return 5

    def columnCount(self, parent):
        return 4

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            return "alma"


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont(r'd:\python_projects\material_test\Roboto\Roboto-Regular.ttf')
    app.setFont(QtGui.QFont("Roboto"))
    app.setProperty(material.PROPERTY_THEME, material.THEME_LIGHT)
    app.setProperty(material.PROPERTY_PRIMARY_COLOR, "#2196f3")
    app.setProperty(material.PROPERTY_SECONDARY_COLOR, "#68efad")

    win = Example()
    win.show()
    sys.exit(app.exec_())
