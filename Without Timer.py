"""
Gauss:
50 pairs of numbers that added up to 100: 1 + 99, 2 + 98, 3 + 97, and so on, until 49 + 51.
Since 50 × 100 is 5,000, when you add that middle 50, the sum of all the numbers from 0 to 100 is 5,050.
"""
while True:
    total = 0
    try:
        num = int(input('Type in the number you want to add up to: '))
        for times in range(num+1):
            total = total + times
            new_total = total + times
            print(f'Total: {new_total} = {total} + {times}')
        print(total)
    except ValueError:
        print('Only accepts integers!')
    except TypeError:
        print('Only accepts integers!')
        """Loop for picking another number"""
    finally:
        choice = input('Want to do for another number?:\n<Any Key> Yes | <X> Exit\n')
        if choice.lower() in {'x'}:
            break
        else:
            continue
