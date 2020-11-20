satuan = ['', 'one', 'two', 'three', 'four','five', 'six', 'seven', 'eight', 'nine']

def terbilang(n):
    if n % 1 > 0:
        nilai = str(n)
        posisi_koma = nilai.find('.')
        depan_koma = int(nilai[:posisi_koma])
        belakang_koma = int(nilai[posisi_koma+1:])
        if '.' not in nilai:
            return terbilang(depan_koma)
        elif '.' in nilai:
            return terbilang(depan_koma) + ' coma ' + terbilang(belakang_koma)
    elif n < 10:
        return satuan[int(n)]
    elif n >= 1_000_000_000:
        return terbilang(n // 1_000_000_000) + ' billion ' + terbilang(n % 1_000_000_000) 
    elif n >= 1_000_000:
        return terbilang(n // 1_000_000) + ' million ' + terbilang(n % 1_000_000) 
    elif n >= 1000:
        if n // 1000 == 1:
            return "one thousand " + terbilang(n % 1000) 
        else:
            return terbilang(n // 1000) + ' thousand ' + terbilang(n % 1000)
    elif n >= 100:
        if n // 100 == 1:
            return " one hundred " + terbilang(n % 100)
        else:
            return terbilang(n // 100) + ' hundred ' + terbilang(n % 100)
    elif n >= 20:
        if n // 10 == 2:
            return'twenty' + terbilang(n % 10) 
        elif n // 10 == 3:
            return'thirty' + terbilang(n % 10) 
        elif n // 10 == 4:
            return'fourty' + terbilang(n % 10) 
        elif n // 10 == 5:
            return'fifty' + terbilang(n % 10) 
        else:
            return terbilang(n // 10) + 'ty' + terbilang(n % 10) 
    else:
        if n == 10:
            return 'ten'
        elif n == 11:
            return 'eleven'
        elif n == 12:
            return 'twelve'
        elif n == 13:
            return 'thirteen'
        elif n == 14:
            return 'forteen'
        elif n == 15:
            return 'fifteen'
        else:
            return terbilang(n % 10) + 'teen'
    

n = float(input('Masukkan nilai = '))
print(f'{n:,} = {terbilang(n)}')