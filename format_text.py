#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Для запуска программы напишите в командной строке:
#   python format_text.py <file_name1> <file_name2>
#
#   где file_name1 - имя файла, содержащее исходный текст
#       file_name2 - имя файла для записи результатов форматирования текста
#
# Ширина строки форматированного текста задается переменной N.
# Значение по умолчанию - 80. Можно менять в диапазоне от 20 до 120
#

from sys import argv

def format_text():
    N = 80 # Задаем ширину строки

    input_file_name, output_file_name = argv[1:3]
    text = open(input_file_name, 'r').read()

    # Разделяем текст на абзацы с помощью символа ¶ вместо \n
    text = text.replace('.\n', u'.¶')
    text = text.replace('\n\n', u'¶¶')
    text = text.replace('\n', ' ')

    result = []
    for paragraph in text.split(u'¶'):  # Обрабатываем каждый абзац по отдельности
        paragraph = paragraph.strip()
        if len(paragraph) > N / 2:      # Если абзац не строка и не является заголовком
            words = paragraph.split(' ') # Делаем из строки список слов
            line_length = len(words[0]) + 5 # Задаем начальное значение счетчика длины строки
            formatted_line = '    ' + words[0] + ' '  # Первое слово с красной строки

            # Объединяем слова в строку пока не достигнем нужной длины строки
            # После каждого прибавленного слова добавляем пробел и увеличиваем счетчик на 1
            # Если строка достигла нужной длинны, вставляем символ переноса строки
            for i in xrange(1, len(words)):
                if line_length + len(words[i]) <= N:
                    formatted_line += words[i] + ' '
                    line_length += len(words[i]) + 1
                else:
                    formatted_line += '\n' + words[i] + ' '
                    line_length = len(words[i]) + 1

            paragraph = formatted_line.replace(' \n', '\n').rstrip().splitlines()

            # Выравниваем строки до заданной ширины.
            # Каждую строчку разбиваем на список слов и добавляем нужное количество
            # пробелов к каждому слову кроме последнего и кроме слово состоящего
            # только из пробела.
            for j in xrange(0, len(paragraph)):
                if j != len(paragraph) - 1:
                    items = paragraph[j].split(' ')
                    if len(items) == 1:
                        items[0] += ' ' * (N - len(paragraph[j]))
                    else:
                        i = 2
                        while len(' '.join(items)) < N:
                            if items[0 - i] != '':
                                items[0 - i] += ' '
                            if i < len(items):
                                i += 1
                            else:
                                i = 2

                    paragraph[j] = ' '.join(items)

                result.append(paragraph[j] + '\n')
            result.append('\n')
        else:
            # если длинна строки меньше N/2, то это заголовок
            result.append('    ' + paragraph + '\n')

    # записываем результаты в файл
    open(output_file_name, 'w').write(''.join(result))

    print ('Тест из файла '+ input_file_name + ' отформатирован и записан в файл '
          + output_file_name + '. Ширина строки: ' + str(N) +'\n\n')



if __name__ == "__main__":

# Получаем имена файлов и читаем исходный текст
    if len(argv) < 3:
        print('Для запуска программы напишите в командной строке:\n\n   python '
              'format_text.py <file_name1> <file_name2>\n\n')
    else:
        format_text()
