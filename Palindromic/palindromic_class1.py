import copy

class Palindromic:
    def __init__(self):
        self.palindromic  = None
        self._palindromic = None     
        self.s_value      = ''

    def analyze(self, n):
        palindromics = []
        numbers = self.make_range(n)
        for a in numbers:
            for b in numbers:
                self.check_palindromic(self.to_string(a, b))
                if self.check_palindromic(self.to_string(a, b)) != False:
                    palindromics.append(self._palindromic)
        self.palindromic = max(palindromics)        

    def make_range(self, n):
        first_value = int('9' * (n - 1))
        last_value  = int('9' * n)
        numbers = range(first_value + 1, last_value + 1)
        numbers.reverse()

        return numbers

    def to_string(self, a, b):
        self.s_value = str(a * b)
        len_s = len(self.s_value)

        return self.s_value

    def check_palindromic(self, value):
        list_v   = [self.s_value[k] for k in range(len(self.s_value))]
        list_v_r = copy.deepcopy(list_v)
        list_v_r.reverse()
        if list_v == list_v_r:
            self._palindromic = int("".join(list_v))
            return self._palindromic

        return False    

    def __str__(self):
        return "%d" %self.palindromic

if __name__ == "__main__":
    one = Palindromic()
    one.analyze(2)
    print(one)
