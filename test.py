from traceback import print_list
from PyKomoran import Komoran, DEFAULT_MODEL

komoran = Komoran(DEFAULT_MODEL['LIGHT'])
print(komoran.get_list('이것은 테스트 문장입니다'))
print(komoran.get_list('SAP 계정이 잠겼습니다'))
print(komoran.get_list('웹ERP 계정이 잠겼습니다'))

