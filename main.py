import module


if __name__ == "__main__":
    while True:
        try:
            module.banner(f"absensi siswa kelas {module.database['class']}")
            choice = module.menu(["absensi siswa", "pantau kehadiran", "petunjuk penggunaan aplikasi"], "keluar")
            
            if choice > 0 and choice < 4:
                module.clear()
            
            match choice:
                case 1:
                    module.absensi(module.database['siswa'])
                    continue
                case 2:
                    choice = module.monitor_student_attendance()
                    if choice == "0":
                        continue
                    break
                case 3:
                    module.help_using_the_aplication()
                    continue
                case 0:
                    module.loading_and_clear("Terima kasih (^-^)")
                    exit()
                case _:
                    module.loading_and_clear(error=True, message="Menu tidak tersedia!")
                    continue
        except ValueError:
            module.loading_and_clear(error=True, message="Input harus berupa angka!")
