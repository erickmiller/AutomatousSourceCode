def sort_by(field, articles, reverse=False):
    return sorted(articles, reverse=reverse, key=lambda p: p.meta[field])
