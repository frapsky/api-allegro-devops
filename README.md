# api-allegro-devops
 
--- HOW TO RUN ---


1)Przygotowałem dwie opcje przetestowania aplikacji, najlepsza i najszybsza zarazem według mnie to
zainstalować Dockera na swoim komputerze, następnie pobrać obraz z repozytorium dockera 
przy użyciu komendy:  

	docker pull frapsky/api-allegro-devops

Następnie z poziomu konsoli wpisz:

	docker run -p 8000:8000 api-allegro-devops
	
Kolejna opcja to sklokonowanie repozytorium i zbudowanie obrazu:

	git clone https://github.com/frapsky/api-allegro-devops.git
	cd ./api-allegro-devops
	docker build -t api-allegro-devops .
	docker run -p 8080:8080 api-allegro-devops

Serwer powinien już wystartować.
Możesz przetestować przy pomocy Postman'a, wysyłając plik .png na endpoint http://localhost:8000/api/rotate 

2) Kolejną opcją jest uruchomienie pobranej aplikacji  z repozytorium GIT
 rozpakuj pliki a następnie uruchom IDE lub konsolę

Musisz mieć zainstalowanego Pythona na swoim komputerze!

3) Zainstaluj dodatkowe biblioteki potrzebne do uruchomienia:

	pip install Pillow aiofile fastapi python-multipart hypercorn asyncio uvicorn
	pip install -r requirements.txt
	
5) Otwórz terminal lub IDE i zmień ścieżkę na taką, w której znajduje się plik main.py
  
5) Wpisz: uvicorn main:app --reload

W tym momencie uruchamia się serwer z otwartym portem localhost:8000

6)Możesz przetestować przy pomocy Postman'a, wysyłając plik .png na endpoint http://localhost:8000/api/rotate 

7)Z poziomu graficznego GUI FastAPI pod linkiem http://127.0.0.1:8000/docs, gdzie klikając przycisk
"Try it out" możesz przesłać plik, który następnie powinien zostać zwrócony :)


## Example POST request which contains a .png file in body

Postman POST request example:

![postman_post_request](https://user-images.githubusercontent.com/59486011/116008351-650f7280-a614-11eb-9037-c35a4b019897.png)

Source image which contains a line (3x white px and 3x red px):

![papuga_kreska](https://user-images.githubusercontent.com/59486011/116008437-d51df880-a614-11eb-844c-e4bcef305c8d.png)

Response image: 

![post_response](https://user-images.githubusercontent.com/59486011/116008424-bcadde00-a614-11eb-8ba6-0d2d699b73d0.png)


