from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipline
from cnnClassifier.pipeline.stage_04_evaluating import ModelEvaluationPipline





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

STAGE_NAME = "Training"

try:
        logger.info(f">>>>>>> stage {STAGE_NAME}  STARTED <<<<<<<<<")
        obj = ModelTrainingPipline
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME}  completed <<<<<<< \n \n x==============x")
except Exception as e :
        logger.exception(e)
        raise e

STAGE_NAME = "Evaluation"

try:
        logger.info(f">>>>>>> stage {STAGE_NAME}  STARTED <<<<<<<<<")
        obj = ModelEvaluationPipline
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME}  completed <<<<<<< \n \n x==============x")
except Exception as e :
        logger.exception(e)
        raise e