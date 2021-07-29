#!/usr/bin/env python
# # Created By: Soumya Deep De
# Created Date: Jan-18-2021
# Description: Apriori Algorithm

from collections import defaultdict
import time

class Apriori:
    def __init__(self, input_filename, output_filename, minsup):
        super().__init__()
        self.Input_Filename = input_filename
        self.Output_Filename = output_filename
        self.min_support = minsup
        self.pattern_dict = dict()
        self.transaction_list = []
        self.rec_cnt = 0

    def __str__(self) -> str:
        return "Input : {0}\nOutput: {1}".format(self.Input_Filename, self.Output_Filename)

    def load_data(self):
        _record = set()
        _transaction_list = []
        _itemset = set()
        with open(self.Input_Filename, "r") as reader:
            for line in reader:
                words = (line.rstrip("\n")).split(" ")
                _record = frozenset(words)
                _transaction_list.append(_record)
                for element in _record:
                    _itemset.add(frozenset([element]))

        self.transaction_list = _transaction_list
        self.rec_cnt = len(self.transaction_list)
        return _itemset

    def getMinSupportItemlist(self, itemset) -> set:
        _itemset = set()
        _l_transaction_list = defaultdict(int)

        for item in itemset:
            for transaction in self.transaction_list:
                if item.issubset(transaction):
                    _l_transaction_list[item] += 1

        for key, value in _l_transaction_list.items():
            _support = float(value) / self.rec_cnt

            if _support > self.min_support:
                self.pattern_dict[key] = value
                _itemset.add(key)
        return _itemset

    def joinSet(self, itemset, k):
        _joined_list = [i.union(j) for i in itemset for j in itemset if(
            len(i.union(j)) == k)]
        return set(_joined_list)

    def write_ref_file(self) -> None:
        with open(self.Output_Filename, "w") as writer:
            for key, val in self.pattern_dict.items():
                writer.write("{0}:{1}\n".format(val, ";".join(str(y)
                                                              for y in [x for x in key])))

    def run_algorithm(self):
        _itemset = set()
        _freqset = set()

        k = 1
        _itemset = self.load_data()
        _freqset = self.getMinSupportItemlist(_itemset)

        while len(_freqset) != 0:
            k += 1
            _itemset = self.joinSet(_freqset, k)
            _freqset = self.getMinSupportItemlist(_itemset)
        self.write_ref_file()


def main():
    _start_time = time.time()
    print("Start Time: {0}".format(_start_time))
    ap = Apriori("./dataset/input/review_sample.txt",
                 "./dataset/output/review_sample_ap.txt", 0.01)
    ap.run_algorithm()
    _end_time = time.time()

    print("End Time: {0}".format(_end_time))
    print("Execution Time: {0}".format(_end_time-_start_time))


if __name__ == "__main__":
    main()
