from parsentence import ReplaceSentence


def test_replace_sentence():
    # Test case 1
    replace_sentence = ReplaceSentence()
    sentence = "Smooth"
    assert replace_sentence.replace(sentence) == "S3h"

    # Test case 2
    replace_sentence = ReplaceSentence()
    sentence = "Space separated"
    assert replace_sentence.replace(sentence) == "S3e s5d"

    # Test case 3
    replace_sentence = ReplaceSentence()
    sentence = "Dash-separated"
    assert replace_sentence.replace(sentence) == "D2h-s5d"

    # Test case 4
    replace_sentence = ReplaceSentence()
    sentence = "Number2separated"
    assert replace_sentence.replace(sentence) == "N4r2s5d"
