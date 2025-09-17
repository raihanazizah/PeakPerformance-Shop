# PeakPerformance-Shop

https://raihana-nur41-peakshop.pbp.cs.ui.ac.id/

upd: https://raihana-nur41-peakshop.pbp.cs.ui.ac.id/

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
# Tugas 3

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery itu cara untuk mengirim data antar bagian sistem, misalnya dari tampilan (frontend) ke server (backend), atau antar service. Tanpa ini, tiap bagian bakal jalan sendiri-sendiri dan nggak bisa ngobrol / connect gitu. Bayangin aja kayak kurir paket: kalau ada yang beli barang di toko online (klik Add to Cart), kurir bakal nganterin pesan itu ke gudang (server). Gudang lalu balikin konfirmasi kalau barang udah masuk keranjang. Nah, proses nganterin “pesan” inilah yang disebut data delivery.

Kenapa penting? Pertama, biar tiap bagian sistem bisa kerja terpisah tapi tetap nyambung. Kedua, bikin aplikasi bisa dipakai di banyak device (web, mobile, IoT) dengan format data umum kayak JSON atau XML. Dari sisi performa, kita bisa pilih jalur yang sesuai: HTTP buat request biasa, message queue atau streaming kalau trafik lagi rame biar sistem nggak tumbang. Ada juga mekanisme antrean (kayak Kafka atau RabbitMQ) supaya data aman walaupun server lagi error. Buat keamanan, data delivery biasanya lewat API gateway supaya akses bisa diatur, ada autentikasi, bahkan bisa dibatesin request-nya. Terus kalau ada update, API bisa di-versioning biar aplikasi lama tetap jalan. Bonusnya, UX juga jadi lebih oke, misalnya lewat WebSocket buat live update atau sync offline kalau koneksi jelek.

Jadi intinya, data delivery itu kayak jalur komunikasi antar bagian aplikasi. Tanpa ini, sistem bakal berantakan. Makanya sebelum bikin, perlu ditentuin dulu: format apa yang dipakai, jalurnya lewat apa (REST, GraphQL, MQ), gimana cara handle error, dan jangan lupa lapisan keamanan biar data tetap aman.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurutku, JSON jauh lebih baik dibanding XML untuk kebanyakan kebutuhan sekarang, terutama di web dan API. JSON tampilannya lebih simpel, ringkas, dan gampang dibaca manusia—nggak kebanyakan tag buka-tutup kayak XML. Selain itu, JSON udah “nyatu” sama JavaScript, jadi gampang banget dipakai di frontend. Parsing JSON juga lebih cepat dan ringan di banyak bahasa pemrograman, makanya hampir semua framework atau library modern (misalnya fetch, axios, atau SDK mobile) langsung support JSON. JSON cocok buat API web/mobile masa kini karena simpel dan efisien, sedangkan XML lebih kepake di sistem lama atau kalau datanya butuh struktur dokumen yang kompleks.

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Di Django, is_valid() itu fungsinya buat ngecek apakah data yang dikirim lewat form udah bener atau belum. Jadi kalau user isi form, Django bakal ngecek: ada datanya nggak, formatnya sesuai nggak (misalnya angka beneran angka, panjang teks nggak kelewat, field wajib diisi nggak kosong), terus kalau kita bikin validasi tambahan di clean_<field>() atau clean(), itu juga dijalankan.
Kalau semua oke, is_valid() bakal balikin True dan data bersihnya bisa diakses lewat form.cleaned_data. Tapi kalau ada yang salah, dia balikin False dan error-nya bisa ditampilkan ke user lewat form.errors.

Kenapa penting? Karena ini yang bikin data kotor atau salah nggak langsung nyelonong masuk ke database, jadi aman dari error atau data aneh. Selain itu, user juga langsung dapet feedback yang jelas tentang apa yang salah di form mereka. Jadi, is_valid() itu semacam filter utama biar data yang masuk ke sistem kita selalu rapi dan sesuai aturan.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Di Django, kita butuh csrf_token buat ngejaga form biar aman dari serangan CSRF (Cross-Site Request Forgery). CSRF itu serangan di mana orang jahat bikin browser kita ngirim request ke website lain tanpa kita sadari. Karena browser otomatis ngirim cookie login kita, server bakal ngira request itu sah, padahal sebenernya disuruh sama penyerang.

Contohnya gini: kita lagi login di situs bank, terus buka website abal-abal yang diam-diam punya form tersembunyi buat transfer uang. Kalau situs bank nggak pakai csrf_token, form itu bisa langsung ke-submit ke bank pake cookie login kita, dan duitnya nyangkut ke rekening penyerang.

Nah, Django ngatasin ini dengan csrf_token. Token ini unik dan ditaruh di setiap form. Pas form dikirim balik ke server, Django ngecek apakah tokennya cocok. Kalau nggak cocok, request ditolak. Jadi, tanpa csrf_token, form kita gampang banget dipakai penyerang buat nyuruh server ngelakuin hal-hal yang nggak pernah kita setujuin.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama aku bikin dulu itu 4 functions di views.py (def itu) untuk show xml dan json, dan juga show xml by id dan show json by id. terus baru tambahin functions itu di urls.py, ditambahinnya tuh di yg import nya yg di atas. trus update home.html biar ada add product dan detail product, nah ini isinya dari kita bikin file html baru yg namanya create_product dan product_detail. jadi nanti di halaman utamanya muncul ada bisa kita add product dan habis itu product yg udh ada bisa di liat detailnya. setelah itu buat forms.py untuk nambahin object product dan fields nya yaitu si 6 atribut itu (nama, harga, dll). setelah itu aku update models.py biar lebih sesuai aja sama toko yg aku buat. setelah itu di migrate. lalu push ke github dan pws. oh iya, cek dengan runserver juga setiap habis buat functions yang di views.py untuk melihat id / pk dari produknya.

##  Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Udah lumayan responsif kok, cukup membantu, dan tutor 2 kmarin '"lebih mudah" dari tutor sebelumnya.

## screenshot postman
<img width="1440" height="900" alt="Screenshot 2025-09-17 at 10 20 09" src="https://github.com/user-attachments/assets/185a20cd-bf3f-40cb-aae7-ba0524228212" />
<img width="1440" height="900" alt="Screenshot 2025-09-17 at 10 20 48" src="https://github.com/user-attachments/assets/daa9622f-c1aa-409f-8df6-7c18049b426c" />
<img width="1440" height="900" alt="Screenshot 2025-09-17 at 10 21 16" src="https://github.com/user-attachments/assets/bb3569bc-6403-4d8f-baa9-8c5c47ef9dcf" />
<img width="1440" height="900" alt="Screenshot 2025-09-17 at 10 21 26" src="https://github.com/user-attachments/assets/4dde8a84-a7cd-4c57-8f49-896cfa8bdc5b" />




