def load_data():
    with open("./dataset/input/zoo_data.csv",newline="") as f:
        reader = csv.reader(f)
        data = [tuple(row) for row in reader]
        return data
def get_feature_data(data,feature_name):
    feature_idx = data[0].index(feature_name)
    class_idx = data[0].index("class_type")
    feature_data = [tuple((data[i][class_idx],data[i][feature_idx])) for i in range(1,len(data))]
    feature_cnt = collections.Counter(feature_data)
    class_type_cnt = Counter(data[i][class_idx] for i in range(1,len(data)))
    feature_type_cnt = Counter(data[i][feature_idx] for i in range(1,len(data)))
    print(class_type_cnt)
    print(feature_type_cnt)
    feature_calc_list = []
    for k,k1 in class_type_cnt.items():
        for j,j1 in feature_type_cnt.items():
            x = tuple((k,j))
            _prob = round(feature_cnt[x]/ class_type_cnt[k],3)
            feature_calc_list.append([tuple(("type",feature_name)),x,feature_cnt[x],_prob])
    return feature_calc_list
