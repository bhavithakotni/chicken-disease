import os
import tensorflow as tf
from src.chicken_project.entity.config_entity import DataIngestionConfig,PrepareBaseModelConfig,EvaluationConfig
from pathlib import Path
from src.chicken_project.utils.common import read_yaml,create_directories,save_json
class Evaluation:
    def __init__(self,config:EvaluationConfig):
        self.config=config
    def _valid_generator(self):
        datagenerator_kwargs= dict(rescale= 1./255,
                                   validation_split= 0.20)
        dataflow_kwargs= dict(target_size= self.config.params_imagesize[:-1],
                              batch_size= self.config.params_batch_size,
                              interpolation= "bilinear")
        valid_datagenerator= tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs)
        self.valid_genetator=valid_datagenerator.flow_from_directory(directory= self.config.training_data,
                                                                     subset="validation",
                                                                     shuffle=False,
                                                                     **dataflow_kwargs)
    @staticmethod
    def load_model(path:Path)->tf.keras.Model:
        return tf.keras.models.load_model(path)
    def evaluation(self):
        self.model= self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score=self.model.evaluate(self.valid_genetator)
    def save_score(self):
        scores={"loss": self.score[0],"accuracy":self.score[1]}
        save_json(path=Path("score.json"),data=scores)