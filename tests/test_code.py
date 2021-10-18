import unittest
from code_review.code import DataOperations

class TestDataOperations(unittest.TestCase):
    sample1 = [x/1.0 for x in range(1,10001)]
    sample2 = [2.0 for x in sample1]
    d1 = DataOperations(sample1)
    d2 = DataOperations(sample2)

    def setUp(self):
        pass
        #self.d1 = DataOperations(self.sample1)
        #self.d2 = DataOperations(self.sample2)

    def testFirst(self):
        print(self.sample1[0])    
        self.assertEqual(self.d1.first(), 1.0)
        self.assertEqual(self.d2.first(), 2.0)

    def testLast(self):
        print(self.sample1[-1])
        self.assertEqual(self.d1.last(), 10000.0)
        self.assertEqual(self.d2.last(), 2.0)

    def testCount(self):
        self.assertEqual(self.d1.count_values(2.0), 1)
        self.assertEqual(self.d2.count_values(2.0), 10000)

if __name__ == '__main__':
    unittest.main()