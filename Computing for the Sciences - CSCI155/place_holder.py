def aggregate_temp(filename, temperature):
    if os.path.exists(filename) == True:
        with open(filename, 'a') as file:
            file.write(get_date() + ',' + str(temperature))
            
    else:
        with open(filename, 'w') as file:
            file.write(get_date() + ',' + str(temperature))