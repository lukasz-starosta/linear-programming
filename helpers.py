def add_row(row1, row2):
    row_sum = [0 for i in range(len(row1))]
    for i in range(len(row1)):
        row_sum[i] = row1[i] + row2[i]
    return row_sum


def max_index(row):
    max_i = 0
    for i in range(0, len(row) - 1):
        if row[i] > row[max_i]:
            max_i = i

    return max_i


def multiply_const_row(const, row):
    mul_row = []
    for i in row:
        mul_row.append(const * i)
    return mul_row


def min_index(row):
    min_i = 0
    for i in range(0, len(row)):
        if row[min_i] > row[i]:
            min_i = i

    return min_i


def print_table(table):
    print()
    for row in table:
        row_str = '|'
        for column in row:
            if column >= 0:
                row_str += ' '
            if column.numerator == 0:
                row_str += ' 0 '
            elif column.denominator == 1:
                row_str += ' ' + str(column.numerator) + ' '
            else:
                row_str += str(column.numerator) + '/' + str(column.denominator)
            row_str += '  | '

        print(row_str)
    print()
