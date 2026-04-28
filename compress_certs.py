import os
import fitz

FOLDER = "certificate"

for filename in os.listdir(FOLDER):
    if filename.lower().endswith(".pdf"):
        path = os.path.join(FOLDER, filename)
        doc = fitz.open(path)
        
        # garbage=4 убирает дубликаты, deflate сжимает потоки, clean чистит структуру
        out_path = path.replace(".pdf", "_opt.pdf")
        doc.save(out_path, garbage=4, deflate=True, clean=True)
        doc.close()
        
        print(f"✅ {filename} → {os.path.getsize(out_path) / 1024:.1f} KB")