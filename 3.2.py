import requests
import os
import chardet


def translate_it(lang, text):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': lang,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


def main():
    while True:
        console = input('Choose file to translate:\n1 - ES.txt\n2 - FR.txt\n3 - DE.txt\nQ - for quit')
        if console.lower() == 'q':
            break
        files = {'1': 'ES.txt', '2': 'FR.txt', '3': 'DE.txt'}
        lang_in = (files[console][:2]).lower()
        file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Text', files[console])
        with open(file, "rb") as f:
            data = f.read()
            decode = chardet.detect(data)
            text = data.decode(decode["encoding"])
        console = input('Translate text to:\n1 - Spanish\n2 - French\n3 - German\n4 - Russian')
        langs_out = {'1': 'es', '2': 'fr', '3': 'de', '4': 'ru'}
        lang = ''.join([lang_in, '-', langs_out[console]])
        a = translate_it(lang, text)
        file_name = ''.join([lang, '.txt'])
        result = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Results', file_name)
        with open(result, 'w', encoding=decode['encoding']) as file:
            print(a, file=file)
        print('TRANSLATION COMPLETE')


main()
