from pathlib import Path

import pandas as pd

from src.readdata.datasets import readBrca
from src.readdata.read_excel import read_excel

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

df1.columns.values[0] = 'value'
df2.columns.values[0] = 'value'

merge = pd.concat([df1, df2], ignore_index=True)

merge['value'] = np.log2(merge['value'] + 1)


fig = px.violin(merge, y="value", color="status", box=True, points='all',
          hover_data=merge.columns)
                #range_y=[-100, 700])
fig.show()


