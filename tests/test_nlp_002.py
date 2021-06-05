import nlp_002

'''
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
'''


def test_execute():
    excepted = 'パタトクカシーー'
    actual = nlp_002.execute('パトカー', 'タクシー')
    assert(excepted == actual)
