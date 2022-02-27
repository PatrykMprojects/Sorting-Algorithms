# This file contains one of the solutions proposed for problem Find the Winner.
# The algorithm used is quicksort

# As the inputs are big, these are stored in separate python files
# As inputs, we have used dictionaries as data structure that store participants' id
# and their records as value
import time
from file_7000 import participants_7000
from file_10000 import participants_10000
from file_15000 import participants_15000
from file_20000 import participants_20000
from file_30000 import participants_30000


class FindTheWinner:

    # Initialise the attribute for class FindTheWinner
    def __init__(self, logs):
        # The function will take the parameter to create the attribute self.logs
        self.logs = logs

    def calculate_results(self):
        # In order to find the winner we have to sort the values
        # Before sorting, we need to sum the record per participant
        # Which then will be returned in another dictionary below
        results = {}
        # Split the items of in name and values
        # create variables distance, running_time giving value 0
        for name, values in self.logs.items():
            distance = 0
            running_time = 0
            # Each participant must collect 8 flags in order to be classified as valid participant
            # We are searching for 'S' in values, which is given in a list as data structure
            if values.count('S') == 8:
                for i in values:
                    # Beside 'S' string we have dictionaries, that store distance and running time before a flag was
                    # collected or finish was reached
                    # following if statement selects only dictionaries from the list
                    if type(i) is dict:
                        # Calculate total distance per participant by adding the keys to distance
                        # for that i.keys() is converted to a list , where it iterates the index 0
                        # Same approach is used to calculate running_time, but instead of i.keys() is used i.values()
                        distance += list(i.keys())[0]
                        running_time += list(i.values())[0]
                        # As during the race somebody can behave as a cheater, we need to avoid it and select only the
                        # ones who run 3000 m or over. Why over? May be the ones who forgot their flag and turned back.
                        if distance >= 3000:
                            # Once the calculation is done, we populate the dictionary with necessary data only.
                            # Which is participant id and his/her total running time
                            results[name] = running_time

        # return the dictionary that store new data
        return results

    def partition(self, list_a, low, high):
        # Select the middle element to be the pivot.
        pivot = list_a[(low + high) // 2][1]
        # Define left part of the list that will store the smaller items
        left = low - 1
        # Define right part of the list that will store the greater items
        right = high + 1
        while True:
            # Move to next index
            left += 1
            # Create a loop that compare value at the index left of the list accessing the second element of the inner
            # tuple to pivot. While the left is smaller move to next index
            while list_a[left][1] < pivot:
                left += 1
            # Move backward to next index
            right -= 1
            # Create a loop that compare value at the index right of the list accessing the second element of the inner
            # tuple to pivot. While the right is grater move backward to next index
            while list_a[right][1] > pivot:
                right -= 1

            if left >= right:
                return right

            # If an element at left is larger than the element at right then swap them
            list_a[left], list_a[right] = list_a[right], list_a[left]

    def quick_sort(self):
        # Create a new empty dictionary to save the results of the sorted list
        results = {}
        # create a variable that stores as value the records needed to be sorted.
        # The data structure used is list, by converting the output from self.calculate_results() into a list
        list_a = list(self.calculate_results().items())
        t0 = time.time()

        # Create a helper function that will be called recursively
        def _quick_sort(lst, low, high):
            if low < high:
                # This is the index after the pivot, where our lists are split
                split_index = self.partition(lst, low, high)
                _quick_sort(lst, low, split_index)
                _quick_sort(lst, split_index + 1, high)

        _quick_sort(list_a, 0, len(list_a) - 1)
        t1 = time.time()
        total_time = t1 - t0
        # As we need the data structured into a dictionary, we update the dictionary with the sorted items
        for x in range(len(list_a)):
            results[f'Place {x + 1}'] = list(list_a[x])
        # Print the first 3 winners
        for i in range(3):
            print(list(results.items())[i][0], ':', list(results.items())[i][1][0])
        # Print all result of the competition
        print(results)
        # Print algorithm's running time
        print(f'Selection sort finished in {t1 - t0} seconds')
        print()


if __name__ == '__main__':
    round_1 = FindTheWinner(participants_7000)
    round_2 = FindTheWinner(participants_10000)
    round_3 = FindTheWinner(participants_15000)
    round_4 = FindTheWinner(participants_20000)
    round_5 = FindTheWinner(participants_30000)
    round_1.quick_sort()
    round_2.quick_sort()
    round_3.quick_sort()
    round_4.quick_sort()
    round_5.quick_sort()
