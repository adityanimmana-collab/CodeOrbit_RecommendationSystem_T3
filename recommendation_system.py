# CodeOrbit Tech - Artificial Intelligence Internship
# Task 4: Simple Recommendation System

# Sample movie dataset
movies = [
    {
        "title": "Kalki 2898 AD",
        "genre": "Action Sci-Fi Thriller",
        "keywords": "dream mind technology"
    },
    {
        "title": "Karthikeya 2",
        "genre": "Adventure Sci-Fi Drama",
        "keywords": "space science technology"
    },
    {
        "title": "Hanu-Man",
        "genre": "Action Sci-Fi",
        "keywords": "technology computer virtual"
    },
    {
        "title": "Avengers: Endgame",
        "genre": "Action Adventure",
        "keywords": "superhero action battle"
    },
    {
        "title": "Drushyam",
        "genre": "Action Crime Drama",
        "keywords": "superhero crime action"
    },
    {
        "title": "Sita Ramam",
        "genre": "Romance Drama",
        "keywords": "love ship relationship"
    },
    {
        "title": "Hi Nanna",
        "genre": "Romance Drama",
        "keywords": "love relationship emotion"
    },
    {
        "title": "Jurassic Park",
        "genre": "Adventure Sci-Fi",
        "keywords": "dinosaurs science adventure"
    }
]


# Calculate similarity between two movies
def calculate_similarity(movie1, movie2):
    # Combine genre and keywords
    words1 = set(
        (movie1["genre"] + " " + movie1["keywords"]).lower().split()
    )

    words2 = set(
        (movie2["genre"] + " " + movie2["keywords"]).lower().split()
    )

    # Find common words
    common_words = words1.intersection(words2)

    # Calculate simple similarity score
    if len(words1.union(words2)) == 0:
        return 0

    similarity = len(common_words) / len(words1.union(words2))

    return similarity


# Generate movie recommendations
def recommend_movies(selected_movie, number_of_recommendations=3):
    selected = None

    # Find the selected movie
    for movie in movies:
        if movie["title"].lower() == selected_movie.lower():
            selected = movie
            break

    if selected is None:
        return []

    recommendations = []

    # Compare selected movie with every other movie
    for movie in movies:
        if movie["title"] != selected["title"]:
            score = calculate_similarity(selected, movie)

            recommendations.append(
                (movie["title"], score)
            )

    # Sort movies by similarity score
    recommendations.sort(
        key=lambda item: item[1],
        reverse=True
    )

    return recommendations[:number_of_recommendations]


# Display available movies
def display_movies():
    print("\nAvailable Movies:")
    print("-" * 30)

    for movie in movies:
        print("-", movie["title"])


# Main program
def main():
    print("=" * 50)
    print("       SIMPLE MOVIE RECOMMENDATION SYSTEM")
    print("=" * 50)

    display_movies()

    selected_movie = input(
        "\nEnter a movie you like: "
    )

    recommendations = recommend_movies(selected_movie)

    if not recommendations:
        print("\nMovie not found. Please choose a movie from the list.")
        return

    print("\nRecommended Movies:")
    print("-" * 30)

    for title, score in recommendations:
        print(
            f"{title} - Similarity Score: {score:.2f}"
        )


# Start the program
if __name__ == "__main__":
    main()