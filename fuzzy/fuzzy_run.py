from fuzzy import *

if __name__ == "__main__":
    fuzzy_set_X1 = FuzzySet(mu_X1)
    fuzzy_set_X2 = FuzzySet(mu_X2)
    fuzzy_function_B = FuzzyFunction(fuzzy_set_X1, fuzzy_set_X2, operation=None)

    mu_B_0 = fuzzy_function_B.apply(0)
    mu_B_1 = fuzzy_function_B.apply(1)
    print(f"mu_B(0) = {mu_B_0}")
    print(f"mu_B(1) = {mu_B_1}")

    # the core of B
    core_B = [z for z in range(-10, 11) if fuzzy_function_B.apply(z) == 1]
    print(f"Core of B: {core_B}")