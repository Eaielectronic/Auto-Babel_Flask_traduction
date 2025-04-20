# Auto-Babel_Flask_traduction
Automatic PO translation using a local Ollama AI model (LLaMA 3). Translate .po or .txt files line by line into gettext format (msgid/msgstr). Supports Windows, macOS, and Linux.


Parfait ! Voici une **description du dépôt** + un **README bilingue (🇬🇧 English + 🇫🇷 Français)** clair, structuré, et détaillé.

---

## 🧾 Description du dépôt (à mettre dans `description` sur GitHub)

> Automatic PO translation using a local Ollama AI model (LLaMA 3). Translate `.po` or `.txt` files line by line into gettext format (`msgid`/`msgstr`). Supports Windows, macOS, and Linux.  

---

## 📘 README.md (Markdown complet, avec 🇬🇧 EN + 🇫🇷 FR)

```markdown
# 🌍 AutoBabel - AI-Powered PO File Translator

Automatically translate `.po` or `.txt` files line by line using a local LLaMA 3 model via [Ollama](https://ollama.com/).  
Generates ready-to-use gettext format entries:

```po
#: templates/index.html:11
msgid "Bonjour"
msgstr "Hello"
```

## 📦 Features

- Translate gettext PO strings using **LLaMA 3** (`llama3:8b`) locally.
- Compatible with `.txt` and `.po` style inputs.
- Cross-platform: works on **Windows, macOS, and Linux**.
- No API keys, no cloud – fully local with Ollama.

---

## 📥 Requirements

- Python 3.8+
- Ollama installed and running
- Model pulled: `llama3` or another preferred model

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/auto-babel.git
cd auto-babel
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Install and run Ollama

#### 🖥️ Install Ollama

- Go to [ollama.com/download](https://ollama.com/download)
- Download and install for your OS

#### 📦 Pull the model

```bash
ollama pull llama3
```

#### 🔄 Start Ollama daemon

```bash
ollama serve
```

(Keep this running in the background)

---

## 🧠 Usage

### Prepare your text

Create a file like `messages.txt`:

```
#: templates/home.html:10
Bonjour
#: templates/home.html:11
Se connecter
```

### Run the translator

```bash
python translate.py
```

This will generate `messages_en.po`:

```po
#: templates/home.html:10
msgid "Bonjour"
msgstr "Hello"

#: templates/home.html:11
msgid "Se connecter"
msgstr "Log in"
```

---

## ⚙️ Configuration

Edit `translate.py` to change:
- Model used (`llama3`, `mistral`, etc.)
- Output path
- Delay between requests

---

## ❓ FAQ

**Q:** Does this require internet?  
**A:** No. Everything runs locally via Ollama and your system resources.

**Q:** Can I translate existing `.po` files?  
**A:** Yes – just extract the French parts to a `.txt` using a script or manually.

---

## 🇫🇷 Documentation en Français

### 📥 Prérequis

- Python 3.8 ou plus
- Ollama installé localement
- Modèle téléchargé (ex: `llama3`)

### 🚀 Installation

1. Cloner le dépôt :
```bash
git clone https://github.com/votre-nom/auto-babel.git
cd auto-babel
```

2. Créer l'environnement :
```bash
python -m venv .venv
source .venv/bin/activate  # Sous Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

3. Installer et lancer Ollama :
```bash
ollama pull llama3
ollama serve
```

Laisser `ollama serve` ouvert dans un terminal.

---

### 📄 Format du fichier d’entrée

Créer un fichier `messages.txt` :

```
#: templates/page.html:20
Mot de passe oublié ?
#: templates/page.html:21
Créer un compte
```

---

### ▶️ Lancer la traduction

```bash
python translate.py
```

Résultat dans `messages_en.po` :

```po
#: templates/page.html:20
msgid "Mot de passe oublié ?"
msgstr "Forgot your password?"

#: templates/page.html:21
msgid "Créer un compte"
msgstr "Create an account"
```

---

## 🛠️ À faire

- [ ] Support des fichiers `.po` directs
- [ ] Interface web
- [ ] Traduction par lots

---

## 📄 Licence

MIT – Utilisation libre, contributions bienvenues !

---

### 💬 Contact

Ouvert aux issues, forks et contributions !  
Made with ❤️ and local AI.

```

---

Souhaites-tu aussi que je te génère le script `translate.py` complet et le `requirements.txt` pour ton dépôt ?
