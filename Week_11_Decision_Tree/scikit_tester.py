#!/usr/bin/env python
from sklearn import tree
def load_data():
    _data = []
    _target =[]
    _predict = []
    homepath="/Users/soumyadeepde/OneDrive/Documents/Study/MS/202101 - Spring/CS_412_Coursework/Week_11_Decision_Tree"
    with open(homepath + "/dataset/input/input22.txt") as f:
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

x,y,z = load_data()

clf = tree.DecisionTreeClassifier(criterion='entropy',max_depth=2)
clf = clf.fit(x, y)
print(tree.export_text(clf))

q = clf.predict(z)
print(q)
