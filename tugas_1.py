satuan = ['', 'satu', 'dua', 'tiga', 'empat','lima', 'enam', 'tujuh', 'delapan', 'sembilan']

def terbilang(n):
    if n % 1 > 0:
        nilai = str(n)
        posisi_koma = nilai.find('.')
        depan_koma = int(nilai[:posisi_koma])
        belakang_koma = int(nilai[posisi_koma+1:])
        if '.' not in nilai:
            return terbilang(depan_koma)
        elif '.' in nilai:
            return terbilang(depan_koma) + ' koma ' + terbilang(belakang_koma)
    elif n < 10:
        return satuan[int(n)]
    elif n >= 1_000_000_000:
        return terbilang(n // 1_000_000_000) + ' milyar ' + terbilang(n % 1_000_000_000) 
    elif n >= 1_000_000:
        return terbilang(n // 1_000_000) + ' juta ' + terbilang(n % 1_000_000) 
    elif n >= 1000:
        if n // 1000 == 1:
            return " seribu " + terbilang(n % 1000) 
        else:
            return terbilang(n // 1000) + ' ribu ' + terbilang(n % 1000)
    elif n >= 100:
        if n // 100 == 1:
            return " seratus " + terbilang(n % 100)
        else:
            return terbilang(n // 100) + ' ratus ' + terbilang(n % 100)
    elif n >= 20:
        return terbilang(n // 10) + ' puluh ' + terbilang(n % 10)
    else:
        if n == 10:
            return ' sepuluh'
        elif n == 11:
            return ' sebelas'
        else:
            return terbilang(n % 10) + ' belas'
    

n = float(input('Masukkan nilai = '))
print(f'{n:,} = {terbilang(n)}')