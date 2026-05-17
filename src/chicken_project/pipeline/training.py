from src.chicken_project.config.configuration import ConfigurationManager
from src.chicken_project.components.preparecallbacks import PrepareCallbacks

from src.chicken_project.components.training import Training
from src import logger


stage_name="Training"
class ModelTrainingpipeline:
    def __init__(self):
        pass
    def main(self):
        config= ConfigurationManager()
        PrepareCallbacks_config= config.get_Preparecallbacksconfig()
        prepare_Callbacks= PrepareCallbacks(config= PrepareCallbacks_config)
        callback_list= prepare_Callbacks.get_tb_ckpt_callbacks
    
        training_config=config.get_trainingconfig()
        training= Training(config=training_config)
        training.get_basemodel()
        training.train_valid_generator()
        training.train(callback_list=callback_list)
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>stage{stage_name}started<<<<<<")
        obj = ModelTrainingpipeline()
        obj.main()
        logger.info(f">>>>>>stage{stage_name} completed<<<<<<\n\nx===============x")
    except Exception as e:
        logger.exception(e)
        raise e
