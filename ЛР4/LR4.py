import math

def combinations(n, m):
    return math.factorial(n)/(math.factorial(m)*math.factorial(n-m))


def task1(black, brown, red, blue):
    return ((red + blue)/(black + brown + red + blue))


def p5(p1, p2, p3, p4):
    return 1 - p1 - p2 - p3 - p4


def task5(total, choose, take):
    return (choose**take/total**take)


def p_ab(prob1, prob2):
    return (prob1 * prob2)


def prob7task(count, prep, total_count, best_mark):
    return (count / total_count) * (prep / best_mark) * ((prep - 1) / (best_mark - 1)) * ((prep - 2) / (best_mark - 2))


def task7(CountBest, CountGood, CountMiddle, CountBad, PrepBest, PrepGood, PrepMiddle, PrepBad, TotalCount, BestMark, mark):
    bestProb = prob7task(CountBest, PrepBest, TotalCount, BestMark)
    goodProb = prob7task(CountGood, PrepGood, TotalCount, BestMark)
    middleProb = prob7task(CountMiddle, PrepMiddle, TotalCount, BestMark)
    badProb = prob7task(CountBad, PrepBad, TotalCount, BestMark)
    totalProb = bestProb + goodProb + middleProb + badProb
    match mark:
        case "Best":
            return (bestProb / totalProb)
        case "Good":
            return (goodProb / totalProb)
        case "Middle":
            return (middleProb / totalProb)
        case "Bad":
            return (badProb / totalProb)
        case _:
            return print("Wrong mark")


def prob(first, second, third, probFrist, probSecond, probThird):
    return first * probFrist + second * probSecond + third * probThird


def task9(first, second, third, probFrist, probSecond, probThird):
        return (prob(second,0, 0, probSecond, 0, 0))/(prob(first, second, third, probFrist, probSecond, probThird))


def task10(first, second, probFrist, probSecond):
    return (prob(first,0, 0, probFrist, 0, 0))/(prob(first, second, 0, probFrist, probSecond, 0))


print("Task 1\nProbability:",
      task1(40, 26, 22, 12),
      "or",
      str(round(task1(40, 26, 22, 12) * 100)) + "%")


print("\nTask 2\nProbability:",
      (combinations(8, 2) + combinations(8, 1))/combinations(10, 2),
      "or",
      str(round(((combinations(8, 2) + combinations(8, 1))/combinations(10, 2)) * 100)) + "%")


print("\nTask 3\nProbability:",
      round((1 - (combinations(8, 3)/combinations(10, 3))), 4),
      "or",
      str(round((1 - (combinations(8, 3)/combinations(10, 3)))*100, 2)) + "%")


print("\nTask 4\nProbability:",
      round(p5(0.15, 0.25, 0.2, 0.1), 4),
      "or",
      str(round(p5(0.15, 0.25, 0.2, 0.1) * 100)) + "%")


print("\nTask 5\nProbability:",
      round(task5(120, 80, 2), 2),
      "or",
      str(round(task5(120, 80, 2) * 100)) + "%")


print("\nTask 6\nProbability:",
      round(p_ab(0.9, 0.8), 2),
      "or",
      str(round(p_ab(0.9, 0.8) * 100, 2)) + "%")


print("\nTask 7", "\nProbability of the best mark:",
      round(task7(3, 4, 2, 1, 20, 16, 10, 5, 10, 20, "Best"), 4),
      "or",
      str(round(task7(3, 4, 2, 1, 20, 16, 10, 5, 10, 20, "Best") * 100, 2)) + "%",

      "\nProbability of bad mark:",
      round(task7(3, 4, 2, 1, 20, 16, 10, 5, 10, 20, "Bad"), 4),
      "or",
      str(round(task7(3, 4, 2, 1, 20, 16, 10, 5, 10, 20, "Bad") * 100, 2)) + "%")


print("\nTask 8\nProbability:",
      round(prob(0.4, 0.3, 0.3, 0.9, 0.95, 0.95), 2),
      "or",
      str(round(prob(0.4, 0.3, 0.3, 0.9, 0.95, 0.95)*100)) + "%")


print("\nTask 9\nProbability:",
      round(task9(0.4, 0.3, 0.3, 0.8, 0.7, 0.85), 4),
      "or",
      str(round(task9(0.4, 0.3, 0.3, 0.8, 0.7, 0.85) * 100, 2)) + "%")


print("\nTask 10\nProbability:",
      round(task10(0.3, 0.7, 0.9, 0.8), 4),
      "or",
      str(round(task10(0.3, 0.7, 0.9, 0.8) * 100, 2)) + "%")