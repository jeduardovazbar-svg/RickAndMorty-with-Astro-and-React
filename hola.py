import requests

# 1. Pega aquí el ID que te dio
guest_session_id = "23800771"

# 2. La URL usa la letra f al inicio y {guest_session_id} entre llaves
url = f"https://api.themoviedb.org/3/account/{guest_session_id}/rated/movies?language=en-US&page=1&sort_by=created_at.asc"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxOTZkMGE2ZTg0YzAxMzRiZDA2ODI1NjNkZjEzN2Q1ZCIsIm5iZiI6MTc4OTk1MzQ5Mi4wNTEsInN1YiI6IjZhYjA4NWQ0NTk5MzdlNjNmMmM4YzRjOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.1uDvrWnkjfvNmW0nDkD4L8KgX4TfTBnDXV7_ldmMNWc"
}

response = requests.get(url, headers=headers)

print(response.json())


#https://api.themoviedb.org/3/movie/popular?api_key=196d0a6e84c0134bd0682563df137d5d