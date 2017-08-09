from datetime import datetime, timedelta


class Palindrome():
    def __init__(self):
        self.phrases = []

    def get_currenttime(self):
        return datetime.now()

    def add(self, val):
        exist = self.existingPhrase(val)
        if exist:
            self.phrases.remove(exist[0])
        post = {
            'phrase': val,
            'time': self.get_currenttime()
        }
        self.phrases.append(post)

    def existingPhrase(self, val):
        if not self.phrases:
            return None
        else:
            return list(filter(lambda x: x['phrase'] == val, self.phrases))

    def getPhrases(self):
        current_time_minus10 = self.get_currenttime() - timedelta(minutes=10)
        return list(filter(lambda x: x['time'] > current_time_minus10,
                           sorted(self.phrases, key=lambda x: x['time'], reverse=True)))
