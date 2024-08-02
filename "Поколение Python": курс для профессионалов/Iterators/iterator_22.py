class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.step > 0 and self.start < self.end) or (self.step < 0 and self.start > self.end):
            value = self.start 
            self.start += self.step 
            return value 
        raise StopIteration 

