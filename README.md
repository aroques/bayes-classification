## Naive Bayes Classification

![Image of Bayes Theorem](http://www.saedsayad.com/images/Bayes_rule.png)


The Naive Bayesian classifier is based on Bayes’ theorem with independence assumptions between predictors. A Naive Bayesian model is easy to build, with no complicated iterative parameter estimation which makes it particularly useful for very large datasets. Despite its simplicity, the Naive Bayesian classifier often does surprisingly well and is widely used because it often outperforms more sophisticated classification methods.
_Source: http://www.saedsayad.com/naive_bayesian.htm_

This implementation assumes the class we are trying to predict is binary and that there is only one binary, categorical, and continuous column (in that order) in the data.

To run this program:

```
python3.6 naive-bayes.py
```
Predicting (True, 'Single', 125000.0)
Will be a defaulted borrower: No
Actual value: No

Predicting (False, 'Married', 100000.0)
Will be a defaulted borrower: No
Actual value: No

Predicting (False, 'Single', 70000.0)
Will be a defaulted borrower: No
Actual value: No

Predicting (True, 'Married', 120000.0)
Will be a defaulted borrower: No
Actual value: No

Predicting (False, 'Divorced', 95000.0)
Will be a defaulted borrower: No
Actual value: Yes

Predicting (False, 'Married', 60000.0)
Will be a defaulted borrower: No
Actual value: No

Predicting (True, 'Divorced', 220000.0)
Will be a defaulted borrower: No
Actual value: No

Predicting (False, 'Single', 85000.0)
Will be a defaulted borrower: Yes
Actual value: Yes

Predicting (False, 'Married', 75000.0)
Will be a defaulted borrower: No
Actual value: No

Predicting (False, 'Single', 90000.0)
Will be a defaulted borrower: Yes
Actual value: Yes

Predicting (1, 'Married', 50700.0)
Will be a defaulted borrower: No
Test vector, so no actual value

