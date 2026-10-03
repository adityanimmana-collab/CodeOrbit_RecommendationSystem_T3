# 🎬 Simple Movie Recommendation System

## CodeOrbit Tech – Artificial Intelligence Internship

### Task 4: Simple Recommendation System

## 📌 Project Description

This project is a simple movie recommendation system developed using Python.

The system recommends movies based on their similarity to a movie selected by the user. It uses a small sample movie dataset containing genres and keywords.

## 🎯 Objectives

* Build a simple recommendation system.
* Use a small sample dataset.
* Calculate similarity between movies.
* Display the top movie recommendations.
* Understand the basic concept of recommendation systems.

## 🛠️ Technologies Used

* Python
* Lists
* Dictionaries
* Sets
* Functions
* String processing

## 🧠 Recommendation Approach

The system uses a simple word-overlap similarity method.

The genre and keywords of each movie are combined and converted into sets of words.

The program then:

1. Takes a movie selected by the user.
2. Compares it with the other movies.
3. Finds common words between the movies.
4. Calculates a similarity score.
5. Sorts movies according to their similarity.
6. Displays the top 3 recommendations.

## ⚙️ How It Works

```text
User selects a movie
        ↓
Find selected movie
        ↓
Compare with other movies
        ↓
Calculate similarity
        ↓
Sort recommendations
        ↓
Display top 3 movies
```

## ▶️ How to Run

Make sure Python is installed.

Run:

```bash
python recommendation_system.py
```

Then enter a movie name from the available movie list.

## 💻 Sample Output

```text
==================================================
       SIMPLE MOVIE RECOMMENDATION SYSTEM
==================================================

Available Movies:
------------------------------
- Inception
- Interstellar
- The Matrix
- Avengers: Endgame
- The Dark Knight
- Titanic
- The Notebook
- Jurassic Park

Enter a movie you like: Inception

Recommended Movies:
------------------------------
```

The recommendation order and similarity scores depend on the sample dataset and similarity calculation.

## 📂 Project Structure

```text
CodeOrbit_RecommendationSystem/
│
├── recommendation_system.py
├── README.md
└── screenshots/
```

## 👨‍💻 Internship Task

**Organization:** CodeOrbit Tech
**Internship:** Artificial Intelligence Internship
**Task:** Simple Recommendation System

## 📚 Learning Outcome

Through this project, I learned the basic concepts of recommendation systems, similarity calculation, Python sets, dictionaries, lists, sorting, and simple data-based recommendations.
