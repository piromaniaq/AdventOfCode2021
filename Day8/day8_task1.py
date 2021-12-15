def get_data(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()
    return data


if __name__ == '__main__':
    digits = get_data('test.txt')
    print(digits)