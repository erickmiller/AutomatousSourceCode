import math

def update_probabilities():
    """Based on the current scores, update the probability of gettings a 
    question."""
    pass

def increment_score(question_id, function):
    """Increment the score of a question based on the given function."""
    pass

def decrement_score(question_id, function):
    """Decrement the score of a question based on a given function."""
    pass

def update_alg_square(score):
    """Change the score by squaring."""
    return score * score

def update_alg_squarert(score):
    """Change the score by taking the square root."""
    return math.sqrt(score)
