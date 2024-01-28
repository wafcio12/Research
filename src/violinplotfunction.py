from src.dto import ResearchData
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def violin_plot_gene(data: ResearchData, geneName: str):
    df = data.expressions[[geneName, geneName + '-norm']]
    df1 = df[[geneName]]
    df1['status'] = 'cancer'
    df2 = df[[geneName + '-norm']]
    df2['status'] = 'normal'

    df1.columns.values[0] = 'Expression Log2'
    df2.columns.values[0] = 'Expression Log2'

    merge = pd.concat([df1, df2], ignore_index=True)

    merge['Expression Log2'] = np.log2(merge['Expression Log2'] + 1)

    fig = px.violin(merge, y="Expression Log2", color="status", box=True, points='all',
                    hover_data=merge.columns)
    # range_y=[-100, 700])

    fig.update_layout(
        title={
            'text': geneName,
            'x': 0.5,
            'xanchor': 'center'
        })

    fig.show()
