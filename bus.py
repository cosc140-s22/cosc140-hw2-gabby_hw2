#######################################################
#
# COSC 140 Homework 2, "bus trip planner" problem
#
#######################################################


time_per_stop = 30; # Time in seconds
kmph = 40;

hours = int(input("What is the departure time of the bus (hour part in 24hr format)? "))
minutes = int(input("What in the departure time (minute part)? "))
distance = int(input("How far do you need to travel (in kmph)? "))
stops = int(input("How many stops are there before your destination? "))

distance = distance / kmph

distance_time = distance * 60 *60
stop_time = stops * time_per_stop
seconds = stop_time + distance_time

minutes = minutes + (seconds // 60)
seconds = int(seconds % 60)

hours = hours + (minutes // 60)
minutes = int(minutes % 60)

hours = int(hours % 24)

print("Time time you should arrive is", f"{hours:02d}:{minutes:02d}:{seconds:02d}")