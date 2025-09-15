import requests
import json
import time
import random


query = '''
query ($username: String) {
  MediaListCollection(userName: $username, type: ANIME) {
    lists {
      name
      entries {
        media {
          id        # Anilist ID
          idMal     # MyAnimeList ID
          title {
            romaji
          }
        }
        score
        status
      }
    }
  }
}
'''

def fetch_user_anime(username, output_file="user_data.jl"):
    url = "https://graphql.anilist.co"
    variables = {"username": username}

    response = requests.post(url, json={"query": query, "variables": variables})
    if response.status_code == 200:
        data = response.json()
        lists = data["data"]["MediaListCollection"]["lists"]

        with open(output_file, "w", encoding="utf-8") as f:
            for list_data in lists:
                for entry in list_data["entries"]:
                    anime_info = {
                        "list_name": list_data["name"],
                        "status": entry.get("status"),
                        "score": entry.get("score"),
                        "id_anilist": entry["media"]["id"],
                        "id_mal": entry["media"].get("idMal"),
                        "title": entry["media"]["title"]["romaji"]
                    }
                    f.write(json.dumps(anime_info, ensure_ascii=False) + "\n")
    else:
        print(f"Error: {response.status_code}: {response.text}")

    time.sleep(random.uniform(2.3, 2.7))


username = "Hausio"
fetch_user_anime(username)