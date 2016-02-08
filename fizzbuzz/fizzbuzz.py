class FizzBuzz(object):

    def value(self, value):
        if value%15 == 0:
            return 'fizzbuzz'
        if value%5 == 0:
            return 'buzz'
        if value%3 == 0:
            return 'fizz'
        return value
