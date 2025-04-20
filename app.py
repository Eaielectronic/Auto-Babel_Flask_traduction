import requests
import time

input_file = "messages.txt"
output_file = "messages_en.po"

# Fonction de traduction via Ollama local
def translate_with_ollama(prompt_text, model="llama3"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": f"Translate this text from French to English:\n\n{prompt_text}",
            "stream": False
        }
    )
    if response.ok:
        return response.json().get("response", "").strip()
    else:
        print(f"❌ Erreur lors de la requête : {response.status_code}")
        return "[TRANSLATION ERROR]"

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    lines = infile.readlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("#:"):
            context = line
            i += 1
            if i < len(lines):
                original = lines[i].strip()
                if original:
                    translated = translate_with_ollama(original)
                    po_entry = f'{context}\nmsgid "{original}"\nmsgstr "{translated}"\n\n'
                    outfile.write(po_entry)
                    print(f"✔️ Traduit : {original} => {translated}")
                    time.sleep(0.5)  # Petite pause pour éviter de spammer Ollama
        i += 1

print("✅ Fichier .po généré :", output_file)
