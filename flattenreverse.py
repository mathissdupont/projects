def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def deep_reverse(lst):
    if isinstance(lst, list):
        return [deep_reverse(item) for item in reversed(lst)]
    else:
        return lst



