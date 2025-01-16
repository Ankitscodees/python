import datetime

def predict_mood():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        mood = "Energetic and ready to seize the day! 🌞"
    elif 12 <= current_hour < 17:
        mood = "Focused and productive. 💼"
    elif 17 <= current_hour < 21:
        mood = "Relaxed and winding down. 🌆"
    elif 21 <= current_hour or current_hour < 5:
        mood = "Sleepy or introspective. 🌜"
    else:
        mood = "Unpredictable mood! 🤔"

    print(f"Based on the current time, you might be feeling: {mood}")

predict_mood()
