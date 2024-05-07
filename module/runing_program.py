from .database import database
from .display import clear, menu, banner, table_absensi, sleep, loading_and_clear
from .code import shift, format_status
from .files import create, read
from .date import date, now


def absensi(siswa):
    date_config = True
    if f"{date['year']}{date['month']}{date['day']}" != now.strftime("%Y%m%d"):
        banner("anda melakukan konfigurasi pada penanggalan di config.conf")
        date_config = False
    banner(f"{date['year']}/{date['month']}/{date['day']}", clear_screen=date_config)
    table_absensi(siswa)
    
    status_last = ""
    index = 0
    while index < len(siswa):
        banner("1/ENTER : HADIR\n2\t: IZIN\n3\t: SAKIT\n4\t: ALPHA\n0\t: PERBAIKI ABSEN TERAKHIR DIATUR\n$\t: UNTUK MENAMPILKAN TABEL ABSENSI\nexit\t: UNTUK KELUAR PAKSA APLIKASI",clear_screen=False)
        if status_last: print(f"{status_last}\n{'-'*84}")
        status = input(
            f"Keterangan untuk ({siswa[index]['name'].upper()}) >> "
        ).lower()

        if status == "0":
            status = input(f"Perbaikan untuk ({siswa[index-1]['name']}) >> ")
            status = format_status(status)
            siswa[index - 1]["status"] = status
            clear
            continue
        elif status == "exit":
            loading_and_clear("Terima kasih (^-^)")
            exit()
        elif status == "$":
            banner(f"{date['year']}/{date['month']}/{date['day']}")
            table_absensi(siswa)
            continue

        status = format_status(status)
        status_last = f"({siswa[index]['name'].upper()}) : {status.upper()}"
        siswa[index]["status"] = status
        index += 1
        clear()

    banner(f"{date['year']}/{date['month']}/{date['day']}")
    table_absensi(siswa)
    
    sleep(5)
    clear()
    
    data_siswa = f"{date['year']},{date['month']},{date['day']}|"
    for i,data in enumerate(siswa, 1):
        data_siswa += f"{data['status']}{',' if i < len(siswa) else ''}"
    
    data = shift(data_siswa, database["key"], to="right")
    create(data, date)


def monitor_student_attendance():
    data_date, data = read(date)
    title = f"{data_date[0]}/{data_date[1]}/{data_date[2]}"
    if not data:
        banner(title)
        loading_and_clear(error=True, message="Data tidak ditemukan!", s=3)
        return "0"
    else:
        banner(title)
        banner("tentukan tahun/bulan/tanggal jika ingin melihat history absensi", clear_screen=False)
        table_absensi(data)
        return input("0: BACK >> ")


def help_using_the_aplication():
    def print_list_teks(list_teks):
        for i, menu in enumerate(list_teks, 1):
            print(f"{i}.) {menu}")
        print("-"*84)
        return input("Untuk mempermudah bisa langsung menekan enter untuk kembali >> ")
    
    def choose(menu_name, num_menu):
        while True:
            try:
                banner(database["library"]["menu"][num_menu])
                choice = menu(["fitur", "desain"], "kembali")
                match choice:
                    case 1:
                        banner(f"fitur pada {menu_name}")
                        print_list_teks(database["library"][menu_name]["feature"])
                    case 2:
                        banner(f"desain pada {menu_name}")
                        print_list_teks(database["library"][menu_name]["design"])
                    case 0:
                        break
                    case _:
                        loading_and_clear(error=True, message="Menu tidak tersedia!")
            except ValueError:
                loading_and_clear(error=True, message="Input harus berupa angka!")
    
    while True:
        banner("petunjuk penggunaan aplikasi")
        try:
            choice = menu(database["library"]["menu"], "kembali")
            match choice:
                case 1:
                    choose("menu_1", choice-1)
                case 2:
                    choose("menu_2", choice-1)
                case 3:
                    banner(database["library"]["menu"][choice-1])
                    print_list_teks(database["library"]["mengatur_konfigurasi_aplikasi"])
                case 0:
                    break
                case _:
                    loading_and_clear(error=True, message="Menu tidak tersedia!")
        except ValueError:
            loading_and_clear(error=True, message="Input harus berupa angka!")