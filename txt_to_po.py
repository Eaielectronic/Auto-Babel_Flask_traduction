import polib

INPUT_FILE = "messages_translated.txt"
OUTPUT_FILE = "messages_final.po"

def txt_to_po():
    po = polib.POFile()
    po.metadata = {
        'Content-Type': 'text/plain; charset=UTF-8',
    }

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    comment = ""
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("#:"):
            comment = line[2:].strip()
            i += 1
            if i + 1 < len(lines):
                msgid = lines[i].strip()
                msgstr = lines[i + 1].strip()
                entry = polib.POEntry(
                    msgid=msgid,
                    msgstr=msgstr,
                    occurrences=[tuple(ref.split(":")) for ref in comment.split()]
                )
                po.append(entry)
                i += 2
            else:
                i += 1
        else:
            i += 1

    po.save(OUTPUT_FILE)
    print(f"✅ Generated {OUTPUT_FILE}")

if __name__ == "__main__":
    txt_to_po()
