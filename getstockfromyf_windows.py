import yfinance as yf
import pandas as pd

# Hisse senedi sembollerini liste halinde tanımlıyoruz
symbols = ["AAPL", "MSFT", "NVDA", "INTC"]

# Veriyi çekmek istediğimiz tarih aralığını tanımlıyoruz
start_date = "2022-01-01"
end_date = "2024-01-01"

# Verilerin kaydedileceği dosya yolunu belirleyin (Bu kısmı kendi bilgisayarınızdaki uygun Windows yoluna göre düzenleyin)
output_path = "C:\\Kendi\\Dosya\\Yolunuz\\yfinance\\tech_stocks_data.xlsx"  # Buraya kendi Windows output dosya yolunuzu yapıştırın

# ExcelWriter ile aynı dosya içinde farklı sayfalara yazmak için bir nesne oluşturuyoruz
with pd.ExcelWriter(output_path) as writer:
    for symbol in symbols:
        # Her sembol için veriyi çekiyoruz
        data = yf.download(symbol, start=start_date, end=end_date)
        # Veriyi o sembol adıyla bir sayfaya kaydediyoruz
        data.to_excel(writer, sheet_name=symbol)

print(f"Veriler başarıyla '{output_path}' konumuna kaydedildi.")
