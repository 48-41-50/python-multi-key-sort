NAME
    multi_key_sort

MODULE
    multi_key_sort

DESCRIPTION
    Module: multi_key_sort
    Contains functions for multiple-key, multiple-direction sort of iterable data
    
    Author: HAP Proctor
    Email: 48.41.50@gmail.com
    GitHub: https://github.com/48-41-50/python_multi_key_sort

FUNCTIONS
    asorted(iterable, *keys)
        asorted(iterable, *keys) -> new sorted list
        This sort will perform a Pythonic stable sort on the iterable using 
        operator.attrgetter and based on the keys.
        
        Each key is a keyspec which is:
            directional-prefix: ''
            directional-prefix: '-'
            directional-prefix: '+'
            
            directional-suffix: ''
            directional-suffix: ' desc'
            directional-suffix: ' asc'
            
            key-string:         any valid key string
            
            keyspec: directional-prefix key-string directional-suffix
            
        So if you had data in a list of classes like this:
            class SomeObj(object):
                def __init__(self, name, age, sex):
                    self.name = name
                    self.age = age
                    self.sex = sex
            
            data = [
                    SomeObj('Jim', 35, 'M'),
                    SomeObj('Sarah', 20, 'F'),
                    SomeObj("Alex", 35, 'M'),
                    SomeObj('Bill', 40, 'M'),
                    SomeObj('Wallace', 20, 'M'),
                    SomeObj('Linda', 25, F')
                    ]
        and you wanted to sort descending by age and ascending by name,
        valid keyspecs would be:
            '-age' or 'age desc'
            'name' or '+name' or 'name asc'
        
        Ascending sort is default so the '+' and ' asc' directionals are optional.
        
        Given all of the above, the call to asorted would be like this:
            asorted(data, 'age desc', 'name')
        and return a new list of the dictionaries sorted by the keys and directionals.
    
    complex_sorted(iterable, getter, *keys)
        complex_sorted(iterable, getter, *keys) -> new sorted list
        This sort will perform a Pythonic stable sort on the iterable and 
        the getter and  based on the keys.
        
        The getter must be either operator.itemgetter or operator.attrgetter
        
        Each key is a keyspec which is:
            directional-prefix: ''
            directional-prefix: '-'
            directional-prefix: '+'
            
            directional-suffix: ''
            directional-suffix: ' desc'
            directional-suffix: ' asc'
            
            key-string:         any valid key string
            
            keyspec: directional-prefix key-string directional-suffix
            
        So if you had data in a list of dictionaries like this:
            data = [
                    {'name': 'Jim', 'age': 35, 'sex': 'M'},
                    {'name': 'Sarah', 'age': 20, 'sex': 'F'},
                    {'name': "Alex", 'age': 35, 'sex': 'M'},
                    {'name': 'Bill', 'age': 40, 'sex': 'M'},
                    {'name': 'Wallace', 'age': 20, 'sex': 'M'},
                    {'name': 'Linda', 'age': 25, 'sex': 'F'}
                    ]
        and you wanted to sort descending by age and ascending by name,
        valid keyspecs would be:
            '-age' or 'age desc'
            'name' or '+name' or 'name asc'
        
        Ascending sort is default so the '+' and ' asc' directionals are optional.
        
        Given all of the above, the call to complex_sorted would be like this:
            ...
            from operator import itemgetter
            ...
            complex_sorted(data, itemgetter, 'age desc', 'name')
        and return a new list of the dictionaries sorted by the keys and directionals.
    
    flatten_all(obj, res=None)
        This will flatten a list of lists or a mix of elements and lists 
        into a single list. It will flatten ALL levels.
        
        Ex:
            flatten_all([1, [2, [3, 4]], 5]) -> [1, 2, 3, 4, 5]
    
    isorted(iterable, *keys)
        isorted(iterable, *keys) -> new sorted list
        This sort will perform a Pythonic stable sort on the iterable using 
        operator.itemgetter and based on the keys.
        
        Each key is a keyspec which is:
            directional-prefix: ''
            directional-prefix: '-'
            directional-prefix: '+'
            
            directional-suffix: ''
            directional-suffix: ' desc'
            directional-suffix: ' asc'
            
            key-string:         any valid key string
            
            keyspec: directional-prefix key-string directional-suffix
            
        So if you had data in a list of dictionaries like this:
            data = [
                    {'name': 'Jim', 'age': 35, 'sex': 'M'},
                    {'name': 'Sarah', 'age': 20, 'sex': 'F'},
                    {'name': "Alex", 'age': 35, 'sex': 'M'},
                    {'name': 'Bill', 'age': 40, 'sex': 'M'},
                    {'name': 'Wallace', 'age': 20, 'sex': 'M'},
                    {'name': 'Linda', 'age': 25, 'sex': 'F'}
                    ]
        and you wanted to sort descending by age and ascending by name,
        valid keyspecs would be:
            '-age' or 'age desc'
            'name' or '+name' or 'name asc'
        
        Ascending sort is default so the '+' and ' asc' directionals are optional.
        
        Given all of the above, the call to isorted would be like this:
            isorted(data, 'age desc', 'name')
        and return a new list of the dictionaries sorted by the keys and directionals.
    
    msort(self, *keys)
        If you subclass from a iterable base class, you can add this method 
        to an instance or to the class.
        If you subclass from list, it will act like list.sort() except it will return
        a reference to the instance.
        If you do not subclass from list, it will return a new sorted list.
        
        You will have to set a class or instance attribute named 'getter' to either
        operator.itemgetter or operator.attrgetter depending on the data being sorted.
        
        This sort will perform a Pythonic stable sort on the iterable using 
        the getter set by the instance or class attribute 'getter' and based on the keys.
        
        Each key is a keyspec which is:
            directional-prefix: ''
            directional-prefix: '-'
            directional-prefix: '+'
            
            directional-suffix: ''
            directional-suffix: ' desc'
            directional-suffix: ' asc'
            
            key-string:         any valid key string
            
            keyspec: directional-prefix key-string directional-suffix
            
        So if you had data in a list of classes like this:
            class SomeObj(object):
                def __init__(self, name, age, sex):
                    self.name = name
                    self.age = age
                    self.sex = sex
            
            data = [
                    SomeObj('Jim', 35, 'M'),
                    SomeObj('Sarah', 20, 'F'),
                    SomeObj("Alex", 35, 'M'),
                    SomeObj('Bill', 40, 'M'),
                    SomeObj('Wallace', 20, 'M'),
                    SomeObj('Linda', 25, F')
                    ]
        and you wanted to sort descending by age and ascending by name,
        valid keyspecs would be:
            '-age' or 'age desc'
            'name' or '+name' or 'name asc'
        
        Ascending sort is default so the '+' and ' asc' directionals are optional.
        
        Given all of the above, the call to the method (assuming it was bound as 'msort') 
        would be like this:
            self.msort('age desc', 'name')
        and return a new list of the dictionaries sorted by the keys and directionals.


