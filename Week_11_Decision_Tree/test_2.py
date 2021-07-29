#!/usr/bin/env python
import operator
from typing import Counter, Set
from operator import itemgetter
import math
def load_data():
    _data = []
    _target =[]
    _predict = []
    with open("./dataset/input/input20.txt") as f:
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
    return _data,_target,_predict

def entropy_A(item_list):
    _entropy = 0.0
    total = sum(item_list.values())
    _entropy = sum(- i/total*math.log2(i/total) for i in item_list.values())
    return _entropy

def entropy_calc(left_list, right_list):
    _entropy = 0.0
    

    return _entropy       

def main():
    sample_dataset,y,z = load_data()
    no_of_features = len(sample_dataset[0])
    no_of_items = len(sample_dataset)
    # print(no_of_items)

    # net_d = Counter(y)
    # _total_ent = entropy_A(net_d)
    # print(net_d)
    # print("Total Entropy :" +  str(_total_ent))

    gain_list = []

    for i in range(no_of_features):
        sorted_feature_list = sorted(list(zip(list(map(itemgetter(i),sample_dataset)),y)),key=operator.itemgetter(0))
        split_pt_list = sorted(list(set(round((sorted_feature_list[j][0] + sorted_feature_list[j+1][0])/2,2) for j in range(len(sorted_feature_list)-1))))
        # split_pt_list.sort()
        # print(str(i) + ":" + str(split_pt_list))
        total_items = len(sorted_feature_list)
        for l in range(0,len(split_pt_list)):
            left_items = Counter(sorted_feature_list[k][1] for k in range(len(sorted_feature_list)) if sorted_feature_list[k][0] < split_pt_list[l])
            right_items = Counter(sorted_feature_list[k][1] for k in range(len(sorted_feature_list)) if sorted_feature_list[k][0] >= split_pt_list[l])
            # print(str(i) + ": < " + str(split_pt_list[l]) + " : " + str(left_items))
            # print(str(i) + ": >=" + str(split_pt_list[l]) + " : " + str(right_items))
            
            _ent = sum(left_items.values())/no_of_items * entropy_A(left_items) + sum(right_items.values())/no_of_items * entropy_A(right_items)
            gain_list.append([i,split_pt_list[l],_ent, left_items,right_items])

    _result = min([min(gain_list, key=lambda x:x[2])], key=lambda y:y[0])

    print("Feature: " + str(_result[0]) + " Threshold : " + str(_result[1]))
    print("Left Label: " + str(_result[3]) )
    print("Right Label: " + str(_result[4]) )

    # print(str(max(_result[4],key=_result[4].get)))

def main_2():
    l = [1,1,1,1,3,3,3,3]
    x = Counter(l)

    print(x.most_common(1)[0][0])


main()

# main_2()

