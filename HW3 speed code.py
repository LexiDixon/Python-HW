'''One cause for speeding is the desire to shorten the time spent traveling. Create a program that calculates the total amount of time saved if you are traveling with an average speed that is above the speed-limit as compared to traveling with an average speed exactly at the speed-limit.
Ask the user for the average speed, speed limit and distance travelled.
Calculate the amount of time saved for the distance travelled.'''
#CODE WORKS
distance = float(input("Enter the distance in miles "))
speedlimit = float(input("Enter miles/hour speed limit "))
speed = float(input("Enter your average speed in miles/hour "))

time = distance / speedlimit
speedtime = distance / speed

#print(time, speedtime)

Minutes_in_hour = 60

speedtimemin = speedtime*Minutes_in_hour
timemin = time * Minutes_in_hour

if speed > speedlimit:
    savedtime = timemin - speedtimemin
else:
    print("safe driver but no time saved")

print(f'time taken at speed limit {timemin:.2f} minutes')
print(f'time taken at your speed {speedtimemin:.2f} minutes')
print(f'time saved in min {savedtime:.2f}')
