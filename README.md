# HHMBTNI EVENT EDITOR
event editor buat hoax harvest moon back to nature
Hai nes,
share event editor  buat hoax hmbtn.

### 
![image](https://i.ibb.co/vVgvgSD/3827-0-EF3.png)


## Tool yang diperlukan:

- Python
untuk android bisa pakai pydroid / termux +python
- Emulator, PC optimal pakai epsxe, bisa juga pakai no$psx, atau DuckStation(gak bisa diedit pas game berjalan, tapi kualitas  graphicnya oke).
	
- ISO Base hoax harvest moon(Bahasa indo oleh Palapa)
	
## Cara install
1. Download  [Python](https://www.python.org/downloads/release/python-3120/), install. Jangan lupa Add Python xxx to PATH diceklis.
2. Download repo extract ke folder epsxe.
3. Download [HHMBTNI_BASE.7z](https://drive.google.com/file/d/1SAHUhEq-xh6JAjA7Be1CXHvSX-OoRvsb/view?usp=drive_link) extract ke folder epsxe/isos/HHMBTNI_BASE.iso.
4. Copy paste/rename COMMAND_BASE.xlsx jadi  COMMAND.xlsx,biar nanti tidak tertimpa jika ada update.
5. Buka cmd cd ke folder epsxe, ketik pip install -r pkg.txt untuk download module yang diperlukan.
6. Selesai, event editor siap digunakan!


## Konten
- HHMBTNI/
- ---------BGM/(list bgm yang ada dalam game,digunakan dalam command BGM)
- ---------DOOR/(index pintu yang diketahui,digunakan dalam command OPENDOOR)
- ---------EVENT_BASE/COMMAND_BASE.xlsx(
- ---------ITEM/(List Item yang bisa di display dalam game,digunakan dalam command MC-HANDLING-ITEM,SET-ITEM-POS)
- ---------LISTFACE/(List face npc, dan control code face npc, digunakan dalam edit text npc jika mau ganti wajah siapa yang ditampilkan)
- ---------MESSEGE/(All editable text harvest moon back to nature,berhubungan dengan command OPENTEXTBOX)
- ---------NPC/(List npc yang bisa di display dalam game+ custom npc(Claire,Dzak,Joy. Bisa Ditambah ntar :v))
- ---------SOUND-MV/(list bgm yang ada dalam game,digunakan dalam command SOUND-MV)

## MessegeX.txt
Berisi hampir semua  text npc dan item name+deskripsi(kecuali system).

Sample text Npc  messege1/index32 |
------------ |
[{0FCB}][{0FF7}][{0FF4}][{0FF5}][{ICON_ARROW}]Tidak, ini masalah pribadi...		|


Sample text Npc  messege1/index42 |
------------ |
[{0FBA}][{0FF7}][{0FF4}][{0FF5}][{ICON_ELLI_HEART}]Kau harusny ke Dokter jika merasa sakit....


[0032],[0042] = Index txt

[{0FCB}] = Ctrl code face Doug
[{0FBA}] = Ctrl code face Elli

lihat folder LISTFACE/, tidak saya kasih table menjadi [{FACE_XXXX}] karena nanti text susah dibaca, dan diedit,
kepanjangan juga,
males juga sih :v.
bisa diganti dengan face yang diperlukan.
Fix delay tampilin face npc.

[{ICON_ARROW}] = Tampilan icon panah di textbox kanan bawah

[{ICON_ELLI_HEART}] = Tampilan icon hati di textbox kanan bawah

## COMMAND_BASE.xlsx
Berisi beberapa Sheet:
1. SAMPLE COMMAND
Berisi command/fungsi yang berhasil diketahui.

2. INFO
Berisi list info, 
nama map(digunakan dalam command CHANGEMAP) ,
nama item(digunakan dalam command MC-HANDLING-ITEM,SET-ITEM-POS)
mc action(digunakan dalam command MC-ACTION)
floating icon(digunakan dalam command FLOATING-ICON)

3.EVENT01 s/d EVENT11

- Kolom A =  index, jangan diedit.
- Kolom B = Nama command/fungsi
- Kolom C = V0/Variable 0
- Kolom D = V1/Variable 1
- kolom E  = V2/Variable 2
- Kolom F = A0/Argument 0
- Kolom G= A1/Argument 1
- Kolom H = A1/Argument 2
- Kolom I = A3/Argument 3
- Kolom J = Insert option, isi J2 dengan YES/NO
- Kolom K =Target map yang dikasih trigger event(event tidak akan ter-trigger jika sama harinya dengan system event seperti festival).
- Kolom L = Nama npc yang akan dimasukan dalam event(jika sprite npc display error, masukan 2 kali npcnya pada baris yang selang seling).
- Kolom M = Nama Item yang akan dimasukan dalam event(jika sprite item display error, maka baris yang error isi dengan item lain, dan isi baris selanjutnya dengan item yang diperlukan).

## AXIS
Sebenarnya sih standar aja , cuma sumbu Z minus dan plusnya terbalik
![me](https://github.com/gil-unx/sos/blob/main/epsxe/HHMBTNI/AXIS.jpg)








