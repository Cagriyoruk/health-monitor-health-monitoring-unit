import time
import Generate_Data as GD
import Data_Collect as DC
import Monitor as M
import Alarm
import Database as db
import Predictor as p

if __name__ == '__main__':
    # description: This is the main function of ICU Monitor.
    #
    # INPUT:  database.csv and 6 APIs: Senor, Data Processor, Database, Monitor, Predictor, Alarm
    # OUTPUT:  1. Real-Time Monitor Screen
    #          2. Real-Time Updated database.csv
    # EXAMPLE: set run_time = 5 it will run 5 sec.
    #
    run_time = 5

    count = 0
    while count < run_time:
        print('----------------------------')
        time.sleep(1)
        localtime = time.asctime( time.localtime(time.time()))
        # timer
        print(localtime)
        # read from sensor
        row_data = GD.get_row_data()
        # data washing
        clean_data = DC.data_collect(row_data)
        # update database
        db.Database([clean_data])
        # predicted data
        dict_precition = p.Predictor("database")
        # printer
        M.monitor(clean_data,Alarm.patient_alarm(clean_data))
        # predict printer
        print(f'Next 60s: {Alarm.patient_alarm(dict_precition)}')
        print()
        count += 1