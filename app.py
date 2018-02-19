from flask import Flask, render_template
from lambdas import appender, biased_number_generator
from animal_names import get_baby_animal_names

app = Flask(__name__)

@app.route('/', methods = ['GET'])
@app.route('/<animal>', methods = ['GET'])
@app.route('/<animal>/<suffix>', methods = ['GET'])
def cloud(animal='lamb', suffix='da'):
    words = get_word_cloud_values(animal=animal, suffix=suffix)
    return render_template('index.html', words=words, animal=animal, suffix=suffix)

def get_word_cloud_values(animal, suffix):
    '''
    Return a list of animal baby names, format like the following with a
    random weight:

    {
        'text':'animalname',
        'weight':100
    }
    '''

    names_set = get_baby_animal_names()

    # Use lambda functions for determining the weight and name
    ranker = biased_number_generator(animal)
    name_fix = appender(suffix)

    formatted_names = map(lambda name: {'text': name_fix(name), 'weight': ranker(name)}, names_set)

    # this is another implementation that doesn't use lambda
    #formatted_names = [{'text': name+suffix, 'weight': 250 if name==animal else random.randint(1, 101)} for name in names_set]

    return list(formatted_names)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
