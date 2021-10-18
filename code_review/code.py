
class DataOperations:
    dataset = []

    def __init__(self, dataset): 
       self.dataset = dataset

    def first(self):
        return self.dataset[0]
    
    def last(self):
        return self.dataset[-1]

    def count_values(self, value, within=0.5):
        def float_range(val):
            min = value - within
            max = value + within
            return min <= val <= max
        return sum([1 for x in self.dataset if float_range(x)])

if __name__ == "__main__":
    ds = DataOperations([1,2,3,4,5,1,1,1,1,2,2,2,3])
    print (ds.count_values(1))
