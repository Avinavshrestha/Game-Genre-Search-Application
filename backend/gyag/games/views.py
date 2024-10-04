from django.http import JsonResponse
from django.views import View
from games.models import GameGenre
import numpy as np
from collections import defaultdict

class SearchView(View):
    def get(self, request):
        print("I'm here")
        query = request.GET.get('query', '')
        if not query:
            return JsonResponse([], safe=False)

        # Synonyms mapping
        synonyms = {
            "shooter": ["shooter", "FPS", "firearm", "gun", "combat", "shooting", "action"],
            "shooting": ["shooter", "FPS", "firearm", "gun", "combat", "shooting", "action"],
            "action": ["action", "combat", "shooter", "battling", "fighting"],
            "role-playing": ["RPG", "role-playing", "adventure", "character"],
            "simulation": ["simulation", "realism", "life sim", "manager"],
            "puzzle": ["puzzle", "logic", "brain teaser"],
            "fighting": ["fighting", "combat", "brawler"],
            "racing": ["racing", "driving", "vehicles"],
            "stealth": ["stealth", "sneaking", "espionage"],
            "horror": ["horror", "thriller", "fear"],
            "survival": ["survival", "endurance", "resource management"],
            "open world": ["open world", "exploration", "sandbox"],
            "MOBA": ["MOBA", "multiplayer online battle arena", "team strategy"],
            "MMO": ["MMO", "massively multiplayer online", "online community"],
            "card": ["card", "deck", "strategy"],
            "text-based": ["text-based", "interactive fiction", "narrative"],
        }

        # Expand the query with synonyms
        expanded_query = set()
        for word in query.lower().split():
            expanded_query.update(synonyms.get(word, [word]))

        # Retrieve all genres from the database
        genres = GameGenre.objects.all()
        documents = []
        for genre in genres:
            # Combine title, description, and games into one document
            documents.append(f"{genre.title} {genre.description} {genre.games}")

        # Create a term frequency (TF) dictionary for documents and the query
        def compute_term_frequency(doc):
            tf = defaultdict(int)
            for term in doc.lower().split():
                tf[term] += 1
            return tf

        # Compute TF for documents
        document_tfs = [compute_term_frequency(doc) for doc in documents]

        # Compute TF for the query
        query_tf = compute_term_frequency(" ".join(expanded_query))

        # Compute the cosine similarity
        def cosine_similarity(doc_tf, query_tf):
            dot_product = sum(doc_tf[term] * query_tf.get(term, 0) for term in doc_tf)
            doc_magnitude = np.sqrt(sum(tf ** 2 for tf in doc_tf.values()))
            query_magnitude = np.sqrt(sum(tf ** 2 for tf in query_tf.values()))
            if doc_magnitude == 0 or query_magnitude == 0:
                return 0.0
            return dot_product / (doc_magnitude * query_magnitude)

        # Calculate similarities and collect results
        results = []
        for index, genre in enumerate(genres):
            score = cosine_similarity(document_tfs[index], query_tf)
            if score > 0:  # Only include scores greater than 0
                results.append({
                    "title": genre.title,
                    "description": genre.description,
                    "games": genre.games,
                    "score": float(score),  # Convert to float for JSON serialization
                })

        # Sort results by score in descending order
        results.sort(key=lambda x: x["score"], reverse=True)

        return JsonResponse(results, safe=False)
