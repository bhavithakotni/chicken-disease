from src.chicken_project.constant import *
import os
from pathlib import Path
from src.chicken_project.utils.common import read_yaml,create_directories
from src.chicken_project.entity.config_entity import DataIngestionConfig,PrepareBaseModelConfig,PrepareCallbacksConfig,TrainingConfig,EvaluationConfig



class ConfigurationManager:
    def __init__(self,config_filepath=config_file_path,
                 params_filepath=params_file_path):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        create_directories([self.config.artifacts_roots])

    def get_dataingestion_config(self)->DataIngestionConfig:
        config=self.config.dataingestion
        create_directories([config.root_dir])
        dataingestion_config=DataIngestionConfig(root_dir=config.root_dir,
                                                 local_data_file=config.local_data_file)
        return dataingestion_config
    def get_PrepareBaseModelConfig(self)->PrepareBaseModelConfig:
        config=self.config.prepareBaseModel
        create_directories([config.root_dir])
        PreparebasemodelConfig= PrepareBaseModelConfig(root_dir= Path(config.root_dir),
                                                       basemodel= Path(config.basemodel),
                                                       updated_basemodel= Path(config.updated_basemodel),
                                                       params_imagesize= self.params.imagesize,
                                                       params_learning_rate= self.params.learning_rate,
                                                       params_include_top= self.params.include_top,
                                                       params_weights= self.params.weights,
                                                       params_classes= self.params.classes)
        
        return PreparebasemodelConfig
    

    def get_Preparecallbacksconfig(self)->PrepareCallbacksConfig:
        config=self.config.preparecallbacks
        model_ckpt_dir= os.path.dirname(config.checkpoint_filepath)
        create_directories([Path(model_ckpt_dir),Path(config.tensorboard_dir)])
        Preparecallbacksconfig= PrepareCallbacksConfig(root_dir= Path(config.root_dir),
                                                       tensorboard_dir= Path(config.tensorboard_dir),
                                                       checkpoint_filepath= Path(config.checkpoint_filepath))
        return  Preparecallbacksconfig
    
    def get_trainingconfig(self)->TrainingConfig:
        training= self.config.training
        preparebasemodel= self.config.prepareBaseModel
        params= self.params
        training_data= os.path.join(self.config.dataingestion.local_data_file)
        create_directories([Path(training.root_dir)])

        trainingconfig= TrainingConfig(root_dir= Path(training.root_dir),
                                       training_model_path= Path(training.training_model_path),
                                       updated_basemodel= Path(preparebasemodel.updated_basemodel),
                                       training_data= Path( training_data),
                                       params_epochs= params.epochs,
                                       params_batch_size= params.batch_size,
                                       params_augmentation= params.augmentation,
                                       params_imagesize= params.imagesize,
                                       params_learning_rate= params.learning_rate
        )
        return trainingconfig
    def get_validation_config(self)->EvaluationConfig:
        eval_config=EvaluationConfig(path_of_model=Path("artifacts/training/model.h5"),
                                     training_data=Path("artifacts/dataingestion/chickendata"),
                                     all_params=self.params,
                                     params_imagesize=self.params.imagesize,
                                     params_batch_size=self.params.batch_size)
        return eval_config