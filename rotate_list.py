def rotate_list(l, n, d):
    n = n%len(l)
    if not d:
        n = -n
    return l[n:] + l[:n]
