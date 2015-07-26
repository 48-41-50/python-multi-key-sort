"""    Module: multi_key_sort
    A simple interface for Python multi-key and multi-directional stable sorts.
    
    Contains functions for multiple-key, multiple-direction sort of iterable data
    
    Author: HAP Proctor
    Email: 48.41.50@gmail.com
    GitHub: https://github.com/48-41-50
"""

def ResolveKeys(keyspec):
    """    ResolveKeys(keyspec) -> (key, doReverse)
    
    This is a generator function.
    
    A keyspec is an iterable of strings that denote a key  for a getter (itemgetter or 
    attrgetter) and an optional direction indicator. The direction indicator can be a 
    single dash '-' or  plus '+' preceeding the key or can be the suffix ' desc' or 
    ' asc' ending the key (the space IS important).
    
    The return value is the key with the directional removed and the reverse indicator
    set to the boolean True or False value as appropriate.
    
    If the key is a string of digits, then an integer conversion is performed.
    
    The default is reverse = False
    """
     
    for key in reversed(keyspec):
        doReverse = False
        myKey = str(key)
        
        if myKey.startswith('+'):
            doReverse = False
            myKey = myKey[1:]
            
        if myKey.endswith(' asc'):
            doReverse = False
            myKey = myKey[:-4]
        
        if myKey.startswith('-'):
            myKey = myKey[1:]
            doReverse = True
            
        if myKey.endswith(' desc'):
            myKey = myKey[:-5]
            doReverse = True
        
        if myKey.isdigit():
            try:
                myKey = int(myKey)
            except:
                pass
        
        yield (myKey, doReverse)
    # End for
# End ResolveKeys


def flatten_all(obj, res=None):
    """    This will flatten a list of lists or a mix of elements and lists 
    into a single list. It will flatten ALL levels.
    
    Ex:
        flatten_all([1, [2, [3, 4]], 5]) -> [1, 2, 3, 4, 5]
    """
    
    if res is None:
        res = []
    
    for x in obj:
        if isinstance(x, (tuple, list, set)):
            flatten_all(x, res)
        else:
            res.append(x)
        # End iterable test
    # End iterate
    
    return res
# End flatten_all
    

def complex_sorted(iterable, getter, *keys):
    """    complex_sorted(iterable, getter, *keys) -> new sorted list
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
    """
    
    if keys:
        keys = flatten_all(keys)
        res = None
        for k, r in ResolveKeys(keys):
            if res is None:
                res = sorted(iterable, key=getter(k), reverse=r)
            else:
                res.sort(key=getter(k), reverse=r)
        # End for
    else:
        res = sorted(iterable)
    
    return res
# End complex_sorted


def isorted(iterable, *keys):
    """    isorted(iterable, *keys) -> new sorted list
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
    """
    
    from operator import itemgetter
    
    return complex_sorted(iterable, itemgetter, *keys)
# End isorted


def asorted(iterable, *keys):
    """    asorted(iterable, *keys) -> new sorted list
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
    """
    
    from operator import attrgetter
    
    return complex_sorted(iterable, attrgetter, *keys)
# End asorted



def msort(self, *keys):
    """    If you subclass from a iterable base class, you can add this method 
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
    """
    
    if not hasattr(self, 'getter'):
        from operator import itemgetter
        
        self.getter = itemgetter
    # End set attribute if not defined
    
    if (self.getter.__class__.__name__ != 'type') or \
       (self.getter.__name__ not in ('itemgetter', 'attrgetter')):
        if self.getter is None:
            self.getter = itemgetter
        else:
            raise ValueError("You must supply an itemgetter or an attrgetter")
    # End getter check 
    
    if isinstance(self, list):
        if keys:
            keys = flatten_all(keys)
            for k, r in ResolveKeys(keys):
                self.sort(key=self.getter(k), reverse=r)
            # End for
        else:
            self.sort()
        
        return self
    else:
        return complex_sorted(self, self.getter, *keys)
# End msort    


