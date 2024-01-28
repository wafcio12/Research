from dataclasses import dataclass
from typing import Callable


@dataclass
class KaplanParameters:
    featureColumn: str
    timeColumn: str
    extract: Callable[[str], str]


config = {
    "OS": KaplanParameters(
        "OS_STATUS",
        "OS_MONTHS",
        lambda value: (
            "1" if value == "0:LIVING" else
            "0" if value == "1:DECEASED" else
            "UNKNOWN"
        )
    )
}
