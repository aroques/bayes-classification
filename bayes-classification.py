
from Dataset import Dataset

# pass in a vector [categorical, continuous]


def main():
    csv_file = 'test_set.csv'
    column_type = ['binary', 'categorical', 'continuous', 'binary']
    dataset = Dataset(csv_file, column_type)

    print(dataset.columns)
    print(dataset.rows)
    print(dataset.cls)

    print(dataset.columns_that_are('continuous'))

    column_probability = []  # Holds P (A | C) and P (A | not C) tuple for each column A

    for column in dataset.columns_that_are('binary'):
        true_count = 0
        for attr_value, class_value in zip(column, dataset.cls):
            if class_value:
                true_councot += 1
        prob_true = true_count / len(column)
        prob_false = 1 - prob_true
        prob_tuple = (prob_true, prob_false)
        column_probability.append(prob_tuple)

    for column in dataset.columns_that_are('categorical'):
        categories = set(column)
        print(categories)

    print(column_probability)

    # classes = set(dataset.columns['Defaulted Borrower'])

    # lets handle discrete first

    probability = {}
    #
    # for categorical_column in dataset.attributes['categorical']:
    #     categories = set(dataset.columns[categorical_column])
    #     d = {category: {cls: 0 for cls in classes} for category in categories}
    #     for attr, cls in zip(dataset.columns[categorical_column], dataset.columns['Defaulted Borrower']):
    #         d[attr][cls] += 1
    #     print(d)


if __name__ == '__main__':
    main()

