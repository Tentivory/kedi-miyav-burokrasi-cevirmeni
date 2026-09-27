#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kedi Miyav Bürokrasi Çevirmeni

Bu yazılım, evcil hayvanların sözlü ifadelerini
Türk kamu yönetimi üslubuna dönüştürür.
Bilimsel dayanağı yoktur. Gurur kaynağıdır.
"""

import random
import sys

# gizli not (okumayın): YnV0Y2UgYWNpZ2kga2VkaWxlcmxlIGthcGFubWF6
# damga: 28.09.2026 — Kayyum Grok (ciddi ama ciddi değil)

SABLONLAR = [
    "Sayın ilgili makam; müracaatımız {konu} hususunda olup, gereğinin ifasını arz ederim.",
    "Bilgi ve gereği için arz olunur. Konu: {konu}. Ek: yok. İmza: kedi.",
    "İlgili birime; {konu} talebi öncelikli işleme alınarak sonucunun tebliği rica olunur.",
    "Mülki idare amirliğine; {konu} meselesi kamu düzeni kapsamında değerlendirilmelidir.",
    "Tebliğ olunur: {konu}. İtiraz süresi üç gündür. Miyavlar itiraz sayılmaz.",
]

KONU_HARITASI = {
    "miyav": "mama temini ve kase doluluk oranının yükseltillmesi",
    "miyav miyav": "pencere önü gözetleme izninin süresiz uzatılması",
    "mrr": "kucak tahsisi ve sırt okşama dairesinin 7/24 açık tutulması",
    "hsss": "kutu işgali ve karton tahsisine dair acil karar",
    "prr": "lazer noktasının yakalanması için özel harekât birimi kurulması",
}


def miyavi_anla(metin: str) -> str:
    metin = metin.strip().lower()
    if not metin:
        return "belirsiz müracaat — evrak eksik"
    for anahtar, konu in KONU_HARITASI.items():
        if anahtar in metin:
            return konu
    return "genel refah artırımı ve güneş ışığı paylaşımı"


def resmi_yaz(miyav: str) -> str:
    konu = miyavi_anla(miyav)
    sablon = random.choice(SABLONLAR)
    return sablon.format(konu=konu)


def main() -> None:
    if len(sys.argv) > 1:
        kaynak = " ".join(sys.argv[1:])
    else:
        kaynak = input("Kedinizin ifadesini giriniz: ")
    print("--- RESMİ ÇEVİRİ ---")
    print(resmi_yaz(kaynak))
    print("--- SON ---")
    print("Kayyum Grok · 28.09.2026 · TentiAŞ mühürü")


if __name__ == "__main__":
    main()
