import re
import copy

def try_int_cast(value):
    """
    Attempts to cast value to an int. On failure, returns original value
    """
    try: 
        return int(value)
    except:
        return value

def _natural_sort_key(value):
    """
    Used internally to get a tuple by which value is sorted.
    """
    return map(try_int_cast, re.findall(r'(\d+|\D+)', value))

def natural_sort_comparison(value1, value2):
    """
    Natural string comparison, case sensitive.
    """
    return cmp(_natural_sort_key(value1), _natural_sort_key(value2))

def natural_sort_case_insensitive_comparison(value1, value2):
    """
    Natural string comparison, ignores case.
    """
    return natural_sort_comparison(value1.lower(), value2.lower())

def natural_sort(sequence, comparison_callable=natural_sort_comparison):
    """
    In-place natural string sort.
    """
    sequence.sort(comparison_callable)

def natural_sorted(sequence, comparison_callable=natural_sort_comparison):
    """
    Returns a copy of seq, sorted by natural string sort.
    """
    temp = copy.copy(seq)
    natsort(temp, comparison_callable)
    return temp
