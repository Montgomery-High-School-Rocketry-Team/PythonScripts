import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

fig = px.line(df, x="#time", y="vel", title="time vs alt")
fig.show()
