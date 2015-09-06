#! /usr/bin/env python
from eshotModule import *

card_no = input('Kart numaranızı giriniz : ')

test = ESHOT()
test.setup()
test.mainPage()
#test.balanceQuery(38008280177)
test.balanceQuery(card_no)
test.tearDown()
