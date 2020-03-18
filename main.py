import sys

def check_mapping(s1, s2):
    # Naieve solution.
    s1_counts = list(get_letter_counts(s1).values())
    s2_counts = list(get_letter_counts(s2).values())

    print(s1_counts)
    print(s2_counts)

    for count in s1_counts:
        if count in s2_counts:
            s2_counts.pop(s2_counts.index(count))
        else:
            return False

    if len(s2_counts) == 0:
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
    print(check_mapping(s1, s2))

if __name__ == "__main__":
    main()