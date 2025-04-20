import requests
import time
import re

# 🛠️ CONFIGURATION
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"
TARGET_LANG = "en"  # Change here: "en", "de", "es", "it", etc.
DELAY = 1.0  # Delay between calls to avoid overload

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
    i = 0

    while i < len(lines):
        line = lines[i]

        # Keep comment lines
        if line.strip().startswith("#:"):
            output.append(line)
            i += 1
            continue

        # If line is msgid
        if line.strip().startswith('msgid'):
            match = re.match(r'msgid\s+"(.*)"', line.strip())
            if match:
                msgid_text = match.group(1)

                if (i + 1 < len(lines)) and lines[i + 1].strip().startswith('msgstr ""'):
                    translated = ask_ollama(msgid_text, TARGET_LANG)

                    print(f"\n📥 msgid: \"{msgid_text}\"\n🌍 msgstr: \"{translated}\"\n")

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
