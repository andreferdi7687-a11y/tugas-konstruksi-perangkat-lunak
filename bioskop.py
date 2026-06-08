git add bioskop.pyHARGA_WEEKDAY = 50000
HARGA_WEEKEND = 70000

MINIMAL_TIKET_DISKON = 3
PERSENTASE_DISKON_MEMBER = 0.10

def hitung_harga_dasar(jumlah_tiket, hari_nonton):
    """Menghitung total harga tiket sebelum potongan berdasarkan hari menonton."""
    if hari_nonton.upper() in ["SABTU", "MINGGU"]:
        return jumlah_tiket * HARGA_WEEKEND
    return jumlah_tiket * HARGA_WEEKDAY

def hitung_potongan_diskon(harga_dasar, jumlah_tiket, is_member):
    """Menghitung total potongan harga jika memenuhi syarat minimal pembelian member."""
    if is_member and jumlah_tiket >= MINIMAL_TIKET_DISKON:
        return harga_dasar * PERSENTASE_DISKON_MEMBER
    return 0.0

def cetak_nota_pemesanan(jumlah_tiket, harga_dasar, diskon, total_akhir):
    """Menampilkan detail nota transaksi pemesanan tiket ke konsol."""
    print("\n" + "=== BIOSKOP XXI - NOTA PEMESANAN ===")
    print(f"Jumlah Tiket : {jumlah_tiket} tiket")
    print(f"Harga Normal : Rp{harga_dasar:,}")
    print(f"Potongan     : Rp{diskon:,}")
    print(f"Total Bayar  : Rp{total_akhir:,}")
    print("====================================")

def hitung_pemesanan_tiket(jumlah_tiket, hari_nonton, status_member):
    """Fungsi utama untuk mengontrol alur proses transaksi tiket bioskop."""
    harga_dasar = hitung_harga_dasar(jumlah_tiket, hari_nonton)
    potongan_diskon = hitung_potongan_diskon(harga_dasar, jumlah_tiket, status_member)
    total_bayar = harga_dasar - potongan_diskon
    
    cetak_nota_pemesanan(jumlah_tiket, harga_dasar, potongan_diskon, total_bayar)
    return total_bayar

if __name__ == "__main__":
    hitung_pemesanan_tiket(jumlah_tiket=4, hari_nonton="Sabtu", status_member=True)