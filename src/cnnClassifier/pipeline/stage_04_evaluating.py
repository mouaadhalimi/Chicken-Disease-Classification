
from cnnClassifier.components.data_ingestion import *
from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier.config.configuration import ConfigurationManager



STAGE_NAME="Evaluation"

class ModelEvaluationPipline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        config= ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.savescore()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME}  STARTED <<<<<<<<<")
        obj = ModelEvaluationPipline
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME}  completed <<<<<<< \n \n x==============x")
    except Exception as e :
        logger.exception(e)
        raise e
