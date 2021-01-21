# Maturitní projekt - webová stránka zabývající se recepty
## Popis projektu
- cílem projektu je vytvořit fungující webovou stránku,
kde bude funkční registrace a přihlášení uživatele
- uživatel bude moci napsat své vlastní recepty, které se samozřejmě uloží do databáze a zobrazí se na stránce tam, 
kde mají a případně si bude moct uživatel připnout recept do oblíbených
- recepty budou roztříděny dle kategorií (např.: oběd, snídaně, atd..)


## Použité technologie
- Projekt je vytvořen v Djangu
- Databáze využívá SQlite3
- Templates = šablony jsou napsány v HTML


## Spuštění projektu pro Windows:
```
git clone https://github.com/SaikiDean/zaverecny_projekt
cd zaverecny_projekt
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

## Spuštění projektu pro Linux
```
git clone https://github.com/SaikiDean/zaverecny_projekt
cd zaverecny_projekt
virtualenv -p python venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
``
