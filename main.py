from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline





STAGE_NAME = "Data Ingestion stage"
try:
        logger.info(f">>>>>>> stage {STAGE_NAME}  STARTED <<<<<<<<<")
        obj = DataIngestionTrainingPipeline
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME}  completed <<<<<<< \n \n x==============x")
except Exception as e :
        logger.exception(e)
        raise e


STAGE_NAME = "Prepare base model"
try:
        logger.info(f">>>>>>> stage {STAGE_NAME}  STARTED <<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME}  completed <<<<<<< \n \n x==============x")
except Exception as e :
        logger.exception(e)
        raise e