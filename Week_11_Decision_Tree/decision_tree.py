#!/usr/bin/env python
from typing import Counter
import collections
import math
import operator


class Node:
    def __init__(self, predicted_class):
        self.predicted_class = predicted_class
        self.feature_index = 0
        self.threshold = 0
        self.left = None
        self.right = None

    def __str__(self) -> str:
        _return = "Feature : " + str(self.feature_index) + " Threshold :" + str(self.threshold) + \
            " Predicted Class :" + str(self.predicted_class)
        return _return


class Classifier:
    def __init__(self, max_depth=2):
        self.max_depth = max_depth
        self.no_of_classes = 0
        self.no_of_features = 0
        self.tree = Node(0)

    def entropy_A(self, item_list):
        _entropy = 0.0
        total = sum(item_list.values())
        _entropy = sum(- i/total*math.log2(i/total)
                       for i in item_list.values())
        # for i in item_list.values():
        #     _entropy += -1*math.log2(i/total)*i/total
        return _entropy

    def entropy_calc(self, classes, left_list, right_list):
        _entropy = 0.0
        for i in classes:
            _temp_total = left_list[i] + right_list[i]
            # _temp_entropy =

        return _entropy

    def split_dataset(self, sample_dataset, sample_label):
        _rtn_idx, _rtn_threshold, _entropy = None, None, None
        no_of_features = len(sample_dataset[0])
        no_of_items = len(sample_dataset)
        gain_list = []
        _dist_labels = list(set(sample_label))

        if no_of_items > 1 or len(set(sample_label)) > 1:
            net_d = Counter(sample_label)
            _total_ent = self.entropy_A(net_d)
            for i in range(no_of_features):
                sorted_feature_list = sorted(list(zip(list(
                    map(operator.itemgetter(i), sample_dataset)), sample_label)), key=operator.itemgetter(0))
                split_pt_list = sorted(list(set(round(
                    (sorted_feature_list[j][0] + sorted_feature_list[j+1][0])/2, 3) for j in range(len(sorted_feature_list)-1))))
                for l in range(0, len(split_pt_list)):
                    left_items = Counter(sorted_feature_list[k][1] for k in range(
                        len(sorted_feature_list)) if sorted_feature_list[k][0] <= split_pt_list[l])
                    right_items = Counter(sorted_feature_list[k][1] for k in range(
                        len(sorted_feature_list)) if sorted_feature_list[k][0] > split_pt_list[l])
                    # if i == 4 and split_pt_list[l] == 2.01:
                    #     test =1

                    _ent = sum(left_items.values())/no_of_items * self.entropy_A(left_items) + sum(
                        right_items.values())/no_of_items * self.entropy_A(right_items)

                    #### Fix Final Calc
                    # _ent = self.entropy_A(left_items) + self.entropy_A(right_items)
                    # , left_items,right_items])
                    gain_list.append(
                        [i, split_pt_list[l], _ent, _total_ent-_ent])

            [print(s) for s in gain_list]            

            if len(gain_list) > 0:
                print("-------")
                print([min(gain_list, key=lambda x:x[2])])
                print("-------")
                
                _result = min([min(gain_list, key=lambda x:x[2])],
                              key=lambda y: y[0])
                _rtn_idx, _rtn_threshold = _result[0], _result[1]

        print("{0}:{1}:{2}".format(_rtn_idx, _rtn_threshold, _dist_labels))
        # print("Feature: " + str(_result[0]) + " Threshold : " + str(_result[1]))
        # print("Left Label: " + str(_result[3]) )
        # print("Right Label: " + str(_result[4]) )
        return _rtn_idx, _rtn_threshold, _dist_labels

    def grow_tree(self, sample_dataset, sample_label, depth=0):
        _label_counter = collections.Counter(sorted(sample_label))
        _index = None
        _threshold = None
        _left_dataset, _right_dataset, _left_label, _right_label = [], [], [], []
        _lbl_cntr = _label_counter.most_common(1)[0][0]
        node = Node(_lbl_cntr)
        if depth < self.max_depth:

            _index, _threshold, _no_of_classes = self.split_dataset(
                sample_dataset, sample_label)
            if _index is not None:
                for i in range(len(sample_dataset)):
                    if sample_dataset[i][_index] < _threshold:
                        _left_dataset.append(sample_dataset[i])
                        _left_label.append(sample_label[i])
                    else:
                        _right_dataset.append(sample_dataset[i])
                        _right_label.append(sample_label[i])

                node.feature_index = _index
                node.threshold = _threshold
                if len(_left_label) > 0 :
                    node.left = self.grow_tree(
                        _left_dataset, _left_label, depth + 1)
                if len(_right_label) > 0:
                    node.right = self.grow_tree(
                        _right_dataset, _right_label, depth + 1)
        return node

    def _predict(self, inputs):
        _temp_node = self.tree
        while _temp_node.left:
            if inputs[_temp_node.feature_index] < _temp_node.threshold:
                _temp_node = _temp_node.left
            else:
                _temp_node = _temp_node.right
        return _temp_node.predicted_class

    def fit(self, dataset, label):
        self.classes = len(set(label))
        self.features_ = len(dataset[0])
        self.tree = self.grow_tree(dataset, label)

    def predict(self, dataset):
        return [self._predict(x) for x in dataset]


def print_tree(node, depth=0):
    if isinstance(node, Node):
        # if node.threshold > 0:
        print('|'.ljust(3*depth) + str(node))
        if node.left is not None:
            print_tree(node.left, depth+1)
        if node.right is not None:
            print_tree(node.right, depth+1)


def load_data():
    _data = []
    _target = []
    _predict = []
    homepath = "/Users/soumyadeepde/OneDrive/Documents/Study/MS/202101 - Spring/CS_412_Coursework/Week_11_Decision_Tree"
    with open(homepath + "/dataset/input/input20.txt") as f:
        for line in f:
            _temp_list = []
            _label = 0
            _record = line.split()
            _label = int(_record[0])
            for i in range(1, len(_record)):
                _temp_list.append(float(_record[i].split(":")[1]))
            if int(_label) != -1:
                _data.append(_temp_list)
                _target.append(_label)
            else:
                _predict.append(_temp_list)
    return _data, _target, _predict


def main():
    _t_data, _t_label, _p_data = load_data()

    clf = Classifier(2)
    clf.fit(_t_data, _t_label)
    # print_tree(clf.tree)
    _output = clf.predict(_p_data)
    print('\n'.join(map(str, _output)))


if __name__ == "__main__":
    main()
