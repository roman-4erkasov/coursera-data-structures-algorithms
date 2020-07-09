import sys
from typing import Dict, List, Tuple, Optional
from random import randint

from collections import namedtuple

# source:
# https://github.com/kentasuzue/python-longest-common-substring/blob/master/common_substring_fast.py

Prime_number_results = namedtuple("Prime_number_results", "prime_id, positions_short_string_substrings, positions_long_string_substrings, matching_substring_length")

Answer = namedtuple("Answer", "position_short_string, position_long_string, matching_substring_length")


class Hashcode:
    def __init__(self):
        #self.primes = [100_000_000_003, 100_000_000_019]
        #self.primes = [10_000_000_019, 10_000_000_033]
        self.primes = [1_000_000_000_039, 1_000_000_000_061]
        #self.primes = [1_000_000_000_000_000_003, 1_000_000_000_000_000_009]
        #self.primes = [1_000_000_000_000_000_000_000_007, 1_000_000_000_000_000_000_000_033]
        #self.primes = [263_130_836_933_693_530_167_218_012_159_999_999, 8_683_317_618_811_886_495_518_194_401_279_999_999]
        #self.primes = [1_000_000_007, 1_000_000_009, 1_000_000_021]
        #self.primes = [1_000_000_007, 1_000_000_009, 1_000_000_021, 1_000_000_033, 1_000_000_087, 1_000_000_093, 1_000_000_097, 1_000_000_103]
        #self.primes = [100_003, 100_019, 100_043, 100_049, 100_057, 100_069]
        #self.primes = [100_003, 100_019]
        self.variable = randint(2, min(self.primes) - 1)
        self.short_hashtable = {}  # short_hashtable for shorter string. key is string length. value is hashcode of the substring.
        # the hashcode is also a key. the value is a list of starting indexes of the substring
        self.long_hashtable = {}  # long_hashtable for longer string. key is string length. value is hashcode of the substring.
        #print(f"at __init__ self.long_hashtable {self.long_hashtable} is at {hex(id(self.long_hashtable))}")
        # the hashcode is also a key. the value is a list of starting indexes of the substring

    def get_hashcode(self, prehash_string: str, prime_id: int) -> int:
        hashcode = 0
        for prehash_char in prehash_string:
            hashcode = (hashcode * self.variable + ord(prehash_char)) % prime_id
        return hashcode

    def get_polynomial_highest_degree_variable(self, substring_length: int, prime_id: int) -> int:
        polynomial_highest_degree_variable = 1
        for __ in range(substring_length):
            polynomial_highest_degree_variable = (polynomial_highest_degree_variable * self.variable) % prime_id
        return polynomial_highest_degree_variable

    def make_entry_in_hashtable(self, prehash_string: str, substring_length: int, prime_id: int, hashtable: Dict):
        hashtable.clear()
        #for starting_index in range(len(prehash_string) - substring_length, -1, -1):

        #starting_index = len(prehash_string) - substring_length
        #hashcode = self.get_hashcode(prehash_string[starting_index:starting_index + substring_length], prime_id)

        starting_index = 0
        hashcode = self.get_hashcode(prehash_string[starting_index:starting_index + substring_length], prime_id)
        hashtable[hashcode] = [starting_index]

        polynomial_highest_degree_variable = self.get_polynomial_highest_degree_variable(substring_length, prime_id)
        #print(f"polynomial_highest_degree_variable {polynomial_highest_degree_variable}")
        old_hashcode = hashcode
        for starting_index in range(1, len(prehash_string) - substring_length + 1):
            new_hashcode = \
                (
                old_hashcode * self.variable \
                + ord(prehash_string[starting_index + substring_length - 1]) \
                - polynomial_highest_degree_variable \
                * ord(prehash_string[starting_index - 1]) \
                + prime_id) \
                % prime_id
            #print(f"new_hashcode {new_hashcode}")
            if new_hashcode not in hashtable:
                hashtable[new_hashcode] = [starting_index]
            else:
                hashtable[new_hashcode].append(starting_index)
            old_hashcode = new_hashcode
        #print(f"broken hashtable {hashtable}")

    def recursive_search(self, left: int, right: int, long_string: str, short_string: str, \
                         prime_id: int) -> (int, Dict):
        #print(f"left {left} right {right} long_string {long_string} old_matching_long_string_hashcodes_dict {old_matching_long_string_hashcodes_dict} prime_id {prime_id}")
        if left > right:
            #print(f"self.long_hashtable at end of recursive search {self.long_hashtable}")
            return left - 1
            #return left - 1, old_matching_long_string_hashcodes_dict
        else:
            middle = (left + right) // 2  # middle, left, right are all possible substring lengths
            #print(
                #f"pre-make_short_hashtable  prime_id {prime_id} middle {middle} short_string {short_string} long_string {long_string}")
            temp_short_hashtable = self.short_hashtable
            self.short_hashtable = {}
            self.make_entry_in_hashtable(short_string, middle, prime_id, self.short_hashtable)
            #print(
                #f"post-make_short_hashtable  prime_id {prime_id} middle {middle} short_string {short_string} long_string {long_string}")
            temp_long_hashtable = self.long_hashtable
            self.long_hashtable = {}
            #print(f"before long_string call self.long_hashtable {self.long_hashtable} hex(id(self.long_hashtable)) {hex(id(self.long_hashtable))}")
            self.make_entry_in_hashtable(long_string, middle, prime_id, self.long_hashtable)
            #print(f"after long_string call self.long_hashtable {self.long_hashtable} hex(id(self.long_hashtable)) {hex(id(self.long_hashtable))}")

            #new_matching_long_string_hashcodes_dict = self.get_matching_long_string_hashcodes_dict(long_string, middle, prime_id)

            matching_hashtable_from_short_hashtable = {}

            for matching_hashcode in self.short_hashtable:
                if matching_hashcode in self.long_hashtable:
                    matching_hashtable_from_short_hashtable[matching_hashcode] = self.short_hashtable[matching_hashcode]

            if matching_hashtable_from_short_hashtable:
                self.short_hashtable = matching_hashtable_from_short_hashtable
                return self.recursive_search(middle + 1, right, long_string, short_string, prime_id)
            else:
                #print(f"recursive search in else branch before temp reassign self.long_hashtable {self.long_hashtable}")
                self.long_hashtable = temp_long_hashtable
                #print(f"recursive search in else branch after temp reassign self.long_hashtable {self.long_hashtable}")
                #print(f"recursive search in else branch before temp reassign self.short_hashtable {self.short_hashtable}")
                self.short_hashtable = temp_short_hashtable
                #print(f"recursive search in else branch after temp reassign self.short_hashtable {self.short_hashtable}")
                #return self.recursive_search(left, middle - 1, long_string, short_string, old_matching_long_string_hashcodes_dict, prime_id)
                return self.recursive_search(left, middle - 1, long_string, short_string, prime_id)

    # binary search among possible matching lengths of the short string
    def binary_search(self, short_string: str, long_string: str, prime_id: int, max_matching_substring_length: int) -> List:
        #print(f"\nbinary_seach for prime_id {prime_id}")
        # recreate short_hashtable for every prime_id

        matching_substring_length =\
            self.recursive_search(1, max_matching_substring_length, long_string, short_string, prime_id)

        assert matching_substring_length >= 0
        assert matching_substring_length <= max_matching_substring_length

        if matching_substring_length == 0:
            return []

        results_one_prime = []


        #for matching_hashcode in self.long_hashtable:
            #if matching_hashcode in self.short_hashtable[matching_substring_length]:
        for matching_hashcode in self.short_hashtable:
            #if matching_hashcode in self.long_hashtable:
            positions_short_string_substrings = self.short_hashtable[matching_hashcode]
            positions_long_string_substrings = self.long_hashtable[matching_hashcode]
            new_prime_number_results_tuple = Prime_number_results(
                prime_id,
                positions_short_string_substrings,
                positions_long_string_substrings,
                matching_substring_length)
            #print(f"new_prime_number_results_tuple {new_prime_number_results_tuple}")

            results_one_prime.append(new_prime_number_results_tuple)

        return results_one_prime


    def compare_matching_substring_lengths(self, results_all_primes) -> int:
        matching_substring_length = results_all_primes[0][0].matching_substring_length
        for matching_prime_number_results_tuples in results_all_primes[1:]:
            for prime_number_results_tuple in matching_prime_number_results_tuples:
                # if a tuple has a mismatched size, then go to the next tuple of current prime number
                if matching_substring_length != prime_number_results_tuple.matching_substring_length:
                    continue
                # if any tuple has matching size, then go to tuples of next prime number
                else:
                    break
            # if every tuple for this prime number mismatches, then present solution is collision
            else:
                return 0
        else:
            # every prime number has equivalent matching_substring_result
            return matching_substring_length

    def compare_tuple_to_tuples_of_other_primes(self, results_all_primes, short_and_long_string_position_tuple_first):
        for matching_prime_number_results_tuples in results_all_primes[1:]:
            for prime_number_results_tuple in matching_prime_number_results_tuples:
                for short_string_substring_position in prime_number_results_tuple.positions_short_string_substrings:
                    for long_string_substring_position in prime_number_results_tuple.positions_long_string_substrings:
                        short_and_long_string_position_tuple_others = (short_string_substring_position, long_string_substring_position)
                        if short_and_long_string_position_tuple_first == short_and_long_string_position_tuple_others:
                            return True
        return False

    def get_positions_short_and_long_substrings(self, results_all_primes) -> Optional[Tuple[int, int]]:
        #for matching_prime_number_results_tuples in results_all_primes[1:]:
        for matching_prime_number_results_tuples in results_all_primes:
            for prime_number_results_tuple in matching_prime_number_results_tuples:
                for short_string_substring_position in prime_number_results_tuple.positions_short_string_substrings:
                    for long_string_substring_position in prime_number_results_tuple.positions_long_string_substrings:
                        #print(f"short_string_substring_position {short_string_substring_position} long_string_substring_position {long_string_substring_position}")
                        short_and_long_string_position_tuple_first = (short_string_substring_position, long_string_substring_position)
                        if self.compare_tuple_to_tuples_of_other_primes(results_all_primes, short_and_long_string_position_tuple_first):
                            return short_and_long_string_position_tuple_first
        return None

    def get_matching_substring_lengths(self, results_all_primes: List[List[Answer]]) -> List[int]:

        matching_substring_lengths = [results_one_prime[0].matching_substring_length for results_one_prime in results_all_primes]

        return matching_substring_lengths

    def compare_results_all_primes(self, short_string: str, long_string: str) -> Answer:
        """
        results_all_primes = [matching_prime_number_results_tuples \
                              for prime_id in self.primes \
                              for matching_prime_number_results_tuples \
                              in self.binary_search(long_string, short_string, prime_id, len(short_string))]
        """
        results_all_primes = [self.binary_search(short_string, long_string, prime_id, len(short_string)) \
                              for prime_id in self.primes]
        #print(f"CC short_string {short_string} long_string {long_string}")
        if any(results_one_prime == [] for results_one_prime in results_all_primes):
            return 0, 0, 0

        matching_substring_lengths = self.get_matching_substring_lengths(results_all_primes)
        #print(f"matching_substring_lengths {matching_substring_lengths}")
        do_all_matching_substring_lengths_match = all(matching_substring_length == matching_substring_lengths[0] \
                                                      for matching_substring_length in matching_substring_lengths)
        #print(f"do_all_matching_substring_lengths_match {do_all_matching_substring_lengths_match}")
        if do_all_matching_substring_lengths_match:
            matching_substring_length = matching_substring_lengths[0]
        else:
            matching_substring_length = min(matching_substring_lengths)
            # all prime numbers will have at least the minimum matching_substring_length
            results_all_primes = []
            for prime_id in self.primes:
                #self.short_hashtable = {}
                self.short_hashtable.clear()
                results_all_primes.append(self.binary_search(short_string, long_string, prime_id, matching_substring_length))

            #results_all_primes = [self.binary_search(short_string, long_string, prime_id, matching_substring_length) \
                                  #for prime_id in self.primes]
        # substring lengths all match across prime numbers.
        # if a a pair of position_short_string and position_long_string matches across at least one hashcode of
        #   every prime number, then success!
        while True:
            result_get_positions_short_and_long_substrings = self.get_positions_short_and_long_substrings(results_all_primes)
            #print(f"X result_get_positions_short_and_long_substrings {result_get_positions_short_and_long_substrings}")

            if result_get_positions_short_and_long_substrings:
                position_short_string, position_long_string = result_get_positions_short_and_long_substrings
                #print(f"Z short_string {short_string} long_string {long_string}")
                return position_short_string, position_long_string, matching_substring_length

            else:
                matching_substring_length -= 1
                if matching_substring_length == 0:
                    return 0, 0, 0
                else:
                    #print(f"Y result_get_positions_short_and_long_substrings {result_get_positions_short_and_long_substrings} short_string {short_string} long_string {long_string}")
                    results_all_primes = [self.binary_search(short_string, long_string, prime_id, matching_substring_length) \
                                          for prime_id in self.primes]

