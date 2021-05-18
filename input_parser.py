filename = 'examples.txt'


class InputParser:
    def __init__(self):
        self.examples = []

        file = open(filename, 'r')
        lines = file.readlines()

        count = 0

        for line in lines:
            count += 1
            # Strips the newline character
            line = line.strip()

            if count == 1:
                minmax, num_vars = line.split(' ')
                example = {'num_vars': int(num_vars), 'type': minmax, 'objective': '', 'constraints': []}
                continue
            if count == 2:
                example['objective'] = line
                continue
            if count == 3:
                continue

            if line != '':
                example['constraints'].append(line)
                continue

            self.examples.append(example)
            count = 0

    def print_examples(self):
        for e in self.examples:
            print(e)

    # Przykład 1 to example[0]
    def get_example(self, number):
        return self.examples[number - 1]
