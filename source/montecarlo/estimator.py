import montecarlo.average_sample as mas;

# integrate() => (1/samplesCount)*sum[0->samplesCount](function(domainStart, domainEnd))
class Estimator:
    def __init__(self, function, domainStart, domainEnd, samplesCount):
        self.function = function
        self.samplesCount = samplesCount
        self.domainStart = domainStart
        self.domainEnd = domainEnd
        
    def integrate(self):
        avg = mas.AverageSample(self.function, self.samplesCount)
        return (self.domainEnd - self.domainStart) * avg.calculate()
    