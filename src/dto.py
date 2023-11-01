from dataclasses import dataclass
from typing import List

from pandas import DataFrame


@dataclass
class ResearchData:
    expressions: DataFrame
    features: DataFrame
    availableGenes: List[str]
    patients: List[str]
