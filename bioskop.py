HARGA_WEEKDAY = 50000
HARGA_WEEKEND = 70000

MINIMAL_TIKET_DISKON = 3
PERSENTASE_DISKON_MEMBER = 0.10

def hitung_pemesanan_tiket(jumlah_tiket, hari_nonton, status_member):
    # Mengganti angka mentah dengan konstanta deskriptif
    if hari_nonton.upper() in ["SABTU", "MINGGU"]:
        harga_normal = jumlah_tiket * HARGA_WEEKEND
    else:
        harga_normal = jumlah_tiket * HARGA_WEEKDAY
        
    potongan_diskon = 0
    if status_member:
        if jumlah_tiket >= MINIMAL_TIKET_DISKON:
            potongan_diskon = harga_normal * PERSENTASE_DISKON_MEMBER
            
    total_bayar = harga_normal - potongan_diskon
    
    print("=== BIOSKOP XXI - NOTA PEMESANAN ===")
    print(f"Jumlah Tiket : {jumlah_tiket}")
    print(f"Harga Normal : Rp{harga_normal:,}")
    print(f"Potongan     : Rp{potongan_diskon:,}")
    print(f"Total Bayar  : Rp{total_bayar:,}")
    print("====================================")
    return total_bayar

hitung_pemesanan_tiket(4, "Sabtu", True)