import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_input(user_input):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(user_input.lower())
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens

def get_response(user_input):
    tokens = preprocess_input(user_input)

    if any(word in tokens for word in ['hello','hi']):
        return "Hello! How can I assist you today?"
    elif any(word in tokens for word in ['how','are','you']):
        return "I'm just a bot, but I'm doing well! How about you?"
    elif any(word in tokens for word in ['name']):
        return "I am responsive chatbot"
    elif any(word in tokens for word in ['bye','goodbye']):
        return "Goodbye! have a wonderful day!"
    else:
        return "I am not sure how to respond to that. Can you please elaborate?"
    
def chat():
    print("Welcome to the responsive chatbot! Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if any(word in preprocess_input(user_input)for word in ['bye', 'goodbye']):
            print("Chatbot: Goodbye! Have a wonderful day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()