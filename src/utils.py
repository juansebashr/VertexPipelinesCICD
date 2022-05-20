"""
Script with util functions
"""


def get_value(parameter):
    value_type = list(parameter.keys())[0]
    if value_type == 'intValue':
        return int(parameter[value_type])
    elif value_type == 'doubleValue':
        return float(parameter[value_type])
    elif value_type == 'floatValue':
        return float(parameter[value_type])
    elif value_type == 'boolValue':
        return bool(parameter[value_type])
    elif value_type == 'stringValue':
        return str(parameter[value_type])
    else:
        raise ValueError()
