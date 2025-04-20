import polib

INPUT_FILE = "messages.po"
OUTPUT_FILE = "messages.txt"

def po_to_txt():
    po = polib.pofile(INPUT_FILE)
    lines = []

    for entry in po:
        if not entry.msgid.strip():
            continue
        if entry.occurrences:
            refs = " ".join([f"{ref[0]}:{ref[1]}" for ref in entry.occurrences])
            lines.append(f"#: {refs}")
        lines.append(entry.msgid)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"✅ Converted {INPUT_FILE} to {OUTPUT_FILE}")

if __name__ == "__main__":
    po_to_txt()
