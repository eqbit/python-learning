def friend(x):
    filtered = filter(lambda f: len(f) == 4, x)
    return list(filtered)
