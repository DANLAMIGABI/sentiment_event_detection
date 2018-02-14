
from stemming.porter2 import stem
plurals = ['caresses', 'flies', 'dies', 'mules', 'denied','died',
           'agreed', 'owned', 'humbled', 'sized','meeting', 'stating',
           'siezing', 'itemization','sensational', 'traditional', 'reference', 'colonizer','plotted']
singles = [stem(plural) for plural in plurals]
print(' '.join(singles))
