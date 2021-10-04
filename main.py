'''
Se dă un număr, să se afișeze numărul dat cu cifrele în ordine inversă.
'''

def invers(n):
    '''
    Calculeaza numarul format din cifrele lui n in ordine inversa - oglinditul unui numar
    :param Input: n: nr natural
    :return Output: nr natural - reprezinta oglinditul lui n
    '''
    og = 0
    while n > 0:
        og = og * 10 + n % 10
        n = n // 10
    return og

def test_invers():
    assert invers(123) == 321
    assert invers(121) == 121
    assert invers(11) == 11
    assert invers(51) == 15
    assert invers(100) == 1

test_invers()
