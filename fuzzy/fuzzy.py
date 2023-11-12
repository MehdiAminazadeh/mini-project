class FuzzySet:
    def __init__(self, membership_function):
        self.membership_function = membership_function

    def membership(self, x):
        return self.membership_function(x)

class FuzzyFunction:
    def __init__(self, fuzzy_set_1, fuzzy_set_2, operation):
        self.fuzzy_set_1 = fuzzy_set_1
        self.fuzzy_set_2 = fuzzy_set_2
        self.operation = operation

    def apply(self, z):
        return max(min(self.fuzzy_set_1.membership(x1), self.fuzzy_set_2.membership(z - x1)) for x1 in range(-10, 11))

# membership function
# define MU * X1  ------- MU * X2
def mu_X1(x):
    if -1 <= x <= 1:
        return x ** 2
    else:
        return 0

def mu_X2(x):
    return max(0, 1 - abs(x) / 0.5)
