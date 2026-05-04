from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import io
import os

# Имя исходного файла
input_filename = os.path.join("certificate", "SQL_basic_OTUS.pdf")
# Имя для исправленного файла
output_filename = os.path.join("certificate", "SQL_basic_OTUS_fixed.pdf")

def fix_alignment(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Ошибка: Файл {input_file} не найден!")
        return

    # 1. Читаем исходный PDF
    reader = PdfReader(input_file)
    writer = PdfWriter()
    
    # Берем первую страницу
    page = reader.pages[0]
    
    # Получаем размеры страницы
    page_width = float(page.mediabox.width)
    page_height = float(page.mediabox.height)
    
    print(f"Размер страницы: {page_width}x{page_height}")

    # 2. Создаем "холст" для рисования поверх
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=(page_width, page_height))
    
    # --- РЕГИСТРАЦИЯ ШРИФТА С КИРИЛЛИЦЕЙ ---
    # Используем стандартный шрифт Windows с поддержкой кириллицы
    try:
        # Для Windows:
        pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
        font_name = 'Arial'
    except:
        try:
            # Для Linux/macOS или если Arial не найден:
            pdfmetrics.registerFont(TTFont('DejaVu', 'DejaVuSans.ttf'))
            font_name = 'DejaVu'
        except:
            font_name = 'Helvetica'
            print("Warning: Кириллический шрифт не найден, используется Helvetica")
    
    # --- НАСТРОЙКИ ИСПРАВЛЕНИЯ ---
    
    # Рисуем белый прямоугольник, закрывающий нижние 200 пунктов
    can.setFillColorRGB(1, 1, 1) # Белый цвет
    can.rect(0, 0, page_width, 200, fill=1, stroke=0) 
    
    # Теперь пишем текст заново с правильным шрифтом
    can.setFont(font_name, 10) # Шрифт с кириллицей
    can.setFillColorRGB(0, 0, 0) # Черный цвет
    
    # Текст "Город" (сдвигаем выше)
    can.drawString(100, 150, "Город: _______________") 
    
    # Текст подписи
    can.setFont(font_name, 9)
    can.setFillColorRGB(0, 0, 0.5) # Синий цвет, как в оригинале
    can.drawString(100, 130, "Зам. директора департамента")
    can.drawString(100, 115, "образования")
    
    can.save()
    
    # 3. Накладываем наш "рисунок" на оригинальную страницу
    packet.seek(0)
    new_pdf = PdfReader(packet)
    page.merge_page(new_pdf.pages[0])
    
    # 4. Сохраняем результат
    writer.add_page(page)
    
    with open(output_file, "wb") as f_out:
        writer.write(f_out)
        
    print(f"Успешно! Исправленный файл сохранен как: {output_file}")

if __name__ == "__main__":
    fix_alignment(input_filename, output_filename)