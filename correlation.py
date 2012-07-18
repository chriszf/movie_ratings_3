#!/usr/bin/env python
from math import sqrt

def pearson_similarity(film1_ratings, film2_ratings):
    """Produces a metric of similarity between movies, 1.0 means the movies are
    essentially identical, -1.0 means they are complete opposites on the
    scale.
    
    @film1_ratings -- A dictionary of movie ratings, of the format {"user_id": rating, "user_id2": rating2}
    @film2_ratings -- A dictionary of movie ratings, of the format {"user_id": rating, "user_id2": rating2}
    
    @returns -- float"""
    common_critics = []

    for critic in film1_ratings:
        if critic in film2_ratings:
            common_critics.append(critic)
    
    if len(common_critics) == 0:
        return 0

    film1_sum = sum(film1_critics[critic] for critic in common_critics)
    film2_sum = sum(film2_critics[critic] for critic in common_critics)

    film1_sum_square  = sum([pow(film1_critics[critic], 2) for critic in common_critics])
    film2_sum_square  = sum([pow(film2_critics[critic], 2) for critic in common_critics])

    product_sum = sum([film1_critics[critic] * film2_critics[critic] for critic in common_critics])

    # Calculate the pearson score
    num_critics = len(common_critics)
    num = product_sum - ((film1_sum * film2_sum)/num_critics)
    den = sqrt((film1_sum_square - pow(film1_sum, 2) / num_critics) * (film2_sum_square - pow(film2_sum, 2)/num_critics))

    if den == 0:
        return 0

    return num/den


if __name__ == "__main__":
    movies = { 
        "Wall-E": { "Ebert": 5.0, "Siskel": 4.0, "LeBron": 5.0, "Moses": 3.7, "Shaq": 4.5, "Bartholomew": 4.8 },
        "The Hangover": { "Ebert": 4.5, "Siskel": 4.2, "LeBron": 4.8, "Moses": 3.5, "Shaq": 4.6, "Bartholomew": 4.7 },
        "The Notebook": { "Ebert": 1.0, "Siskel": 4.5, "LeBron": 3.2, "Moses": 5.7, "Shaq": 0.5, "Bartholomew": 1.2 } }

    print pearson_similarity(movies["Wall-E"], movies["The Notebook"])
    print pearson_similarity(movies["Wall-E"], movies["Wall-E"])
    print pearson_similarity(movies["Wall-E"], movies["The Hangover"])
