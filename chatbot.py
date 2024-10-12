import datetime


# Function to get a response based on user input
def get_response(user_input, user_name):
    user_input = user_input.lower()

    # Define responses based on specific keywords or phrases
    if "sad" in user_input:
        return f"I'm sorry to hear that, {user_name}! There is an interesting quote about that kind of feeling and I would like to share with you 'If you think you are too small to make a difference, try sleeping with a mosquito.' -Gandhi."
    elif "angry" in user_input:
        return f"I'm sorry to hear that, {user_name}! There is an interesting quote about that kind of feeling and I would like to share with you 'Anger makes dull men witty, but it keeps them poor.' -Elizabeth I."
    elif "unhappy" in user_input:
        return f"I'm sorry to hear that, {user_name}! There is an interesting quote about that kind of feeling and I would like to share with you 'There is no path to happiness. Happiness is the path.' –Buddha."
    elif "annoyed" in user_input:
        return f"I'm sorry to hear that, {user_name}! There is an interesting quote about that kind of feeling and I would like to share with you 'Everything that irritates us about others can lead us to an understanding of ourselves.' –Carl Jung."
    elif "frustrated" in user_input:
        return f"I'm sorry to hear that, {user_name}! There is an interesting quote about that kind of feeling and I would like to share with you 'Good decisions come from experience. Experience comes from making bad decisions.' –Mark Twain."
    elif "lonely" in user_input:
        return f"I'm sorry to hear that, {user_name}! There is an interesting quote about that kind of feeling and I would like to share with you 'Feeling sorry for yourself, and your present condition, is not only a waste of energy but the worst habit you could possibly have.' –Dale Carnegie."
    elif "fearful" in user_input:
        return f"I'm sorry to hear that, {user_name}! There is an interesting quote about that kind of feeling and I would like to share with you 'The whole secret of existence is to have no fear. Never fear what will become of you.' –Buddha."
    elif "worried" in user_input:
        return f"I'm sorry to hear that, {user_name}! There is an interesting quote about that kind of feeling and I would like to share with you 'Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.' –Buddha."
    elif "jealous" in user_input:
        return f"I'm sorry to hear that, {user_name}! There is an interesting quote about that kind of feeling and I would like to share with you 'Do not be jealous of others' good fortune, nor be overjoyed by your own.' –Buddha."
    elif "guilty" in user_input:
        return f"I'm sorry to hear that, {user_name}! There is an interesting quote about that kind of feeling and I would like to share with you 'There has to be evil so that good can prove its purity above it.' –Buddha."
    elif "disappointed" in user_input:
        return f"I'm sorry to hear that, {user_name}! There is an interesting quote about that kind of feeling and I would like to share with you 'In the end, these things matter most: How well did you love? How fully did you live? How deeply did you let go?' –Buddha."
    elif "bye" in user_input or "goodbye" in user_input:
        return f"Goodbye, {user_name}! Have a great day!"
    else:
        return f"I'm sorry, {user_name}, I don't understand that. Can you please rephrase?"

# Function to get the current greeting based on the time of day
def get_greeting():
    now = datetime.datetime.now()
    current_hour = now.hour
    if current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"

# Main function to run the chatbot
def main():
    print("Hello! Welcome to the simple Python chatbot!")
    
    user_name = input("What's your name? ")
    greeting = get_greeting()
    
    print(f"{greeting}, {user_name}!  I'm here to motivate you.  How are you feeling today?")
    print("Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print(f"Chatbot: Goodbye, {user_name}! Have a great day!")
            break
        response = get_response(user_input, user_name)
        print(f"Chatbot: {response}")
        print(f"Chatbot: How else are you feeling?")

# Run the chatbot
if __name__ == "__main__":
    main()