## **Projekt zaliczeniowy w ramach studiów podyplomowych Tester oprogramowania dla aplikacji mobilnych i serwerowych**


- ### Celem projektu była automatyzacja przypadków testowych dla aplikacji internetowej Strava przy pomocy Selenium Webdriver z zastosowaniem Page Object Pattern.





- Projekt opiera się na języku programownia Python oraz korzysta z bibliotek pytest, selenium, faker oraz re. Wymagany jest również Chromedriver
do pobrania z https://chromedriver.chromium.org/getting-started




- Środowisko testowe:

  ```bash
  1. chrome wersja 113.0.5672.126
  2. Ubuntu 22.04.2 LTS

- W projekcie wykorzystamy virtual environment, dla utworzenia hermetycznego środowisko dla aplikacji:
- Sprawdź: [tutorial venv](https://docs.python.org/3/tutorial/venv.html)

  ```bash
  # W projekcie wykorzystamy virtual environment, dla utworzenia hermetycznego środowiska dla bibliotek aplikacji:
  python3 -m venv .venv

  # aktywowanie hermetycznego środowiska
  source .venv/bin/activate
  # przywracamy zależnosci
   pip install -r requirements.txt
  #Deaktywacja środowiska wirtualego
     deactivate

- Procedura uruchomienia  testów:

  ```bash
  #Należy pobrać repozytorium z github na swoje lokalne środowisko:
  $ git clone git@github.com:Anqetil/stravaProjekt.git
  #virtualenv i zależności
  Tworzymy wirtual envirment i przyrwacamy xzależności
  #uruchomienie testów:
  $ pytest ./Tests/tests.py*



- Informacje dodatkowe:

  ```bash
  Lokatory dla projektu aktualne na dzień 05.06.2023, w przypadku zauważenia zmian w lokatorach na stronie głownej testowanej 
  aplikacji, projekt zostanie zaktualizowany.