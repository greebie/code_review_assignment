from typing import List
from statistics import median

class DataOperations:
    dataset: List[float] = []

    def __init__(self, dataset: List[float]): 
       self.dataset = dataset

    def first(self) -> float:
        return self.dataset[0]
    
    def last(self) -> float:
        return self.dataset[-1]

    def count_values(self, value, within=0.5) -> int:
        def float_range(val):
            min = value - within
            max = value + within
            return min <= val <= max
        filtered = filter(float_range, self.dataset)
        return sum(map(lambda x: 1, filtered))

    def mean(self) -> float:
        return sum(self.dataset) / len(self.dataset)

    def median(self) -> float:
        return median(self.dataset)

if __name__ == "__main__":
    ds = DataOperations([1,2,3,4,5,1,1,1,1,2,2,2,3])
    print (ds.count_values(1))
