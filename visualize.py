import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_csv("data.csv")


fig = make_subplots(rows=3, cols=3)

fig.add_trace(
    go.Scatter(x=df["#time"], y=df["vel"], mode="lines", name="time vs velocity"),
    row=1,
    col=1,
)
fig.add_trace(
    go.Scatter(x=df["#time"], y=df["alt"], mode="lines", name="time vs alt"),
    row=1,
    col=2,
)
fig.add_trace(
    go.Scatter(x=df["#time"], y=df["press"], mode="lines", name="time vs pressure"),
    row=1,
    col=3,
)


fig.add_trace(
    go.Scatter(x=df["#time"], y=df["ax"], mode="lines", name="time vs ax"),
    row=2,
    col=1,
)
fig.add_trace(
    go.Scatter(x=df["#time"], y=df["ay"], mode="lines", name="time vs ay"),
    row=2,
    col=2,
)
fig.add_trace(
    go.Scatter(x=df["#time"], y=df["ay"], mode="lines", name="time vs az"),
    row=2,
    col=3,
)
fig.add_trace(
    go.Scatter(x=df["#time"], y=df["a"], mode="lines", name="time vs a"),
    row=3,
    col=1,
)


fig.update_layout(title_text="Subplots")
fig.show()
