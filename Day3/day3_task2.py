
def get_data(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()
    return data


def check_ones(checkData, checkBit):
    checkValue = 0
    for currentValue in checkData:
        if currentValue[checkBit] == '1':
            checkValue += 1
        else:
            checkValue -= 1
    if checkValue >= 0:
        return 1
    else:
        return 0


def check_zeros(checkData, checkBit):
    checkValue = 0
    for currentValue in checkData:
        if currentValue[checkBit] == '1':
            checkValue += 1
        else:
            checkValue -= 1
    if checkValue >= 0:
        return 0
    else:
        return 1


def oxygen_generator(data, factor_determination, factor_value):
    onesRate = []
    for line in data:
        if line[factor_determination] == str(factor_value):
            onesRate.append(line)
    return onesRate


def co2_scrubber(data, factor_determination, factor_value):
    zerosRate = []
    for line in data:
        if line[factor_determination] == str(factor_value):
            zerosRate.append(line)
    return zerosRate


if __name__ == '__main__':
    reports = get_data('data.txt')
    reportOnes = oxygen_generator(reports, 0, check_ones(reports, 0))
    reportZeros = co2_scrubber(reports, 0, check_zeros(reports, 0))
    for i in range(1, len(reports[0]) + 1):
        if len(reportOnes) > 1:
            reportOnes = oxygen_generator(reportOnes, i, check_ones(reportOnes, i))
        else:
            oxygen = int(reportOnes[0], 2)

    for i in range(1, len(reports[0]) + 1):
        if len(reportZeros) > 1:
            reportZeros = co2_scrubber(reportZeros, i, check_zeros(reportZeros, i))
        else:
            co2 = int(reportZeros[0], 2)
    print(oxygen * co2)