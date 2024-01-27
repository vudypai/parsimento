
def octave_rule(degrees):
    figures = [0] * len(degrees)
    for i in range(len(degrees)):
        if degrees[i] == 4:
            if degrees[i - 1] == 5:
                figures[i] = "6/4/2"
            elif degrees[i + 1] == 5:
                figures[i] = "6/5/3"
            else:
                figures[i] = "5/3"

        if degrees[i] == 6:
            if degrees[i + 1] == 7:
                figures[i] = "6/3"
            elif degrees[i + 1] == 5:
                figures[i] = "#6/5/3"
            else:
                figures[i] = "5/3"

        if degrees[i] == 1 or degrees[i] == 5:
            figures[i] = "5/3"
        if degrees[i] == 2:
            figures[i] = "6/4/3"
        if degrees[i] == 3 or degrees[i] == 7:
            figures[i] = "6/3"

    return figures
