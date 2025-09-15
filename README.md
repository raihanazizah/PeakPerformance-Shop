# PeakPerformance-Shop

https://raihana-nur41-peakshop.pbp.cs.ui.ac.id/

...

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Pertama banget aku buat folder baru dgn nama PeakPerfomace-Shop, lalu aku buat repository baru juga di github dengan nama yang sama. setelah itu aku buka terminal dari folder PeakPerformance-Shop atau bisa juga buka terminal trus jalanin [cd PeakPerformance-Shop]. Setelah itu aku jalanin [git init] lalu [git remote add (url repo github yang ku buat tadi)]. Setelah itu aku bikin virtual environment pakai [python3 -m venv env] trus aktifkan env nya pakai [source env/bin/activate]. Trus di vscode dalam folder PeakPerformance-Shop aku buat requirements.txt yang isinya sesuai dengan di tutor 0. Nah, terus jalanin di terminal => [pip install -r requirements.txt] Nanti dia install semua dependencies yang dibutuhkan. Selebihnya aku ikut tutor 0 dan tutor 1. Ga lupa commit ke github juga.
Untuk proyek django aku pertama isntall project dan app nya dengan setup virtual environment tadi, lalu aktifkan env nya juga, terus jalanin di terminal => [pip install django]. Nanti setelah install aku bikin project baru dgn cara => [django-admin startproject PeakPerformance_Shop .] dijalanin di terminal. Setelah itu aku bikin app main dgn cara jalanin ini di terminal => [python manage.py startapp main]. Setelah itu tambahin model Product di main/models.py dengan field seperti name, price, description, thumbnail, category, dan is_featured. Lalu daftarin app 'main' di settings.py Caranya buka settings.py, cari bagian INSTALLED_APPS, trus tambahin 'main'. Terus setelah 'edit' models.py itu harus make migrations dan migrate, caranya jalanin ini di terminal => [python manage.py migrate]. Lalu edit isi views.py dengan buat method show_main untuk menampilkan daftar produk yang ada di models.py tadi. Lalu routing dgn cara konfigurasi urls.py di project untuk include main/urls.py dan juga mapping URL ke views. Lalu buat folder bernama templates yang isinya home.html. Di home.html ini kita isi nama apps, nama kita, npm, dan kelas juga, initnya isi home.html ini nantinya akan muncul di halaman utama ketika runserver dijalanin. Jangan lupa git add, commit, dan push. Nah terus tinggal deploy ke PWS deh.
Buat deploy ke PWS itu login dulu pake sso, terus create new project dgn nama peakshop (ini soalnya gabisa pake kapital namanya, aku udh coba pake yang PeakPerformance-Shop gabisa), habis itu edit environsnya, dan sesuaikan sama isi file .env.prod yang ada data kita yang dikasih di email itu. Kalau udah yauda push deh ke pws, trus liat di builds itu pasti ada buildnya, inshaallah tulisannya building, trus nanti beberapa detik kemudian jadi succesfull, nah kalau udh gini langsung klik view project. TARAAA, udah jadii dehh karena halaman utamanya udah muncull. 

...
 
## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

foto bagannya ada di sini: https://drive.google.com/drive/folders/1R-NvBxykXzDVgTCbXBLNG2LXV400J4qX?usp=drive_link

penjelasannya: user sbg client kirim request ke server django melalui browser, terus dari urls.py itu si django cek url nya, lalu diarahkan ke view yang sesuai yg ada di views.py. views.py ini menjalankan logika appsnya, trus lanjut deh ke models.py di mana akses dan operasi pada database-nya diatur. lalu views.py menerima hasil dari model, yang kemudian diteruskan ke templates. nah di templates, lebih tepatnya di home.html itu dia format data jadi tampilan halaman webnya. Nah, halaman webnya dikirim lagi deh ke browser user yang menjadi response atas request si user.

...

## Jelaskan peran settings.py dalam proyek Django!

settings.py itu ibarat pusat pengaturan di Django. Di file ini kita menentukan konfigurasi penting seperti database yang dipakai, daftar aplikasi yang dijalankan, middleware, sampai lokasi file statis dan template. Kalau file ini nggak ada, Django bakal bingung harus nyambung ke database mana, aplikasi apa aja yang aktif, dan di mana nyari file HTML maupun aset pendukung lainnya.

...

## Bagaimana cara kerja migrasi database di Django?

Pertama, kita bikin atau ubah isi file models.py.
Setelah itu jalanin perintah [python manage.py makemigrations]. Nah, di tahap ini Django bakal nyiapin file migrasi, yaitu semacam catatan instruksi buat ngubah database.
Lanjut, kita jalankan [python manage.py migrate]. Perintah ini yang bener-bener nerapin instruksi tadi ke database. misalnya bikin tabel baru, nambah atau ngubah kolom, dan lain-lain.
Intinya, proses migrasi ini biar struktur database selalu sesuai sama kode yang kita tulis di models.py.

...

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django cocok dijadikan framework pertama karena sejak awal sudah dilengkapi fitur-fitur penting seperti autentikasi, admin panel, dan keamanan. Hal tersebut memudahkan kita sebagai pemula agar tidak perlu membangun semuanya dari nol. Dokumentasi yang jelas serta komunitas yang luas juga membuat proses belajar lebih terarah. Dengan konsep MVT yang terstruktur, alur pengembangan web menjadi lebih mudah dipahami sekaligus relevan dengan kebutuhan industri. Oleh karena itu, Django sering dipilih sebagai framework awal dalam mempelajari web development.

...

## Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Pada sesi tutorial 1 di minggu kedua, asisten dosen cukup responsif dan menjelaskan dengan baik, sehingga membantu ketika ada masalah saat pengerjaan. Namun, ketika menghadapi kendala di luar sesi tutorial, respon yang diberikan cenderung lebih lama. Secara keseluruhan, jalannya sesi sudah cukup baik meskipun masih ada beberapa kendala.

...
