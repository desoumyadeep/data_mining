#!/usr/bin/env python
# # Created By: Soumya Deep De
# Created Date: Jan-18-2021
# Description: Apriori Algorithm

from collections import defaultdict
from itertools import combinations
import time
import ast


class Apriori:
    def __init__(self, input_filename, output_filename, minsup):
        super().__init__()
        self.Input_Filename = input_filename
        self.Output_Filename = output_filename
        self.min_support = minsup
        self.pattern_dict = dict()
        self.transaction_list = []
        self.rec_cnt = 0
        self.itemset_1 = []

    def __str__(self) -> str:
        return "Input : {0}\nOutput: {1}".format(self.Input_Filename, self.Output_Filename)

    def load_data(self):
        _record = ()
        _transaction_list = []
        _itemset = set()
        with open(self.Input_Filename, "r") as reader:
            for line in reader:
                words = (line.rstrip("\n")).split(" ")
                _record = tuple(words)
                _transaction_list.append(_record)
                for element in _record:
                    _itemset.add(frozenset([element]))

        self.transaction_list = _transaction_list
        self.rec_cnt = len(self.transaction_list)
        return [list(x) for x in _itemset]

    # fix the code below after set to list conversion
    def getMinSupportItemlistk(self, itemset, k) -> set:
        _itemset = []
        _l_transaction_list = defaultdict(int)
        _temp_list = []

        for item in itemset:
            for transaction in self.transaction_list:
                _temp_list = []
                for x in range(len(transaction)):
                    tran = list(transaction[x:x+k])
                    if len(tran) == k:
                        _temp_list.append(tran)
                _temp_item = item  
                if _temp_item in _temp_list:
                    _l_transaction_list[repr(item)] += 1

        for key, value in _l_transaction_list.items():
            _support = float(value) / self.rec_cnt

            if _support >= self.min_support:
                self.pattern_dict[key] = value
                
                _t_list = ast.literal_eval(key)
                _itemset.append(_t_list)
        return _itemset

    def joinSet(self, itemset, k):
        return [i + j for i in itemset for j in self.itemset_1]

    def write_ref_file(self) -> None:
        with open(self.Output_Filename, "w") as writer:
            for key, val in self.pattern_dict.items():
                #_t_list = list(key.replace("[", "").replace("]", "").replace(
                #    "'", "").replace(",", "").replace(" ", ""))
                _t_list = ast.literal_eval(key)
                writer.write("{0}:{1}\n".format(val,_t_list))

    def run_algorithm(self):
        _itemset = []
        _freqset = set()

        k = 1
        self.itemset_1 = self.load_data()
        _freqset = self.getMinSupportItemlistk(self.itemset_1, k)

        
        while len(_freqset) != 0:
            k += 1
            _itemset = self.joinSet(_freqset, k)
            _freqset = self.getMinSupportItemlistk(_itemset, k)
        
        self.write_ref_file()


def main():
    _start_time = time.time()
    print("Start Time: {0}".format(_start_time))
    ap = Apriori("/Users/soumyadeepde/OneDrive/Documents/Study/MS/202101 - Spring/CS_412_Coursework/Week_4_GSP/dataset/input/review_sample.txt",
                 "/Users/soumyadeepde/OneDrive/Documents/Study/MS/202101 - Spring/CS_412_Coursework/Week_4_GSP/dataset/output/review_sample_33.txt", 0.01)
    ap.run_algorithm()
    _end_time = time.time()

    print("End Time: {0}".format(_end_time))
    print("Execution Time: {0}".format(_end_time-_start_time))


if __name__ == "__main__":
    main()
