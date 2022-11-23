import math
from scipy import integrate


def C(m, n):
    return (math.factorial(n))/(math.factorial(m) * math.factorial(n-m))


def p(m, n):
    return(m/n)


def bernoulli(m, n, prob):
    return (C(m,n)*math.pow(prob, m)*math.pow(1-prob,n-m))


def gauss_func(m, n, prob):
    return ((m-n*prob)/(math.sqrt(n*prob*(1-prob))))


def gauss_table(x):
    return (1/math.sqrt((2*math.pi)))*math.exp(-x**2/2)


def f(x):
    return math.exp(-x**2/2)


def laplass_table(x):
    integral = integrate.quad(f, 0, x)[0]
    return (1/math.sqrt((2*math.pi))) * integral


def moivre_laplace(m, n, prob):
    return (1/math.sqrt(n * prob * (1-prob)) * gauss_table(gauss_func(m, n, prob)))


def integral_func(m1, m2, n, prob):
    return laplass_table(gauss_func(m2, n, prob)) - (laplass_table(gauss_func(m1, n, prob)))


def tasks(n, prob):
    q = 1 - prob
    m1 = (n * prob) - q
    m2 = (n * prob) + prob
    b = (m2 - m1) / 2
    return round(m1+b)


print("Task 1")
print("Probability: ", round(bernoulli(3, 5, 0.2), 5), "or", str(round(bernoulli(3, 5, 0.2) * 100, 2)) + "%")

print("\nTask 2")
print("a) (4 times)  \nProbability:", bernoulli(4, 5, 0.8), "or", str(bernoulli(4, 5, 0.8) * 100) + "%")
print("b) (more or equal than 4 times)"
      "  \nProbability:", 1 - bernoulli(1, 5, 0.8) - bernoulli(2, 5, 0.8) - bernoulli(3, 5, 0.8),
      "or", str((1 - bernoulli(1, 5, 0.8) - bernoulli(2, 5, 0.8) - bernoulli(3, 5, 0.8)) * 100) + "%")

print("\nTask 3")
print("Probability: ", round(moivre_laplace(80, 400, 0.2), 4), "or",
      str(round(moivre_laplace(80, 400, 0.2) * 100, 2)) + "%")

print("\nTask 4")
print("Probability: ", round(moivre_laplace(5, 100000, 0.0001), 4), "or",
      str(round(moivre_laplace(5, 100000, 0.0001) * 100, 2)) + "%")

print("\nTask 5")
print("Probability: ", round(integral_func(228, 252, 600, 0.4), 4), "or", str(round(integral_func(228, 252, 600, 0.4) * 100, 2)) + "%")

print("\nTask 6")
print("The most likely number: ", tasks(100, 0.4))

print("\nTask 7")
print("Probability: ", round(integral_func(0, 170, 4000, 0.04), 2), "or", str(round(integral_func(0, 170, 4000, 0.04) * 100)) + "%")

print("\nTask 8")
print("Probability: ", round(moivre_laplace(5000, 10000, 0.5), 5), "or",
      str(round(moivre_laplace(5000, 10000, 0.5) * 100, 3)) + "%")

print("\nTask 9")
print("Probability: ", round(moivre_laplace(5, 1000, 0.002), 5), "or",
      str(round(moivre_laplace(5, 1000, 0.002) * 100, 3)) + "%")

print("\nTask 10")
print("The most likely number: ", tasks(150, 0.03))