import spacy

nlp = spacy.load("en_core_web_sm")

with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()

doc = nlp(text)

entities = set()

for ent in doc.ents:
    if ent.label_ in ["ORG", "PRODUCT", "WORK_OF_ART"]:
        clean = ent.text.strip()
        if len(clean) > 3:
            clean = clean.replace("\u200c", "")
            entities.add(clean)

# Save safely
with open("entities.txt", "w", encoding="utf-8") as f:
    for e in entities:
        f.write(e + "\n")

print("✅ Entities extracted and saved successfully!")
