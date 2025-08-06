n = int(input("How many words do you want to enter? "))
user_words = []
for i in range(n):
    word = input(f"Enter word {i+1}: ").lower()
    user_words.append(word)
print("Your words:", user_words)
user_anagrams = {}
for word in user_words:
    sorted_letters = ''.join(sorted(word))
    if sorted_letters in user_anagrams:
        user_anagrams[sorted_letters].append(word)
    else:
        user_anagrams[sorted_letters] = [word]

found_anagrams = False
for pattern, group in user_anagrams.items():
    if len(group) > 1:
        print(f"Anagrams: {group}")
        found_anagrams = True

if not found_anagrams:
    print("No anagrams found in your list.")