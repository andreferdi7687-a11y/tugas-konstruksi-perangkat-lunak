def OrderTiket(jml, hari, member):
    if hari.upper() == "SABTU" or hari.upper() == "MINGGU":
        p = jml * 70000
    else:
        p = jml * 50000
        
    d = 0
    if member == True:
        if jml >= 3:
            d = p * 0.10
            
    tot = p - d
    
    print("=== BIOSKOP XXI - NOTA PEMESANAN ===")
    print(f"Jumlah Tiket : {jml}")
    print(f"Harga Normal : Rp{p:,}")
    print(f"Potongan     : Rp{d:,}")
    print(f"Total Bayar  : Rp{tot:,}")
    print("====================================")
    return tot

# Driver code
OrderTiket(4, "Sabtu", True)