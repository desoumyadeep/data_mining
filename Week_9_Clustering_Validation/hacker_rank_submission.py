#!/usr/bin/env python

import math
from collections import Counter
from typing import DefaultDict
import fileinput


class Cluster_Validation:
    def __init__(self) -> None:
        self.ground_truth_dict = DefaultDict(int)
        self.predicted_dict = DefaultDict(int)
        self.temp_dict = DefaultDict(int)
        self.no_of_data_point = 0

    def load(self):
        _gt_label = []
        _pc_label = []
        #with open("./dataset/input/input_0.txt") as f:
        for line in fileinput.input():
            #for line in f:
            self.no_of_data_point += 1
            var = line.split()
            _gt_label.append(var[0])
            _pc_label.append(var[1])

        self.no_of_data_point = 1 if self.no_of_data_point == 0 else self.no_of_data_point
        _comb_label = [(x, y) for x, y in zip(
            _pc_label, _gt_label)]

        self.ground_truth_dict = Counter(_gt_label)
        self.predicted_dict = Counter(_pc_label)
        self.temp_dict = Counter(_comb_label)

    def combination(self, n, k):
        return 0.0 if k > n else math.factorial(n) // math.factorial(k) // math.factorial(n-k)

    def run_NMI(self):
        _mutual_info = 0.0
        _entropy_p = 0.0
        _entropy_gt = 0.0
        for key, value in self.temp_dict.items():
            _pl_idx, _gt_idx = key
            p_ij = value / self.no_of_data_point
            p_c_i = self.predicted_dict[_pl_idx] / \
                self.no_of_data_point if self.predicted_dict[_pl_idx] != 0.0 else 1.0
            p_t_j = self.ground_truth_dict[_gt_idx] / \
                self.no_of_data_point if self.ground_truth_dict[_gt_idx] != 0.0 else 1.0

            _mutual_info += p_ij * math.log(p_ij/(p_c_i*p_t_j))

        for key, value in self.predicted_dict.items():
            p = value / self.no_of_data_point
            _entropy_p -= p*math.log(p)

        for key, value in self.ground_truth_dict.items():
            p = value / self.no_of_data_point
            _entropy_gt -= p*math.log(p)

        _entropy_p = _entropy_p if _entropy_p != 0.0 else 1.0
        _entropy_gt = _entropy_gt if _entropy_gt != 0.0 else 1.0

        return round(_mutual_info / math.sqrt(_entropy_gt*_entropy_p), 3)

    def run_jaccard(self):
        _true_positive = 0.0
        _false_negative = 0.0
        _false_positive = 0.0

        for key, value in self.temp_dict.items():
            _true_positive += value ** 2
        _true_positive = (_true_positive - self.no_of_data_point)/2

        for key, value in self.predicted_dict.items():
            _false_negative += self.combination(value, 2)
        _false_negative -= _true_positive

        for key, value in self.ground_truth_dict.items():
            _false_positive += self.combination(value, 2)
        _false_positive -= _true_positive

        return 0.0 if (_true_positive + _false_negative + _false_positive) == 0.0 else round(_true_positive / (_true_positive + _false_negative + _false_positive), 3)


def main():
    cv = Cluster_Validation()
    cv.load()

    print("{0:1.3f} {1:1.3f}".format(cv.run_NMI(), cv.run_jaccard()))


if __name__ == "__main__":
    main()
