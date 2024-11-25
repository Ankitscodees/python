from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Example text
text = "Python is amazing! Python is fun. Learn Python programming to create amazing projects."

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
