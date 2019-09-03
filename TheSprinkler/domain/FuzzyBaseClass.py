
class FuzzyBaseClass:

    def triangleMethod(self, val, a, b, c):
        if a == b and b == c:
            result = 1
        elif a == b:
            result = max(0, min(1, (c - val)/(c - b)))
        elif b == c:
            result = max(0, min((val - a)/(b - a), 1))
        else:
            result = max(0, min((val - a)/(b - a), 1, (c - val)/(c - b)))

        return result

    def trapezoidMethod(self, val, a ,b ,c ,d):
        if a == b and d == c:
            result = 1
        elif a == b:
            result = max(0, min(1, (d - val)/(d - c)))
        elif d == c:
            result = max(0, min((val - a)/(b - a), 1))
        else:
            result = max(0, min((val - a)/(b - a), 1, (d - val)/(d - c)))

        return result