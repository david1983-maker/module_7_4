from pprint import pprint


class WordsFinder:

    def __init__(self, file_name):
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}

        x = [',', '.', '=', '!', '?', ';', ':', ' - ', ]
        with open(self.file_name, encoding='utf-8') as file:
            digits = file.read()
            for name in digits:
                name = name.lower()

                for i in name:
                    if i in x:
                        digits = digits.replace(i, ' ')
            all_words[self.file_name] = digits.split()
            return all_words

    def find(self, word):
        all_words = {}

        self.word = word
        for name, word in self.get_all_words().items():
            pos = word.index(self.word.lower())
            all_words[self.file_name] = pos + 1
        return all_words

    def count(self, word):
        all_words = {}
        self.word = word
        for name, word in self.get_all_words().items():
            count_elem = word.count(self.word.lower())
            all_words[self.file_name] = count_elem
        return all_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
