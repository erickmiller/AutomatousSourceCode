##字典排序
def sort_dict(dic):
##在python3中 用dic.items()返回一组列表，d[0]表示对字典的key值进行排序，d[1]表示对value排序，reverse = 0表示按从小到达的顺序
    sorted_d = sorted(dic.items(), key=lambda d:d[1],reverse=0)
    return sorted_d
