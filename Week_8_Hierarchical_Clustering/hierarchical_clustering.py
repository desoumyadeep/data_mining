#!/usr/bin/env python

from typing import DefaultDict, Dict, Set
import math


class Hier_Clustering:
    def __init__(self, input_filename, output_filename) -> None:
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.no_of_rows = 0
        self.no_of_cluster = 0
        self.similarity_measure = 0
        self.dataset_header = []
        self.dataset = []
        self.raw_dataset = []
        self.cluster_list =[]
        self.final_output = []

    def print_config(self):
        print("No of rows : " + str(self.no_of_rows))
        print("No of Cluster :" + str(self.no_of_cluster))
        print("Similarity Measure : " + str(self.similarity_measure))

    def print_dataset(self):
        print("Dataset..")
        print('{0:>5}{1:>10}'.format('', ''.join(str(x).rjust(15)
                                                 for x in self.dataset_header[0])))

        [print('{0:>5}{1:>10}'.format(str(i).ljust(5), ''.join(str(x).rjust(15)
                                                               for x in self.dataset[i]))) for i in range(len(self.dataset))]

   

    def print_cluster(self):
        print("Clusters..")
        [print('{0:>5}{1:>10}'.format(str(i).ljust(5), ''.join(str(x).rjust(15)
                                                               for x in self.cluster_list[i]))) for i in range(len(self.cluster_list))]                                                           

    def add_dataset_column(self, column_name, column_data):
        self.dataset_header[0].append(column_name)

        for i in range(len(self.dataset)):
            self.dataset[i].append(column_data[i])

      

    def get_eq_dist(self,point_1, point_2):
        return round(math.sqrt((float(point_1[0]) - float(point_2[0]))**2 + (float(point_1[1]) - float(point_2[1]))**2),4)

    def load(self):
        with open(self.input_filename) as f:
            for line in f:
                var = line.split()
                self.dataset.append(var)
            self.no_of_rows, self.no_of_cluster, self.similarity_measure = self.dataset.pop(
                0)
            self.dataset_header.append(["X", "Y"])
            self.raw_dataset = self.dataset

    def generate_proximity_matrix(self):
        _temp_cluster = []
        for i in range(len(self.raw_dataset)):
            _temp_list = []
            for j in range(len(self.raw_dataset)):
                _temp_list.append(self.get_eq_dist(self.raw_dataset[i],self.raw_dataset[j]))
            self.add_dataset_column(str(i),_temp_list)
            _temp_cluster.append([i])

        self.cluster_list.append(_temp_cluster)

    def get_proximity_dist(self, item_1, item_2):
        return self.dataset[item_1][item_2 + 2]


    def get_dist(self, cluster_1, cluster_2):
        _return = 0.0000
        
        _item_dist = set()

        for i in range(len(cluster_1)):
            for j in range(len(cluster_2)):
                _item_dist.add(float(self.get_proximity_dist(cluster_1[i],cluster_2[j])))

        if int(self.similarity_measure) == 0:
            _return = min(_item_dist)
        elif int(self.similarity_measure) == 1:
            _return = max(_item_dist)
        elif int(self.similarity_measure) == 2:
            _return = sum(_item_dist) / len(_item_dist)                
        
        return _return

    def run_anglomerate_algo(self):
        _temp_cluster = []
        _temp_dist = []
        _temp_index = []
        _temp_final_cluster = []
        _cluster_len = int(self.no_of_rows)

        while (_cluster_len > int(self.no_of_cluster)):
            _temp_final_cluster = []
            _temp_dist = []
            _temp_index = []
            _temp_cluster = self.cluster_list[len(self.cluster_list)-1]
            for i in range(len(_temp_cluster)):
                for j in range(i):
                    _dist = self.get_dist(_temp_cluster[i],_temp_cluster[j])
                    _temp_dist.append(_dist)
                    _temp_index.append([j,i])

            # print(_temp_dist)
            # print(min(_temp_index))
            _min_dist_index = _temp_index[_temp_dist.index(min(_temp_dist))]
            # print(_min_dist_index)

            _temp_final_cluster.append(sorted(_temp_cluster[_min_dist_index[0]] + _temp_cluster[_min_dist_index[1]]))

            for i in range(len(_temp_cluster)):
                if i not in _min_dist_index:
                    _temp_final_cluster.append(_temp_cluster[i]) 

            self.cluster_list.append(_temp_final_cluster)       
            
            _temp_cluster = self.cluster_list[len(self.cluster_list)-1] 
            _cluster_len = len(_temp_cluster)
        
        _temp_cluster = self.cluster_list[len(self.cluster_list)-1]
        
        _temp_final_cluster = []

        for i in range(len(self.dataset)):
            for j in range(len(_temp_cluster)):
                if i in _temp_cluster[j]:
                    _temp_final_cluster.append(j)

        self.add_dataset_column("CLUSTER",_temp_final_cluster)       
        self.final_output =_temp_final_cluster

        #------------




def main():
    hc = Hier_Clustering("/Users/soumyadeepde/OneDrive/Documents/Study/MS/202101 - Spring/CS_412_Coursework/Week_8_Hierarchical_Clustering/dataset/input/sample_input_5.txt",
                         "/Users/soumyadeepde/OneDrive/Documents/Study/MS/202101 - Spring/CS_412_Coursework/Week_8_Hierarchical_Clustering/dataset/output/sample_2_opt.txt")
    hc.load()
    #hc.print_config()
    hc.generate_proximity_matrix()
    # hc.print_dataset()
    hc.run_anglomerate_algo()
    # hc.print_cluster()
    # hc.print_dataset()
    [print(x) for x in hc.final_output]

if __name__ == "__main__":
    main()
