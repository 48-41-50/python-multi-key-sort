import unittest

class FunctionalTests(unittest.TestCase):
    def setUp(self):
        self.sampleData = [
            {'name': 'Jim', 'age': 35, 'sex': 'M'},
            {'name': 'Sarah', 'age': 20, 'sex': 'F'},
            {'name': "Alex", 'age': 35, 'sex': 'M'},
            {'name': 'Bill', 'age': 40, 'sex': 'M'},
            {'name': 'Wallace', 'age': 20, 'sex': 'M'},
            {'name': 'Linda', 'age': 25, 'sex': 'F'}
           ]
    # End setUp
    
    
    def test_ResolveKeysAsc(self):
        import multi_key_sort as mks
        
        myKeys = ['key0', '+key1', 'key2 asc', '+key3 asc']
        expectedOutput = [('key3', False), ('key2', False), ('key1', False), ('key0', False)]
        actualOutput = [x for x in mks.ResolveKeys(myKeys)]
        
        self.assertEqual(expectedOutput, actualOutput, "Ascending key resolution differs from expected output.")
    # End test_ResolveKeysAsc
    
    
    def test_ResolveKeysDesc(self):
        import multi_key_sort as mks
        
        myKeys = ['-key0', 'key1 desc', '-key2 desc']
        expectedOutput = [('key2', True), ('key1', True), ('key0', True)]
        actualOutput = [x for x in mks.ResolveKeys(myKeys)]
        
        self.assertEqual(expectedOutput, actualOutput, "Descending key resolution differs from expected output.")
    # End test_ResolveKeysAsc
    
    
    def test_ResolveKeysDigit(self):
        import multi_key_sort as mks
        
        myKeys = ['-0', '1 desc', '-2 desc', '3', 4, '+5', '6 asc', '+7 asc']
        expectedOutput = [(7, False), (6, False), (5, False), (4, False), 
                          (3, False), (2, True), (1, True), (0, True)]
        actualOutput = [x for x in mks.ResolveKeys(myKeys)]
        
        self.assertEqual(expectedOutput, actualOutput, "Digit key resolution differs from expected output.")
    # End test_ResolveKeysDigit
    
    
    def test_flatten_all_1_level(self):
        import multi_key_sort as mks
        
        myKeys = [1, 2, 3, [4, 5]]
        expectedOutput = [1, 2, 3, 4, 5]
        actualOutput = mks.flatten_all(myKeys)
        
        self.assertEqual(expectedOutput, actualOutput, "List flattening output differs from expected output.")
    # End test_flatten_all_1_level
    
    
    def test_flatten_all_n_level(self):
        import multi_key_sort as mks
        
        myKeys = [1, 2, 3, [4, [5]], [6, [7, [8, [9]]]], 10]
        expectedOutput = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actualOutput = mks.flatten_all(myKeys)
        
        self.assertEqual(expectedOutput, actualOutput, "List flattening output differs from expected output.")
    # End test_flatten_all_n_level
    
    
    def test_flatten_all_iterable_types(self):
        import multi_key_sort as mks
        
        myKeys = [1, (2, 3), [4, 5], {6, 7}]
        actualOutput = [isinstance(x, int) for x in mks.flatten_all(myKeys)]
        
        self.assertTrue(all(actualOutput), "List flattening output differs from expected output.")
    # End test_flatten_all_iterable_types
    
    
    def test_complex_sort_item(self):
        import multi_key_sort as mks
        from operator import itemgetter
        
        myKeys = ['age', 'name desc']
        
        expectedOutput = [
            {'name': 'Wallace', 'age': 20, 'sex': 'M'},
            {'name': 'Sarah', 'age': 20, 'sex': 'F'},
            {'name': 'Linda', 'age': 25, 'sex': 'F'},
            {'name': 'Jim', 'age': 35, 'sex': 'M'},
            {'name': "Alex", 'age': 35, 'sex': 'M'},
            {'name': 'Bill', 'age': 40, 'sex': 'M'},
                         ]
        
        actualOutput = mks.complex_sorted(self.sampleData, itemgetter, *myKeys)
        
        self.assertEqual(expectedOutput, actualOutput, "complex_sorted (itemgetter) output differs from expected output.")
    # End test_complex_sort_item
    
    
    def test_complex_sort_attr(self):
        import multi_key_sort as mks
        from operator import attrgetter
        
        class MyData(object):
            def __init__(self, **kwargs):
                self.attrNames = sorted(kwargs.keys())
                for k, v in kwargs.iteritems():
                    setattr(self, k, v)
            
            def __cmp__(self, other):
                res = 0
                for n in self.attrNames:
                    res = cmp(getattr(self, n), getattr(other, n))
                    if res != 0:
                        break
                
                return res
        # End class MyData
        
        myKeys = ['sex desc', 'name desc']
        
        myInput = [MyData(**x) for x in self.sampleData]
        
        expectedOutput = [
            {'name': 'Wallace', 'age': 20, 'sex': 'M'},
            {'name': 'Jim', 'age': 35, 'sex': 'M'},
            {'name': 'Bill', 'age': 40, 'sex': 'M'},
            {'name': "Alex", 'age': 35, 'sex': 'M'},
            {'name': 'Sarah', 'age': 20, 'sex': 'F'},
            {'name': 'Linda', 'age': 25, 'sex': 'F'},
                         ]
        expectedOutput = [MyData(**x) for x in expectedOutput]
        
        actualOutput = mks.complex_sorted(myInput, attrgetter, *myKeys)
        
        self.assertEqual(expectedOutput, actualOutput, "complex_sorted (attrgetter) output differs from expected output.")
    # End test_complex_sort_attr
    
    
    def test_isorted(self):
        import multi_key_sort as mks
        
        myKeys = ['age', 'name desc']
        
        expectedOutput = [
            {'name': 'Wallace', 'age': 20, 'sex': 'M'},
            {'name': 'Sarah', 'age': 20, 'sex': 'F'},
            {'name': 'Linda', 'age': 25, 'sex': 'F'},
            {'name': 'Jim', 'age': 35, 'sex': 'M'},
            {'name': "Alex", 'age': 35, 'sex': 'M'},
            {'name': 'Bill', 'age': 40, 'sex': 'M'},
                         ]
        
        actualOutput = mks.isorted(self.sampleData, *myKeys)
        
        self.assertEqual(expectedOutput, actualOutput, "isorted output differs from expected output.")
    # End test_isorted
    
    
    def test_asorted(self):
        import multi_key_sort as mks
        
        class MyData(object):
            def __init__(self, **kwargs):
                self.attrNames = sorted(kwargs.keys())
                for k, v in kwargs.iteritems():
                    setattr(self, k, v)
            
            def __cmp__(self, other):
                res = 0
                for n in self.attrNames:
                    res = cmp(getattr(self, n), getattr(other, n))
                    if res != 0:
                        break
                
                return res
        # End class MyData
        
        myKeys = ['sex desc', 'name desc']
        
        myInput = [MyData(**x) for x in self.sampleData]
        
        expectedOutput = [
            {'name': 'Wallace', 'age': 20, 'sex': 'M'},
            {'name': 'Jim', 'age': 35, 'sex': 'M'},
            {'name': 'Bill', 'age': 40, 'sex': 'M'},
            {'name': "Alex", 'age': 35, 'sex': 'M'},
            {'name': 'Sarah', 'age': 20, 'sex': 'F'},
            {'name': 'Linda', 'age': 25, 'sex': 'F'},
                         ]
        expectedOutput = [MyData(**x) for x in expectedOutput]
        
        actualOutput = mks.asorted(myInput, *myKeys)
        
        self.assertEqual(expectedOutput, actualOutput, "asorted output differs from expected output.")
    # End test_asorted
    
    
    def test_msort_list(self):
        import multi_key_sort as mks
        import types
        from operator import itemgetter
        
        class MyList(list):
            pass
        
        myData = MyList(self.sampleData)
        setattr(myData, 'getter', itemgetter)
        setattr(myData, 'msort', types.MethodType(mks.msort, myData))
        
        myKeys = ['age', 'name desc']
        
        expectedOutput = [
            {'name': 'Wallace', 'age': 20, 'sex': 'M'},
            {'name': 'Sarah', 'age': 20, 'sex': 'F'},
            {'name': 'Linda', 'age': 25, 'sex': 'F'},
            {'name': 'Jim', 'age': 35, 'sex': 'M'},
            {'name': "Alex", 'age': 35, 'sex': 'M'},
            {'name': 'Bill', 'age': 40, 'sex': 'M'},
                         ]
        
        actualOutput = myData.msort(*myKeys)
        
        self.assertTrue(isinstance(actualOutput, MyList), "msort did not return a reference to the instance")
        self.assertNotEqual(myData, self.sampleData, "The list subclass instance was not changed as it should have been")
        self.assertEqual(expectedOutput, myData, "msort output differs from expected output.")
    # End test_msort_list
    
    
    def test_msort_tuple(self):
        import multi_key_sort as mks
        import types
        from operator import itemgetter
        
        class MyList(tuple):
            pass
        
        myData = MyList(self.sampleData)
        setattr(myData, 'getter', itemgetter)
        setattr(myData, 'msort', types.MethodType(mks.msort, myData))
        
        myKeys = ['age', 'name desc']
        
        expectedOutput = [
            {'name': 'Wallace', 'age': 20, 'sex': 'M'},
            {'name': 'Sarah', 'age': 20, 'sex': 'F'},
            {'name': 'Linda', 'age': 25, 'sex': 'F'},
            {'name': 'Jim', 'age': 35, 'sex': 'M'},
            {'name': "Alex", 'age': 35, 'sex': 'M'},
            {'name': 'Bill', 'age': 40, 'sex': 'M'},
                         ]
        
        actualOutput = myData.msort(*myKeys)
        
        cmpVector = [myData[i] == self.sampleData[i] for i in range(len(myData))]
        
        self.assertFalse(isinstance(actualOutput, MyList), "msort did not return a reference to the instance")
        self.assertTrue(isinstance(actualOutput, list), "The output of msort should have been a list type")
        self.assertTrue(all(cmpVector), "The tuple subclass instance was changed, but should have stayed static")
        self.assertEqual(expectedOutput, actualOutput, "msort output differs from expected output.")
    # End test_msort_tuple
# End class

