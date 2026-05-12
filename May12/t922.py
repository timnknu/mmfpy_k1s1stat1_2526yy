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
        print('WordPrinter:', line)

# Підрахуйте v слів у текстовому файлі;
class WordCounter:
    def onReceive(self, line):
        print('WordCounter', len(line.split()))

# Перевірте чи містить текстовий рядок задане слово.
class WordChecker:
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
    obj.subscribe(le)

    obj.run('inp.txt')