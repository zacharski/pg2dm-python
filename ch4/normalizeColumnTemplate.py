#
#  normalize column 
#
#  This is the template for you to write and test the method
#
#  normalizeColumn
#
#  You will also need the file athletesTrainingSet.txt
#
#  For use with the book Programmer's Guide to Data Mining
#  http://guidetodatamining.com
#
#  Ron Zacharski
#

   
            

class Classifier:

    def __init__(self, filename):

        self.medianAndDeviation = []       
        # reading the data in from the file
        f = open(filename)
        lines = f.readlines()
        f.close()
        self.format = lines[0].strip().split('\t')
        self.data = []
        for line in lines[1:]:
            fields = line.strip().split('\t')
            ignore = []
            vector = []
            for i in range(len(fields)):
                if self.format[i] == 'num':
                    vector.append(int(fields[i]))
                elif self.format[i] == 'comment':
                    ignore.append(fields[i])
                elif self.format[i] == 'class':
                    classification = fields[i]
            self.data.append((classification, vector, ignore))
        self.rawData = list(self.data)
        # get length of instance vector
        self.vlen = len(self.data[0][1])
        # now normalize the data
        for i in range(self.vlen):
            self.normalizeColumn(i)
        

    

    def getMedian(self, alist):
        """return median of alist"""
        if alist == []:
            return []
        blist = sorted(alist)
        length = len(alist)
        if length % 2 == 1:
            # length of list is odd so return middle element
            return blist[int(((length + 1) / 2) -  1)]
        else:
            # length of list is even so compute midpoint
            v1 = blist[int(length / 2)]
            v2 =blist[(int(length / 2) - 1)]
            return (v1 + v2) / 2.0
        

    def getAbsoluteStandardDeviation(self, alist, median):
        """given alist and median return absolute standard deviation"""
        sum = 0
        for item in alist:
            sum += abs(item - median)
        return sum / len(alist)


    ##################################################
    ###
    ### FINISH WRITING THIS METHOD

    
    def normalizeColumn(self, columnNumber):
       """given a column number, normalize that column in self.data
       using the Modified Standard Score"""

       """ TO BE DONE"""


    
    ###
    ### 
    ##################################################



def unitTest():
    classifier = Classifier('athletesTrainingSet.txt')
    #
    #  test median and absolute standard deviation methods
    list1 = [54, 72, 78, 49, 65, 63, 75, 67, 54, 76, 68,
             61, 58, 70, 70, 70, 63, 65, 66, 61]
    list2 = [66, 162, 204, 90, 99, 106, 175, 123, 68,
             200, 163, 95, 77, 108, 155, 155, 108, 106, 97, 76]
    m1 = classifier.getMedian(list1)
    assert(round(m1, 3) == 65.5)
    m2 = classifier.getMedian(list2)
    assert(round(m2, 3) == 107)
    assert(round(classifier.getAbsoluteStandardDeviation(list1, m1),3) == 5.95)
    assert(round(classifier.getAbsoluteStandardDeviation(list2, m2),3) == 33.65)
    print("getMedian and getAbsoluteStandardDeviation are OK")

    # test normalizeColumn
    list1 = [[-1.9328, -1.2184], [1.0924, 1.6345], [2.1008, 2.8826],
             [-2.7731, -0.5052], [-0.084, -0.2377], [-0.4202, -0.0297],
             [1.5966, 2.0208], [0.2521, 0.4755], [-1.9328, -1.159],
             [1.7647, 2.7637], [0.4202, 1.6642], [-0.7563, -0.3566],
             [-1.2605, -0.8915], [0.7563, 0.0297], [0.7563, 1.4264],
             [0.7563, 1.4264], [-0.4202, 0.0297], [-0.084, -0.0297],
             [0.084, -0.2972], [-0.7563, -0.9212]]
    

    for i in range(len(list1)):
        assert(round(classifier.data[i][1][0],4) == list1[i][0])
        assert(round(classifier.data[i][1][1],4) == list1[i][1])
    print("normalizeColumn is OK")
     
unitTest()
