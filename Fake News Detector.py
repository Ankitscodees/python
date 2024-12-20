def fake_news_detector(text):
    fake_keywords = ['clickbait', 'hoax', 'viral', 'rumor', 'unbelievable']
    score = sum(1 for word in text.lower().split() if word in fake_keywords)
    return "Fake News" if score > 2 else "Probably Real News"

text = input("Enter a news headline: ")
print("Analysis Result:", fake_news_detector(text))
