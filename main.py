from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"\nx============================================================================================================x\n\n")
    logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<< \n\nx============================================================================================================x\n\n")
except Exception as e:
    logger.exception(e)

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<< \n\nx============================================================================================================x\n\n")
except Exception as e:
    logger.exception(e)

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<< \n\nx============================================================================================================x\n\n")
except Exception as e:
    logger.exception(e)



