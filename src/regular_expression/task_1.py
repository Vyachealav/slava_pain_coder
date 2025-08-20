# Написать регулярные выражения на
# 1. Проверку email в домменых зонах eu, com, net
#     > dsjdsk22@mail.ru — Нет
#     > kogami@oldeleven.eu - Да
import re

emails = """dsjdsk22@mail.ru
kogami@oldeleven.eu
marshall@mat.com
kogai@oleleven.eu
kogai@oleleven.net
"""

pattern = re.compile(r'\w+@[a-zA-Z]+\.(?:eu|com|net)')
result = re.findall(pattern, emails)
print(result)
