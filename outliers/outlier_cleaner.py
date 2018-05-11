#!/usr/bin/python


def takeError(a):
    return a[2]

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """
    errors = [abs(predictions[i]-net_worths[i]) for i in range(len(net_worths))]

    # top_errors = list(sorted(errors, reverse=True))[:len(errors)//10]

    data = [(ages[i], net_worths[i], errors[i]) for i in range(len(net_worths))]

    cleaned_data = list(sorted(data, key=takeError))[:len(errors)*9//10]


    return cleaned_data

