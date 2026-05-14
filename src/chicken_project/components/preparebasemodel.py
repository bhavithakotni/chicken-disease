import os
import tensorflow as tf

from src.chicken_project.entity.config_entity import DataIngestionConfig,PrepareBaseModelConfig
from pathlib import Path


class PrepareBaseModel:
    def __init__(self,config:PrepareBaseModelConfig):
        self.config=config
 

    def get_basemodel(self):
        self.model=tf.keras.applications.vgg16.VGG16(
        input_shape= self.config.params_imagesize,
        weights= self.config.params_weights,
        include_top=self.config.params_include_top
    )
        self.save_model(path=self.config.basemodel,model=self.model)
    @staticmethod
    def preparefullmodel(model,classes,freeze_all,freeze_till,learning_rate):
        if freeze_all:
            for layer in model.layers:
                model.trainable=False
        elif(freeze_till is not None ) and (freeze_till > 0):
           for layer in model.layer[: -freeze_till]:
                model.trainable=False
        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units = classes,
            activation ="softmax")(flatten_in)
        full_model= tf.keras.Model(inputs=model.input,outputs=prediction)
        full_model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),loss=tf.keras.losses.CategoricalCrossentropy(),metrics=["accuracy"])
        full_model.summary()
        return full_model
    def update_basemodel(self):
        self.full_model = self.preparefullmodel(model=self.model,
                                            classes=self.config.params_classes,
                                            freeze_all=True,freeze_till=None,
                                            learning_rate=self.config.params_learning_rate)
        self.save_model(path=self.config.updated_basemodel,model=self.full_model)
    @staticmethod
    def save_model(path: Path,model: tf.keras.Model):
        model.save(path)
