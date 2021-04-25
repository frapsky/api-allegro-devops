# api-allegro-devops
 
--- HOW TO RUN ---


1)Przygotowałem dwie opcje przetestowania aplikacji, najlepsza i najszybsza zarazem według mnie to
zainstalować Dockera na swoim komputerze, następnie pobrać obraz z repozytorium dockera 
przy użyciu komendy:  

	docker pull frapsky/api-allegro-devops

Następnie z poziomu konsoli wpisz:

	docker run -p 8000:8000 api-allegro-devops

Serwer powinien już wystartować.
Możesz przetestować przy pomocy Postman'a, wysyłając plik .png na endpoint http://localhost:8000/api/rotate 

2) Kolejną opcją jest uruchomienie pobranej aplikacji  z repozytorium GIT
 rozpakuj pliki a następnie uruchom IDE lub konsolę

Musisz mieć zainstalowanego Pythona na swoim komputerze!

3) Zainstaluj dodatkowe biblioteki potrzebne do uruchomienia:
	pip install Pillow aiofile fastapi python-multipart hypercorn asyncio uvicorn

4) Otwórz terminal lub IDE i zmień ścieżkę na taką, w której znajduje się plik main.py
  
5) Wpisz: uvicorn main:app --reload

W tym momencie uruchamia się serwer z otwartym portem localhost:8000

6)Możesz przetestować przy pomocy Postman'a, wysyłając plik .png na endpoint http://localhost:8000/api/rotate 

7)Z poziomu graficznego GUI FastAPI pod linkiem http://127.0.0.1:8000/docs, gdzie klikając przycisk
"Try it out" możesz przesłać plik, który następnie powinien zostać zwrócony :)

