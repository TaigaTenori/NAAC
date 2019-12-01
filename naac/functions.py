# helper functions


# get experience needed for character level x
def get_exp_for_level(x):
    return int(50/3*(x**3 - 6*x**2 + 17*x - 12))
