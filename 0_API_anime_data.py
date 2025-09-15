import requests
import json
import time
import random


query = ''' 
query Query($page: Int, $perPage: Int, $type: MediaType, $sort: [MediaSort], $popularityGreater: Int, $averageScoreGreater: Int, $isAdult: Boolean, $isMain: Boolean, $recommendationsSort2: [RecommendationSort], $recommendationsPage2: Int, $recommendationsPerPage2: Int) {
  Page(page: $page, perPage: $perPage) {
    media(type: $type, sort: $sort, popularity_greater: $popularityGreater, averageScore_greater: $averageScoreGreater, isAdult: $isAdult) {
      popularity
      averageScore
      id
      idMal
      title {
        romaji
      }
      description
      format
      genres
      startDate {
        month
        year
      }
      status
      source
      duration
      episodes
      countryOfOrigin
      studios(isMain: $isMain) {
        edges {
          node {
            name
          }
        }
      }
      tags {
        name
        rank
      }
      relations {
        edges {
          relationType
          node {
            id
            title {
              romaji
            }
            type
          }
        }
      }
      recommendations(sort: $recommendationsSort2, page: $recommendationsPage2, perPage: $recommendationsPerPage2) {
        edges {
          node {
            mediaRecommendation {
              id
              idMal
            }
          }
        }
      }
    }
  }
}
'''

def fetch_anime(total_pages, per_page=20, start_page=1, output_file="anime_data.jl"):
    url = "https://graphql.anilist.co"

    for p in range(start_page, start_page + total_pages):
        variables = {
            "page": p,
            "perPage": per_page,
            "type": "ANIME",
            "popularityGreater": 1000,
            "isMain": True,
            "isAdult": False,
            "sort": ["POPULARITY_DESC"],
            "recommendationsSort2": ["RATING_DESC"],
            "recommendationsPage2": 1,
            "recommendationsPerPage2": 10,
        }

        response = requests.post(url, json={"query": query, "variables": variables})
        if response.status_code == 200:
            data = response.json()
            media_list = data["data"]["Page"]["media"]

            if not media_list:
              print(f"Fetched all media")
              break

            with open(output_file, "a", encoding="utf-8") as f:
                for anime in media_list:
                    f.write(json.dumps(anime, ensure_ascii=False) + "\n")

            print(f"Fetched page {p}, {len(media_list)} items saved to {output_file}")
        else:
            print(f"Error: {response.status_code} on page {p}")
            break

        time.sleep(random.uniform(2.3, 2.7))


fetch_anime(total_pages=100, per_page=20, start_page=401, output_file="anime_data.jl")