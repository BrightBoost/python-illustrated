library = {
    "Jane Eyre": {
        "author(s)": [{"name": "Charlotte Brontë", "birth_year": 1816, "nationality": "British"}],
        "page_count": 659,
        "publication_year": 1847,
        "genres": ["Victorian fiction", "Bildungsroman", "Historical"],
        "rating": 4.6,
        "available": True,
        "borrowed_by": None
    },
    "Python Illustrated": {
        "author(s)": [{"name": "Zia van Putten", "birth_year": 2024, "nationality": "Dutch"}, {"name": "Maaike van Putten", "birth_year": 1991, "nationality": "Dutch"}, {"name": "Imke van Putten", "birth_year": 1997, "nationality": "Dutch"}],
        "page_count": 321,
        "publication_year": 2025,
        "genres": ["Informative", "Education"],
        "rating": 5,
        "available": False,
        "borrowed_by": "Jacob",
    },
    "If Cats Disappeared From The World": {
        "author(s)": [{"name": "Genki Kawamura", "birth_year": 1979, "nationality": "Japanese"}],
        "page_count": 144,
        "publication_year": 2012,
        "genres": ["Literary Fiction", "Magical Realism", "Philosophical Fiction"],
        "rating": 4.2,
        "available": False,
        "borrowed_by": "Wiesje",
    }
}

# Print all book titles (The keys of the library dictionary)
print(list(library.keys()))

# Check and see if Python illustrated is a romance
if "Romance" in library["Python Illustrated"]["genres"]:
    print("Romance is a genre of Python Illustrated")
else:
    print("Romance is not a genre of Python Illustrated")

# Print the nationality of the author of Jane Eyre
print(library["Jane Eyre"]["author(s)"][0]["nationality"])

# Update values when Wiesje returned a book
library["If Cats Disappeared From The World"]["available"] = True
library["If Cats Disappeared From The World"]["borrowed_by"] = None

# Check whether Python Illustrated is available and print who borrowed it if it isn't
if library["Python Illustrated"]["available"]:
    print("Python Illustrated is available!")
elif library["Python Illustrated"]["borrowed_by"]: # checks if borrowed_by is not None before using its value
    print("Python Illustrated is not available and currently borrowed by:", library["Python Illustrated"]["borrowed_by"])
