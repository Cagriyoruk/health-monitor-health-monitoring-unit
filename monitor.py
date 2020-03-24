def monitor(data,message):
    try:
        if len(data)!=3:
            print("wrong input length")
        else:
            output_type = ["Pulse", "Blood_Pressure", "Oxygen_Level"]
            for i in range(0,3):
                if str(data[output_type[i]]).isdigit():
                    print(output_type[i] + ": " + str(data[output_type[i]]))
                else:
                    print(output_type[i] + " EORROR!")
                    break
        if message[0] == 'Good':
            print('Status: [Alive]')
        else:
            print(f'Status: [{message}]')
    except:
        print("input is not array")


# test cases:
# a = { "Pulse" : 12,  "Blood_Pressure" : 120, "Oxygen_Level" : 340}
# monitor(a,'Good')