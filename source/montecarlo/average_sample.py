import random;
from threading import Thread;

class ReturnValueCallbackThread(Thread):
    def __init__(self, callback):
        Thread.__init__(self)
        self.result = 0
        self.callback = callback
 
    def run(self):
        self.result = self.callback()
        
# calculate() => (1/samplesCount)*sum[0->samplesCount](function())
class AverageSample:
    def __init__(self, function, samplesCount):
        self.function = function
        self.samplesCount = samplesCount
        
    def sumSamples(self, samplesCount):
        sums = 0
        for i in range(samplesCount):
            sums = sums + self.function()
        return sums
    
    def calculate(self):
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
        return (1.0 / (samplesPerThread * threadsCount)) * sums
    