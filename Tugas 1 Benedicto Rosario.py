hidden_word = "oxva"

while True
    user_input = input("Input satu huruf: ")

    if len(user_input) == 1 and user_input.isalpha():
        if user_input.lower() in hidden_word.lower():
            print("Huruf ini ada di dalam kata rahasia.")
            continue
        else:
            print("Huruf ini tidak ada di dalam kata rahasia.")
            break
    else:
        print("Input tidak valid, harap masukkan satu huruf.")