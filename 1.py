def caesar(text: str, shift: int) -> str:
    """Encrypt or decrypt text using Caesar cipher."""
    result = []
    for char in text:
        if char.isupper():
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        elif char.islower():
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(char)
    return ''.join(result)

def main():
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    
    encrypted = caesar(text, shift)
    print(f"Encrypted: {encrypted}")
    
    decrypted = caesar(encrypted, -shift)
    print(f"Decrypted: {decrypted}")

if __name__ == "__main__":
    main()

#OUTPUT

Enter the text: wrong
Enter the shift value: 3
Encrypted: zurqj
Decrypted: wrong

play

key = input("Enter key: ").upper().replace("J","I")
text = input("Enter text: ").upper().replace("J","I")
mode = input("Encrypt (e) or Decrypt(d): ").lower()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key_square = []
for char in key + alphabet:
    if not char in key_square:
        key_square.append(char)

if len(text) % 2!= 0:
    text += "X"
    
shift = 1 if mode == "e" else -1
result = ""
for i in range(0, len(text), 2):
    a, b = text[i], text[i+1]
    row_a, col_a = divmod(key_square.index(a), 5)
    row_b, col_b = divmod(key_square.index(b), 5)
    
    if row_a == row_b:
        result += key_square[row_a*5 + (col_a+shift)%5]
        result += key_square[row_b*5 + (col_a+shift)%5]
        
    elif col_a == col_b:
        result += key_square[((row_a+shift)%5)*5 + col_a]
        result += key_square[((row_b+shift)%5)*5 + col_b]
        
    else:
        result += key_square[row_a*5 + col_b]
        result += key_square[row_b*5 + col_a]
print("Result:", result)

