# Get the time interval data from the data collection
def patient_alarm(dictionary):
	problems = []
	# Base Case
	if dictionary['Pulse'] is None:
		problems.append('No Pulse Value')
	# If pulse is not None in range 20-60
	elif dictionary['Pulse'] > 60 or dictionary['Pulse'] < 20:
		if dictionary['Pulse'] > 60:
			problems.append('High Pulse!!!')
		else:
			problems.append('Low Pulse!!!')
	# Blood Pressure range is 80-140
	if dictionary['Blood_Pressure'] > 140 or dictionary['Blood_Pressure'] < 80:
		if dictionary['Blood_Pressure'] > 140:
			problems.append('High Blood Pressure!!!')
		else:
			problems.append('Low Blood Pressure!!!')
	# Oxygen level range is 60-110
	if dictionary['Oxygen_Level'] > 110 or dictionary['Oxygen_Level'] < 60:
		if dictionary['Oxygen_Level'] > 110:
			problems.append('High Oxygen Level')
		else:
			problems.append('Low Oxygen Level')
	if not problems:
		problems.append('Everything is fine')
	return problems
"""

def patient_alarm_test():
	# Pulse is None, Blood Pressure and Oxygen level are fine
	data1 = {'Pulse': None, 'Blood_Pressure': 120, 'Oxygen_Level': 70}
	# Pulse is High, Blood Pressure and Oxygen level are fine
	data2 = {'Pulse': 140, 'Blood_Pressure': 100, 'Oxygen_Level': 80}
	# Blood Pressure is High, Pulse and Oxygen level are fine
	data3 = {'Pulse': 50, 'Blood_Pressure': 160, 'Oxygen_Level': 90}
	# Oxygen level is High, Pulse and Blood Pressure are fine
	data4 = {'Pulse': 40, 'Blood_Pressure': 100, 'Oxygen_Level': 130}
	# Everything is Fine
	data5 = {'Pulse': 40, 'Blood_Pressure': 100, 'Oxygen_Level': 100}
	# Double Trouble
	data6 = {'Pulse': 10, 'Blood_Pressure': 20, 'Oxygen_Level': 100}
	assert patient_alarm(data1) == ['No Pulse Value!!!']
	assert patient_alarm(data2) == ['High Pulse!!!']
	assert patient_alarm(data3) == ['High Blood Pressure!!!']
	assert patient_alarm(data4) == ['High Oxygen Level!!!']
	assert patient_alarm(data5) == ['Everything is fine']
	assert patient_alarm(data6) == ['Low Pulse!!!', 'Low Blood Pressure!!!']

def main():
	print(patient_alarm({'Pulse': None, 'Blood_Pressure': 170, 'Oxygen_Level': 100}))
	print(patient_alarm({'Pulse': 30, 'Blood_Pressure': 100, 'Oxygen_Level': 100}))
	print(patient_alarm({'Pulse': 10, 'Blood_Pressure': 20, 'Oxygen_Level': 100}))

if __name__ == '__main__':
	main()

"""