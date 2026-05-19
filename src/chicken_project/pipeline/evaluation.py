from src.chicken_project.config.configuration import ConfigurationManager
from src.chicken_project.components.evaluation import Evaluation
from src import logger

stage_name= "evaluation stage"

class EvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        val_config=config.get_validation_config()
        evaluation=Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>stage{stage_name}started<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>stage{stage_name} completed<<<<<<\n\nx===============x")
    except Exception as e:
        logger.exception(e)
        raise e