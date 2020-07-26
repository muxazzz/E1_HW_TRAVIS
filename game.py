#import pytest
import random

words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
choices = random.choice(words)
number = len(choices)
print ('\n\nСлово состоит из %d букв \nНАЗОВИТЕ БУКВУ \n_ _ _ _ _ _ _ _ \n\n' % number)


image=list(choices)
image_new = set()
image2 = []
mistakes = 0
answer = ''
#for letters in list(choices):
#    image_new.append('_ ')
while answer != choices and mistakes != 4:
    letter = input()
    if letter in list(choices):
        for letterers in list(choices):
            image_new.add(letter)
    else:
        mistakes += 1
    if mistakes == 4:
        print("ИГРА ПРОИГРАНА")
    answer = ''.join(letter if letter in image_new else '_ ' for letter in choices)
    print(answer)
#    image_new = []


def endgame():

    pass

for word in words:
    number = len(word)
