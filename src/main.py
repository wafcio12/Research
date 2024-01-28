from pathlib import Path

import pandas as pd
from src.readdata.read_excel import read_excel


path = Path(r'C:\Users\Virtu\OneDrive\PYTONG projekty\Dane TCGA\BRCA\PanCancer BRCA - expresja (tumor); klinika; próbki TCGA normal (zmatchowane do nowotworowych).xlsx')
brca_df = read_excel(path, "brca", "Expression (tumor) PanCancer ")
