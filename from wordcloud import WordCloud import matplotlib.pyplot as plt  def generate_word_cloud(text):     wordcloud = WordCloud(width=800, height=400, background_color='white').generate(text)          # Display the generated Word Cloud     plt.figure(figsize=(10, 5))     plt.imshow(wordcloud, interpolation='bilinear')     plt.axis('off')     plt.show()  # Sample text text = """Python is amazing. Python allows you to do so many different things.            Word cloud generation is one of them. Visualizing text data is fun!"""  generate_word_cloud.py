from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    # Display the generated Word Cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Sample text
text = """Python is amazing. Python allows you to do so many different things.
           Word cloud generation is one of them. Visualizing text data is fun!"""

generate_word_cloud(text)
