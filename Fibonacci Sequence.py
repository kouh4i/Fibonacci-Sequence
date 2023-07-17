def fibonacci(x):
    if x <= 1:
        return x
    else:
        return (fibonacci(x-1)+fibonacci(x-2))

range_seq = input('How far do you want to see the sequence?')

try:
    if int(range_seq) <= 0:
        print('put a natural number higher than 0')
    else:
        print('Fibonacci Sequence: ')
        for x in range(int(range_seq)):
            print(fibonacci(x))
except Exception as e:
    print('Error:\t {}'.format(e))

