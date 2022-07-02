import random;
from threading import Thread;

class ReturnValueCallbackThread(Thread):
    def __init__(self, callback):
        Thread.__init__(self)
        self.result = 0
        self.callback = callback
 
    def run(self):
        self.result = self.callback()
        
class Estimator:
    def __init__(self, function, randomSampleGenerator, domainStart, domainEnd, samplesCount):
        self.function = function
        self.randomSampleGenerator = randomSampleGenerator
        self.samplesCount = samplesCount
        self.domainStart = domainStart
        self.domainEnd = domainEnd
        
    def sumSamples(self, samplesCount):
        sums = 0
        for i in range(samplesCount):
            sums = sums + self.function(self.randomSampleGenerator(self.domainStart, self.domainEnd))
        return sums
    
    def integrate(self):
        threadsCount = 16
        samplesPerThread = int(self.samplesCount / threadsCount)
        threads = list()
        sums = 0
        for i in range(threadsCount):
            t = ReturnValueCallbackThread(lambda : self.sumSamples(samplesPerThread))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
            sums = sums + t.result
        return ((self.domainEnd - self.domainStart) / (samplesPerThread * threadsCount)) * sums
    