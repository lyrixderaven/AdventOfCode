import md5
import sys

base = 'bgvyzdsv'
counter = 1

while True:
    current = '{}{}'.format(base, counter)
    m = md5.new()
    m.update(current)
    if m.hexdigest().startswith('000000'):
        print counter, current, m.hexdigest()
        sys.exit(0)
    counter += 1
