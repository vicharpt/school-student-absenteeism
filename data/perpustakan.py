petunjuk = {
    "menu": ["menu 1", "menu 2", "mengatur konfigurasi aplikasi"],
    "menu_1": {
        "feature": [
            "Memberikan keterangan siswa dengan simbol yang tertera pada menu di bagian bawah tabel absensi",
            "Dapat keluar paksa aplikasi dengan mengetikan (exit)",
            "Ketika memberikan keterangan pada siswa maka tabel secara otomatis di hilangkan, kecuali tampilan menu",
            "Ketika sudah memberikan keterangan pada siswa akan memunculkan history siswa yang sebelumnya di isi",
            "Jika ingin menampilkan tabel siswa maka bisa mengetikan simbol ($)",
            "Jika melakukan perubahan pada file (config.conf). maka pada bagian atas akan menampilkan sebuah peringatan tentang perubahan tanggal"
        ],
        "design": [
            "Pada bagian atas berisi keterangan tahun, bulan, dan tanggal",
            "Memiliki tampilan layar utama yaitu tabel yang mepresentasikan data siswa seperti nomor absen, nomor induk, nama siswa, jenis kelamin, keterangan kehadir siswa",
            "Memiliki menu untuk memudahkan penggunaan aplikasi"
        ]
    },
    "menu_2": {
        "feature": [
            "Fitur pada menu 2 menggunakan file (config.conf) yang berisi konfigurasi aplikasi",
        ],
        "design": [
            "Pada bagian atas berisi keterangan tahun, bulan, dan tanggal",
            "Memiliki tampilan layar utama yaitu tabel yang mepresentasikan data siswa seperti nomor absen, nomor induk, nama siswa,enis kelamin, keterangan kehadir siswa",
            "Input user untuk kembali ke menu utama"
        ]
    },
    "mengatur_konfigurasi_aplikasi": [
        "File konfigurasi terdapat pada (module/config/config.conf).",
        "Fitur pada menu 1 dan 2 menggunakan file (config.conf) yang berisi konfigurasi aplikasi.",
        "Pada file tersebut terdapat 4 section yaitu [options], [class], [date], dan [information status symbol].",
        "Pada section [options] terdapat 3 variabel yaitu auth, key, dan information_succes.",
        "Auth yaitu untuk menentukan apakah aplikasi setiap user harus login terlebih dahulu.",
        "Jika tidak ingin login setiap kali program dijalankan, maka auth ubah menjadi 0.",
        "Key yaitu kata sandi yang digunakan untuk login dan sebagai key untuk algoritma encryption file untuk history absensi.",
        "Information_succes yaitu untuk menampilkan apakah data berhasil di simpan atau tidak setelah melakukan absensi.",
        "Pada section [class] terdapat 2 variabel yaitu teacher dan class.",
        "Teacher yaitu nama guru yang mengajar, class yaitu kelas yang di absen.",
        "Pada section [date] terdapat 3 variabel yaitu year, month, dan day.",
        "Ini di gunakan untuk menentukan tanggal absensi, dan melihat history absensi untuk menu 2.",
        "Year yaitu tahun absen, month yaitu bulan absen, day yaitu tanggal absen.",
        "Pada section [information status symbol] terdapat 4 variabel yaitu hadir, izin, sakit, dan alpha.",
        "Hadir yaitu simbol yang menunjukan keterangan siswa hadir.",
        "Izin yaitu simbol yang menunjukan siswa izin, sakit yaitu simbol yang menunjukan siswa sakit, dan alpha yaitu simbol yang menunjukan siswa alpha.",
        "Simbolnya dapat di ubah sesuai kebutuhan.",
        "Jika ingin mengetahui lebih lanjut tentang konfigurasi aplikasi dapat bertanya pada pembuat aplikasi."
    ]
}