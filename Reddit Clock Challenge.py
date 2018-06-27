hour_dict = {0: "twelve",
              1: "one",
              2: "two",
              3: "three",
              4: "four",
              5: "five",
              6: "six",
              7: "seven",
              8: "eight",
              9: "nine",
              10: "ten",
              11: "eleven",
              12: "twelve",
              12: "twelve",
              13: "thirteen",
              14: "fourteen",
              15: "fifteen",
              16: "sixteen",
              17: "seventeen",
              18: "eighteen",
              19: "nineteen",
              20: "twenty",
              21: "twenty-one",
              22: "twenty-two",
              23: "twenty-three",
              24: "twenty-four",
                   }
# A dictionary for all of the hours and minutes
# I had to have two different dictionaries for the minutes and hours
# The minutes needed the "oh" in case the minute was 1-9
# I also had to go up to 24 for my hour dictionary so it wouldn't get an error
# The challenged input also only asks for up to 30 for the minute so I stopped at 30
minute_dict = {
              0: "",
              1: "oh one",
              2: "oh two",
              3: "oh three",
              4: "oh four",
              5: "oh five",
              6: "oh six",
              7: "oh seven",
              8: "oh eight",
              9: "oh nine",
              10: "ten",
              11: "eleven",
              12: "twelve",
              13: "thirteen",
              14: "fourteen",
              15: "fifteen",
              16: "sixteen",
              17: "seventeen",
              18: "eighteen",
              19: "nineteen",
              20: "twenty",
              21: "twenty-one",
              22: "twenty-two",
              23: "twenty-three",
              24: "twenty-four",
              25: "twenty-five",
              26: "twenty-six",
              27: "twenty-seven",
              28: "twenty-eight",
              29: "twenty-nine",
              30: "thirty",
                   }

def number_to_word ():
    #a function that takes no value and prints out the time
    l = False
    while l == False: #creates a loop so you don't have to restart the program
        time_input = str(input("What time is it? ")) # input a time
        time = time_input.split(":") # splits the time into the hour and minute
        hour = hour_dict[int(time[0])] # translates from number to text
        minute = minute_dict[int(time[1])]
        if int(time[0]) < 12: # handles the am and pm
            am_or_pm = "am"
        elif int(time[0]) == 24:
            hour = hour_dict[int(time[0])-12]
            am_or_pm = "am"
        else:
            hour = hour_dict[int(time[0])-12]
            am_or_pm = "pm"
        print("It's {} {} {}".format(hour,minute,am_or_pm)) # Formats the hour, minute, and the am/pm

number_to_word() #calls the funciton
