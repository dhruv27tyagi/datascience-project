from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainingTrainingPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline

STAGE_NAME= "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx========x")
except Exception as e: 
    logger.exception(e)
    raise e


STAGE_NAME= "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx========x")
except Exception as e: 
    logger.exception(e)
    raise e

STAGE_NAME= "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation= DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<<< \n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= "Model Trainer Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = ModelTrainingTrainingPipeline()
    data_ingestion.initiate_model_training()
    logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<<< \n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model evaluation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = ModelEvaluationTrainingPipeline()
    data_ingestion.initiate_model_evaluation()
    logger.info(f">>>>>>>> {STAGE_NAME} completed <<<<<<<<< \n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e  