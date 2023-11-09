from pathlib import Path
from typing import Dict

import pandas as pd

from src.dto import ResearchData
from src.readdata.read_excel import read_excel
from enum import Enum

dir = "data"


class Dataset(Enum):
    BRCA = 1


def get_path(set: str, name: str) -> Path:
    return Path("../data/" + set + "/" + name)


def _ensure_matching_indices(df1: pd.DataFrame, df2: pd.DataFrame):
    df1Indices = set(df1.index.tolist())
    df2Indices = set(df2.index.tolist())
    patientsDiff = df1Indices.difference(df2Indices)

    df1.drop(index=df1.index.intersection(list(patientsDiff)), inplace=True)
    df2 = df2.drop(index=df2.index.intersection(list(patientsDiff)), inplace=True)


_datasets: Dict[Dataset, ResearchData] = {}


def _init():
    global _datasets
    _datasets = {}


def dataset(dataset: Dataset):
    if not dataset in _datasets:
        _datasets[dataset] = readBrca()

    return _datasets[dataset]


def readBrca() -> ResearchData:
    set_name = "BRCA"
    features = read_excel(Path(r"C:\Users\klaud\OneDrive\PYTONG projekty\Dane TCGA\BRCA\PanCancer BRCA - expresja (tumor); klinika; próbki TCGA normal (zmatchowane do nowotworowych).xlsx"), set_name, 'Patient clinic')
    features.set_index("PATIENT_ID", inplace=True)
    features.index = features.index.map(lambda idx: idx.removesuffix("-01"))

    expressions = read_excel(Path(r"C:\Users\klaud\OneDrive\PYTONG projekty\Dane TCGA\BRCA\PanCancer BRCA - expresja (tumor); klinika; próbki TCGA normal (zmatchowane do nowotworowych).xlsx"), set_name, 'Expression (tumor) PanCancer ')
    expressions.set_index(expressions.columns[0], inplace=True)
    expressions = expressions.T
    expressions.index = expressions.index.map(lambda idx: idx.removesuffix("-01"))
    expressions = expressions.sort_index()



    expressions_normal = read_excel(Path(r"C:\Users\klaud\OneDrive\PYTONG projekty\Dane TCGA\BRCA\PanCancer BRCA - expresja (tumor); klinika; próbki TCGA normal (zmatchowane do nowotworowych).xlsx"), set_name, 'Expression (normals) PanCancer ')
    expressions_normal.set_index(expressions_normal.columns[0], inplace=True)
    expressions_normal = expressions_normal.T
    expressions_normal.index = expressions_normal.index.map(lambda idx: idx.removesuffix("-11"))
    expressions_normal = expressions_normal.sort_index()
    expressions_normal = expressions_normal.add_suffix('-norm')

    expressions_merged = expressions.join(expressions_normal, how='left')

    genes = expressions.columns.tolist()

    _ensure_matching_indices(features, expressions)

    patients = features.index.tolist()

    return ResearchData(
        expressions_merged,
        features,
        genes,
        patients
    )
