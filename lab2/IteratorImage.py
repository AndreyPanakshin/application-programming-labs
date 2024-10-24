import csv

class Iterator:
    def __init__(self, pathfile: str)->None:
        """
        Class Constructor
        :param pathfile: the path to the annotation file
        """
        self.pathfile = pathfile
        self.paths = self.__load__()
        self.limit = len(self.paths)
        self.counter = 0

    def __load__(self) -> list:
        with open(self.pathfile, mode='r', encoding='utf-8') as file_csv:
            readfile = csv.reader(file_csv)
            next(readfile)
            paths = [row[1] for row in readfile]
            return paths

    def __iter__(self)->'Iterator':
        return self

    def __next__(self) ->str:
        """
       The function of getting the next element from the iterator.
       :return:the next element from the iterator.
       """
        if self.counter < self.limit:
            Next_Element = self.paths[self.counter]
            self.counter += 1
            return Next_Element
        else:
            raise StopIteration

