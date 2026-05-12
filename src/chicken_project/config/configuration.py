from src.chicken_project.constant import *
from src.chicken_project.utils.common import read_yaml,create_directories
from src.chicken_project.entity.config_entity import DataIngestionConfig
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