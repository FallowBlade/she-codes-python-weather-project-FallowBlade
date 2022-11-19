import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

# Degree symbol is a constant

#empty functions that contain doc strings are belolow


# ############### FREE PASS FOR DEF FORMAT_TEMPERATURE ***********

def format_temperature(temp):
   
    return f"{temp}{DEGREE_SYBMOL}"

# print (format_temperature)

#     """Takes a temperature and returns it in string format with the degrees
#         and celcius symbols.

# #     Args:
# #         temp: A string representing a temperature.
# #     Returns:
# #         A string contain the temperature and "degrees celcius."
# #     """
#     # ############### FREE PASS FOR DEF FORMAT_TEMPERATURE ***********


# ############### PASSED CONVERT_DATE  ################# 
def convert_date(iso_string):

    # from datetime import datetime is at top of page.
    
    change_to_iso_string = datetime.fromisoformat (iso_string)
    formatted_date = change_to_iso_string.strftime ("%A %d %B %Y")
    return formatted_date
   
   #### PASSED DEF CONVERT_DATE ##### 

#TEST 2 (didn't work)
    # iso_string = datetime.fromisoformat as iso_string
    # iso_string2 = strftime(iso_string))
    # date_test2= (date_test)
    # iso_string = date_test.strftime

# TEST 3 (OVERCOMPLICATED IT!)
    # iso_string = datetime.strftime("A% %d B% %Y")
    # month = int(5:6)
    # day = int(8:9)
    # weekday = str("Monday")
    # year = now.strftime("%Y")

#TEST 4 (On the right track)
    # strftime("%M %B %d %Y")
    # %b = month
    # %d = day of month
    #%B = 

# A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021

    # datetime.isoformat('YYY)

    # pass

# *********************PASSED = CONVERT_F_TP_C ************

def convert_f_to_c(temp_in_farenheit):

    celsius = (float (temp_in_farenheit) - 32)*(5/9)
    rounded_c = round(celsius,1)

    return (rounded_c)

    #     """Converts antemperature from farenheit to celcius.
    # Args:
    #     temp_in_farenheit: float representing a temperature.
    # Returns:
    #     A float representing a temperature in degrees celcius, rounded to 1dp.
    # """
    pass

# *********************PASSED = CONVERT_F_TP_C ************

# print (convert_f_to_c(10))

# def add_num(num1, num2)

#     total = num1 + num2 

#     return total

# ###############  PASSED CALCULATE MEAN ###########

def calculate_mean(weather_data):

# searching the list, creating a sum, then creating a mean, then returning a mean.

    if len(weather_data)==0:
        return() 

    total = 0
# This is a loop - the num = the numbers in the list inside the weather data (in the mean test sheet).
# We are telling it that for every number in weather data, += mean loop the numbers. There is a "float" option to turn one of the strings from the example to a float.
# 
    for num in weather_data:
        total += float(num) 

    mean = total / len(weather_data)

    return mean

#data types in there are strings, floats.
#final result to be a float

    """Calculates the mean value from a list of numbers.
    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    pass

# ############### PASSED DATA LOAD #####

def load_data_from_csv(csv_file):
# this is defining the function - in which case the function is csv_file

    datalist = []

    with open(csv_file, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader) 
        # next (reader) = skips the headers of a csv file
        
        # for line in reader:
        #     datalist.append(line[0]),int(line[1]),int(line[2])
        for line in reader:
            if line:
                print(line)
                datalist.append([line[0],int(line[1]),int(line[2])])
                # indentation MATTERS. When this wasn't indented it was returning another empty list...

    # print(datalist) 
    return datalist   
    # """Reads a csv file and stores the data in a list.
    # Args:
    #     csv_file: a string representing the file path to a csv file.
    # Returns:
    #     A list of lists, where each sublist is a (non-empty) line in the csv file.
    # """
    pass

# ############### PASSED FIND_MIN ################

def find_min(weather_data):

    if len(weather_data)==0:
        return() 

        # two '==" means if lengh IS 0 then do this...
        # 1 = shouldn't be an equal, change it to an arrow --> in visual description
        #making min index = 0 then return nothing. One of tests if there's no value, you stil have to return something.
        # If YES then indent and update the minimum with the temp and max the 

    min_position = 0
    min_value = float(weather_data[0])

    for item in range(len(weather_data)):
        value = float(weather_data [item])
        
        if value <= min_value:
            min_value = value 
            min_position = item

    return (min_value,min_position)

