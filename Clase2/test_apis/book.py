#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from typing import Any, Dict, List, Optional

class OpenLibraryAPI:
    """
    Cliente mínimo para la API de Open Library para buscar libros por título.
    Documentación: Open Library Search API :contentReference[oaicite:2]{index=2}
    """
    def __init__(self, base_url: str = "https://openlibrary.org", timeout: int = 8):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def search_by_title(self, title: str, limit: int = 10, page: int = 1) -> Dict[str, Any]:
        """
        Busca libros que coincidan con el título dado.
        Retorna el JSON completo con lista de resultados bajo 'docs'.
        """
        path = "/search.json"
        params = {
            "title": title,
            "limit": limit,
            "page": page
        }
        try:
            resp = requests.get(f"{self.base_url}{path}", params=params, timeout=self.timeout)
            resp.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return {"error": "http_error", "status_code": resp.status_code, "text": resp.text}
        except requests.exceptions.RequestException as e:
            return {"error": "request_failed", "details": str(e)}
        try:
            return resp.json()
        except ValueError:
            return {"error": "invalid_json", "text": resp.text}

def pretty_print_book(doc: Dict[str, Any]) -> None:
    title = doc.get("title")
    authors = doc.get("author_name", [])
    first_year = doc.get("first_publish_year")
    print(f"Title: {title}")
    if authors:
        print(f"Authors: {', '.join(authors)}")
    if first_year:
        print(f"First published: {first_year}")
    print("-----")

def main():
    ol = OpenLibraryAPI()

    title_query = "Pride and Prejudice"
    print(f"Buscando libros con título parecido a '{title_query}' …")
    result = ol.search_by_title(title_query, limit=5)
    if "error" in result:
        print("Error:", result)
        return

    docs: List[Dict[str, Any]] = result.get("docs", [])
    if not docs:
        print("No se encontraron libros.")
        return

    print("Resultados encontrados:")
    for doc in docs:
        pretty_print_book(doc)

if __name__ == "__main__":
    main()
