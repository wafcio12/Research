from dataclasses import dataclass
from typing import Callable

from src.cox.cox_datasets_configuration import config, CoxParameters
from src.dto import ResearchData
from src.readdata.datasets import Dataset, dataset
from lifelines import KaplanMeierFitter, CoxPHFitter
import matplotlib.pyplot as plt
import matplotlib

# matplotlib.use('TkAgg')

research_data = dataset(Dataset.BRCA)
genes = ['SPC25', 'ANLN', 'KPNA2', 'SLC7A5']
cox_parameters = config["OS"]


def cox(research_data: ResearchData, genes: list[str], cox_parameters: CoxParameters):
    geneData = research_data.expressions[genes]
    features = research_data.features[[cox_parameters.featureColumn, cox_parameters.timeColumn]]
    features = features.rename(columns={cox_parameters.featureColumn: "outcomeRaw", cox_parameters.timeColumn: "time"})
    features["outcome"] = features["outcomeRaw"].map(cox_parameters.extract)
    features["outcome"] = features["outcome"].map(lambda e: float(e))
    features["outcome"] = features["outcome"].map(lambda e: 0 if e == 1 else 1)

    data = features[['outcome', 'time']].join(geneData)

    fitter = CoxPHFitter()
    fitter.fit(data, duration_col="time", event_col="outcome")
    fitter.print_summary()

    pass
