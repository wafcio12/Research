from dataclasses import dataclass
from typing import Callable


@dataclass
class CoxParameters:
    featureColumn: str
    timeColumn: str
    extract: Callable[[str], str]


config = {
    "OS": CoxParameters(
        "OS_STATUS",
        "OS_MONTHS",
        lambda value: (
            "1" if value == "0:LIVING" else
            "0" if value == "1:DECEASED" else
            "UNKNOWN"
        )
    )
}
