def print_sym_diff(M, N):
    M_diff_N = M.difference(N)
    N_diff_M = N.difference(M)
    symm_diff = M_diff_N.union(N_diff_M)
    print('\n'.join(sorted(symm_diff, key=int)))

if __name__ == "__main__":
    M = input()
    Mlst = input().split()
    N = input()
    Nlst = input().split()

    Mset = set(Mlst)
    Nset = set(Nlst)

    print_sym_diff(Mset,Nset)
