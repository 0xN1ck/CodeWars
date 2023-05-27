from collections import Counter
from random import choice, random
LOVE_LANGUAGES = ["words", "acts", "gifts", "time", "touch"]


def love_language(partner, weeks):
    answers = []
    action_success = ''
    for _ in range(weeks * 7):
        if not action_success:
            action = choice(LOVE_LANGUAGES)
            if partner.response(action) == 'positive':
                answers.append(action)
                action_success = action
        else:
            if partner.response(action_success) == 'positive':
                answers.append(action_success)
            else:
                action_success = ''
    return Counter(answers).most_common(1)[0][0]


class TestPartner:
    def __init__(self, main_lang):
        self.main = main_lang

    def response(self, language):
        r = random()
        if language == self.main:
            if r < 0.85:
                return 'positive'
            else:
                return 'neutral'
        else:  # language != self.main
            if r < 0.15:
                return 'positive'
            else:
                return 'neutral'


if __name__ == "__main__":
    weeks = 6
    partner = TestPartner('words')
    if love_language(partner, weeks) == partner.main:
        print('Task is solved')

    partner = TestPartner('gifts')
    if love_language(partner, weeks) == partner.main:
        print('Task is solved')
