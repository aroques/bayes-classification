from operator import add
from Dataset import Dataset
from statistics import mean, stdev
from math import pow, sqrt, pi, e


def main():
    csv_file = 'train_set.csv'
    column_type = ['binary', 'categorical', 'continuous', 'binary']
    dataset = Dataset(csv_file, column_type)
    test_vector = (1, 'Married', 50700.0)

    # Handle binary
    binary_column_prob = get_binary_column_prob(dataset)

    # Handle categorical
    categorical_column_prob = get_categorical_column_prob(dataset)

    # Handle continuous column
    continuous_column_by_class = get_continuous_column_by_class(dataset)

    test_set = dataset.rows
    test_set.append(test_vector)

    # Declare index  variable that will be use in proceeding loop
    binary_column_idx = 0
    categorical_column_idx = 1
    continuous_column_idx = 2
    cls_idx = 3
    true_idx = 0
    false_idx = 1

    for i, row in enumerate(test_set):

        p1 = binary_column_prob[row[binary_column_idx]]
        p2 = categorical_column_prob[row[categorical_column_idx]]

        continuous_val = row[continuous_column_idx]
        prob_true = gaussian_pdf(continuous_column_by_class[true_idx], continuous_val)
        prob_false = gaussian_pdf(continuous_column_by_class[false_idx], continuous_val)
        p3 = (prob_true, prob_false)

        # Now predict
        prob_true = p1[true_idx] * p2[true_idx] * p3[true_idx]
        prob_false = p1[false_idx] * p2[false_idx] * p3[false_idx]

        test_vector = (row[binary_column_idx], row[categorical_column_idx], row[continuous_column_idx])
        print('Predicting {}'.format(test_vector))

        if prob_true > prob_false:
            print('Will be a defaulted borrower: {}'.format('Yes'))
        else:
            print('Will be a defaulted borrower: {}'.format('No'))
        if i < len(test_set) - 1:
            actual_value = row[cls_idx]
            if actual_value:
                actual_value = 'Yes'
            else:
                actual_value = 'No'
            print('Actual value: {}'.format(actual_value))
        else:
            print('Test vector, so no actual value')

        print()


def get_binary_column_prob(dataset):
    """Returns a probability tuples for binary class = True and binary class = False
        for the binary column in the dataset"""
    binary_column = dataset.columns_that_are('binary')[0]
    a_count = 0
    not_a_count = 0
    for attr_value, class_value in zip(binary_column, dataset.cls):
        if attr_value and class_value:
            a_count += 1
        if not attr_value and class_value:
            not_a_count += 1

    if a_count == 0:
        laplace_smoothing = True
        a_count += 1
    if not_a_count == 0:
        laplace_smoothing = True
        not_a_count += 1

    if laplace_smoothing:
        num_values = len(binary_column) + 1
    else:
        num_values = len(binary_column)

    prob = {True: (0, 0), False: (0, 0)}

    prob_a_given_true = a_count / num_values
    prob_a_given_false = 1 - prob_a_given_true
    prob[True] = (prob_a_given_true, prob_a_given_false)

    prob_not_a_given_true = not_a_count / num_values
    prob_not_a_given_false = 1 - prob_not_a_given_true
    prob[False] = (prob_not_a_given_true, prob_not_a_given_false)

    return prob


def get_categorical_column_prob(dataset):
    """Returns probability tuples for each category in categorical column"""
    categorical_column = dataset.columns_that_are('categorical')[0]
    categories = list(set(categorical_column))
    num_true = dict.fromkeys(categories, 0)

    # Count num true
    for attr_value, class_value in zip(categorical_column, dataset.cls):
        if class_value:
            num_true[attr_value] += 1

    # Laplace smooth if needed
    if any(v == 0 for k,v in num_true.items()):
        laplace_smoothing = True
        num_true = {k: add(v, 1) for k, v in num_true.items()}

    if laplace_smoothing:
        num_values = len(categorical_column) + 1
    else:
        num_values = len(categorical_column)

    prob = dict.fromkeys(categories)

    for k, v in num_true.items():
        prob_true = v / num_values
        prob_false = 1 - prob_true
        prob_tuple = (prob_true, prob_false)
        prob[k] = prob_tuple

    return prob


def gaussian_pdf(column, x):
    """Gaussian probability density function that
        uses values in column to calculate probability of x"""
    sigma = stdev(column)
    variance = pow(sigma, 2)
    mu = mean(column)
    numerator = pow((x - mu), 2)
    denominator = 2 * variance
    return (1 / (sqrt(2 * pi * variance))) * pow(e, -(numerator / denominator))


def get_continuous_column_by_class(dataset):
    """Separates continuous column by binary class"""
    # Separate continuous column by class
    continuous_column = dataset.columns_that_are('continuous')[0]
    continuous_true = []
    continuous_false = []
    for cont_value, class_value in zip(continuous_column, dataset.cls):
        if class_value:
            continuous_true.append(cont_value)
        else:
            continuous_false.append(cont_value)

    continuous_column_by_class = [continuous_true, continuous_false]
    return continuous_column_by_class


if __name__ == '__main__':
    main()