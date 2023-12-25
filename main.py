from dotenv import load_dotenv
from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"\nx============================================================================================================x\n\n")
    logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<< \n\nx============================================================================================================x\n\n")
except Exception as e:
    logger.exception(e)

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<< \n\nx============================================================================================================x\n\n")
except Exception as e:
    logger.exception(e)

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<< \n\nx============================================================================================================x\n\n")
except Exception as e:
    logger.exception(e)

STAGE_NAME = "Model Training stage"

try:
    logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<< \n\nx============================================================================================================x\n\n")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Model Evaluation stage"

try:
    load_dotenv()
    logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<< \n\nx============================================================================================================x\n\n")
except Exception as e:
    logger.exception(e)



