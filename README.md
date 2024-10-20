# Get Stock Data from Yahoo Finance with Python

## English

This repository contains a Python script to fetch stock data from Yahoo Finance using the `yfinance` library. The script retrieves stock data for specific companies, saves it to an Excel file, and organizes the data into separate sheets for each stock.

### How to Use

1. **Install Required Libraries**:
   Before running the script, ensure you have `yfinance` and `pandas` installed. You can install them using the following commands:
   ```bash
   pip install yfinance pandas

   This Python script allows you to fetch stock data from Yahoo Finance and save it in an Excel file. The script works for both Windows and Mac operating systems. However, paths differ depending on the system you are using. Below is how you can update the file paths accordingly:

Windows Path: In Windows, paths use backslashes (\\). For example:

python
output_path = "C:\\Users\\your-username\\Downloads\\yfinance\\tech_stocks_data.xlsx"
Mac Path: In Mac, paths use forward slashes (/). For example:

python
output_path = "/Users/your-username/Downloads/yfinance/tech_stocks_data.xlsx"
Please make sure to adjust the file path according to your operating system before running the script.

## Türkçe
Bu depo, Yahoo Finance üzerinden yfinance kütüphanesi kullanarak hisse senedi verisi çekmek için bir Python betiği içerir. Betik, belirli şirketler için hisse senedi verilerini alır, bir Excel dosyasına kaydeder ve her bir hisse senedi için ayrı sayfalara organize eder.

Gerekli Kütüphaneleri Kurun: Betiği çalıştırmadan önce yfinance ve pandas kütüphanelerini kurduğunuzdan emin olun.
pip install yfinance pandas

Bu Python betiği, Yahoo Finance üzerinden hisse senedi verilerini çekip bir Excel dosyasına kaydetmenize olanak tanır. Betik, hem Windows hem de Mac işletim sistemlerinde çalışır. Ancak, kullandığınız sisteme bağlı olarak dosya yolları farklılık gösterir. Aşağıda, dosya yollarını nasıl güncelleyeceğiniz açıklanmıştır:

Windows Dosya Yolu: Windows'ta yollar ters eğik çizgi (\\) kullanır. Örneğin:

python
output_path = "C:\\Users\\kullanıcı-adınız\\Downloads\\yfinance\\tech_stocks_data.xlsx"
Mac Dosya Yolu: Mac'te yollar eğik çizgi (/) kullanır. Örneğin:

python
output_path = "/Users/kullanıcı-adınız/Downloads/yfinance/tech_stocks_data.xlsx"


