import requests

ACCESS_TOKEN = 'BQB5dgKXyZ0HrbKyQwPc4WVYvdbHEy07IWZT9xr6ndNbjSsQIevxSj76nNjqbtLvNRApLwuIG6qC40xFzvD4ZAKfFW5pnsJh_cA0FPHX9GGnaNzmmVs'

ARTISTS_IDS = [
    "6eUKZXaKkcviH0Ku9w2n3V", "1dfeR4HaWDbWqFHLkxsg1d", "66CXWjxzNUsdJxJ2JdwvnR",
    "04gDigrS5kc9YWfZHwBETP", "53XhwfbYqKCa1cC15pYq2q", "7dGJo4pcD2V6oG8kP0tJRR",
    "1HY2Jd0NmPuamShAr6KMms", "4gzpq5DPGxSnKTe4SA8HAU", "6vWDO969PvNqNYHIOW5v0m",
    "0du5cEVh5yTK9QJze8zA0C", "5pKCCKE2ajJHZ9KAiaK11H", "0EmeFodog0BfCgMzAIvKQp",
    "1uNFoZAHBGtllmzznpCI3s", "6S2OmqARrzebs0tKUEyXyp", "06HL4z0CvFAxyc27GXpf02"
]

def get_artist_data(artist_id, token):
    artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {'Authorization': f'Bearer {token}'}
    
    try:
        response = requests.get(artist_url, headers=headers)
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter dados do artista {artist_id}: {e}")
        return None
    
    try:
        return response.json()
    except ValueError:
        print(f"Erro ao decodificar a resposta JSON para o artista {artist_id}")
        return None

def get_data():
    token = ACCESS_TOKEN
    artists_data = []

    for artist_id in ARTISTS_IDS:
        artist = get_artist_data(artist_id, token)
        if artist:
            artists_data.append({
                'name': artist.get('name', 'N/A'),
                'followers': artist.get('followers', {}).get('total', 0),
                'popularity': artist.get('popularity', 0),
                'genres': artist.get('genres', [])
            })

    # Filtra artistas de pop e ordena por número de seguidores
    pop_artists = [artist for artist in artists_data if 'pop' in artist['genres']]
    pop_artists_sorted = sorted(pop_artists, key=lambda x: x['followers'], reverse=True)

    # Conta a quantidade de artistas por gênero
    genres_count = {}
    for artist in artists_data:
        for genre in artist['genres']:
            if genre in genres_count:
                genres_count[genre] += 1
            else:
                genres_count[genre] = 1

    # Obtém os 5 gêneros mais comuns
    common_genres = sorted(genres_count.items(), key=lambda x: x[1], reverse=True)[:5]

    return {
        'pop_artists': [{'artist_name': artist['name'], 'followers': artist['followers'], 'popularity': artist['popularity']} for artist in pop_artists_sorted],
        'common_genres': [genre[0] for genre in common_genres],
        'genres_count': {genre[0]: genre[1] for genre in common_genres}
    }

# Exemplo de execução
if __name__ == "__main__":
    data = get_data()
    print(data)
