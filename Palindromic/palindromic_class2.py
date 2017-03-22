class Palindromic:
    def __init__(self, n):
        self.palindromic = None
        self.first_value = 0
        self.last_value  = 0
        self.n           = n

    def analyze(self):
        palindromics = []
        numbers = self.make_range()
        for a in numbers:
            for b in numbers:
                value = a * b
                if self.check_palindromic(value) == True:
                    palindromics.append(value)
        self.palindromic = max(palindromics)

    def make_range(self):
        self.first_value = int('1'+('0'*(self.n - 1)))
        self.last_value  = int('9' * self.n)
        numbers = range(self.first_value , self.last_value + 1)

        return numbers

    def check_palindromic(self, value):
        value_s = str(value)
        if len(str(value)) / 2 == 1: 
            half1 = value // self.first_value
            _half1 = str(half1)
            half2 = value_s[-self.n:]
            if _half1 == half2[::-1]:
                return True
        else:  
            half1 = value // (self.last_value + 1)
            _half1 = str(half1)
            half2 = value_s[-self.n:]
            if _half1 ==half2[::-1]:
                return True

    def __str__(self):
        return "%d" %self.palindromic

if __name__ == "__main__":
    one = Palindromic(2)
    one.analyze()
    print(one)
