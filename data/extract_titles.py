import os
import json

docs_folder = "C:/Users/visha/Music/TDS project-1/data/docs"
index_file = os.path.join(docs_folder, "index.json")

titles = {}

for filename in os.listdir(docs_folder):
    if filename.endswith(".md"):
        file_path = os.path.join(docs_folder, filename)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("#"):
                        titles[filename] = line.strip("# ").strip()
                        break
        except UnicodeDecodeError:
            print(f"⚠️ Unicode error in {filename}, skipping.")

with open(index_file, "w", encoding="utf-8") as f:
    json.dump(titles, f, indent=4)

print(f"✅ Index file saved at: {index_file}")
