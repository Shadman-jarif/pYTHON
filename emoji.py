# Emoji Converter

def emoji_converter(text):
    # Define a dictionary with words and their corresponding emojis
    emoji_dict = {
        "happy": "😊",
        "sad": "😢",
        "heart": "❤️",
        "love": "😍",
        "fire": "🔥",
        "cool": "😎",
        "thumbs up": "👍",
        "smile": "😄",
        "cry": "😭",
        "laugh": "😂",
        "angry": "😠",
        "clap": "👏",
        "star": "⭐",
        "sun": "☀️",
        "moon": "🌙",
        "dog": "🐶",
        "cat": "🐱",
        "bear": "🐻",
        "rocket": "🚀",
        "phone": "📱",
        "computer": "💻",
        "money": "💵",
        "cake": "🍰",
        "pizza": "🍕",
        "coffee": "☕",
        "car": "🚗",
        "bike": "🚴",
        "tree": "🌳",
        "flower": "🌸",
    }
    
    # Split the input text into words
    words = text.split()

    # Replace words with emojis where applicable
    converted_text = [emoji_dict.get(word.lower(), word) for word in words]

    # Join the words back into a single string
    return ' '.join(converted_text)


# Example Usage
user_input = input("Enter a sentence: ")
print("Converted: ", emoji_converter(user_input))