def get_inputs():
    line = sys.stdin.readline()
    #print(line)
    return line.split()


def rename_strings_to_long_short(s:str , t: str)-> [bool, str, str]:
    s_longer_flag = (len(s) > len(t))
    if s_longer_flag:
        short_string = t
        long_string = s
    else:
        short_string = s
        long_string = t

    return s_longer_flag, short_string, long_string


def rename_short_long_to_strings(s_longer_flag: bool, position_short_string:int, position_long_string:int):
    if s_longer_flag:
        return position_long_string, position_short_string
    else:
        return position_short_string, position_long_string


def common_substring_main():
    h = Hashcode()

    # while True:
    for line in sys.stdin.readlines():
        # s, t = get_inputs()
        s, t = line.split()
        s_longer_flag, short_string, long_string = rename_strings_to_long_short(s, t)
        #print(f"s_longer_flag {s_longer_flag} short_string {short_string} long_string {long_string}")

        position_short_string, position_long_string, matching_substring_length =\
            h.compare_results_all_primes(short_string, long_string)

        #print(f"position_short_string {position_short_string} position_long_string {position_long_string}")

        position_s, position_t = rename_short_long_to_strings(s_longer_flag, position_short_string, position_long_string)

        print(position_s, position_t, matching_substring_length)


if __name__ == '__main__':
    common_substring_main()
    # print("Print two string separated by space to continue or print Ctrl+D (Cmd+D for Mac) to exit...")
    # for line in sys.stdin.readlines():
    #         s, t = line.split()
    #         ans = get_longest_common_substring(s, t, verbose=False)
    #         print(" ".join([str(x) for x in ans]))
