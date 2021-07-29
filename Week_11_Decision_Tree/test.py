#!/usr/bin/env python
# Split a dataset based on an attribute and an attribute value
def test_split(index, value, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right

# Calculate the Gini index for a split dataset


def gini_index(groups, classes):
    # count all samples at split point
    n_instances = float(sum([len(group) for group in groups]))
    # sum weighted Gini index for each group
    gini = 0.0
    for group in groups:
        size = float(len(group))
        # avoid divide by zero
        if size == 0:
            continue
        score = 0.0
        # score the group based on the score for each class
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        # weight the group score by its relative size
        gini += (1.0 - score) * (size / n_instances)
    return gini

# Select the best split point for a dataset


def get_split(dataset):
    class_values = list(set(row[-1] for row in dataset))
    b_index, b_value, b_score, b_groups = 999, 999, 999, None
    for index in range(len(dataset[0])-1):
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups
    return {'index': b_index, 'value': b_value, 'groups': b_groups}

# Create a terminal node value


def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)

# Create child splits for a node or make terminal


def split(node, max_depth, min_size, depth):
    left, right = node['groups']
    del(node['groups'])
    # check for a no split
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return
    # check for max depth
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return
    # process left child
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left)
        split(node['left'], max_depth, min_size, depth+1)
    # process right child
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right)
        split(node['right'], max_depth, min_size, depth+1)

# Build a decision tree


def build_tree(train, max_depth, min_size):
    root = get_split(train)
    split(root, max_depth, min_size, 1)
    return root

# Print a decision tree


def print_tree(node, depth=0):
    if isinstance(node, dict):
        print('%s[X%d < %.3f]' %
              ((depth*' ', (node['index']+1), node['value'])))
        print_tree(node['left'], depth+1)
        print_tree(node['right'], depth+1)
    else:
        print('%s[%s]' % ((depth*' ', node)))


dataset = [[3.002960644434825, 2.003505994069331, 3.0069518481578, 2.002277058087728, 2.007738742256265, 2.008694201013412, 1.00203390682574, 2.003610104517811, 1], [2.007243939222775, 4.008947287014401, 1.007224120445235, 4.00808416638163, 1.009428968868237, 1.008414775629485, 2.001501471880121, 2.002776744392906, 2], [3.00876015277119, 5.007131055084347, 2.004173546336901, 1.006703933454298, 3.008038662631673, 1.00488111553581, 2.001522588451825, 2.0042260389539, 1], [2.006693543842259, 5.002618288708655, 2.006640973753513, 2.001617236981819, 1.000071614340482, 2.008999087372374, 2.006276686099762, 3.001283840985822, 4], [3.003352795672506, 2.008968839275118, 1.006552312045746, 3.00786518325273, 1.006276919105265, 1.002692245821269, 2.002969922279258, 3.004737170641705, 4], [1.001974293370207, 1.006110403507846, 2.003508907320828, 1.006620007383308, 2.001287536198164, 1.004673461616186, 2.000654654625326, 1.003392514610608, 3], [1.001159800680915, 2.005885347524898, 2.003059816131739, 3.00455916862074, 1.001967122451297, 1.00200879607745, 1.001955007729126, 2.004305484483456, 3], [3.000529198728464, 3.007880806410274, 3.003231187307115, 4.003621508647133, 2.000651335787178, 1.003318519311152, 2.002219585971603, 1.006681609920093, 3], [3.003374969375134, 3.00447559610458, 2.003446210391416, 2.007378167730819, 2.000178377735241, 1.001755552721926, 3.001888633270976, 2.005111287442453, 3], [3.003949418992904, 1.003295405019511, 2.000623681511815, 3.009123442324529, 3.009697651861967, 2.004378663344039, 3.003715061564123, 1.007924567864731, 1], [
    3.003229914777412, 1.006181849978662, 2.00296436349643, 1.005453086780824, 3.008131781908895, 2.009379757841848, 2.000898675590626, 1.009004760226585, 1], [2.004663708246147, 5.005528730276464, 2.000877917594719, 1.004363008179558, 1.002860226272128, 1.001578752110318, 1.003996444050716, 3.002547540597547, 4], [1.003888526347494, 1.008989461376069, 2.009282436059185, 2.001154307944855, 1.005735347658816, 1.006997636792891, 1.000326145090629, 3.002210735701415, 4], [3.009204320462942, 4.007499035563294, 4.00090445052381, 2.002985418435296, 2.008401967396984, 1.008019020834483, 1.003048544504447, 1.004931960691041, 1], [1.006120295207472, 1.00030275498732, 4.008444417467132, 3.009701341358785, 2.003777512813082, 2.001640319567241, 1.00514629881895, 1.003506058313176, 3], [1.007265854270638, 2.00136097087985, 4.000944043471068, 2.002919751509017, 2.000180602256334, 2.005437941634239, 3.007163949062067, 2.003568744389076, 3], [3.000379897978113, 4.009845328443293, 4.006976084389468, 2.005747631469031, 2.009944346249421, 2.004107565233541, 2.006295011855727, 2.007171171461218, 1], [1.002218849489948, 4.007480199002066, 2.009868523228773, 2.0021942896717, 2.004754659766787, 1.003638230192141, 2.006610951368161, 1.006897759766957, 3], [1.009153562401892, 1.001200481883644, 3.00005466739299, 3.003261318934608, 2.005377731887876, 1.00625158192251, 1.002847300746289, 1.006692071038365, 3], [2.003825329265541, 5.005965988738118, 1.007495011679902, 1.00197696655711, 1.008577606335805, 1.000913772725648, 1.001542853982155, 3.00657715059783, 4]]
# dataset = [[1.0, 1.0, 1], [1.0, 2.0, 1], [2.0, 1.0, 1], [2.0, 2.0, 3], [
# 	3.0, 1.0, 1], [3.0, 2.0, 3], [3.0, 3.0, 3], [4.5, 3.0, 3]]
# dataset = [[2.771244718,1.784783929,0],
# 	[1.728571309,1.169761413,0],
# 	[3.678319846,2.81281357,0],
# 	[3.961043357,2.61995032,0],
# 	[2.999208922,2.209014212,0],
# 	[7.497545867,3.162953546,1],
# 	[9.00220326,3.339047188,1],
# 	[7.444542326,0.476683375,1],
# 	[10.12493903,3.234550982,1],
# 	[6.642287351,3.319983761,1]]
tree = build_tree(dataset, 3, 1)
print_tree(tree)
# print('Split: [X%d < %.3f]' % ((split['index']+1), split['value']))
