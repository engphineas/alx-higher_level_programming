#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        len_sentence = len(sentence)
    else:
        len_sentence = 0
    return (len_sentence, sentence if not sentence else sentence[:1])
