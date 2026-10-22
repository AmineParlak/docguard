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

def sistem_mesaji_olustur(belge):
    talimat = ( "Sen bir belge asistanısın. "
               "Yalnızca aşağıdaki belgeye dayanarak cevap ver. "
               "Cevap belgede yoksa 'Bilmiyorum' de, tahmin yürütme. "
               "Kısa ve nazik bir şekilde cevap ver. Düz metin yaz. ")
    return talimat + "\n\nBELGE:\n" + belge

def cevap_al(gecmis):
    cevap = client.chat.completions.create(
        model=MODEL,
        messages=gecmis,    
    )
    return cevap.choices[0].message.content


belge = belge_oku("ornek_belge.txt")
gecmis = [
    {"role": "system", "content": sistem_mesaji_olustur(belge)},
    {"role": "user", "content": "Şirketin kaç çalışanı var?"},
]
print(cevap_al(gecmis))