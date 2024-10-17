import requests
from bs4 import BeautifulSoup

def get_random_word():
    url = "https://de.wiktionary.org/wiki/Spezial:Zuf%C3%A4llig_in_Kategorie/Wiktionary:Beispiele_fehlen_(Deutsch)"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        bedeutungen_header = soup.find('p', {'title': 'Sinn und Bezeichnetes (Semantik)'})
        
        if bedeutungen_header:
            bedeutungen_section = bedeutungen_header.find_next('dl')  # Find the definition list <dl> after the header
            
            # Extract the list of definitions from <dd> tags
            if bedeutungen_section:
                bedeutungen_list = bedeutungen_section.find_all('dd')
                meanings = []
                for idx, bedeutung in enumerate(bedeutungen_list, 1):
                    # meanings.append(f"Bedeutung {idx}: {bedeutung.text.strip()}")
                    meanings.append(bedeutung.text.strip())
                return soup.title.text.split(' – ')[0].strip(), meanings        
        return soup.title.text.split(' – ')[0].strip(),[]
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return "Fehler", []

def print_word(word, char_list):
    hidden_word = "".join([ char if char.lower() in char_list else '_' for char in word])
    print("==>", hidden_word)

def ask_for_letter(word, guessed_letters):
    letter = input("Bitte einen Buchstaben raten: ")
    if letter.lower() in guessed_letters:
        return guessed_letters, False
    guessed_letters.append(letter.lower())
    if letter.lower() in word.lower():
        return guessed_letters, True
    return guessed_letters, False

def is_finished(word, guessed_letters):
    return all(char.lower() in guessed_letters for char in word)

def handle_gallows(word, guessed_letters, num_wrong_guesses, success, gallows):
        if success:
            print("Richtig")
        else:
            num_wrong_guesses += 1
            print("Falsch")
        print(gallows[num_wrong_guesses])
        return num_wrong_guesses, is_finished(word, guessed_letters)

 