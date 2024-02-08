import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

fig = px.line(df, x="#time", y="ax", title="time vs vel")
fig.show()

figg = px.line(df, x="#time", y="ay", title="time vs ax")
figg.show()
figgg = px.line(df, x="#time", y="az", title="time vs ax")
figgg.show()
