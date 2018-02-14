def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        print('noun')
        return 'n'

    if tag.startswith('V'):
        print('verb')
        return 'v'

    if tag.startswith('J'):
        print('adjective')
        return 'a'

    if tag.startswith('R'):
        print('adverb')
        return 'r'

    return None
