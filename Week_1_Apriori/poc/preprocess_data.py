#!/usr/bin/env python
# # Created By: Soumya Deep De
# Created Date: Jan-18-2021
# Description: Apriori Algorithm

from typing import List


class Apriori:
    def __init__(self, input_filename, ref_output, output_filename):
        super().__init__()
        self.Input_Filename = input_filename
        self.Ref_Output_Filename = ref_output
        self.Output_Filename = output_filename
        self.Itemset = []
        self.Itemset_dict = dict()

    def __str__(self) -> str:
        return "Input : {0}\nRef File: {1} \nOutput: {2}".format(self.Input_Filename, self.Ref_Output_Filename, self.Output_Filename)

    def get_itemset(self) -> None:
        temp_list = []
        with open(self.Input_Filename, "r") as reader:
            for line in reader:
                words = (line.rstrip("\n")).split(";")
                words.sort()
                temp_list.extend(words)

        self.Itemset = list(set(temp_list))
        self.Itemset.sort()

        self.Itemset_dict = {
            self.Itemset[i]: i for i in range(0, len(self.Itemset), 1)}

    def write_ref_file(self) -> None:
        with open(self.Ref_Output_Filename, "w") as writer:
            for key, val in self.Itemset_dict.items():
                writer.write("{0}:{1}\n".format(val, key))

    def gen_normalized_data(self) -> List:
        norm_data_list = []
        with open(self.Input_Filename, "r") as reader:
            for line in reader:
                words = (line.rstrip("\n")).split(";")
                words.sort()
                norm_data = [self.Itemset_dict.get(
                    words[i]) for i in range(0, len(words), 1)]
                norm_data_list.append(norm_data)
        return norm_data_list        

    def write_norm_file(self,data_list) -> None:
        with open(self.Output_Filename, "w") as writer:
            for data_row in data_list:
                writer.write("".join(str(data_row)).replace("[","\"").replace("]","\"").replace(" ",""))
                writer.write("\n")

def main():
    ap = Apriori("category.txt", "ref_file.txt", "output.csv")
    print(ap)
    ap.get_itemset()
    ap.write_ref_file()
    ap.write_norm_file(ap.gen_normalized_data())


if __name__ == "__main__":
    main()
