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
    name = "BRCA do WGCNA.xlsx"
    set_name = "set_1"
    features = read_excel(get_path(set_name, name), set_name, "clinical data patient")
    features.set_index("PATIENT_ID", inplace=True)
    expressions = read_excel(get_path(set_name, name), set_name, "expression")
    expressions.set_index("Hugo_Symbol", inplace=True)
    expressions = expressions.T
    expressions.index = expressions.index.map(lambda idx: idx.removesuffix("-01"))

    genes = expressions.columns.tolist()

    _ensure_matching_indices(features, expressions)

    patients = features.index.tolist()

    return ResearchData(
        expressions,
        features,
        genes,
        patients
    )
