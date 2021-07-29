#!/usr/bin/env python
# # Created By: Soumya Deep De
# Created Date: Jan-18-2021
# Description: Apriori Algorithm

from typing import List
from collections import Counter
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import apriori


class Apriori:
    def __init__(self, input_filename, output_filename, minsup):
        super().__init__()
        self.Input_Filename = input_filename
        self.Intermediate_Filename = "./dataset/output/temp.csv"
        self.Output_Filename = output_filename
        self.min_support = minsup
        self.dataset = []
        self.pattern_list = []

    def __str__(self) -> str:
        return "Input : {0}\nOutput: {1}".format(self.Input_Filename, self.Output_Filename)

    def get_dataset(self) -> None:

        with open(self.Input_Filename, "r") as reader:
            for line in reader:
                words = (line.rstrip("\n")).split(";")
                words.sort()
                self.dataset.append(words)
        self.dataset.sort()

    def load_df(self):
        te = TransactionEncoder()
        te_ary = te.fit(self.dataset).transform(self.dataset)
        df = pd.DataFrame(te_ary, columns=te.columns_)
        #final_df = fpgrowth(df, min_support=self.min_support, use_colnames=True)
        #final_df.to_csv(self.Output_Filename,columns= ["support","itemsets"])
        apriori_fp = apriori(df, self.min_support, use_colnames=True)
        apriori_fp.to_csv(self.Intermediate_Filename,
                          index=False, header=False)
        self.pattern_list = [list(x) for x in list(apriori_fp["itemsets"])]

    def get_key(l) -> str:
        l_return = str(l).replace("[", "")

    def get_support_cnt(self):
        temp_dict = dict()
        for i in self.pattern_list:
            temp_dict[str(i)] = 0

        with open(self.Input_Filename, "r") as reader:
            for line in reader:
                words = (line.rstrip("\n")).split(";")
                words.sort()

                for item in self.pattern_list:
                    if all(x in words for x in item):
                        temp_dict[str(item)] += 1

        with open(self.Output_Filename, "w") as writer:
            for i in self.pattern_list:
                writer.write("{1}:{0}\n".format(str(i).replace('"', "'").replace(
                    "['", "").replace("']", "").replace("', '", ";"), temp_dict[str(i)]))


def main():
    #ap = Apriori("./dataset/input/min_tester.txt", "./dataset/output/min_tester_process.txt",0)
    ap = Apriori("./dataset/input/category.txt",
                 "./dataset/output/category_pattern.txt", 0.01)
    print(ap)
    ap.get_dataset()
    ap.load_df()
    ap.get_support_cnt()


if __name__ == "__main__":
    main()
