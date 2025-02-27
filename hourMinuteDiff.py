'''
Calculate the angle between the hour and minute hands.
'''

def calculateAngle(hour, minute):
    if hour >= 12:
        hour -= 12

    minute_angle = minute * 6  # 360* / 60 mins = 6*/min
    hour_angle = (hour * 30) + (minute * 0.5)  # 360* / 12 hours = 30* per h + 0.5* every min

    angle = abs(hour_angle - minute_angle) # difference between the two angles

    if angle > 180:
        angle = 360 - angle

    return angle


hour = 3
minute = 30
angle = calculateAngle(hour, minute)