# DU Larose P1
# Movie recommender

import csv

def load_movies(filename):
    # Load movies from CSV file
    movies = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Clean up the data
                movie = {}
                movie['title'] = row['Title'].strip()
                movie['director'] = row['Director'].strip()
                
                # Split genres by / and clean them
                genres = row['Genre'].split('/')
                movie['genres'] = [g.strip().lower() for g in genres]
                
                movie['rating'] = row['Rating'].strip()
                
                # Convert length to integer
                try:
                    movie['length'] = int(row['Length (min)'])
                except:
                    movie['length'] = 0
                
                # Split actors by comma and clean them
                actors = row['Notable Actors'].split(',')
                movie['actors'] = [a.strip().lower() for a in actors]
                
                movies.append(movie)
        
        print(f"Loaded {len(movies)} movies from {filename}")
        return movies
    
    except FileNotFoundError:
        print(f"Error: Could not find {filename}")
        print("Please make sure movies.csv is in the same folder")
        return []
    except Exception as e:
        print(f"Error loading movies: {e}")
        return []

def filter_by_genre(movies, genre_query):
    # Filter movies by genre
    genre_query = genre_query.strip().lower()
    results = []
    
    for movie in movies:
        if 'genres' in movie:
            for genre in movie['genres']:
                if genre_query in genre:
                    results.append(movie)
                    break
    
    return results

def filter_by_director(movies, director_query):
    # Filter movies by director
    director_query = director_query.strip().lower()
    results = []
    
    for movie in movies:
        if 'director' in movie and director_query in movie['director'].lower():
            results.append(movie)
    
    return results

def filter_by_actor(movies, actor_query):
    # Filter movies by actor
    actor_query = actor_query.strip().lower()
    results = []
    
    for movie in movies:
        if 'actors' in movie:
            for actor in movie['actors']:
                if actor_query in actor:
                    results.append(movie)
                    break
    
    return results

def filter_by_length(movies, min_length=None, max_length=None):
    # Filter movies by length
    results = []
    
    for movie in movies:
        if 'length' in movie and movie['length'] > 0:
            length = movie['length']
            
            # Check if movie length is within range
            if min_length is not None and max_length is not None:
                if min_length <= length <= max_length:
                    results.append(movie)
            elif min_length is not None:
                if length >= min_length:
                    results.append(movie)
            elif max_length is not None:
                if length <= max_length:
                    results.append(movie)
            else:
                # No length filter, include all
                results.append(movie)
    
    return results

def combine_filters(movies, filters):
    # Combine multiple filters (AND logic)
    if not filters:
        return movies
    
    # Start with all movies
    results = movies
    
    # Apply each filter one by one
    for filter_type, filter_value in filters:
        if filter_type == 'genre':
            results = filter_by_genre(results, filter_value)
        elif filter_type == 'director':
            results = filter_by_director(results, filter_value)
        elif filter_type == 'actor':
            results = filter_by_actor(results, filter_value)
        elif filter_type == 'length':
            min_len, max_len = filter_value
            results = filter_by_length(results, min_len, max_len)
    
    return results

def print_movies(movies, show_all=False):
    # Print movie list
    if not movies:
        print("No movies found.")
        return
    
    if show_all:
        print(f"\n=== FULL MOVIE LIST ({len(movies)} movies) ===")
    else:
        print(f"\n=== SEARCH RESULTS ({len(movies)} movies) ===")
    
    for i, movie in enumerate(movies, 1):
        # Format genres for display
        genres = ', '.join([g.title() for g in movie['genres']])
        
        # Format actors for display
        actors = ', '.join([a.title() for a in movie['actors'][:3]])  # Show first 3 actors
        
        print(f"{i}. {movie['title']}")
        print(f"   Genres: {genres}")
        print(f"   Director: {movie['director']}")
        print(f"   Rating: {movie['rating']} | Length: {movie['length']} min")
        print(f"   Actors: {actors}")
        print()

def get_user_filters():
    # Get filter choices from user
    print("\n=== SEARCH / GET RECOMMENDATIONS ===")
    print("Choose filters to apply (enter numbers separated by commas, e.g., 1,3):")
    print("1. Genre")
    print("2. Director")
    print("3. Actor")
    print("4. Length")
    
    while True:
        choice = input("\nEnter your choices (or 'back' to go to main menu): ").strip()
        
        if choice.lower() == 'back':
            return None
        
        try:
            choices = [int(c.strip()) for c in choice.split(',')]
            valid_choices = [1, 2, 3, 4]
            
            # Check if all choices are valid
            if all(c in valid_choices for c in choices):
                return choices
            else:
                print("Please enter only numbers 1-4, separated by commas")
        except:
            print("Please enter numbers separated by commas, like: 1,3")

