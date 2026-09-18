from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import Modeltrainer


if __name__ == "__main__":

    # 1. Data Ingestion
    data_ingestion = DataIngestion()
    train_data, test_data = data_ingestion.initiate_data_ingestion()

    # 2. Data Transformation
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
        train_data,
        test_data
    )

    # 3. Model Training
    model_trainer = Modeltrainer()
    r2_score = model_trainer.initiate_model_trainer(
        train_arr,
        test_arr
    )

    print("Final R2 Score:", r2_score)