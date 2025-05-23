import google.generativeai as genai
from datetime import datetime

# Configuration -
GEMINI_API_KEY = 'AIzaSyCzVAwxMHwc5G9bAOXl-VxJnGiON4je1vY'  

# Initialize Gemini
genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel('gemini-1.5-pro')

# Supported platforms and genres
PLATFORMS = ['netflix', 'amazon prime', 'disney+', 'hbo max', 'hulu', 'apple tv+']
GENRES = ['action', 'comedy', 'horror', 'romance', 'sci-fi', 'thriller', 'drama', 'animation']

def get_gemini_response(prompt):
    """Get response from Gemini AI with error handling"""
    try:
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"⚠️ Error getting Gemini response: {str(e)}")
        return None

def recommend_movie(genre, platform):
    """Get movie recommendation from Gemini"""
    prompt = f"""
You are a friendly, confident, and fun movie recommender bot.

Recommend a **specific and currently available** {genre} movie on {platform} (India region). Avoid giving warnings or saying you can't predict the future. Keep the tone exciting and casual like you're talking to a friend.

Provide the following:

🎬 Title: [movie title] ([release year])  
📺 Platform: {platform.capitalize()}

📖 Description: 2-3 sentences summarizing the movie in an engaging way.

🍿 Similar Movies: List 3 similar movies also available on {platform}.

💡 Trivia: 1 cool fact or fun behind-the-scenes trivia about the main movie.

Be confident in your recommendation. Do **not** say things like "it depends" or "I cannot guarantee."
"""

    response = get_gemini_response(prompt)
    return response if response else "Sorry, I couldn't generate a recommendation right now."

def chatbot():
    # Generate dynamic greeting
    greeting = get_gemini_response("Create a friendly 1-sentence welcome message for a movie recommendation chatbot")
    print(greeting or "🎥 Welcome to MovieBot! Let's find your perfect film.")

    print("\nI can recommend movies based on genre and streaming platform.")
    print(f"\nAvailable genres: {', '.join(GENRES)}")
    print(f"Available platforms: {', '.join(PLATFORMS)}")
    print("\nType 'quit' to exit or 'help' for assistance.\n")

    while True:
        # Get genre input
        genre = input("What genre of movie are you interested in? ").strip().lower()

        if genre == 'quit':
            farewell = get_gemini_response("Create a friendly goodbye message for a movie chatbot")
            print(farewell or "🎬 Goodbye! Happy watching!")
            break
        elif genre == 'help':
            print("\nJust tell me a genre and streaming platform, and I'll recommend a great movie!")
            print(f"Genres: {', '.join(GENRES)}")
            print(f"Platforms: {', '.join(PLATFORMS)}\n")
            continue

        if genre not in GENRES:
            print(f"⚠️ Sorry, we don't support '{genre}'. Available genres: {', '.join(GENRES)}\n")
            continue

        # Get platform input
        platform = input(f"What streaming platform? ({', '.join(PLATFORMS)}) ").strip().lower()
        if platform == 'quit':
            farewell = get_gemini_response("Create a friendly goodbye message for a movie chatbot")
            print(farewell or "🎬 Goodbye! Happy watching!")
            break
        elif platform == 'help':
            print(f"\nChoose from these platforms: {', '.join(PLATFORMS)}\n")
            continue

        if platform not in PLATFORMS:
            print(f"⚠️ Sorry, we don't support '{platform}'. Available platforms: {', '.join(PLATFORMS)}\n")
            continue

        # Get and display recommendation
        print("\n🍿 Searching for the perfect recommendation...\n")
        recommendation = recommend_movie(genre, platform)
        print("-" * 60)
        print(recommendation)
        print("-" * 60)

        # Continue or quit
        again = input("\nWould you like another recommendation? (yes/no) ").strip().lower()
        if again != 'yes':
            farewell = get_gemini_response("Create a friendly goodbye message for a movie chatbot")
            print(farewell or "🎬 Goodbye! Happy watching!")
            break
        print()

if __name__ == "__main__":
    try:
        # Verify API key
        if GEMINI_API_KEY == 'YOUR_GEMINI_API_KEY':
            raise ValueError("Please replace 'YOUR_GEMINI_API_KEY' with your actual Gemini API key")

        # Start chatbot
        chatbot()
    except Exception as e:
        print(f"🚨 Error: {e}")
