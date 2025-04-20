import requests
import time

INPUT_FILE = "messages.txt"
OUTPUT_FILE = "messages_en.po"
MODEL_NAME = "llama3"
LANGUAGE = "English"  # change to any language supported by the model

def translate_text(text):
    prompt = f'Translate the following French phrase to {LANGUAGE}, respond ONLY with the translated phrase, nothing else:\n"{text.strip()}"'

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": MODEL_NAME, "prompt": prompt, "stream": False}
    )
    
    if response.status_code != 200:
        print(f"❌ Error: {response.status_code}")
        return "[TRANSLATION ERROR]"
    
    try:
        result = response.json()["response"]
        result = clean_translation(result)
        return result
    except Exception as e:
        print("❌ Parsing error:", e)
        return "[TRANSLATION ERROR]"

def clean_translation(response_text):
    """
    Extracts the most probable single-line translation from the LLM's verbose response.
    """
    lines = response_text.strip().split("\n")
    # Find first valid line that is not empty or explaining things
    for line in lines:
        line = line.strip().strip('"')  # remove extra quotes
        if line and not any(k in line.lower() for k in ["translation", "means", "breakdown", "example", "let me", "here is"]):
            return line
    return response_text.strip()

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    output_lines = []
    current_comment = ""

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("#:"):
            current_comment = line
        else:
            original = line
            translation = translate_text(original)
            output_lines.append(f"{current_comment}\nmsgid \"{original}\"\nmsgstr \"{translation}\"\n")
            print(f"✔️ {original} => {translation}")
            time.sleep(1.5)  # polite delay for local model

    with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
        outfile.write("\n".join(output_lines))

    print(f"\n✅ Done. Translations saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
