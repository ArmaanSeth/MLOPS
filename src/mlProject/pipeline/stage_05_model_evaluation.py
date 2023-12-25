from pathlib import Path
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_configuration()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_to_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<< \n\nx============================================================================================================x")
    except Exception as e:
        logger.exception(e)