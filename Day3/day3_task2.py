reports = []

with open('day3_test.txt') as f:
    lines = f.readlines()
    for line in lines:
        reports.append(line.strip())

zerosRate = reports
onesRate = reports


def check_value(x):
    value = []
    for i in range(0, len(reports[0])):
        checkValue = 0
        for report in reports:
            if report[i] == '1':
                checkValue += 1
            else:
                checkValue -= 1
        value.append(checkValue)
    return value
