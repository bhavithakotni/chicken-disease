from src.chicken_project.config.configuration import ConfigurationManager
from src.chicken_project.components.dataingestion import DataIngestion
from src import logger

stage_name= "data ingestion stage"

class DataIngestionPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        dataingestion_config = config.get_dataingestion_config()
        dataingestion = DataIngestion(config=dataingestion_config)



if __name__ == "__main__":
    try:
        logger.info(f">>>>>>stage{stage_name}started<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>stage{stage_name} completed<<<<<<\n\nx===============x")
    except Exception as e:
        logger.exception(e)
        raise e
