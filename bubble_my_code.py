import time
from file_7000 import participants_7000
from file_10000 import participants_10000
from file_15000 import participants_15000
from file_20000 import participants_20000
from file_30000 import participants_30000


class WinnerWinner:

    def __init__(self, records):
        self.records = records

    def calculate_results(self):
        results = {}  # variable that will store results
        # from dict we took two elements name(p1,p2..) and value list of dicts {distance:time} and flags "S" or "F"
        for name, values in self.records.items():
            distance = 0  # variable for distance
            running_time = 0  # variable for time
            if values.count('S') == 8:  # this condition will check if value of the "S" flags is equal 8
                for i in values:  # from the value list we take an element i
                    if type(i) is dict:  # condition if i is dict then
                        # first element of dict(key) represent distance. Add to distance variable
                        distance += list(i.keys())[0]
                        # second element of dict(value) represent running time. Add to running time variable
                        running_time += list(i.values())[0]
                        if distance >= 3000:  # check if distance is equal or greater than 3000
                            results[name] = running_time  # if yes, use variable results to output:name and running time
        return results

    def bubble(self):
        list_a = list(self.calculate_results().items())  # list of the records to sort
        results = {}  # variable for sorted items
        t0 = time.time()  # start measuring time
        index_length = len(list_a) - 1  # variable that stores length of list records - 1
        sort = False  # breaking point

        while not sort:  # As long as our records are not sorted program will proceed
            sort = True
            for i in range(0, index_length):
                # if value to the left of the list is greater than  list position to the right
                if list_a[i][1] > list_a[i + 1][1]:
                    sort = False  # if it is greater then flip the values
                    list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]  # flip the values in order lower->higher

                results[f'Place {i + 1}'] = list_a[i]  # output format

        t1 = time.time()  # stop time measuring
        total_time = t1 - t0  # variable with total time

        print('The results of the contest are as following :')  # final output
        for i in range(3):  # top 3 results
            print(list(results.items())[i][0], ':', list(results.items())[i][1][0])
        print(results)  # All sorted values in order
        print(f'Bubble sort finished in {total_time} seconds')  # time result
        print()


# Driver code
if __name__ == '__main__':
    round_1 = WinnerWinner(participants_7000)
    round_2 = WinnerWinner(participants_10000)
    round_3 = WinnerWinner(participants_15000)
    round_4 = WinnerWinner(participants_20000)
    round_5 = WinnerWinner(participants_30000)
    round_1.bubble()
    round_2.bubble()
    round_3.bubble()
    round_4.bubble()
    round_5.bubble()
