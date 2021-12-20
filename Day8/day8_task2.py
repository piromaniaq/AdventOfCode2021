import collections

def get_data(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()
        input_final = []
        output_final = []
        for line in data:
            input, output = line.split(' | ')
            output_split = output.split()
            input_split = input.split()
            input_final.append(input_split)
            output_final.append(output_split)
    return input_final, output_final


def digit_check(first, last):
    digit_counter = collections.Counter('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')



if __name__ == '__main__':
    input_full, output_full = get_data('input.txt')
    print('Input:',input_full, '\nOutput:', output_full)