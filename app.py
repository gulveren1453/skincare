import os
from flask import Flask, request, render_template

app = Flask(__name__)

# Ana sayfa (index1.html)
@app.route('/')
def index():
    return render_template('index1.html')  # index1.html sayfasını render et

# Form sayfası (form.html)
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        try:
            # Form verilerini alıyoruz
            name = request.form['name']
            surname = request.form['surname']
            age = request.form['age']
            skin_type = request.form['skin-type']

            # Dosyaya kaydedeceğiz
            file_path = os.path.join('templates', 'form_data.txt')  # Veriyi templates klasöründe kaydediyoruz

            # Verileri dosyaya kaydediyoruz
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write(f"Name: {name}\n")
                file.write(f"Surname: {surname}\n")
                file.write(f"Age: {age}\n")
                file.write(f"Skin Type: {skin_type}\n")
                file.write("-" * 40 + "\n")  # Verileri ayırmak için

            return f"Form submitted successfully! Data saved to {file_path}"
        except Exception as e:
            return f"Error saving data: {str(e)}"
    return render_template('form.html')  # form.html'yi render et

# Barcode sayfası (proje.html)
@app.route('/proje')
def barcode():
    return render_template('proje.html')  # proje.html sayfasını render et

if __name__ == '__main__':
    app.run(debug=True)  # Debug modda çalıştırıyoruz




