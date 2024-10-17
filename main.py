import requests
from bs4 import BeautifulSoup
import galgenraten
import ascii_gallows

def main():
    guessed_letters = []
    finished = False
    num_wrong_guesses = 0
    word, meanings = galgenraten.get_random_word()
    while not finished and num_wrong_guesses < len(ascii_gallows.gallows)-1:
        galgenraten.print_word(word, guessed_letters)
        guessed_letters, success = galgenraten.ask_for_letter(word, guessed_letters)
        num_wrong_guesses, finished = galgenraten.handle_gallows(word, guessed_letters, num_wrong_guesses, success, ascii_gallows.gallows)
        
        # print("Fehlversuche:", num_wrong_guesses)
        # print("Fertig:", finished)

    if finished: 
        print("Gewonnen!")
    else:
        print("Verloren!")
    print("Das gesuchte Wort war:", word)
    print("Seine Bedeutung:")
    for meaning in meanings:
        print(meaning)


if __name__ == "__main__":
    main()

 