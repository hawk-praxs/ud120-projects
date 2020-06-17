#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    error = [abs(net_worths[i]-predictions[i]) for i in range(len(net_worths))]

    for i in range(len(net_worths)):
        if error[i] <= 80:
            cleaned_data.append((ages[i], net_worths[i], error[i]))

    return cleaned_data

