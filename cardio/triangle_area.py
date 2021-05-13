import math


def check_triangle_type(s):
    if s[0] + s[1] < s[2] or s[1] + s[2] < s[0] or s[0] + s[2] < s[1]:
        return None
    elif s[0] == s[1] and s[1] == s[2] and s[2] == s[0]:
        return "Equilateral"
    elif s[0] == s[1] or s[1] == s[2] or s[2] == s[0]:
        return "Isosceles"
    else:
        return "Escalene"


def triangle(base, height, s):
    # try:
    area = base * height / 2
    if s is not None and len(s) == 3:
        # Optionally, check type of triangle if sides (s) are provided
        triangle_type = check_triangle_type(s)
        if not triangle_type:
            print("You did not provide a valid triangle")
            return None
        elif base not in s:
            print(
                "The base you provided is not equal to one of the sides of the triangle"
            )
            return None
        else:
            '''
            Apply Heron's formula to check if area calculaded with base and height 
            corresponds to the sides provided
            '''
            s_p = sum(s) / 2  # s_p stands for semi_perimeter
            heron = math.sqrt(s_p * (s_p - s[0]) * (s_p - s[1]) * (s_p - s[2]))
            if round(area, 2) == round(heron, 2):
                return f"The area of your {triangle_type} triangle is {area}"
            else:
                print("You did not provide a valid triangle")
                return None
    elif s is None:
        return f"The area of your triangle is {area}"


def run():
    message = None
    print('Welcome, this tool helps you calculate the area of triangles')
    while not message:
        base = float(input('Provide the base of the triangle: '))
        height = float(input('Provide the height of the triangle: '))
        sides = input(
            'Optionally, type the sides of the triangle separated by commas, or "skip": ')

        if sides != 'skip':
            sides = [float(x) for x in sides.split(',')]
            message = triangle(base, height, sides)
    print(message)


if __name__ == "__main__":
    run()
