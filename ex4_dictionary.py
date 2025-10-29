import xml.etree.ElementTree as XML
tree = XML.parse('currency.xml')

result = {}

for currency in tree.findall('.//Valute'):
    code = currency.find('CharCode').text
    nominal_text = currency.find('Nominal').text
    nominal_number = int(nominal_text)
    result[code] = nominal_number

print("Коды валют и их номиналы:")
for code, nominal in result.items():
    print(f"{code} - {nominal}")