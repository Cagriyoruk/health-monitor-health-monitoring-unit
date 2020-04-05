# health-monitor-health-monitoring-unit
## General System Architecture:
<p align="center">
  <img width="800" height="500" src="/PNG image-08D2E2371294-1.png">
</p>

## Smart ICU Section (Suli Hu):
This section eventually assembles each of the features as `run.py`, which is the entrance of the product.  Under the timer frame, `Data Generator`, `Data Collector`, `DataBase`, `AIPredictor`, `Alarm` and `Monitor(screen)` are synchronized with 2 client-adjustable  arguments in seconds. They are listed below:
>  run_time = 1000

>  time.sleep(1) 

`run_time` represents how long will this monitor keeps working and the number inside `time.sleep()` is  the refreshing frequency. 

Here is a demo picture of the monitor running:
<p align="center">
  <img width="600" height="375" src="/demo_pic.png">
</p>

You will also be able to find the demo video as `demo.mov`.

<p align="center">
  <img width="800" height="500" src="https://github.com/BUEC500C1/health-monitor-health-monitoring-unit/blob/master/demo.gif">
</p>

## Data Generator Section (Qingxuan Pei):
**Description**:
produce in-time data (Pulse, Blood Pressure and Oxygen Level) in the fixed range, then create three random parameters to make exception.

**INPUT**: 
None

**OUTPUT**: 
Python Dictionary data with exception.
```
EXAMPLE:  
Output:       data1 = {'Pulse': None, 'Blood_Pressure': 120, 'Oxygen_Level': 140}
```

## Data Collector Section ([Kefan Zhang](https://github.com/h4x0rMadness))

### [Data_Collector Code](https://github.com/BUEC500C1/health-monitor-health-monitoring-unit/blob/master/Data_Collect.py)

**Description**:  
Receive in-time data (Pulse, Blood Pressure and Oxygen Level) and handle exception, return in time data

**INPUT**:        
Python Dictionary in time generated (value of items can be int or float)

**OUTPUT**:       
Python Dictionary data after exception handle
```
EXAMPLE:  
INPUT:            data1 = {'Pulse': None, 'Blood_Pressure': 120, 'Oxygen_Level': 340} # int parse
EXPECTED OUTPUT:  {'Pulse': None, 'Blood_Pressure': 120, 'Oxygen_Level': 340}

INPUT:            data2 = {'Pulse': 75, 'Blood_Pressure': 120.0, 'Oxygen_Level': 340} # float parse
EXPECTED OUTPUT:  {'Pulse': 75, 'Blood_Pressure': 120.0, 'Oxygen_Level': 340}

INPUT:            data3 = {'Pulse': "wrong type test", 'Blood_Pressure': 120, 'Oxygen_Level': 340} # wrong type exception
EXPECTED OUTPUT:  {'Pulse': None, 'Blood_Pressure': 120, 'Oxygen_Level': 340}

INPUT:            data4 = {'Pulse': "wrong type test", 'Blood_Pressure': -120, 'Oxygen_Level': 340} # negative number exception
EXPECTED OUTPUT:  {'Pulse': None, 'Blood_Pressure': None, 'Oxygen_Level': 340}

```

**Exception Handle**:
```
## for Oxygen Level, Pulse and Blood Pressure, non-negative int or float are expected.

'None' type data              -> 'None'
'Str'  type data              -> 'None'
'int' / 'float' but negative  -> 'None'
```


## DataBase Section:

## AI Predictor Section (Peixi Zhao):
**Description:**

The AI Predictor Section is to predict the health condition of the patient.

**Input:**

CSV file which is collected by the DataBase Section.

**Output:**

Result from the AI function which predict the health condition of the patient.(Here we choose to output the maen value of the Pulse, Blood Pressure and Oxygen level).

## Monitor Section:

## Alarm Section (Cagri Yoruk):
**Description:**

Check whether the recieved data (Pulse, Blood Pressure and Oxygen level) are lethal. Send a notice to the doctor if the levels are critical.

**Input:**

Python Dictionary recieved from Data_Collector

**Output:**

List of abnormal values

**Example:**

```
INPUT:	  data1 = {'Pulse': None, 'Blood_Pressure': 120, 'Oxygen_Level': 70}
OUTPUT:	  ['No Pulse Value!!!']

INPUT:	  data2 = {'Pulse': 140, 'Blood_Pressure': 100, 'Oxygen_Level': 80}
OUTPUT:	  ['High Pulse!!!']

INPUT:	  data3 = {'Pulse': 50, 'Blood_Pressure': 160, 'Oxygen_Level': 90}
OUTPUT:	  ['High Blood Pressure!!!']

INPUT:	  data4 = {'Pulse': 40, 'Blood_Pressure': 100, 'Oxygen_Level': 130}
OUTPUT:	  ['High Oxygen Level!!!']

INPUT:	  data5 = {'Pulse': 10, 'Blood_Pressure': 20, 'Oxygen_Level': 100}
OUTPUT:	  ['Low Pulse!!!', 'Low Blood Pressure!!!']

```

