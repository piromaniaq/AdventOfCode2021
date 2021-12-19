def get_data(file):
    with open(file, 'r') as f:
        count = 0
        data = f.read().splitlines()
        for line in data:
            input, output = line.split(' | ')
            output_split = output.split()
            for x in output_split:
                if len(x) in {2, 3, 4, 7}:
                    count += 1
    return count


if __name__ == '__main__':
    digits = get_data('input.txt')
    print(digits)