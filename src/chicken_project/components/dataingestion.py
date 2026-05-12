import os
from src import logger
from src.chicken_project.utils.common import get_size
from src.chicken_project.entity.config_entity import DataIngestionConfig 
from pathlib import Path
class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config