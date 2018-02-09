def qsort(list):
    """Quicksort using list comprehensions"""
    if list == []: 
        return []
    else:
        pivot = list[0]
        lesser = qsort([x for x in list[1:] if x < pivot])
        greater = qsort([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater
def testQSort(stimulus, response, test):
    result = qsort(stimulus)
    if response == result:
        print ("qsort - passed - " + test)
    else:
        print ("qsort - failed - " + test)
        print ("Expected: ",)
        print (response)
        print ("Got: ",)
        print (result)
def testNumericSort():
    stimulus = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3]
    response = [1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 9]
    testQSort(stimulus, response, "numeric sort")
    
def testStringSort():       
    stimulus = ["bob","alice","barry","zoe","charlotte","fred","marvin"]
    response = ["alice","barry","bob","charlotte","fred","marvin","zoe"]
    testQSort(stimulus, response, "string sort")

testNumericSort()
testStringSort()
exit()
