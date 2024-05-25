

def calc(age, height, weight, gend, coef):
    gender = {'m': 5, 'f': -161}
    c = {'1': 1.2, '2': 1.375, '3': 1.55, '4': 1.725, '5': 1.9}
    ccal = ((10 * weight) + (6.25 * height) - (5 * age) + gender[gend]) * c[coef]
    print(ccal)
    return ccal

