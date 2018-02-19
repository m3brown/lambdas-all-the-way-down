def get_baby_animal_names():
    return [
        'sprat', 'leveret', 'squab', 'foal', 'bunny', 'cria', 'fingerling',
        'squeaker', 'cygnet', 'kitten', 'duckling', 'stot', 'antling',
        'codling', 'froglet', 'neonate', 'colt', 'pupa', 'infant', 'lambkin',
        'fledgling', 'cub', 'tumbler', 'hog-colt', 'eaglet', 'pup', 'fry',
        'hatchling', 'maggot', 'tadpole', 'cheeper', 'calf', 'peachick',
        'whelp', 'snakelet', 'cosset', 'flapper', 'stag', 'youngster', 'shoat',
        'piglet', 'ephyna', 'spiderling', 'lamb', 'eyas', 'poult', 'wriggler',
        'pinkie', 'billy', 'toddler', 'porcupette', 'pluteus', 'farrow', 'hake',
        'spat', 'puggle', 'caterpillar', 'owlet', 'sprag', 'juvenile', 'joey',
        'nit', 'polliwog', 'kit', 'nymph', 'pig', 'stat', 'chick', 'kid',
        'larva', 'gosling', 'chrysalis', 'fawn', 'baby'
    ]

def get_baby_animal_names_scrape():
    # dependencies not imported at the top since the functionality is
    # only here for informational purposes
    from bs4 import BeautifulSoup
    import requests

    url_to_scrape = 'http://www.zooborns.com/zooborns/baby-animal-names.html'
    response = requests.get(url_to_scrape)
    soup = BeautifulSoup(response.text)

    names_set = set()
    for row in soup.findAll("tr"):
        cells = row.findAll('td')
        if len(cells) >= 3:
            names_text = cells[2].text
            names = [name for name in names_text.split(', ') if ' ' not in name]
            names_set.update(names)
    return names_set
