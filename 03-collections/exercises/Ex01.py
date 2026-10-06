'''Given the following two lists:

first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]
Concatenate the two lists by index into a new list that, when printed, looks as follows:

["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]'''

first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]
week = list()
for day in range(len(first)-1):
    week = week + [first[day] + second[day]]
    
print(week)