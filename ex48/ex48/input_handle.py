class lexicon(object):

    def __init__(self):

        self.direct_list = ['north','south','east','west','down','up','left','right','back']
        self.verb_list = ['go','stop','kill','eat']
        self.stop_list = ['the','in','of','from','at','it']
        self.noun_list = ['door','bear','princess','cabinet']

    def scan(self, stuff):
        words = stuff.split()
        result = []
        for word in words:
            if self.convert_num(word) != None:
                result.append(self.convert_num(word))
            elif self.convert_word(word) != None:
                result.append(self.convert_word(word))
            else:
                result.append(self.convert_error(word))
        return result

    def convert_word(self, preword):
        word = preword.lower()
        if (word in self.direct_list):
            return ('direction', word)
        elif (word in self.verb_list):
            return ('verb', word)
        elif (word in self.stop_list):
            return ('stop', word)
        elif (word in self.noun_list):
            return ('noun', word)
        else:
            return None

    def convert_num(self, word):
        try:
            a = int(word)
            return ('number', word)
        except ValueError:
            return None

    def convert_error(self, word):
        return ('error', word)
