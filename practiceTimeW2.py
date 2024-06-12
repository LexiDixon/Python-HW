'''There are 60 seconds in a minute. If the number of seconds entered by the user is greater than or equal to 60, the program should convert the number of seconds to minutes and seconds.
 There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater than or equal to 3,600, the program should convert the number of seconds to hours, minutes, and seconds.
 There are 86,400 seconds in a day. If the number of seconds entered by the user is greater than or equal to 86,400, the program should convert the number of seconds to days, hours, minutes, and seconds.
 '''
#CODE WORKS
#Get the number of seconds from the user.
seconds = int(input('Enter the number of seconds:  '))

#calculate the minutes.
if seconds < 60:
    print(f'{seconds} seconds')

if seconds >= 60 and seconds < 3600:
    minutes = seconds // 60
    mintuesRemainder = seconds % 60
    print(f'{seconds} seconds are equal to: {minutes} minutes and {minuteRemainder} seconds')

if seconds >= 3600 and seconds < 86400:
    hours=seconds//3600
    hoursRemainder = seconds % 3600
    minutes = hoursRemainder // 60
    minutesRemainder = hoursRemainder % 60
    print(f'{seconds} seconds are equal to: {hours} hours {minutes} minutes and {minuteRemainder} seconds')


if seconds >= 86400:
    days=seconds//86400
    daysRemainder=seconds%86400
    hours= daysRemainder// 3600
    hoursRemainder = daysRemainder % 3600
    minutes = hoursRemainder // 60
    minuteRemainder = hoursRemainder % 60
    print(f'{seconds} are equal to: {days} days {hours} hours {minutes} minutes and {minuteRemainder} seconds')

