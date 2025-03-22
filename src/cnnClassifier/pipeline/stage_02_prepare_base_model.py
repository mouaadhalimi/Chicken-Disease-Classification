from cnnClassifier.config.configuration import *
from cnnClassifier.components.prepare_base_model import * 
from cnnClassifier import logger


STAGE_NAME = "prepare base model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        config= ConfigurationManager()
        prepare_base_model_config= config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME}  STARTED <<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME}  completed <<<<<<< \n \n x==============x")
    except Exception as e :
        logger.exception(e)
        raise e