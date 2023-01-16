from rich.prompt import Prompt
from rich.console import Console
from random import choice
from kelimeler import kelime_listesi

SQUARES = {
    'dogru_yer': '🟩',
    'dogru_harf': '🟨',
    'yanlis_yer': '⬛'
}

HOSGELDİN_MESAJI = f'\n[white on blue] KELİMELİĞE HOŞGELDİNİZ [/]\n'   
OYUNCU_TALIMATI = "Tahmin etmeye başlayabilirsiniz.\n" 
TAHMIN_BILDIRISI = "\nTahmininizi girin" 
TAHMIN_HAKKI = 6 

def dogru_yer(letter):
    return f'[black on green]{letter}[/]'

def dogru_harf(letter):
    return f'[black on yellow]{letter}[/]'

def yanlis_yer(letter):
    return f'[black on white]{letter}[/]'

def tahmin_kontrolu(tahmin, cevap):
    tahmin_edilen = []
    kelimelik_sablonu = []
    for i, letter in enumerate(tahmin):
        if cevap[i] == tahmin[i]:
            tahmin_edilen += dogru_yer(letter)
            kelimelik_sablonu.append(SQUARES['dogru_yer'])
        elif letter in cevap:
            tahmin_edilen += dogru_harf(letter)
            kelimelik_sablonu.append(SQUARES['dogru_harf'])
        else:
            tahmin_edilen += yanlis_yer(letter)
            kelimelik_sablonu.append(SQUARES['yanlis_yer'])
    return ''.join(tahmin_edilen), ''.join(kelimelik_sablonu)

def game(console, secilen_kelime):
    oyunu_bitir = False  
    tahmin_edilen_kelimeler = []
    tam_kelimelik_sablonu = []
    tahmin_edilen_kelimeler_hepsi = []

    while not oyunu_bitir:
        tahmin = Prompt.ask(TAHMIN_BILDIRISI).upper()
        while len(tahmin) != 5 or tahmin in tahmin_edilen_kelimeler:
            if tahmin in tahmin_edilen_kelimeler:
                console.print("[red]Bu kelimeyi zaten tahmin ettiniz!!\n[/]")
            else:
                console.print('[red]Lütfen 5 harfli bir kelime giriniz!!\n[/]')
            tahmin = Prompt.ask(TAHMIN_BILDIRISI).upper()
        tahmin_edilen_kelimeler.append(tahmin)
        tahmin_edilen, pattern = tahmin_kontrolu(tahmin, secilen_kelime)
        tahmin_edilen_kelimeler_hepsi.append(tahmin_edilen)
        tam_kelimelik_sablonu.append(pattern)

        console.print(*tahmin_edilen_kelimeler_hepsi, sep="\n")
        if tahmin == secilen_kelime or len(tahmin_edilen_kelimeler) == TAHMIN_HAKKI:
            oyunu_bitir = True
    if len(tahmin_edilen_kelimeler) == TAHMIN_HAKKI and tahmin != secilen_kelime:
        console.print(f"\n[red]WORDLE X/{TAHMIN_HAKKI}[/]")
        console.print(f'\n[green]Correct Word: {secilen_kelime}[/]')
    else:
        console.print(f"\n[green]KELİMELİK {len(tahmin_edilen_kelimeler)}/{TAHMIN_HAKKI}[/]\n")
    console.print(*tam_kelimelik_sablonu, sep="\n")

if __name__ == '__main__':
    console = Console()
    secilen_kelime = choice(kelime_listesi)
    console.print(HOSGELDİN_MESAJI)
    console.print(OYUNCU_TALIMATI)
    game(console, secilen_kelime)


