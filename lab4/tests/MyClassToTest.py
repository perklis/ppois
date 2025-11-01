class MyClassToTest:
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def __repr__(self):
        return f"MyClassToTest({self.value})"
