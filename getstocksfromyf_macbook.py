import yfinance as yf
import pandas as pd
symbols = ["PLTR", "BAC", "DNLI", "PFE", "AAPL"]
start_date = "2022-01-01"
end_date = "2024-10-11"
output_path = "/Users//Library/yolunuz/kendi sisteminiz/…/compared_stocks_data.xlsx"
with pd.ExcelWriter(output_path) as writer:
    for symbol in symbols:
        data = yf.download(symbol, start=start_date, end=end_date)
        data.to_excel(writer, sheet_name=symbol)

print(f"Veriler başarıyla '{output_path}' konumuna kaydedildi.")
