import csv 
import os
    # description: Receive in-time data (Pulse, Blood Pressure and Oxygen Level)
    #              and handle exception, return in time data
    # INPUT:   Python Dictionary data after exception handle
    # OUTPUT:  1.CSV file: "datavase.csv". The headers of the file are the keys of input Python Dictionary 
    #            and each row of the file is the value of input Python Dictionary
    #          2.The filename of csv file: in the form requiried in the predictor part
    # EXAMPLE: Input the dictionary "parse" which defined in the test function, then will see the database_test.csv
    #          on github.     
    #              
def Database(parse):
    # initialize the header of csv
    headers = ["Pulse","Blood_Pressure","Oxygen_Level"]
    # open an csv file at current dictionary with name database.csv
    filepath = './database.csv'
    if (os.path.exists(filepath)):
        #if the file exist add the value of the dictionary,else will build a new file with the header
        with open(filepath,'a+') as f:
            
            f_csv = csv.DictWriter(f, headers)             
            for item in parse:
                f_csv.writerow(item) 
    else:
        with open(filepath,'a+') as f:
            f_csv = csv.DictWriter(f, headers)
            # write headers to database.csv
            f_csv.writeheader() 
    # write values of input Python Dictionary to database.csv row by row
            for item in parse:
                f_csv.writerow(item) 
    # return the filename in the form required in the predictor part.
    filename = './database'
    return filename 



if __name__ == '__main__':    
    parse = [{'Pulse': None, 'Blood_Pressure': 120, 'Oxygen_Level': 340}]
    Database(parse)
    parse = [{'Pulse': 75, 'Blood_Pressure': 120.0, 'Oxygen_Level': 340}]
    Database(parse)
