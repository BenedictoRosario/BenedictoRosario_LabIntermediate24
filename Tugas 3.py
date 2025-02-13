word = "porsche"
tries = 6
guessed = ""

while tries > 0:
    failed = 0
    
    for char in word:
        if char in guessed:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    print()
    
    if failed == 0:
        print("\nKamu menang!")
        break
    
    guess = input("\nMasukkan huruf: ").lower()
    
    if guess not in guessed:
        guessed += guess
        if guess not in word:
            tries -= 1
            print(f"Salah! Sisa kesempatan: {tries}")
    else:
        print("Kamu sudah menebak huruf ini!")

if tries == 0:
    print(f"\nKamu kalah! Kata yang benar adalah: {word}")