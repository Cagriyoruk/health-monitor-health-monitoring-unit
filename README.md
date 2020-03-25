# health-monitor-health-monitoring-unit
health-monitor-heal-monitoring-unit created by GitHub Classroom

<p align="center">
  <img width="800" height="500" src="/PNG image-08D2E2371294-1.png">
</p>

## Smart ICU (Main Function) Section:

## Data Generator Section:

## Data Collector Section:

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

## AI Predictor Section:

## Monitor Section:

## Alarm Section:
