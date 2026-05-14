from src.chicken_project.config.configuration import ConfigurationManager
from src.chicken_project.components.preparebasemodel import PrepareBaseModel
from src.chicken_project.components.dataingestion import DataIngestion
from src import logger

stage_name= "PrepareBaseModel"

class PrepareBaseModelpipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        prepareBaseModelConfig=config.get_PrepareBaseModelConfig()
        prepareBaseModel=PrepareBaseModel(config=prepareBaseModelConfig)
        prepareBaseModel.get_basemodel()
        prepareBaseModel.update_basemodel()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>stage{stage_name}started<<<<<<")
        obj = PrepareBaseModelpipeline()
        obj.main()
        logger.info(f">>>>>>stage{stage_name} completed<<<<<<\n\nx===============x")
    except Exception as e:
        logger.exception(e)
        raise e
