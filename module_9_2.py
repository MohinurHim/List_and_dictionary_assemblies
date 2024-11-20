# Списковые, словарные сборки:
# список состоящий из длин строк списка first_strings, условие: длина строк не менее 5 символов
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
first_result = [len(first_strings) for f_str in first_strings if len(f_str) > 5]
#список состоящий из пар слов(кортежей) одинаковой длины. Сравнение слов из first_strings с словами из second_strings
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
second_result = [ (f_str, s_str) for f_str in first_strings for s_str in second_strings if len(f_str) == len(s_str)]
# словарь , где пара ключ:значение-строка:длина строки. Объединённие списков. Значения перебираются из объединённых вместе списков. Условие: чётная длина строки.
third_result = {t_str: len(t_str) for t_str in first_strings + second_strings if not len(t_str) % 2}

print(first_result)
print(second_result)
print(third_result)