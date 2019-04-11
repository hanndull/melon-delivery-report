
business_days = {
    "1" : "20140519",
    "2" : "20140520",
    "3" : "20140521",
    }

def printing_delivery_info(days = business_days):
    """loops through the lines of each day to print out sales info.
   
    Prints out melon type, count, and $ amount for each day.
    """
    for day, date in days.items(): 

        print("Day ", day)
        the_file = open(f"um-deliveries-{date}.txt")
        for line in the_file:
            line = line.rstrip()
            words = line.split('|')

            melon = words[0] 
            count = words[1] #needed to switch from index 0 to index 1
            amount = words[2] #needed to switch from index 0 to index 2

            print("Delivered {} {}s for total of ${}".format(
                count, melon, amount))
        the_file.close()

printing_delivery_info()

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
