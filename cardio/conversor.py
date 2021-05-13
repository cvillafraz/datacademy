def conversor(choice, quantity):
    if choice == 1:
        return quantity*1.609344
    elif choice == 2:
        return quantity*0.6213712


def run():
    print('Welcome to distance conversor, you can convert from miles to km or viceversa')
    value = 0
    choice = 0
    quantity = 0
    while value == 0:
        choice = int(
            input('Type 1 for miles to km, or type 2 for km to miles: '))
        quantity = float(input('Type how much you want to convert: '))
        value = conversor(choice, quantity)
    if choice == 1:
        print(f"{quantity} miles = {value} km")
    elif choice == 2:
        print(f"{quantity} km = {value} miles")


if __name__ == '__main__':
    run()
