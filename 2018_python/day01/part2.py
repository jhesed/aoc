def get_frequency(frequencies: set = None, current_frequency: int = 0) -> int:
    with open("input.txt") as _file:

        if not frequencies:
            # Initialization step
            frequencies = {0}

        for line in _file.readlines():
            operator = line[0]
            number = int(line[1:])

            if operator == "+":
                current_frequency += number
            elif operator == "-":
                current_frequency -= number

            # Terminating condition
            if current_frequency in frequencies:
                print(frequencies)
                return current_frequency

            frequencies.add(current_frequency)

    # Recursive step
    return get_frequency(frequencies, current_frequency)


if __name__ == "__main__":
    freq = get_frequency()
    print(freq)
