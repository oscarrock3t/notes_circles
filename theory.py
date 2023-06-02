scales = {
    'ионийскй': [2, 2, 1, 2, 2, 2, 1],
    'дорийский': [2, 1, 2, 2, 2, 1, 2],
    'фригийский': [1, 2, 2, 2, 1, 2, 2],
    'лидийский': [2, 2, 2, 1, 2, 2, 1],
    'миксолидийский': [2, 2, 1, 2, 2, 1, 2],
    'эолийский': [2, 1, 2, 2, 1, 2, 2],
    'локрийский': [1, 2, 2, 1, 2, 2, 2]
}

notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']


def get_notes(key):
    key = notes.index(key)
    return notes[key:] + notes[:key]


def get_scale(key, scale):
    tonal_notes = get_notes(key)
    scale = scales[scale]
    available_notes = []
    counter = 0
    for i in scale:
        available_notes.append(tonal_notes[counter])
        counter += i
    return available_notes
