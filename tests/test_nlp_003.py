import nlp_003

'''
03. 円周率
“Now I need a drink, alcoholic of course, after the heavy
lectures involving quantum mechanics.”
という文を単語に分解し，各単語の（アルファベットの）文字数を
先頭から出現順に並べたリストを作成せよ．．
'''


def test_execute():
    excepted = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
    arg = 'Now I need a drink, alcoholic of course, after the heavy lectures \
involving quantum mechanics.'
    actual = nlp_003.execute(arg)
    assert(excepted == actual)
