#!/usr/bin/env python
# # Created By: Soumya Deep De
# Created Date: Jan-18-2021
# Description: Apriori Algorithm

from collections import defaultdict
from itertools import combinations
import time
import ast


class Gsp:
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
        _temp_dict = defaultdict(int)
        _temp_dict_2 = defaultdict(int)
        _temp_2_itemset = set()
        _temp_list = []
        _temp_dict_3 = defaultdict(int)
        _temp_3_itemset = set()
        with open(self.Input_Filename, "r") as reader:
            for line in reader:
                _record = (line.rstrip("\n"))
                self.transaction_list.append(_record)
                _temp_list = _record.split(" ")
                _temp_2_itemset = set()
                _temp_3_itemset = set()
                for i in set(_temp_list):
                    _temp_dict[i] += 1

                for j in range(len(_temp_list)-1):
                    _temp_2_itemset.add(
                        str(_temp_list[j]) + " " + str(_temp_list[j+1]))

                for k in _temp_2_itemset:
                    _temp_dict_2[k] += 1

                for j in range(len(_temp_list)-2):
                    _temp_3_itemset.add(
                        str(_temp_list[j]) + " " + str(_temp_list[j+1])+ " " + str(_temp_list[j+2]))

                for k in _temp_2_itemset:
                    _temp_dict_3[k] += 1    

        self.rec_cnt = len(self.transaction_list)
        for key, val in _temp_dict.items():
            if (float(val) / self.rec_cnt) >= self.min_support:
                self.pattern_dict[key] = val
                self.itemset_1 .append(key)
        for key, val in _temp_dict_2.items():
            if (float(val) / self.rec_cnt) >= self.min_support:
                self.pattern_dict[key] = val       

        for key, val in _temp_dict_3.items():
            if (float(val) / self.rec_cnt) >= self.min_support:
                self.pattern_dict[key] = val           

        self.itemset_1 .sort()

        return self.itemset_1

    def write_ref_file(self) -> None:
        with open(self.Output_Filename, "w") as writer:
            for key, val in self.pattern_dict.items():
                writer.write("{0}:{1}\n".format(
                    val, str(key).replace(" ", ";")))

    def run_algorithm(self):
        _itemset = []
        _freqset = []
        k = 1
        _freqset = self.load_data()
        _itemset = self.itemset_1
        print("Pass: {0} \tPattern Cnt : {1}".format(
            str(k), str(len(self.pattern_dict))))

        self.write_ref_file()


def main():
    _start_time = time.time()
    print("Start Time: {0}".format(_start_time))
    ap = Gsp("/Users/soumyadeepde/OneDrive/Documents/Study/MS/202101 - Spring/CS_412_Coursework/Week_4_GSP/dataset/input/review_sample.txt",
             "/Users/soumyadeepde/OneDrive/Documents/Study/MS/202101 - Spring/CS_412_Coursework/Week_4_GSP/dataset/output/gsp_run_4.txt", 0.01)
    ap.run_algorithm()
    _end_time = time.time()

    print("End Time: {0}".format(_end_time))
    print("Execution Time: {0}".format(_end_time-_start_time))


if __name__ == "__main__":
    main()
