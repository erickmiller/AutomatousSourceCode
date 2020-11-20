import logging
import logging.handlers


logging.basicConfig(
    level=logging.DEBUG,
    format='LINE %(lineno)-4d  %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    filename="tree" + ".log",
    filemode='w')


def quick_sort(array, p, r):
    logging.info(array)
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)


def partition(be_sorted, pivot, last_element):
    x = be_sorted[last_element]
    i = pivot - 1  # what's the i doing?
    for j in range(pivot, last_element):
        print(be_sorted)
        if be_sorted[j] < x:
            i += 1
            be_sorted[j], be_sorted[i] = be_sorted[i], be_sorted[j]
    i += 1
    be_sorted[i], be_sorted[last_element] = be_sorted[last_element], be_sorted[i]
    return i


if __name__ == "__main__":
    be_sorted = [1, 99, 5, 23, 64, 7, 23, 6, 34, 98, 100, 9]
    logger = logging.getLogger()
    file_handler = logging.FileHandler('tree2.log', encoding='utf-8')
    logger.addHandler(file_handler)
    logging.info('这是中文')
    quick_sort(be_sorted, 0, len(be_sorted) - 1)



