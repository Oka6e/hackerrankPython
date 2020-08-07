class Difference:
    def __init__(self, a):
        self.__elements = a

	def computeDifference(self):
        self.maximumDifference = None
        for i, x in enumerate(self.__elements):
            for j, y in enumerate(self.__elements):
                if i != j:
                    diff = abs(self.__elements[i] - self.__elements[j])
                    if self.maximumDifference == None:
                        self.maximumDifference = diff
                    elif self.maximumDifference < diff:
                        self.maximumDifference = diff

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)