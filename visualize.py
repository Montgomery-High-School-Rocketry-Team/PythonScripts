import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
df = df.astype(float)

fig = make_subplots(rows=3, cols=3)

fig.add_trace(
    go.Scatter(
        x=df["#time"], y=df["vel"], mode="lines", name="time vs velocity (integration)"
    ),
    row=1,
    col=1,
)

fig.add_trace(
    go.Scatter(x=df["#time"], y=df["alt"], mode="lines", name="time vs alt"),
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
    go.Scatter(x=df["#time"], y=df["az"], mode="lines", name="time vs az"),
    row=2,
    col=3,
)


fig.add_trace(
    go.Scatter(x=df["#time"], y=df["dumb1"], mode="lines", name="time vs dummy1"),
    row=3,
    col=3,
)
fig.add_trace(
    go.Scatter(x=df["#time"], y=df["dumb2"], mode="lines", name="time vs dummy2"),
    row=3,
    col=1,
)
fig.add_trace(
    go.Scatter(x=df["#time"], y=df["dumb3"], mode="lines", name="time vs dummy3"),
    row=1,
    col=2,
)


fig.update_layout(title_text="Subplots")
fig.show()


# df["ay"].plot()
# plt.show()
