phonebook = {
    'TTS': 123,
    'Nakov': 1234,
    'Stamat': 2134,
    'Nikolay': 1239123,
    'asd': 123,
    'sdf': 1234,
    'gfh': 2134,
    'asfa': 1239123,
    'fahash': 123,
    'dghfdgh': 1234,
    'sdflsd': 2134
}
revese_phonebook = {}

for key in phonebook:
    value = phonebook[key]
    if value in revese_phonebook:
        revese_phonebook[value].append(key)
    else:
        revese_phonebook[value] = [key]

for i in revese_phonebook:
    print('{} -> {}'.format(i, revese_phonebook[i]))
