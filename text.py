def crossing(a, b):
    return list(set(a) & set(b))
    
def remove_zero(a):
    return list(filter(lambda x: x > 0, a))
