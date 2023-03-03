def get_frequency():
    with open("input.txt") as _file:
        frequency = 0
        for line in _file.readlines():
            operator = line[0]
            number = int(line[1:])

            if operator == "+":
                frequency += number
            elif operator == "-":
                frequency -= number

        return frequency


if __name__ == "__main__":
    freq = get_frequency()
    print(freq)
