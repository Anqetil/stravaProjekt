### Projekt zaliczeniowy w ramach studiów podyplomowych Tester oprogramowania dla aplikacji mobilnych i serwerowych

**Celem projektu była automatyzacja przypadków testowych dla aplikacji internetowej Strava przy pomocy Selenium Webdriver z zastosowaniem Page Object Pattern.**

Projekt opiera się na języku programownia Python oraz korzysta z bibliotek pytest, selenium, faker. 

**W celu wykonania automatyzcji wymagany jest również Chromedriver do pobrania z https://chromedriver.chromium.org/getting-started**

> **ⓘ Środowisko testowe** :
>  - chrome wersja 113.0.5672.126
>  - Ubuntu 22.04.2 LTS

W projekcie wykorzystane jest wirtualne środowisko w cely utworzenia hermetycznego środowisko dla aplikacji. Szczegóły: [tutorial venv](https://docs.python.org/3/tutorial/venv.html)


Przygotowanie środowiska testowego:

  ```bash
  git clone git@github.com:Anqetil/stravaProjekt.git
  python3 -m venv .venv
  source .venv/bin/activate
pip install -r requirements.txt
  ```

Wykonanie procedury testowej:

```bash
 pytest ./Tests/tests.py
 ```



> **⚠ UWAGA:** Lokatory dla projektu aktualne na dzień **05.06.2023**, w przypadku zauważenia zmian w lokatorach na stronie głownej testowanej aplikacji, projekt zostanie zaktualizowany.