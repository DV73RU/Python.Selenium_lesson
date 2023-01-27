# lesson_2_19
"""Работа с файлами."""
# a - запись новыйх данных в файл, и посещение новых данных в файл
# w - запиь новых данных но удаление страрых файлов 
# r - чтение данных из файла
# var = input("Напиши что нибудь :")

# fw = open('file.txt', 'w')
# fw.write(var)
# fw.close


fr = open('file.txt', 'r')
text = fr.read()


fr.close
print(text)