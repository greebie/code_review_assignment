import unittest
from code_review.code import DataOperations
import timeit

class TestDataOperations:
    sample1 = [x/1.0 for x in range(1,10001)]
    sample2 = [2.0 for x in sample1]
    bigsample3 = [2.0 for x in range(1,1000000000)]
    d1 = DataOperations(sample1)
    d2 = DataOperations(sample2)
    

    def setUp(self):
        pass
        #self.d1 = DataOperations(self.sample1)
        #self.d2 = DataOperations(self.sample2)

    def test_first(self):   
        assert(self.d1.first() == 1.0) 
        assert(self.d2.first() == 2.0)

    def testLast(self):
        assert(self.d1.last() == 10000.0)
        assert(self.d2.last() == 2.0)

    def testCount(self):
        assert(self.d1.count_values(2.0) == 1)
        assert(self.d2.count_values(2.0) == 10000)

    def testCountSpeed(self):
        a = 2.0
        time = timeit.timeit(lambda: self.d2.count_values(a), number=10000)
        assert(time <= 16.0)

    def testMean(self):
        assert(self.d2.mean() == 2.0)

    def testMedian(self):
        assert(self.d2.median() == 2.0) 

if __name__ == '__main__':
    unittest.main()