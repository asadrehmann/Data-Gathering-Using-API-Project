import requests

api_key = "50894786170734923bca3c91d9bf29ee"


def get_data(base_url, end_point, page=1):
    url = f"{base_url}/{end_point}?api_key={api_key}&page={page}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} on page {page}")
        return None


def fetch_all_movies(base_url, end_point, api_key, total_pages=10):
    movie_data = []

    for page in range(1, total_pages + 1):
        data = get_data(base_url, end_point, page=page)

        if data and "results" in data:
            movie_data.extend(data["results"])
        else:
            print(f"Error fetching page {page}")

    return movie_data
