from housing.config.configuration import Configuration
from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation


def main():
    try:
        pipeline=Pipeline()
        pipeline.run_pipeline()

        #data_validation_config=Configuration().get_data_validation_config()
        #print(data_validation_config)

        #schema_file_path=r"C:\project\machine-learning-project\config\shcema.yaml"
        #file_path=r"C:\project\machine-learning-project\housing\artifact\data_ingestion\2022-07-29-11-18-56\ingested_data\train\housing.csv"
        #DataTransformation.load_data()

        #data_transformation_config=Configuration().get_data_transformation_config()
        #print(data_transformation_config)


    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()

