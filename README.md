# Tuya/Ledvance Gerätedaten-Manager

Ein Desktop-Tool zum Abrufen und Verwalten von Gerätedaten für Ledvance-Geräte über die Tuya-API.

## Funktionen

- Benutzeroberfläche zum Verwalten und Abrufen von Gerätedaten.
- Speichern und Laden von Benutzerdaten (E-Mail und Passwort) für zukünftige Sitzungen.
- Doppelklick auf eine Zeile in der Geräteübersicht, um detaillierte Informationen anzuzeigen.
- Möglichkeit, Zelleninhalte aus der Tabelle zu kopieren.
- Anzeige des Status und Fehlerbehandlung bei Verbindungsproblemen.

## Voraussetzungen

- Python 3.12 (andere Versionen sollten ebenfalls funktionieren, aber 3.12 wurde getestet)
- Die Python-Bibliotheken:
  - `pycryptodome`
  - `requests`

## Installation

### 1. Python installieren

Stellen Sie sicher, dass Python auf Ihrem System installiert ist. Sie können dies überprüfen, indem Sie den folgenden Befehl im Terminal oder in der Eingabeaufforderung ausführen:

```bash
python --version
```

**Hinweis:** Diese Anwendung wurde mit Python 3.12 getestet. Wenn Python noch nicht installiert ist, können Sie die neueste Version über den Microsoft Store installieren:

```bash
start ms-windows-store://search/?query=python
```

### 2. Abhängigkeiten installieren

Nachdem Python installiert wurde, öffnen Sie das Terminal oder die Eingabeaufforderung und installieren Sie die erforderlichen Python-Bibliotheken mit dem folgenden Befehl:

```bash
pip install pycryptodome requests
```

### 3. Batch-Skript ausführen

Laden Sie das Batch-Skript `ledvance-key-DE.bat` herunter und führen Sie es aus. Das Skript überprüft, ob Python und die notwendigen Bibliotheken installiert sind und startet die Anwendung:

```bash
start ledvance-key-DE.bat
```

Wenn eine der erforderlichen Bibliotheken fehlt, wird sie automatisch installiert.

## Nutzung

1. Starten Sie das Programm, indem Sie das Batch-Skript ausführen.
2. Geben Sie Ihre E-Mail-Adresse und Ihr Passwort in die Eingabefelder ein.
3. Klicken Sie auf **"Gerätedaten abrufen"**, um eine Liste Ihrer Geräte anzuzeigen.
4. Klicken Sie auf eine Zelle in der Tabelle, um deren Inhalt in die Zwischenablage zu kopieren.
5. Doppelklicken Sie auf eine Zeile, um detaillierte Geräteinformationen anzuzeigen.
6. Klicken Sie auf **"Benutzerdaten speichern"**, um Ihre Anmeldedaten für zukünftige Sitzungen zu speichern.

## Lizenz

Dieses Projekt ist unter der [MIT-Lizenz](LICENSE) lizenziert.

## Hilfe

Falls du Hilfe benötigst, kannst du auf den **"Hilfe"**-Button in der Anwendung klicken, um eine detaillierte Anleitung zur Verwendung des Programms zu erhalten.
