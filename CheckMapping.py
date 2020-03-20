class CheckMapping(object):

    def __init__(self):
        return

    def check_mapping(self, s1, s2):
        # Naieve solution.
        s1_counts = list(self.get_letter_counts(s1).values())
        s2_counts = list(self.get_letter_counts(s2).values())
        # Runtime = 2N Where N is length of each input list.

        print(s1_counts)
        print(s2_counts)
        print("Hello")

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

    def check_mapping_better(self, s1, s2):
        # Slightly better
        s1_counts = list(self.get_letter_counts(s1).values())
        s2_counts = list(self.get_letter_counts(s2).values())
        # Runtime (Build Dicts) = 2N Where N is length of each input list.

        if len(s1_counts) != len(s2_counts):
            return False

        s1_counts.sort()
        s2_counts.sort()
        # Runtime (sort) = 2*N*Log(N)

        matches = 0

        # Runtime Compare and Assign: N
        for count1, count2 in zip(s1_counts, s2_counts):
            if count1 == count2:
                matches += 1
            else: return False

        # Total runtime in the order of N*Log(N)
        return matches == len(s1_counts)

    def check_mapping_no_anagrams(self, s1, s2):
        # Create a character to character mapping for each string.
        # Make sure matches are consistent accross the board.

        s1_mapping = {}
        s2_mapped = set()

        for char1, char2 in zip(s1,s2):
            if char1 in s1_mapping:
                if char2 != s1_mapping[char1]:
                    return False
            if char2 in s2_mapped:
                # char2 has already been mapped to a character!
                return False
            s1_mapping[char1] = char2
            s2_mapped.add[char2]

        return True

    def check_mapping_actual(self, s1, s2):
        # Create a character to character mapping for each string.
        # Make sure matches are consistent accross the board.

        s1_mapping = {}

        for char1, char2 in zip(s1, s2):
            if char1 in s1_mapping:
                if char2 != s1_mapping[char1]:
                    return False
            s1_mapping[char1] = char2

        return True

    def get_letter_counts(self, s):
        counts = {}
        for letter in s:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
        return counts
