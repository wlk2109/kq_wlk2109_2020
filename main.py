import sys


def check_mapping(s1, s2):
    # Naieve solution.
    s1_counts = list(get_letter_counts(s1).values())
    s2_counts = list(get_letter_counts(s2).values())
    # Runtime = 2N Where N is length of each input list.

    # print(s1_counts)
    # print(s2_counts)

    # Runtime (worst case)  = (N^2 + N)/2 for in call
    # n*k where k is element of list for pop call.
    for count in s1_counts:
        if count in s2_counts:
            s2_counts.pop(s2_counts.index(count))
        else:
            return False

    # Total runtime in the order of N^2

    if len(s2_counts) == 0:
        return True

    return False


def check_mapping_better(s1, s2):
    # Slightly better
    s1_counts = list(get_letter_counts(s1).values())#.sort()
    s2_counts = list(get_letter_counts(s2).values())#.sort()
    # Runtime (Build Dicts) = 2N Where N is length of each input list.

    s1_counts.sort()
    s2_counts.sort()

    # Runtime (sort) = 2*N*Log(N)

    # Runtime Compare and Assign: 2*N
    for i, count in enumerate(s1_counts):
        if s2_counts[i] == count:
            s2_counts[i] = 0
        else:
            return False

    # Total runtime in the order of N*Log(N)
    if sum(s2_counts) == 0:
        return True

    return False


def get_letter_counts(s):
    counts = {}
    for letter in s:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts


def main():
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    print(check_mapping_better(s1, s2))
    return(check_mapping_better(s1, s2))


if __name__ == "__main__":
    main()