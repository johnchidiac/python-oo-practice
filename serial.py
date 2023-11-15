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
        self.start = start
        self.current = None

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.generate()}>"

    def generate(self):
        
        """Generate a new serial number incremented by 1"""
        self.current = self.start if self.current == None else self.current + 1
        return self.current
    
    def reset(self):
        
        """Reset the count to original start number"""
        
        self.current = None


