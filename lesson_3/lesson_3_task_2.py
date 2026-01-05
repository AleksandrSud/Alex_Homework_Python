from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S24 Ultra", "+79101234567"),
    Smartphone("Apple", "iPhone 15 Pro Max", "+79202345678"),
    Smartphone("Xiaomi", "14 Pro", "+79303456789"),
    Smartphone("Google", "Pixel 8 Pro", "+79404567890"),
    Smartphone("OnePlus", "12", "+79505678901")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
