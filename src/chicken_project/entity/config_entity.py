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

@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir:Path
    tensorboard_dir: Path
    checkpoint_filepath: Path

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    training_model_path: Path
    updated_basemodel: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_augmentation: bool
    params_imagesize: list
    params_learning_rate: float
