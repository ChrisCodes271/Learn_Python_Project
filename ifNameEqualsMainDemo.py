# if __name__ = '__main__'

# With if name = main we are checking if something is being run

# Module can be run as standalone program
# Can also be imported

# Interpreter sets 'special var', one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if it's the initial module being run

#import module_two
#print(__name__)
#print(ifNameEqualsMainDemo.__name__)

if __name__ == '__main__':
    print('Running directly')
else:
    print('Running indirectly')