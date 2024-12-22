def mood_checker():
    mood = input("How are you feeling today? (happy/sad/angry/excited): ").strip().lower()
    emojis = {
        "happy": "😊",
        "sad": "😢",
        "angry": "😡",
        "excited": "😄",
    }
    print("Your mood emoji is:", emojis.get(mood, "🤔 (Mood not recognized)"))

mood_checker()
