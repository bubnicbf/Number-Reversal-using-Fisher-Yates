import random
 
print(__doc__)
data, trials = list('123456789'), 0
while data == sorted(data):
    random.shuffle(data)
while data != sorted(data):
    trials += 1
    flip = int(input('#%2i: LIST: %r Flip how many?: ' % (trials, ' '.join(data))))
    data[:flip] = reversed(data[:flip])
 
print('\nYou took %2i attempts to put the digits in order!' % trials)
