import nltk
'''all run in venv & download once
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')'''


# 1. preprocess the text
# clean html tags
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
    
# tokenization: Breaking input text into words/sentences
from nltk.tokenize import word_tokenize

# lemmatization: converting words to their root forms ex: running -> run
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def preprocess(text):
	text = remove_html_tags(text)
	# filter alphanumeric chars
	filtered_text = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text)
	# tokenize
	tokens = word_tokenize(filtered_text.lower()) # convert to lower and tokenize
	tokens = [lemmatizer.lemmatize(word) for word in tokens] # lemmatization into list
	return tokens


# 2. predifined responses
import random
responses = {
	'hello': ['Hi', 'whazzzup!', 'hey'],
	'how are you': ['fine'],
	'bye': ['gobi', 'bye', 'go touch grass'],
	'run': ['I am speed'],
	'swim': ['I can\'t swim', 'fish'],
	'default': ['huh?', 'kos ki mama?', 'can you please rephrase that', 'LoL, tell me more']
}

def get_response(user_input):
	user_input = ' '.join(preprocess(user_input)) # preprocess input
	#print(user_input)
	for key in responses:
		if key in user_input:
			#print('key =', key)
			return random.choice(responses[key])
	return random.choice(responses['default'])

# 3. chat loop
def chat():
	print('Simple NLP chatbot (type exit to stop)')
	while True:
		user_input = input('User: ')
		if user_input.lower() == 'exit':
			print('Goodbye')
			break
		response = get_response(user_input)
		print('Bot:', response)

# 4. start program
if __name__ == '__main__':
	chat()
