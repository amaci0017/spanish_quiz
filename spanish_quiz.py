import random
from gtts import gTTS
import os 

words = {
    "la casa": "the house",
    "el perro": "the dog",
    "el gato": "the cat",
    "el agua": "the water",
    "el pan": "the bread",
    "la leche": "the milk",
    "el libro": "the book",
    "la ventana": "the window",
    "la puerta": "the door",
    "el coche": "the car",
    "la ciudad": "the city",
    "el amigo": "the friend",
    "la familia": "the family",
    "el trabajo": "the job",
    "el tiempo": "the time",
    "la cuenta": "the bill",
    "la llave": "the key",
    "la maleta": "the suitcase",
    "el aeropuerto": "the airport",
    "el desayuno": "the breakfast",
}

    


def spanish_quiz():
    print('Welcome to the spanish quiz!')
    print('Let see what youve got ;)')

    score=0 # initialisation of the score

    word=random.sample(list(words),10) #make a list of 10 different words
    number=0
    
    for zord in word:
        number=number+1
        filename= "zord" + str(number) + ".mp3"
        gTTS(text=zord, lang='es').save(filename)
        os.startfile(filename)
        answer= input(f'What is the translation of {zord} in english ').lower().strip()
        correct_answer=words[zord]
        

        if answer==correct_answer or 'the '+ answer==correct_answer:
            score=score+1
            print('!Bien hecho!')
        else:
            print(f'Oh no the right answer was {correct_answer}')
    print(f'Your score is: {score}/10')

spanish_quiz()
