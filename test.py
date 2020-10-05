def f(A):
    """
    change healthcare test
    """
    N = len(A)
    if N == 0:
        return 0
    if N == 1:
        return A[0]
    if N > 1:
        seq1 = f(A[1:])
        seq2 = f(A[2:])
        if A[0] + seq2 >= seq1:
            return A[0] + seq2
        else:
            return seq1

B = [3, 2, 7, 10]
print(f(B))
B = [3, 2, 5, 10, 7]
print(f(B))
