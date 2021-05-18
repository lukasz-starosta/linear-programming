import sys

from input_parser import InputParser
from scipy.optimize import linprog

from simplex import Simplex

if __name__ == '__main__':
    parser = InputParser()

    try:
        if sys.argv[1] != '' and 0 < int(sys.argv[1]) < 10:
            idx = int(sys.argv[1])
            example = parser.get_example(idx)
            print(f'Przykład to: {example}')
        else:
            raise Exception()
    except:
        print('Podaj numer przykładu (od 1 do 9).')
        exit(1)

    try:
        simplex = Simplex(num_vars=example['num_vars'], objective_function=(example['type'], example['objective']),
                          constraints=example['constraints'])
        print(simplex.solution, simplex.optimize_val)
    except ValueError as e:
        print(e)

    if idx == 1:
        scipy_result = linprog(c=[2, 1], A_ub=[[-1, -1], [-1, -2]], b_ub=[-3, -4], method='simplex')
    elif idx == 2:
        scipy_result = linprog(c=[5, 4, 6], A_eq=[[1, 0, 0], [0, 1, 0], [0, 0, 5]], b_eq=[20, 6, 15], method='simplex')
    elif idx == 3:
        scipy_result = linprog(c=[200, 100], A_ub=[[-3, 0], [0, -2]], b_ub=[-9, -4], method='simplex')
    elif idx == 4:
        scipy_result = linprog(c=[200, 100], A_ub=[[-3, -1], [-1, -2]], b_ub=[-6, -4], method='simplex')
    elif idx == 5:
        scipy_result = linprog(c=[-5, -3], A_ub=[[3, 5], [5, 2]], b_ub=[15, 10], method='simplex')
    elif idx == 6:
        scipy_result = linprog(c=[-1, 1, 0], A_ub=[[6, -1, 0], [-1, -5, 0]], b_ub=[10, -4], A_eq=[[1, 5, 1]],
                               b_eq=[5],
                               method='simplex')
    elif idx == 7:
        # Prints OK result, should be an error
        scipy_result = linprog(c=[-1, 0], A_ub=[[-1, -1]], b_ub=[-6], method='simplex')
    elif idx == 8:
        # Prints OK result, should be an error
        scipy_result = linprog(c=[5, 4, 6], A_eq=[[1, 0, 0], [0, 1, 0], [0, 0, 5], [1, 1, 1]], b_eq=[20, 6, 15, 10],
                               method='simplex')
    elif idx == 9:
        scipy_result = linprog(c=[-1, -1], A_ub=[[1, 0], [0, -1]], b_ub=[4, 4], A_eq=[[1, 1]], b_eq=[6],
                               method='simplex')

    print('\nScipy result:')
    print(f'Optimal point is {scipy_result.x}')
    print(f'Optimal value is {scipy_result.fun}')
