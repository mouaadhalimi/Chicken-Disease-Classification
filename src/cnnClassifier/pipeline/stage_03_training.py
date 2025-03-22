
from cnnClassifier.components.prepare_callback import PrepareCallback
from cnnClassifier.components.traning import Training
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import *



STAGE_NAME="Training"

class ModelTrainingPipline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbackss()

        training_config= config.get_training_config()
        training= Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME}  STARTED <<<<<<<<<")
        obj = ModelTrainingPipline
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME}  completed <<<<<<< \n \n x==============x")
    except Exception as e :
        logger.exception(e)
        raise e
