import csv

class Iterator:
    def __init__(self, pathfile: str) :
        self.pathfile = pathfile
        self.paths = None
        self.read_csv = None

    def __iter__(self):
        self.paths = open(self.pathfile)
        self.read_csv = csv.reader(self.paths)
        next(self.read_csv)
        return self

    def __next__(self) :
        try:
            return self.read_csv.__next__()
        except StopIteration:
            self.paths.close()
            raise StopIteration
