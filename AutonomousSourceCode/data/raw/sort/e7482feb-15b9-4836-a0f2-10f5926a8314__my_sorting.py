def sort_goods_by_name(goods):
    return sorted(goods, key=lambda good: good.good_name)


def sort_goods_by_country(goods):
    return sorted(goods, key=lambda good: good.good_country)


def sort_goods_by_price(goods):
    return sorted(goods, key=lambda good: good.good_price)


def sort_goods_in_order_by_name(order):
    return sorted(order.goods, key=lambda good: good.good_name)


def sort_goods_in_order_by_price(order):
    return sorted(order.goods, key=lambda good: good.good_price)