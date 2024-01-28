from lifelines import CoxPHFitter, KaplanMeierFitter


from src.dto import ResearchData
from src.kaplan.kaplan_datasets_configuration import KaplanParameters, config
from src.readdata.datasets import Dataset, dataset
import matplotlib.pyplot as plt
# matplotlib.use('TkAgg')

research_data = dataset(Dataset.BRCA)
genes = ['SPC25', 'ANLN', 'KPNA2', 'SLC7A5']
parameters = config["OS"]


def kaplan(research_data: ResearchData, genes: list[str], parameters: KaplanParameters):
    geneData = research_data.expressions[genes]

    values = geneData.iloc[:, :].median(axis=1)

    features = research_data.features[[parameters.featureColumn, parameters.timeColumn]]
    features = features.rename(columns={parameters.featureColumn: "outcomeRaw", parameters.timeColumn: "time"})
    features["outcome"] = features["outcomeRaw"].map(parameters.extract)
    features["outcome"] = features["outcome"].map(lambda e: float(e))
    features["outcome"] = features["outcome"].map(lambda e: True if e == 1 else False)



    data = features[['outcome', 'time']].join(values.rename("value"))

    fitter = KaplanMeierFitter()
    fitter.fit(data['time'], data['outcome'])
    fitter.plot_survival_function()

    plt.clf()
    plt.show()

    pass
