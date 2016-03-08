
time = "8&#189; Hours"
timeValue = time.split(' ')
timeValue[0] = timeValue[0].replace('&#188;', '.25').replace('&#189;', '.5').replace('&#190;', '.75')

inMinutes = float(timeValue[0]) * 60

print inMinutes
