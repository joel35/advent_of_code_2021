def main():
    data = load_data('example_input')
    print(f'Part 1: {do_part_1(data)}')
    data = load_data('example_input_part_2')
    do_part_2(data)


def do_part_1(data):
    return sum(
        len([digit for digit in digits if len(digit) in [2, 3, 4, 7]])
        for digits in [entry['output'] for entry in data]
    )


def do_part_2(data):
    lengths = {
        2: 1,
        4: 4,
        3: 7,
        7: 8
    }
    answer = {
        8: 'acedgfb',
        5: 'cdfbe',
        2: 'gcdfa',
        3: 'fbcad',
        7: 'dab',
        9: 'cefabd',
        6: 'cdfgeb',
        4: 'eafb',
        0: 'cagedb',
        1: 'ab'
    }
    for entry in data:
        pattern = entry['pattern']
        output = entry['output']

        values = {i: None for i in range(10)}

        for p in pattern:
            number = lengths.get(len(p))
            if number:
                values[number] = p

        top = [i for i in values[7] if i not in values[1]]
        print(top)
        tl_or_m = [i for i in values[4] if i not in values[1] + values[7]]
        print(tl_or_m)

        print(values)
        remaining = [p for p in pattern if p not in values.values()]
        print(remaining)



        # for number in remaining:


def load_data(file: str):
    with open(file, 'r') as f_in:
        return [
            dict(pattern=a.split(), output=b.split())
            for a, b
            in [item.split(' | ')
                for item
                in f_in.readlines()]
        ]


if __name__ == '__main__':
    main()
