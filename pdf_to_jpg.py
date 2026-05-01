import os
import fitz  # PyMuPDF

FOLDER = "certificate"
OUTPUT_FOLDER = "certificate_jpg"
DPI = 150  # Качество

# Создаем папку для JPG
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

print(f"🔄 Конвертация PDF в JPG...\n")

converted = 0
for filename in sorted(os.listdir(FOLDER)):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(FOLDER, filename)
        base_name = os.path.splitext(filename)[0]
        
        try:
            doc = fitz.open(pdf_path)
            
            # Конвертируем каждую страницу
            for page_num in range(len(doc)):
                page = doc[page_num]
                mat = fitz.Matrix(DPI/72, DPI/72)
                pix = page.get_pixmap(matrix=mat)
                
                # Имя файла
                if len(doc) == 1:
                    jpg_name = f"{base_name}.jpg"
                else:
                    jpg_name = f"{base_name}_page{page_num + 1}.jpg"
                
                jpg_path = os.path.join(OUTPUT_FOLDER, jpg_name)
                
                # Сохраняем JPEG с правильным параметром
                pix.save(jpg_path, output="jpg", jpg_quality=85)
                
                size_kb = os.path.getsize(jpg_path) / 1024
                print(f"✅ {filename} → {jpg_name} ({size_kb:.1f} KB)")
                converted += 1
            
            doc.close()
            
        except Exception as e:
            print(f"❌ Ошибка с {filename}: {e}")

print(f"\n🎉 Готово! Конвертировано {converted} страниц(ы)")
print(f"📁 JPG файлы в папке: {OUTPUT_FOLDER}")