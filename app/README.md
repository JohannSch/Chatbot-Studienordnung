# Backend

## Projekt Einrichtung

Python 3.13 (!) ([Download-Link](https://www.python.org/downloads/)) installieren, unter Linux idealerweise mit dem Package Manager.
Dann im Verzeichnis `app` den folgenden Befehl ausführen

```sh
python3.13 -m venv .venv
```

Unter Windows dann bei Benutzung von CMD

```
.venv\Scripts\activate.bat
```

oder bei Benutzung von PowerShell

```
.venv\Scripts\Activate.ps1
```

oder unter Linux/MacOS

```sh
source .venv/bin/activate
```

die virtuelle Umgebung aktivieren und mit dem folgenen Befehl die benötigten Packages installieren

```sh
pip install -r requirements.txt
```

### Ausführen

Bevor der Server gestartet werden kann, muss ein API-Schlüssel als Umgebungsvariable gesetzt werden.
Für ChatAI kann dieser auf der [KISSKI LLM Service page](https://kisski.gwdg.de/en/leistungen/2-02-llm-service/) mit einem Klick auf "Book" auf der rechten Seite erlangt werden. Dafür muss das Formular augefüllt und die Anfrage abgesendet werden.

Nachdem der API-Schlüssel versendet wurde, kann dieser unter Windows mit dem Befehl

```
setx CHAT_AI_API_KEY 'xxxxxx'
```

oder unter Linux/MacOS mit dem Befehl

```sh
export CHAT_AI_API_KEY='xxxxxx'
```

gesetzt werden.
Je nach Entwicklungsumgebung kann es hilfreich sein die IDE danach neu zu starten.

Um für die Entwicklung einen Server zu starten die virtuelle Umgebung aktivieren, falls nicht schon passiert, und den folgenden Befehl nutzen

```sh
uvicorn main:app --reload
```

Dieser Server wird beim Speichern von Änderungen im Code automatisch neu geladen.

## Entwicklung

Für die Entwicklung mit FastAPI stehen die [FastAPI Reference](https://fastapi.tiangolo.com/reference/) und die [FastAPI Tutorials](https://fastapi.tiangolo.com/tutorial) zur Verfügung.