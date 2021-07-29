#!/usr/bin/env python

import csv
import collections
from typing import Counter, DefaultDict
import fileinput


class NaiveBayesClassifier:
    def __init__(self) -> None:
        self.data = []
        self.predict_data = []
        self.class_probability = DefaultDict(float)
        self.feature_proability = DefaultDict(float)
        self.unique_feature = [[1, ['0', '1']], [2, ['0', '1']], [3, ['0', '1']], [4, ['0', '1']], [5, ['0', '1']], [6, ['0', '1']], [7, ['0', '1']], [8, ['0', '1']], [
            9, ['0', '1']], [10, ['0', '1']], [11, ['0', '1']], [12, ['0', '1']], [13, ['0', '2', '4', '5', '6', '8']], [14, ['0', '1']], [15, ['0', '1']], [16, ['0', '1']]]
        self.unique_class = ['1', '2', '3', '4', '5', '6', '7']

    def load_data(self):
        for line in fileinput.input():
            word = line.rstrip().split(",")
            if word[-1] == "-1":
                self.predict_data.append(tuple(word))
            else:
                self.data.append(tuple(word))

    def set_all_probabilities(self):
        class_idx = len(self.data[0]) - 1
        class_type_cnt = Counter(self.data[i][class_idx]
                                 for i in range(1, len(self.data)))
        total_class_cnt = sum(x for x in class_type_cnt.values()) + 0.1*len(self.unique_class)

        for key, value in class_type_cnt.items():
            self.class_probability[key] =  (value + 0.1) / total_class_cnt
            feature = [x for x in self.data if x[class_idx] == key]
            for a, b in self.unique_feature:
                class_cnt = Counter(x[a] for x in feature)
                class_total = sum(x for x in class_cnt.values()) + 0.1 * len(b)
                for f_val in b:
                    self.feature_proability[str(key) + "," + str(a) + "_" + str(
                        f_val)] = (class_cnt[f_val] + 0.1) / class_total

    def predict(self):

        for x in self.predict_data:
            _predicted_list = []
            _feature_data = []
            _temp_list = []
            for y in range(1, len(x)-1):
                _temp_list.append(str(y) + "_" + str(x[y]))
            _feature_data.append(_temp_list)

            for i in self.unique_class:
                _prob = 1
                for j in _feature_data:
                    for k in j:
                        _prob = _prob * \
                            self.feature_proability[str(
                                i) + "," + k]
                _prob = _prob * self.class_probability[i]
                _predicted_list.append([i, _prob])

            q = max(_predicted_list, key=lambda x: x[1])
            print(q[0])

def main():
    nbc = NaiveBayesClassifier()
    nbc.load_data()
    nbc.set_all_probabilities()
    nbc.predict()


if __name__ == "__main__":
    main()
