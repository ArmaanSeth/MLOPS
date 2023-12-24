from pathlib import Path
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger

STAGE_NAME = "Data Validation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status = f.read().split(" ")[-1]

            if status=="True":
                config = ConfigurationManager()
                data_validation_config = config.get_data_transformation_configuration()
                data_validation = DataTransformation(config=data_validation_config)
                data_validation.train_test_splitting()

            else:
                raise Exception("Your data schema is not valid!")
        except Exception as e:
            raise e

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<< \n\nx============================================================================================================x")
    except Exception as e:
        logger.exception(e)