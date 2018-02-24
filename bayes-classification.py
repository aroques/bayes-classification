
from Dataset import Dataset




def main():
    csv_file = 'test_set.csv'

    dataset = Dataset(csv_file)

    print(dataset.columns)
    print(dataset.rows)
    print(dataset.cls)

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

