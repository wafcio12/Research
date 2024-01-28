import plotly.express as px

df = px.data.tips()
fig = px.violin(df, y="total_bill", box=True, points='all')
fig.show()
