import numpy
from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets
import pandas
import plotly.express as px


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QtWidgets.QPushButton('Plot', self)
        self.browser = QtWebEngineWidgets.QWebEngineView(self)

        vlayout = QtWidgets.QVBoxLayout(self)
        vlayout.addWidget(self.button, alignment=QtCore.Qt.AlignHCenter)
        vlayout.addWidget(self.browser)

        self.button.clicked.connect(self.show_graph)
        self.resize(1000, 800)

    def show_graph(self):
        numpy.random.seed(33)
        normal_data_a = numpy.random.normal(size=500, loc=100, scale=10)
        normal_data_b = numpy.random.normal(size=700, loc=75, scale=5)

        df_normal_a = pandas.DataFrame(data=normal_data_a, columns=['score']).assign(group='Group A')
        df_normal_b = pandas.DataFrame(data=normal_data_b, columns=['score']).assign(group='Group B')

        score_data = pandas.concat([df_normal_a, df_normal_b])

        fig = px.histogram(
            data_frame=score_data,
            x="score"
        )

        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Widget()
    widget.show()
    app.exec()
