# Frontend

## Empfohlene VS Code Extension

[Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) ist die von Vue.js selbst empfohlene VS Code Extension, die Installation ist also sehr sinnvoll.

## Konfigurationsreferenz

Für die Konfiguration von Vite (Webserver, der das Vue Projekt bereitstellt) kann in der [Vite Configuration Reference](https://vite.dev/config/) nachgelesen werden, wie man etwas konfiguriert.

## Projekt Einrichtung

Node.js ([Download-Link](https://nodejs.org/en/download)) installieren, nicht mit Docker, unten gibt es für Windows/MacOS einen Installer, Linux idealerweise mit dem Package Manager. Dann im Verzeichnis `frontend` den folgenden Befehl ausführen

```sh
npm install
```

### Kompilieren und mit Hot-Reload fürs Development ausführen

Um für die Entwicklung einen Webserver zu starten den folgenden Befehl nutzen

```sh
npm run dev
```

Dieser Server lädt bei Speichern von Änderungen in Code automatisch die Änderungen direkt in die Webseite. Hot-Reload ist nicht immer perfekt, manchmal muss man auch einfach den Server neustarten.

### Kompilieren und Minifizieren für die Produktion

Um das Projekt für das Deployment zu bauen, wird der folgende Befehl verwendet

```sh
npm run build
```

## Entwicklung

Als Ressourcen für die Entwicklung stehen von Vue [Vue Guide](https://vuejs.org/guide/introduction.html) für Vue allgemein und [Vue Router Guide](https://router.vuejs.org/guide/) für Vue Router zur Verfügung.
Zusätzlich ist im bereits erstellten Basis Projekt ein kleines Beispiel zu sehen, wie man Vue und Vue Router verwendet.

## Achitekturielle Herangehensweise

Das Frontend ist, wie im Verzeichnis `frontend/src` zu sehen, in 2 Ordner unterteilt.

In `assets` werden statische Dateien (z.B. Stylesheets oder Bilder) abgelegt, welche innerhalb der Web-App genutzt werden.
Diese kann man dann mittels `@/assets/<Dateiname>` verwenden.
Hier müssen die Dateien mit absoluten Pfad angegeben werden z.B. `/favicon.ico`.

In `components` werden .vue-Dateien abgelegt, die einzelne, wiederverwendbare Komponenten darstellen.
Diese Komponenten können Variablen bekommen, um dynamischer zu werden.
Hier könnte man also beispielsweise eine Textblase als Komponente erstellen.

Die Datei `App.vue` ist die Hauptdatei der Web-App.
Hier wird also der Startpunkt und der Rahmen der App definiert.

Die Datei `main.js` ist das Startskript der App, hier wird das App-Objekt initialisiert.