def get_filter_values(choices):
    # Get values for each selected filter
    filters = []
    
    for choice in choices:
        if choice == 1:
            # Genre filter
            genre = input("Enter genre ('Science Fiction', 'Comedy' 'etc'): ").strip()
            if genre:
                filters.append(('genre', genre))
        
        elif choice == 2:
            # Director filter
            director = input("Enter director name: ").strip()
            if director:
                filters.append(('director', director))
        
        elif choice == 3:
            # Actor filter
            actor = input("Enter actor name: ").strip()
            if actor:
                filters.append(('actor', actor))
        
        elif choice == 4:
            # Length filter
            print("Enter length range (in minutes):")
            min_str = input("Minimum length (or press Enter for no minimum): ").strip()
            max_str = input("Maximum length (or press Enter for no maximum): ").strip()
            
            min_len = None
            max_len = None
            
            if min_str:
                try:
                    min_len = int(min_str)
                except:
                    print("Invalid minimum length, ignoring...")
            
            if max_str:
                try:
                    max_len = int(max_str)
                except:
                    print("Invalid maximum length, ignoring...")
            
            if min_len is not None or max_len is not None:
                filters.append(('length', (min_len, max_len)))
    
    return filters

def show_movie_details(movie):
    # Show detailed information about a movie
    print(f"\n=== {movie['title'].upper()} ===")
    print(f"Director: {movie['director']}")
    
    genres = ', '.join([g.title() for g in movie['genres']])
    print(f"Genres: {genres}")
    
    print(f"Rating: {movie['rating']}")
    print(f"Length: {movie['length']} minutes")
    
    actors = ', '.join([a.title() for a in movie['actors']])
    print(f"Notable Actors: {actors}")
    print("=" * 40)

def search_movies(movies):
    # Handle the search flow
    while True:
        choices = get_user_filters()
        
        if choices is None:
            return  # Go back to main menu
        
        if not choices:
            print("No filters selected. Try again.")
            continue
        
        filters = get_filter_values(choices)
        
        if not filters:
            print("No filter values entered. Try again.")
            continue
        
        # Apply filters
        results = combine_filters(movies, filters)
        
        if not results:
            print("\nNo movies match those filters.")
            print("Try removing one filter or widening the length range.")
            continue
        
        # Show results
        print_movies(results)
        
        # Option to see detals
        print("Enter a movie number to see details,")
        print("or 'search' to search again,")
        print("or 'menu' to return to main menu.")
        
        while True:
            action = input("\nYour choice: ").strip().lower()
            
            if action == 'menu':
                return
            elif action == 'search':
                break  #go back to search screen
            else:
                try:
                    movie_num = int(action)
                    if 1 <= movie_num <= len(results):
                        show_movie_details(results[movie_num - 1])
                        
                        print("\nEnter 'back' to return to results,")
                        print("or 'menu' to return to main menu.")
                        
                        sub_action = input("Your choice: ").strip().lower()
                        if sub_action == 'menu':
                            return
                        # Otherwise just show the results again
                        print_movies(results)
                        print("Enter a movie number, 'search', or 'menu':")
                    else:
                        print(f"Please enter a number between 1 and {len(results)}")
                except:
                    print("Please enter a valid movie number, 'search', or 'menu'")

def main():
    # Main function that runs the progran
    print("=" * 50)
    print("MOVIE RECOMMENDER SYSTEM")
    print("=" * 50)
    print("Find movies based on genre, director, actors, or length!")
    print("You can search with multiple filters at once.")
    print()
    
    # Load movies
    movies = load_movies("movies.csv")
    
    if not movies:
        print("Cannot run without movie data. Exiting.")
        return
    
    # Main menu loop
    while True:
        print("\n=== MAIN MENU ===")
        print("Type the number for the action you want:")
        print("1. Search / Get Recommendations")
        print("2. Print Full Movie List")
        print("3. Exit")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == '1':
            search_movies(movies)
        
        elif choice == '2':
            print_movies(movies, show_all=True)
            
            # Ask if they want to see details
            print("Enter a movie number to see details,")
            print("or 'menu' to return to main menu.")
            
            while True:
                action = input("\nYour choice: ").strip().lower()
                
                if action == 'menu':
                    break
                else:
                    try:
                        movie_num = int(action)
                        if 1 <= movie_num <= len(movies):
                            show_movie_details(movies[movie_num - 1])
                            print("\nEnter another movie number or 'menu':")
                        else:
                            print(f"Please enter a number between 1 and {len(movies)}")
                    except:
                        print("Please enter a valid movie number or 'menu'")
        
        elif choice == '3':
            print("\nThanks for using Movie Recommender! Goodbye!")
            break
        
        else:
            print("Please enter 1, 2, or 3")
# Restart/ Start the program again            
main()

