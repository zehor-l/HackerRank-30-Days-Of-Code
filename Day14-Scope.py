self.maximumDifference = None

    # Add your code here
    def computeDifference(self):
        lengthElem = len(self.__elements)
        max = 0
        for i in range(lengthElem):
            for j in range(lengthElem):
                value = abs(self.__elements[i] - self.__elements[j])
                if (max < value):
                    max = value
        self.maximumDifference = max