def caesar_cipher(text: str, key: int) -> str:
    if key == 0:
        return text
        
    encrypted_chars = []
    
    for char in text:
        if char == ' ':
            encrypted_chars.append(char)
        elif 'a' <= char <= 'z':
            ascii_offset = ord('a')
            current_pos = ord(char) - ascii_offset
            new_pos = (current_pos + key) % 26
            
            encrypted_chars.append(chr(new_pos + ascii_offset))
        else:
            encrypted_chars.append(char)
            
    return "".join(encrypted_chars)

def main():
    print("szyfr cezara - Aplikacja Konsolowa")
    try:
        user_text = input("Podaj tekst do zaszyfrowania (tylko male litery i spacje): ")
        user_key = int(input("Podaj wartosc klucza (liczba calkowita): "))
        
        result = caesar_cipher(user_text, user_key)
        
        print("\nWynik dzialania programu:")
        print(f"Tekst zaszyfrowany: {result}")
    except ValueError:
        print("Blad: Klucz musi byc liczba calkowita!")

if __name__ == "__main__":
    main()