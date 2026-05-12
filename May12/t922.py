class FileReader:
    def __init__(self):
        self._followers = []
    def subscribe(self, obj):
        if isinstance(obj, Observer):
            self._followers.append(obj)
        else:
            raise ValueError("об'єкт-підписник не реалізовує інтерфейс Observer")

    def run(self, fname):
        with open(fname, 'r') as f:
            for line in f:
                new_info = line.rstrip('\n\r')
                # передавати кожен прочитай рядок файлу усім підписаним спостерігачам
                for sbs in self._followers:
                    sbs.onReceive(new_info)
###

#from abc import ABC, abstractmethod
import abc

#class Observer(metaclass=abc.ABCMeta):
class Observer(abc.ABC):
    @abc.abstractmethod
    def onReceive(self, line):
        pass


# Виведіть усі прочитані рядки на екран;
class WordPrinter(Observer):
    def onReceive(self, line):
        print('WordPrinter:', line)

# Підрахуйте v слів у текстовому файлі;
class WordCounter(Observer):
    def onReceive(self, line):
        print('WordCounter', len(line.split()))

# Перевірте чи містить текстовий рядок задане слово.
class WordChecker(Observer):
    def onReceive(self, line):
        words = line.split()
        res = 'spam' in words
        print('WordChecker', res)

class LengthEvaluator:
    def get_len(self, line):
        print('LengthEvaluator', len(line))
####

if __name__ == "__main__":

    wwriter = WordPrinter()
    wcounter = WordCounter()
    wchecker = WordChecker()
    le = LengthEvaluator()

    obj = FileReader()

    obj.subscribe(wwriter)
    obj.subscribe(wcounter)
    obj.subscribe(wchecker)
    #obj.subscribe(le)

    obj.run('inp.txt')

