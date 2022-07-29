from collections import namedtuple

DataIngestionConfig=namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])

DataValidationConfig=namedtuple("DataValidationConfig",["schema_file_path","report_file_path","report_page_file_path"])




DataTransformationConfig=namedtuple("DataTransformationConfig",["add_bedroom_per_room",
                                                                "transformed_train_dir",
                                                                "transformed_test_dir",
                                                                "preprocessed_object_file_path"])

  # add_bedroom_per_room is a column name that we will add in the dataset. 
  # if we want to add this column then add_bedroom_per_room =True else false                                                            

ModelTrainerConfig=namedtuple("ModelTrainerconfig",["trained_model_file_path","base_accuracy"])

ModelEvaluationConfig=namedtuple("ModelEvaluationConfig",["model_evaluation_file_path","time_stamp"])

# model_evaluation_file_path will contain some file that will contain all the models that
#  are currently in the production

ModelPusherConfig=namedtuple("ModelPusherConfig",["export_dir_path"])
# export_dir_path will specify the location where the trained model will be exported.

TrainingPipelineConfig=namedtuple("TrainingPipelineConfig",["artifact_dir"])



