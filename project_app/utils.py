import numpy as np  
import json
import pickle
import config

class TitanicClass():
    def __init__(self,Pclass,Gender,Age,SibSp,Parch,Fare,Embarked):
        self.Pclass = Pclass
        self.Gender = Gender
        self.Age = Age
        self.SibSp = SibSp
        self.Parch = Parch
        self.Fare = Fare
        self.Embarked = Embarked
        

    def load_model(self):
        with open (config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)


    def get_predict_survived(self):
        self.load_model()

        # GenderIndex = self.json_data['columns'].index(self.Gender)
        # EmbarkedIndex = self.json_data['columns'].index(self.Embarked) #We write this code when we use one hot encoding for the replacement

        test_array = np.zeros(len(self.json_data['columns']))

        test_array[0] = self.Pclass
        test_array[1] = self.json_data["Gender"][self.Gender]
        test_array[2] = self.Age
        test_array[3] = self.SibSp
        test_array[4] = self.Parch
        test_array[5] = self.Fare
        test_array[6] = self.json_data["Embarked"][self.Embarked]        
        

        print("test_array:",test_array) 

        Survived_Pred = self.model.predict([test_array])[0]
        return Survived_Pred


if __name__ == "__main__":

    Pclass = 1,
    Gender = "male",
    Age = 28,
    SibSp = 5,
    Parch = 3,
    Fare = 445,
    Embarked = "S"


    survived1 = TitanicClass(Pclass,Gender,Age,SibSp,Parch,Fare,Embarked)
    survived = survived1.get_predict_survived()
    print(f"Survived prediction is : {survived}")