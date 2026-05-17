from src import logger
from src.chicken_project.utils.common import get_size
import tensorflow as tf
import time
import os
from src.chicken_project.entity.config_entity import PrepareCallbacksConfig


class PrepareCallbacks:
    def __init__(self,config:PrepareCallbacksConfig):
        self.config=config
    @property
    def create_callbacks(self):
        timestamp = time.strftime("%y-%m-%d-%H-%M-%S")
        tb_running_log_dir= os.path.join(self.config.tensorboard_dir,f"tb logs_at{timestamp}",)
        return tf.keras.callbacks.TensorBoard(log_dir= tb_running_log_dir)
    @property
    def create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(filepath=str(self.config.checkpoint_filepath),
                                                  save_best_only=True)
    @property
    def get_tb_ckpt_callbacks(self):
        return [
            self.create_callbacks,
            self.create_ckpt_callbacks
        ]