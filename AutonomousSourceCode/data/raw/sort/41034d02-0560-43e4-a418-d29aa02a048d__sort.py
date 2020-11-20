def sort_by_likes(decks):
    return sorted(decks, key=lambda l: l[0], reverse=True)


def sort_by_faves(decks):
    return sorted(decks, key=lambda l: l[1], reverse=True)


def sort_by_comments(decks):
    return sorted(decks, key=lambda l: l[2], reverse=True)


def sort_by_name(decks):
    return sorted(decks, key=lambda l: l[3].lower())


def sort_by_user(decks):
    return sorted(decks, key=lambda l: l[5].lower())


def sort_by_rep(decks):
    return sorted(decks, key=lambda l: l[6], reverse=True)


def sort_by_date(decks):
    return sorted(decks, key=lambda l: l[7], reverse=True)


def sort_by_most_decks(decks):
    user_dict = most_prolific_users(decks)
    return sorted(user_dict.items(), key=lambda l: l[1], reverse=True)


def sort_by_most_rep(decks):
    user_dict = most_prolific_users(decks)
    return sorted(user_dict.items(), key=lambda l: l[1][1], reverse=True)


def most_prolific_users(decks):
    """Retrieves rep and number of decks in Hall of Fame for each user"""
    users = {}
    decks = sort_by_user(decks)
    for deck in decks:
        user = deck[5]
        if not user in users:
            users[user] = [1, deck[6]]
        else:
            users[user][0] += 1
    return users
