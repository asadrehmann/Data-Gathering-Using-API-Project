from der_module.fetch_data import fetch_all_movies
from der_module.save_data import save_to_json

def main():
    base_url = "https://api.themoviedb.org/3"
    end_point = "movie/popular"
    api_key = "YOUR_API_KEY"

    movies = fetch_all_movies(base_url, end_point, api_key, total_pages=10)

    if movies:   # ✅ safety check
        save_to_json(movies, "data/raw/movies.json")
    else:
        print("No data fetched. Skipping save.")


if __name__ == "__main__":
    main()