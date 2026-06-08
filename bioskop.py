def hitung_pemesanan_tiket(jumlah_tiket, hari_nonton, status_member):
    # Mengubah nama fungsi dan variabel menjadi lebih deskriptif sesuai PEP 8
    if hari_nonton.upper() in ["SABTU", "MINGGU"]:
        harga_normal = jumlah_tiket * 70000
    else:
        harga_normal = jumlah_tiket * 50000
        
    potongan_diskon = 0
    if status_member:
        if jumlah_tiket >= 3:
            potongan_diskon = harga_normal * 0.10
            
    total_bayar = harga_normal - potongan_diskon
    
    print("=== BIOSKOP XXI - NOTA PEMESANAN ===")
    print(f"Jumlah Tiket : {jumlah_tiket}")
    print(f"Harga Normal : Rp{harga_normal:,}")
    print(f"Potongan     : Rp{potongan_diskon:,}")
    print(f"Total Bayar  : Rp{total_bayar:,}")
    print("====================================")
    return total_bayar

hitung_pemesanan_tiket(4, "Sabtu", True)