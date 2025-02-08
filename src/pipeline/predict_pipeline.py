
import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            # print("done")
            preds=model.predict(data_scaled)
            # print("done2")
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(self,
        area : float,
        latitude : float,
        longitude : float,
        Bedrooms : float,
        Bathrooms : float,
        neworold,
        type_of_building,
        Furnished_status_Semi_Furnished : bool,
        Furnished_status_Unfurnished : bool):
        

        self.area = area

        self.latitude = latitude

        self.longitude = longitude

        self.Bedrooms = Bedrooms

        self.Bathrooms = Bathrooms

        self.neworold = neworold

        self.type_of_building = type_of_building
        self.Furnished_status_Semi_Furnished = Furnished_status_Semi_Furnished
        self.Furnished_status_Unfurnished = Furnished_status_Unfurnished



    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "area": [self.area],
                "latitude": [self.latitude],
                "longitude": [self.longitude],
                "Bedrooms": [self.Bedrooms],
                "Bathrooms": [self.Bathrooms],
                "neworold": [self.neworold],
                "type_of_building": [self.type_of_building],
                "Furnished_status_Semi_Furnished" :[self.Furnished_status_Semi_Furnished],
                "Furnished_status_Unfurnished" :[self.Furnished_status_Unfurnished]

            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

