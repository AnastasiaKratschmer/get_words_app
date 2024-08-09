from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load your dictionary
word_frame = pd.read_csv("cor1.02.tsv", sep="\t", header=None)
word_set = set(word_frame[1])

def generate_words(input_word, required_letter):
    raw_output_holder = []
    
    for letter0 in input_word:
        for letter1 in input_word:
            if letter1 == letter0:
                continue
            for letter2 in input_word:
                if letter2 in [letter0, letter1]:
                    continue
                for letter3 in input_word:
                    if letter3 in [letter0, letter1, letter2]:
                        continue
                    word = [letter0, letter1, letter2, letter3]
                    if required_letter in word:
                        raw_output_holder.append(''.join(word))

    for letter0 in input_word:
        for letter1 in input_word:
            if letter1 == letter0:
                continue
            for letter2 in input_word:
                if letter2 in [letter0, letter1]:
                    continue
                for letter3 in input_word:
                    if letter3 in [letter0, letter1, letter2]:
                        continue
                    for letter4 in input_word:
                        if letter4 in [letter0, letter1, letter2, letter3]:
                            continue
                        word = [letter0, letter1, letter2, letter3, letter4]
                        if required_letter in word:
                            raw_output_holder.append(''.join(word))

    for letter0 in input_word:
        for letter1 in input_word:
            if letter1 == letter0:
                continue
            for letter2 in input_word:
                if letter2 in [letter0, letter1]:
                    continue
                for letter3 in input_word:
                    if letter3 in [letter0, letter1, letter2]:
                        continue
                    for letter4 in input_word:
                        if letter4 in [letter0, letter1, letter2, letter3]:
                            continue
                        for letter5 in input_word:
                            if letter5 in [letter0, letter1, letter2, letter3, letter4]:
                                continue
                            word = [letter0, letter1, letter2, letter3, letter4, letter5]
                            if required_letter in word:
                                raw_output_holder.append(''.join(word))

    for letter0 in input_word:
        for letter1 in input_word:
            if letter1 == letter0:
                continue
            for letter2 in input_word:
                if letter2 in [letter0, letter1]:
                    continue
                for letter3 in input_word:
                    if letter3 in [letter0, letter1, letter2]:
                        continue
                    for letter4 in input_word:
                        if letter4 in [letter0, letter1, letter2, letter3]:
                            continue
                        for letter5 in input_word:
                            if letter5 in [letter0, letter1, letter2, letter3, letter4]:
                                continue
                            for letter6 in input_word:
                                if letter6 in [letter0, letter1, letter2, letter3, letter4, letter5]:
                                    continue
                                word = [letter0, letter1, letter2, letter3, letter4, letter5, letter6]
                                if required_letter in word:
                                    raw_output_holder.append(''.join(word))

    return raw_output_holder

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_word = request.form['input_word']
        required_letter = request.form['required_letter']
        
        # Generate words based on the user input
        raw_output_holder = generate_words(input_word, required_letter)
        
        valid_words_list = []
        valid_words_counter = 0
        for word in raw_output_holder:
            if word in word_set:
                valid_words_counter += 1
                valid_words_list.append(word)
        
        return render_template('index.html', valid_words=valid_words_list, count=valid_words_counter)
    
    return render_template('index.html', valid_words=None)

if __name__ == '__main__':
    app.run(debug=True)
