#!/usr/bin/env python
# # Created By: Soumya Deep De
# Created Date: Jan-18-2021
# Description: Apriori Algorithm

from typing import List
from collections import Counter


class Apriori:
    def __init__(self, input_filename, output_filename, minsup):
        super().__init__()
        self.Input_Filename = input_filename
        self.Output_Filename = output_filename
        self.min_support = minsup
        self.Itemset_dict = dict()

    def __str__(self) -> str:
        return "Input : {0}\nOutput: {1}".format(self.Input_Filename, self.Output_Filename)

    def get_itemset(self) -> None:
        temp_list = []
        with open(self.Input_Filename, "r") as reader:
            for line in reader:
                words = (line.rstrip("\n")).split(";")
                words.sort()
                temp_list.extend(words)

        self.Itemset_dict = Counter(temp_list)

    def write_ref_file(self) -> None:
        with open(self.Output_Filename, "w") as writer:
            for key, val in self.Itemset_dict.items():
                if val > self.min_support:
                    writer.write("{0}:{1}\n".format(val, key))


def main():
    #ap = Apriori("./dataset/input/min_tester.txt", "./dataset/output/min_tester_process.txt",0)
    ap = Apriori("./dataset/input/category.txt",
                 "./dataset/output/part_1_patterns.txt", 771)
    print(ap)
    ap.get_itemset()
    ap.write_ref_file()


if __name__ == "__main__":
    main()
