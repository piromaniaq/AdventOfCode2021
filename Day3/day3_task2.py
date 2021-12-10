
def get_data(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()
    return data


def check_value(check):
    value = []
    for i in range(0, len(check[0])):
        checkValue = 0
        for report in check:
            if report[i] == '1':
                checkValue += 1
            else:
                checkValue -= 1
        value.append(checkValue)
    return value


def oxygen_generator(factor):
    onesRate = []
    tempList = reports
    for x in factor:
        for y in range(0, len(tempList)):
            if x >= 0:
                onesRate.append(tempList[y])
            else:
                continue
            tempList = onesRate
            onesRate = []
    print(onesRate)
    return onesRate


#def co2_scrubber(reports):



if __name__ == '__main__':
    reports = get_data('day3_test.txt')
    factors = check_value(reports)
    print(factors)
    oxygen = oxygen_generator(factors)
    #co2 = co2_scrubber(factors)

    #print(co2)
    print(oxygen)