def get_data(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()
        dataSplit = [int(x) for x in data[0].split(',')]
    return dataSplit


#def check_position(data):


if __name__ == '__main__':
    input = get_data('test.txt')
    #check_position(input)
    print(input[5])
