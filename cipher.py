def keyboard_shift_cipher_fast(text):
    russian_lower = "йцукенгшщзхъфывапролджэячсмитьбю"
    russian_upper = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
    english_lower = "qwertyuiopasdfghjklzxcvbnm"
    english_upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
   
    def create_translation_table(layout):
        n = len(layout)
        return str.maketrans(layout, layout[:1] + layout[:-1]) #йцу --> уйц

    translation_table = {}
    translation_table.update(create_translation_table(russian_lower))
    translation_table.update(create_translation_table(russian_upper))
    translation_table.update(create_translation_table(english_lower))
    translation_table.update(create_translation_table(english_upper))

    return text.translate(translation_table)

def keyboard_shift_decipher_fast(text):
    russian_lower = "йцукенгшщзхъфывапролджэячсмитьбю"
    russian_upper = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
    english_lower = "qwertyuiopasdfghjklzxcvbnm"
    english_upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
   
    def create_translation_table(layout):
        n = len(layout)
        return str.maketrans(layout, layout[1:] + layout[:1]) # уйц --> йцу

    translation_table = {}
    translation_table.update(create_translation_table(russian_lower))
    translation_table.update(create_translation_table(russian_upper))
    translation_table.update(create_translation_table(english_lower))
    translation_table.update(create_translation_table(english_upper))

    return text.translate(translation_table)

text = "Привет Hello"
encrypted = keyboard_shift_cipher_fast(text)
decrypted = keyboard_shift_decipher_fast(encrypted)
test = keyboard_shift_decipher_fast(text)

print(f"Исходный: {text}")
print(f"Зашифрованный: {encrypted}")
print(f"Расшифрованный: {decrypted}")
print(f"Тест: {test}")