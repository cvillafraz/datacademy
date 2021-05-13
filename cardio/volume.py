import math


def calc_volume(choice, params):
    if choice == 1:
        # Volume of a cylinder: pi*r^2*h
        return params[0]**2*math.pi*params[1]
    elif choice == 2:
        return 3/4*math.pi*params[0]**3
    elif choice == 3:
        return math.pi*params[0]**2*params[1]/3
    elif choice == 4:
        return params[0]**3


def run():
    shapes = {
        1: {
            'name': 'cylinder',
            'params': 'radius and height seperated by commas. Example: 1,1'
        },
        2: {
            'name': 'sphere',
            'params': 'radius'
        },
        3: {
            'name': 'cone',
            'params': 'radius and height seperated by commas. Example: 1,1'
        },
        4: {
            'name': 'cube',
            'params': 'side lenght'
        }
    }
    print('Calculate the volume of one of the following shapes.')
    print('1. Cylinder\n2. Sphere\n3. Cone\n4. Cube')
    volume = None
    while volume is None:
        try:
            choice = int(input('Type the number of the shape: '))
            shape_name = shapes[choice]['name']
            params = input(
                f"To calculate the volume of your {shape_name}, type the {shapes[choice]['params']}: ")
            params = [float(x) for x in params.split(',')]
            volume = round(calc_volume(choice, params), 2)
            print(
                f'The volume of your {shape_name} is {volume}')
        except (ValueError, IndexError):
            print('Please type a valid number or set of numbers separated by commas')


if __name__ == '__main__':
    run()