##############PASSED############################

    # find the position of the number of this particular set.
    # create a list
    # convert weather data into list.
# EXAMPLE FROM PREV. WORK
# ls = [3, 6, 7, 2, 1, 5]
# # find min value using loop
# min_val = ls[0]
# for val in ls:
#     if val < min_val:
#         min_val = val
# # display the min value
# print(min_val)

    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass

############### PASSED FIND MAX ############# 

def find_max(weather_data):

    if len(weather_data)==0:
        return() 

    max_position = 0
    max_value = float(weather_data[0])
    
    for item in range(len(weather_data)):
        value = float(weather_data [item])
        
        if value >= max_value:
            max_value = value 
            max_position = item

    return (max_value,max_position)

    #could have used enumerated = assigns a factor (number might be 47, then it assigns a '0' to it, and then tey are countring up)to your data.
    """Calculates the maximum value in a list of numbers.
    Args:
        weather_data: A list of numbers (values)
    Returns:
        The maximum value (number) and it's position in the list.
    """
    pass
# # ############### PASSSED FIND_MAX ################

# #################################################

def generate_summary(weather_data):

    day = len(weather_data)

    min_list = []
    max_list = []

    for item in weather_data:
        # min_list.append(item[1])
        # max_list.append(item[2]) Hasn't worked, missing function?

        min_list.append(convert_f_to_c(item[1]))
        max_list.append(convert_f_to_c(item[2]))

    low_temp = find_min(min_list)
    low_temp_to_celsius = format_temperature(low_temp[0])
    low_temp_day = convert_date(weather_data[low_temp[1]][0])

    high_temp = find_max(max_list)
    high_temp_day = convert_date(weather_data[high_temp[1]][0])
    high_temp_to_celsius = format_temperature(high_temp[0])
    
    low_avg = calculate_mean(min_list)
    low_avg_celsius = format_temperature(round(low_avg,1))
    
    high_avg = calculate_mean(max_list)
    high_avg_celsius = format_temperature(round(high_avg,1))

# \n = newline. two spaces after the \n means indentation by 2.
    summary = (f"{day} Day Overview\n  The lowest temperature will be {low_temp_to_celsius}, and will occur on {low_temp_day}.\n  The highest temperature will be {high_temp_to_celsius}, and will occur on {high_temp_day}.\n  The average low this week is {low_avg_celsius}.\n  The average high this week is {high_avg_celsius}.\n"  )  

    # print(summary)    
    
    return summary 

    # mins=[]
    # max=[]

    # generate_summary = []
    # this is wrong - don't generate summary as a list, summar should be ""

    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

# "The maximum temperature of this day is 90 degrees"


# # ############### 

def generate_daily_summary(weather_data):


    daily_summary = ""
# daily summary to be a "" as strings with float variables?
# ---- Friday 02 July 2021 ----
# the formatted date = our converted date into an f string, index positon is 0, create a \n for newline
#   Minimum Temperature: 9.4°C
# the min temp in index position 1 to be converted into a celsius, then add degree symbol 
#   Maximum Temperature: 19.4°C
# max temp in index position 2, conver to celsius, then degree symbol
# daily_summary +- means add the following f string with expressions.

    for item in weather_data:
            string_date = convert_date(item[0])
            min_celsius_temp = convert_f_to_c(item[1])
            format_min_temp = format_temperature(min_celsius_temp)
            max_celsius_temp = convert_f_to_c(item[2])
            format_max_temp = format_temperature(max_celsius_temp)

            daily_summary+=(f"---- {string_date} ----\n  Minimum Temperature: {format_min_temp}\n  Maximum Temperature: {format_max_temp}\n\n"  )
        
    # print(daily_summary)

    return daily_summary

  # daily_summary+-(f"---{string_date}---\n  Minimum Temperature: {format_min_temp}\n  Maximum Temperature: {format_max_temp}\n"  )
#     """Outputs a daily summary for the given weather data.

#     Args:
#         weather_data: A list of lists, where each sublist represents a day of weather data.
#     Returns:
#         A string containing the summary information.
#     """
#     pass
