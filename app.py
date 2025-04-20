import requests
import time
import re

# 🛠️ CONFIGURATION
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

TARGET_LANG = "en"  # 🌐 Language cible de la traduction ("en", "de", "es", etc.)
DELAY = 1.5  # ⏱️ Délai entre chaque requête (en secondes)

# ⚠️ Important : réduire ce délai peut surcharger le modèle ou provoquer des réponses tronquées.
# Ollama fonctionne localement, donc si vous enchaînez trop vite les prompts, le LLM peut devenir instable ou bugger.

INPUT_FILE = "messages.po"
OUTPUT_FILE = f"messages_{TARGET_LANG}.po"

def ask_ollama(text, lang):
    prompt = f'Translate the following from French to {lang.upper()}.\nReturn only the translation:\n\n"{text}"'
    try:
        res = requests.post(OLLAMA_URL, json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        })
        if res.status_code == 200:
            translation = res.json().get("response", "").strip()
            return translation.replace('"', '').strip()
        else:
            print(f"⚠️ HTTP Error {res.status_code} for text: {text}")
            return ""
    except Exception as e:
        print(f"❌ Exception: {e}")
        return ""

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f_in:
        lines = f_in.readlines()

    output = []
    total_strings = sum(1 for l in lines if l.strip().startswith('msgid ') and '""' not in l)
    translated_count = 0
    i = 0

    while i < len(lines):
        line = lines[i]

        if line.strip().startswith("#:"):
            output.append(line)
            i += 1
            continue

        if line.strip().startswith('msgid'):
            match = re.match(r'msgid\s+"(.*)"', line.strip())
            if match:
                msgid_text = match.group(1)

                if (i + 1 < len(lines)) and lines[i + 1].strip() == 'msgstr ""':
                    translated = ask_ollama(msgid_text, TARGET_LANG)
                    translated_count += 1
                    percent = (translated_count / total_strings) * 100

                    print(f"\n🔄 [{translated_count}/{total_strings}] {percent:.1f}%")
                    print(f" 📥msgid: \"{msgid_text}\"\n🌍 msgstr: \"{translated}\"\n")

                    output.append(f'msgid "{msgid_text}"\n')
                    output.append(f'msgstr "{translated}"\n\n')

                    i += 2
                    time.sleep(DELAY)
                else:
                    output.append(line)
                    i += 1
            else:
                output.append(line)
                i += 1
        else:
            output.append(line)
            i += 1

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f_out:
        f_out.writelines(output)

    print(f"\n✅ Translation complete! File saved as: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
