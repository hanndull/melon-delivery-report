
business_days = {       #contains dates of current files 
    "1" : "20140519",   #add new business days and dates into dictionary as needed
    "2" : "20140520",   #be sure to add associated files to same folder 
    "3" : "20140521",
    }

def printing_delivery_info(days = business_days):
    """Loops through the lines of each day and date to print out sales info.
   
    Prints out melon type, count, and $ amount for each day.
    Note that the default set for the days parameter is currently a static dictionary of outer scope 
    """
    for day, date in days.items():  #unpacks and loops thru the day and date items of the dictionary

        print("Day ", day)  #prints the day number
        the_file = open(f"um-deliveries-{date}.txt")    #opens the file associated with the date
        for line in the_file:   #loops thru the lines of the associated file
            line = line.rstrip()    #removes extra spacing of the line
            words = line.split('|')     #splits apart the words of the line into a list

            melon = words[0]    #stores the first indice of the list
            count = words[1]    #stores the second indice of the list (needed to switch from index 0 to index 1)
            amount = words[2]   #stores the third indice of the list (needed to switch from index 0 to index 2)

            print(f"Delivered {count} {melon}s for total of ${amount}") #prints sentence for each line's count, melon, and $ amount (made easier to read w/ updated f-string)
        the_file.close()    #closes the file we were referring to in the loop 

printing_delivery_info()    #calls the function above 




##LEFTOVER OLD CODE

# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()
