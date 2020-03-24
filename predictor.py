import pandas as pd
import numpy as np

# collecting data from the csv file from the database
def Predictor(file):
    try:
        df = pd.read_csv(file+'.csv')
        Pulse = df.iloc[:,0].values
        BloodPressure = df.iloc[:,1].values
        OxygenLevel = df.iloc[:,2].values
        a,b,c = healthPredict(Pulse,BloodPressure,OxygenLevel)   #call the AI function to predict health
        dict = {}
        dict["Pulse"] = int(a)
        dict["Blood_Pressure"] = int(b)
        dict["Oxygen_Level"] = int(c)
        return dict  # Return the result from the AI function
    except:
        print("an error occurs")

# making prediction based on the data collect from the Predictor
def healthPredict(Pulse,BloodPressure,OxygenLevel):
    return np.mean(Pulse), np.mean(BloodPressure),np.mean(OxygenLevel)  #AI function, here we use average of the number instead

print(Predictor("database"))