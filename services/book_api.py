import requests as req

OPENLIBRARY_URL = "https://openlibrary.org/api/books"
GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/v1/volumes"

def fetch_book_by_isbn(isbn:str)->dict:
    url = f"{OPENLIBRARY_URL}?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    response = req.get(url)

    if response.status_code != 200:
        return {}
    
    data = response.json().get(f"ISBN:{isbn}",{})

    if not data:
        return {}
    
    return {"title":data.get("title"),"author":data["author"][0]["name"]
             if "author" in data else "Unknown","isbn":isbn,"pages":data.get("number_of_pages",0),
             "release_date":data.get("publish_date"),"price":0.0}

def search_books(query:str,max_results:int=5)->list[dict]:
    params = {"q":query,"maxResults":max_results}
    response = req.get(GOOGLE_BOOKS_URL,params=params)

    if response.status_code != 200:
        return []
    
    results = []

    for item in response.json().get("items",[]):
        volume = item.get("volumeInfo",{})
        sale = item.get("saleInfo",{})

        results.append({
            "title":volume.get("title"),
            "author":", ".join(volume.get("authors",[])) if "authors" in volume else "Unknown",
            "isbn":volume.get("industryIndentifiers",[{}])[0].get("identifier",""),
            "pages":volume.get("pagesCount",0),
            "release_date": volume.get("publishedDate"),
            "price": sale.get("retailPrice", {}).get("amount", 0.0) if "retailPrice" in sale else 0.0,
            })
        
    return results