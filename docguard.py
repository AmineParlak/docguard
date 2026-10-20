import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv(override=True)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
MODEL = "openai/gpt-oss-120b"


def belge_oku(dosya_adi):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            return dosya.read()
    except FileNotFoundError:
        print(f"Hata: '{dosya_adi}' adlı dosya bulunamadı.")
        return None

print(belge_oku("ornek_belge.txt"))
print(belge_oku("olmayan.txt"))