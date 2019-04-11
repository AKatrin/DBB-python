class Operators:

    @staticmethod
    def perform_operation(f, s, o):
        res = 0
        if o == '+':
            res = f + s
        elif o == '-':
            res = f - s
        elif o == '*':
            res = f * s
        elif o == '/':
            res = f / s
        else:
            res = 0
        return res
