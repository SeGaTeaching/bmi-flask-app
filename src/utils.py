def is_valid_weight(weight):
    return isinstance(weight, (int, float)) and weight > 0

def is_valid_height(height):
    return isinstance(height, (int, float)) and height > 0