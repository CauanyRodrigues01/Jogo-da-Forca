import random

#sorteia a palavra que vai ser descoberta pelo jogador
def get_word():
    lista_palavras = ['gata','cão', 'largato','centopéia','boi']
    word = random.choice(lista_palavras)
    return word.upper()

#
def play(word):
    word_completion = "_" * len(word) #mostrar anderlaines que representam letras da palavra a ser descoberta
    guessed = False
    guessed_letters = [] #armazena as letras que já foram sugeridas pelo jogador
    guessed_words = [] #armazena as palavras que já foram sugeridas pelo jogador
    tries = 6 #tentativas
    print(f"JOGO DA FORCA!\nDica: {len(word)} letras!")
    print(display_hangman(tries)) #mostrar o homem na forca
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Advinhe uma letra ou palavra: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Você já tentaou ", guess)
            elif guess not in word:
                print(guess, "Não.")
                tries -= 1 #diminuindo astentativas
                guessed_letters.append(guess)
            else:
                print(guess, "está na palavra!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Você já tentou a palavra", guess)
            elif guess != word:
                print(guess, "não é a palavra.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guess = True
                word_completion = word
        else:
            print("Inválido.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Parabéns, você adivinhou a palavra! Você venceu!")
    else:
        print("Você perdeu!. A palavras era " + word + ".")
        
def display_hangman(tries):
    stanges = [ """
    
                --------
                |      |
                |      0
                |     \|/
                |      |
                |     / \
                """,
    
                """
                --------
                |      |
                |      0
                |     \|/
                |      |
                |     / 
                """,
    
                """
                --------
                |      |
                |      0
                |     \|/
                |      |
                |     
                """,
    
                """
                --------
                |      |
                |      0
                |     \|
                |      |
                |      
                """,

                """
                --------
                |      |
                |      0
                |      |
                |      |
                |      
                """,
        
                """
                --------
                |      |
                |      0
                |      
                |      
                |      
                """,
    
                """
                --------
                |      |
                |      
                |      
                |      
                |      
                """
             ]                
    return stanges[tries]

def main():
    word = get_word()
    play(word)
    while input("Jogar de novo? (S/N) ").upper == "S":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()




        
