from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    local_data_file:Path

    
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    basemodel: Path
    updated_basemodel: Path
    params_imagesize: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int
