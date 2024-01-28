from pathlib import Path

import pandas as pd

from src.readdata.datasets import readBrca
from src.readdata.read_excel import read_excel
from src.violinplotfunction import violin_plot_gene

data = readBrca()

#violin plots

import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = data.expressions[['ZNF695', 'ZNF695-norm']]
df1 = df[['ZNF695']]
df1['status'] = 'cancer'
df2 = df[['ZNF695-norm']]
df2['status'] = 'normal'

df1.columns.values[0] = 'Expression Log2'
df2.columns.values[0] = 'Expression Log2'

merge = pd.concat([df1, df2], ignore_index=True)

merge['Expression Log2'] = np.log2(merge['Expression Log2'] + 1)


fig = px.violin(merge, y="Expression Log2", color="status", box=True, points='all',
          hover_data=merge.columns)
                #range_y=[-100, 700])

fig.update_layout(
            title={
            'text' : "ZNF695",
            'x':0.5,
            'xanchor': 'center'
        })

fig.show()

from src.violinplotfunction import violin_plot_gene
violin_plot_gene(data, "MYBL2")
