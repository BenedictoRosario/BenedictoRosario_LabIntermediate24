hidden_word = "oxva"
attempts = 6
guessed_letters = []

for attempt in range(attempts):
    user_input = input(f"Attempt {attempt + 1}/{attempts} - Input satu huruf: ")

    if len(user_input) == 1 and user_input.isalpha():
        if user_input.lower() in hidden_word.lower():
            if user_input.lower() not in guessed_letters:
                guessed_letters.append(user_input.lower())
                print("Huruf ini ada di dalam kata rahasia.")
            else:
                print("Huruf ini sudah pernah ditebak.")
        else:
            print("Huruf ini tidak ada di dalam kata rahasia.")
    else:
        print("Input tidak valid, harap masukkan satu huruf.")

    if all(letter in guessed_letters for letter in hidden_word):
        print("Selamat! Anda telah menebak semua huruf dalam kata rahasia.")
        break

print("Game over!")
