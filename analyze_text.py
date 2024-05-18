import requests

# Fetching the text
lynx --dump https://shakespeare.mit.edu/romeo_juliet/full.html > file.text
links -dump https://shakespeare.mit.edu/romeo_juliet/full.html
url = 'https://shakespeare.mit.edu/romeo_juliet/full.html'
response = requests.get(url)
text = response.text.lower()

print(text)