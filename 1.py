import csv
import pandas as pd
import plotly.express as px
def plotfig():
    file = "C:/Users/iliea/OneDrive/Desktop/Code/Python/Hw/HW103/Copy+of+data+-+data.csv"
    with open(file) as csvFile:
        df = csv.DictReader(csvFile)
        scatterPlot = px.scatter(df,x = "cases",y = "country")
        scatterPlot.show()
plotfig()