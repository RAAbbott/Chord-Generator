import random
from playsound import playsound

# This is a code that randomly selects a user-defined number of chords that can be used in progression in order
# to aid with songwriting and help jumpstart creativity

# Uses playsound to play the chords

chord_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
generated_chords = []


def play_sound(chord):
    path = 'C:/Users/Alex/Documents/Python Scripts/Audio/' + chord + ' Chord.mp3'
    playsound(path)
    return " "


def main():
    print("This is a program that randomly generate chords that can be used", end=" ")
    print("in a chord progression and can help jumpstart your songwriting creativity!")
    num_chords = int(input("How many chords would you like to generate?"))
    print(num_chords)
    for _ in range(num_chords):
        generated_chords.append(random.choice(chord_list))
    print("Here are your chords: ", ' '.join(generated_chords))
    input("Press \'ENTER\' to hear your chords")
    for i in range(len(generated_chords)):
        play_sound(generated_chords[i])
    return " "


main()
