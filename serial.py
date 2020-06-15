"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """create a generator with a chosesn start point"""
        self.start = start
        self.iteration = start
    
    def __repr__(self):
        return f"<serial number generator: sequence intialized on {self.start}. Current iteration  is {self.iteration}>"

    def generate(self):
        """return new serial number unique in this generator """
        tmp = self.iteration
        self.iteration = self.iteration + 1
        return tmp

    def reset(self):
        self.iteration = self.start




