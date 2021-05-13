def check_range(lower, upper, to_check):
    if lower <= to_check and upper >= to_check:
        return True
    elif lower > to_check or upper < to_check:
        return False


def run():
    try:
        in_range = False
        bounds = input(
            'Type the lower and upper bounds of your numeric range separated by commas: ')
        bounds = [float(bound) for bound in bounds.split(',')]
        while not in_range:
            to_check = float(
                input(f'Type the number you want to check if in the range [{bounds[0]}, {bounds[1]}]: '))
            in_range = check_range(bounds[0], bounds[1], to_check)
            if not in_range:
                print(
                    f'The number {to_check} is not in the range [{bounds[0], bounds[1]}]')
            else:
                print(
                    f'The number {to_check} is in the range [{bounds[0]}, {bounds[1]}]')
    except (ValueError, IndexError):
        print('Please type a valid number or set of numbers separated by commas')


if __name__ == '__main__':
    run()
