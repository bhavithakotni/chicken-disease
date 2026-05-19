from src import logger
from src.chicken_project.pipeline.stage_01dataingestion import DataIngestionPipeline
from src.chicken_project.pipeline.stage_02preparebasemodel import PrepareBaseModelpipeline 
from src.chicken_project.pipeline.training import ModelTrainingpipeline 
from src.chicken_project.pipeline.evaluation import EvaluationPipeline 



stage_name= "data ingestion stage"

try:
    logger.info(f">>>>>>stage{stage_name}started<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>stage{stage_name} completed<<<")
except Exception as e:
    logger.exception(e)
    raise e    

stage_name= "prepare base model"

try:
    logger.info(f">>>>>>stage{stage_name}started<<<<<<")
    obj = PrepareBaseModelpipeline()
    obj.main()
    logger.info(f">>>>>>stage{stage_name} completed<<<<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e  
 
stage_name="Training"
try:
    logger.info(f">>>>>>stage{stage_name}started<<<<<<")
    obj = ModelTrainingpipeline()
    obj.main()
    logger.info(f">>>>>>stage{stage_name} completed<<<<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e     
stage_name="evaluation stage"
try:
    logger.info(f">>>>>>stage{stage_name}started<<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>stage{stage_name} completed<<<<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e