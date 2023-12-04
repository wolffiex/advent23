class Source:
    def __init__(self, sample, filename=""):
        self.sample = sample
        self.filename = filename

    def get_sample(self):
        for line in self.sample.split("\n"):
            yield line

    def get_input(self):
        assert self.filename
        with open(self.filename, "r") as file:
            for line in file:
                yield line
