class FileReader:
    def __init__(self):
        self._followers = []
    def subscribe(self, obj):
        self._followers.append(obj)

    def run(self, fname):
        with open(fname, 'r') as f:
            for line in f:
                new_info = line.rstrip('\n\r')
                # передавати кожен прочитай рядок файлу усім підписаним спостерігачам
                for sbs in self._followers:
                    sbs.onReceive(new_info)
###

# Виведіть усі прочитані рядки на екран;
class WordPrinter:
    def onReceive(self, line):
        pass

# Підрахуйте v слів у текстовому файлі;
class WordCounter:
    def onReceive(self, line):
        pass

# Перевірте чи містить текстовий файл задане слово.
class WordChecker:
    def onReceive(self, line):
        pass

####

if __name__ == "__main__":

    wwriter = WordPrinter()
    wcounter = WordCounter()
    wchecker = WordChecker()

    obj = FileReader()

    obj.subscribe(wwriter)
    obj.subscribe(wcounter)
    obj.subscribe(wchecker)

    obj.run('inp.txt')