from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets
import pandas
import plotly.graph_objects


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
        df = pandas.read_csv("Binance_ETHUSDT_1m_2022_spot.csv")
        df['date'] = pandas.to_datetime(df["timestamp"], unit="ms")
        df = df.iloc[0:1000]
        fig = plotly.graph_objects.Figure(
            data=[
                plotly.graph_objects.Candlestick(
                    x=df["date"],
                    open=df["open"],
                    high=df["high"],
                    low=df["low"],
                    close=df["close"],
                )
            ]
        )
        # fig.update_traces(quartilemethod="exclusive")
        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Widget()
    widget.show()
    app.exec()
