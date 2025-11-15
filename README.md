# PeakPerformance-Shop

https://raihana-nur41-peakshop.pbp.cs.ui.ac.id/

upd: https://raihana-nur41-peakshop.pbp.cs.ui.ac.id/

...
<<<<<<< HEAD
=======
# Tugas 2
>>>>>>> master

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
<<<<<<< HEAD
=======

>>>>>>> master
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

# Tugas 4

## Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
AuthenticationForm itu form bawaan Django untuk proses login. Form ini memvalidasi username dan password yang dimasukkan user dengan data yang tersimpan di database (model User).
Biasanya dipakai di views.LoginView atau form login kustom kayak views.py yang dibuat sekarang.
Kelebihan AuthenticationForm adalah sudah terhubung langsung dengan sistem autentikasi bawaan Django, sehingga pengembang tidak perlu membuat logika validasi sendiri. Pengecekan seperti kecocokan password, status akun yang masih aktif, dan apakah akun tidak dinonaktifkan sudah ditangani secara otomatis. Form ini juga fleksibel untuk disesuaikan, baik dengan menambahkan field baru maupun dengan mempercantik tampilannya. Namun, kekurangannya terletak pada keterbatasan: form ini hanya ditujukan untuk proses login dengan model User default. Jika dibutuhkan mekanisme login yang lebih khusus, misalnya menggunakan nomor ponsel atau kode OTP, pengembang harus melakukan penyesuaian besar. Selain itu, tampilan standar form ini sangat sederhana sehingga perlu diubah di template, dan kegunaannya memang hanya untuk login, bukan untuk registrasi atau penggantian password.

## Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi dan otorisasi itu punya makna yang berbeda. Autentikasi adalah langkah untuk memastikan identitas pengguna, yaitu mengecek apakah orang yang login benar-benar pemilik akun, contohnya dengan memeriksa username dan password. Otorisasi adalah langkah setelahnya, yaitu menentukan apa saja yang boleh atau tidak boleh dilakukan oleh pengguna yang sudah terbukti identitasnya, misalnya hanya admin yang diizinkan menghapus data. Di Django, autentikasi ditangani lewat modul django.contrib.auth dengan fungsi seperti authenticate() dan login(), dibantu backend seperti ModelBackend. Sementara itu, otorisasi dikelola lewat sistem permission dan group bawaan, misalnya menggunakan decorator @login_required, method user.has_perm(), atau dengan mengecek atribut seperti user.is_staff dan user.is_superuser.

## Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Dalam aplikasi web, cara menyimpan “state” bisa dilakukan dengan session atau cookies, dan keduanya bekerja dengan cara berbeda. Session menaruh data utama di sisi server, sedangkan di browser hanya disimpan ID sebagai penanda. Karena data asli tetap berada di server, informasi sensitif lebih terlindungi, meski konsekuensinya server perlu menyediakan tempat penyimpanan (misalnya di database atau cache) sehingga bebannya bertambah. Cookies, sebaliknya, menyimpan data langsung di browser pengguna, jadi tidak memerlukan ruang tambahan di server dan cocok untuk informasi yang ringan. Tapi karena datanya berada di sisi klien, cookies lebih mudah diintip atau dimodifikasi oleh pihak yang tidak berwenang jika tidak diamankan dengan baik.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Pakai cookies itu nggak otomatis aman. Data di dalamnya bisa dicuri lewat serangan XSS (Cross-Site Scripting) atau disadap saat dikirim kalau websitenya nggak pakai HTTPS. Untuk mencegah hal ini, Django sudah menyiapkan beberapa lapisan pengaman. Secara bawaan, Django mengaktifkan opsi HttpOnly, jadi cookie nggak bisa dibaca lewat JavaScript. Ada juga pilihan Secure flag supaya cookie cuma dikirim kalau koneksi pakai HTTPS. Selain itu, Django menambahkan CSRF token di setiap form POST untuk melindungi dari serangan Cross-Site Request Forgery. Django juga bisa membuat signed cookies dengan modul django.core.signing, yang berarti isi cookie akan ditandatangani; kalau ada orang yang coba mengubah isinya tanpa tanda tangan yang benar, Django bisa tahu. Meskipun sudah ada perlindungan bawaan ini, developer tetap dianjurkan mengaktifkan pengaturan keamanan tambahan di settings.py seperti CSRF_COOKIE_SECURE = True atau SESSION_COOKIE_SECURE = True supaya cookies lebih aman lagi.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama aku aktifin env, eh virtual environment itu. Terus aku buat fungsi registrasi di views.py yang ada di main. Lalu aku buat file baru namanya register.html di templates dalam subdirektory main. Setelah itu aku impor fungsi dan nambahin path url untuk si register ini di urls.py yang ada di main. Nah terus aku ulang lagi semua step itu buat bikin fungsi login dan logut. Jadi nanti ada file baru jg di templates dalam main itu namanya login.html dan logout.html. Setelah itu aku restriksi akses ke halaman main dan product detail nya. Aku tambahin import login required ke views.py di main terus tambahin ini [@login_required(login_url='/login')] di atas fungsi home dan show_product yang ada di dalam views.py tadi. Habis itu jalanin [python manage.py runserver]. Terus buka deh http://localhost:8000/ di web browser buat lihat tampilan baru dari halaman utamanya. Habis itu aku coba buat 2 akun dummy (bikinnya pakai yg register itulo) yang tiap akunnya tuh bikin 3 produk. Setelah itu aku logout. Habis itu aku import HttpResponseRedirect, reverse, dan datetime. Terus aku ganti bagian kode di fungsi login_user buat menyimpan cookie baru bernama last_login yang berisi timestamp terakhir kali pengguna melakukan login. Habis itu aku tambahin potongan kode 'last_login': request.COOKIES['last_login'] ke dalam variabel context yang ada di fungsi home dalam vies.py di dalam main. Lalu aku ganti juga fungsi logout_user buat menghapus cookie last_login setelah melakukan logout. Trus aku tambahin kode kayak buat kasih info sesi terakhir loginnya kapan di home.html yang ada di templates yang ada di main. Terus buat hubungin product sama user, aku tambahin import user ke dalam models.py yang ada di main. Lalu tambahin kode ini [user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)] ke dalam class Product yang ada di models.py tadi. Nah karena udh edit2 models.py, jadi aku migrasi model pakai python manage.py makemigrations. Terus jalanin migrasi model dengan python manage.py migrate. Habis itu edit2 fungsi create_product yg ada di views.py yg ada di main biar dia bisa ada product entry dan product user. Disini nih jd beneran terhubung antara product dan usernya. Edit juga fungsi home biar ada filter_type untuk product_list nya. Setelah itu tambahin tombol filter My Products dan All Products di home.html. Terus tampilin nama author di product_details.html nya.
Nah aku balik lg ke halaman web yang tadi tuh yg udh aku logout. Terus disitu aku login lagi pake akun dummy nya, nah buat lagi 3 produk untuk tiap akun dummy deh. Terus di cek lagi pak klik my products ada atau engga produk yg udh di add tadii. Selesai dehh.

# Tugas 5

## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas pengambilan CSS Selector itu sebutannya Specificity. Jadi di dalam CSS, urutan prioritas aturan ditentukan oleh tingkat spesifisitasnya. Tingkat pertama dengan prioritas tertinggi adalah inline style yang ditulis langsung pada atribut style elemen. Tingkat kedua adalah selector berbasis ID, karena ID dianggap unik dalam dokumen. Tingkat ketiga ditempati oleh selector berbasis class, attribute selector, serta pseudo-class seperti :hover atau :nth-child. Tingkat keempat dengan prioritas paling rendah adalah selector berbasis elemen/tag (misalnya p, div, h1) dan pseudo-element seperti ::before atau ::after. Jika ada beberapa aturan dengan tingkat yang sama, maka yang digunakan adalah aturan yang ditulis paling akhir dalam kode CSS. Selain itu, aturan yang diberi tanda !important akan mengalahkan semua aturan lain di semua tingkat, kecuali ada aturan lain yang juga menggunakan !important, maka kembali diputuskan berdasarkan spesifisitas dan urutan penulisan.

## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design merupakan konsep penting dalam pengembangan aplikasi web karena pengguna kini mengakses internet melalui berbagai perangkat dengan ukuran layar yang berbeda, mulai dari komputer, tablet, hingga ponsel. Dengan menerapkan responsive design, tampilan web dapat menyesuaikan diri secara otomatis terhadap ukuran layar yang digunakan, sehingga pengalaman pengguna tetap nyaman dan konsisten. Tanpa desain yang responsif, pengguna perangkat dengan layar kecil akan kesulitan membaca teks, menekan tombol, atau harus sering melakukan perbesaran dan pengguliran, yang pada akhirnya dapat menurunkan minat mereka untuk menggunakan aplikasi tersebut.
Sebagai contoh, Pinterest telah mengadopsi responsive design dengan baik. Pada tampilan desktop, pengguna dapat melihat banyak pin(image) tersusun dalam grid dengan beberapa kolom, sementara pada tampilan ponsel, jumlah kolom otomatis berkurang dan tata letak disusun lebih sederhana agar sesuai dengan ukuran layar. Hal ini memastikan Pinterest tetap nyaman digunakan di berbagai perangkat. Sebaliknya, beberapa situs lama, seperti portal pemerintah atau media berita jadul, masih belum menerapkan desain responsif. Ketika dibuka melalui ponsel, teks terlihat kecil, tata letak melebar ke samping, dan pengguna harus melakukan pengguliran horizontal atau zoom manual, yang tentu menyulitkan.
Dengan demikian, penerapan responsive design menjadi krusial karena berhubungan langsung dengan aspek kenyamanan, keterjangkauan, dan keberlangsungan penggunaan aplikasi web.

## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin itu ruang di luar elemen, yaitu jarak antara elemen dengan elemen lain di sekitarnya. Bisa dianggap sebagai “ruang bebas” yang bikin elemen nggak terlalu nempel dengan elemen lain.
Implementasi margin di CSS:
.box {
  margin-top: 15px;
  margin-right: 20px;
  margin-bottom: 20px;
  margin-left: 20px;
}

Border itu garis tepi elemen yang berada di antara margin dan padding. Border biasanya dipakai buat kasih bingkai visual di sekitar elemen.
Implementasi broder di CSS:
.box {
  border-top: 3px dashed red;   /* garis atas merah putus-putus */
  border-bottom: 5px dotted blue; /* garis bawah biru titik-titik */
  border: 2px solid black; /* garis tepi hitam tebal 2px */
}

Padding itu ruang di dalam elemen, yaitu jarak antara konten (misalnya teks atau gambar) dengan border elemen. Jadi padding ngatur “nafas” di dalam kotak agar isinya nggak terlalu nempel sama tepi.
Implementasi padding di CSS:
.box {
  padding-top: 10px; /* jarak konten ke border 10px di sisi atas*/
  padding-right: 20px;
  padding-bottom: 15px;
  padding-left: 25px;
}

Gambaran box model untuk implementasi ketiganya:
[ MARGIN ]
  [ BORDER ]
    [ PADDING ]
      [ CONTENT ]

di mana Content itu isi kotaknya (teks, gambar, dll.). Padding itu jarak isi dengan tepi kotak. Border itu garis tepi kotak. Margin itu jarak antar kotak (elemen lain).

Implementasi ketiganya di CSS:
<!DOCTYPE html>
<html>
<head>
  <style>
    .box {
      margin: 20px;              /* jarak antar elemen */
      border: 3px solid blue;    /* bingkai biru */
      padding: 15px;             /* jarak isi ke bingkai */
      background-color: lightgray;
    }
  </style>
</head>
<body>
  <div class="box">
    Ini contoh box dengan margin, border, dan padding.
  </div>
</body>
</html>
Hasilnya => kotak abu-abu dengan teks di dalamnya, ada ruang di dalam (padding), dibatasi garis biru (border), dan ada jarak dengan elemen lain di luar (margin).


##  Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox atau Flexible Box Layout adalah sistem layout satu dimensi di CSS yang berfungsi untuk mengatur elemen dalam satu arah, baik secara horizontal (baris) maupun vertikal (kolom). Flexbox memudahkan pengembang dalam menyusun elemen agar sejajar, menyesuaikan ukuran secara fleksibel, dan menjaga tata letak tetap rapi meskipun ukuran layar berubah. Karena sifatnya satu dimensi, Flexbox sangat cocok digunakan untuk komponen kecil seperti navigasi, tombol yang disusun sejajar, atau card dalam satu baris. Flexbox = fokus 1 dimensi (hanya baris atau kolom saja).

CSS Grid Layout adalah sistem layout dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom secara bersamaan. Grid memberikan kontrol penuh untuk membuat struktur halaman yang kompleks dan terorganisir, misalnya membangun layout dengan header, sidebar, konten utama, dan footer. Grid sangat efektif untuk membuat desain berbasis grid seperti galeri, dashboard, atau layout majalah online. Grid = fokus 2 dimensi (baris dan kolom).

Secara sederhana, perbedaan utama keduanya adalah Flexbox lebih cocok untuk tata letak dalam satu arah, sedangkan Grid lebih tepat digunakan untuk kerangka besar yang melibatkan baris dan kolom sekaligus. Nah, biasanya pengembang web pakai Grid buat bikin kerangka halaman utama, terus di dalam kotak-kotak Grid itu pakai Flexbox lagi buat ngerapiin isi kecilnya.

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Buat awalnya pilih dulu gitu mau pake framework apa, karena lebih pengen customization yg ga ribet, aku pilihnya tailwind. terus baru deh script CDN dari tailwind ke aplikasi lewat kode yang di base.html kayak gini [
<script src="https://cdn.tailwindcss.com">
]. Setelah itu, buat bikin fitur edit dan delete itu sama kayak bikin fitur sebelum-sebelumnya. Caranya itu bikin function baru di views.py yang namanya edit_product dan delete_product. Setelah buat itu, bikin juga edit_product.html. di templates yang ada di main. Lalu tambahin deh / import edit_product dan delete_product ke urls.py, terus tambahin path nya juga buat mereka. Nah, edit juga product_list yang looping itu di home.html buat munculin tombol Edit dan Delete. 
Sekarang mau buat navigation bar, bikin navbar.html di templates yang ada di root directory. Configure juga static files pada aplikasinya di settings.py bagian middleware, tambahkan white noise middleware. Configure juga STATIC_ROOT, STATICFILES_DIRS, dan STATIC_URL di settings.py tadi.
Nah, buat stylingnya, aku mau buat temanya kayak sporty tapi coquette gitulo, jadi pink tapi masih sporty. Pertama bikin dulu folder static di root directory, trus di dalem folder static dibuat folder css yang isinya global.css. Trus buat hubungin global.css sama framework tailwind yang aku pakai, edit base.html biar ada cdn tailwind nya. Nah, abis itu baru deh tambahin custom styling ke global.css. Trus aku juga customize navbar.html, login.html, register.html, card_product.html, detail_product.html, create_product.html, dan edit.product.html.

# Tugas 6

## Apa perbedaan antara synchronous request dan asynchronous request?
Synchronous request => Browser akan mengirim permintaan ke server dan berhenti total sambil menunggu respons. Pengguna tidak bisa melakukan apa-apa (tidak bisa mengklik tombol, mengisi formulir, atau bahkan men-scroll halaman) sampai server selesai memproses dan mengirimkan kembali data. Hal ini bisa dibayangkan seolah antrean di kasir: orang yang sedang antre tidak bisa dilayani sampai orang di depannya selesai bertransaksi.

Alur kerja synchronous request:
1. Pengguna melakukan aksi (misalnya, mengklik link).
2. Browser mengirim request ke server.
3. Browser "membeku" dan menunggu.
4. Server memproses request dan mengirimkan halaman HTML baru.
5. Browser memuat ulang seluruh halaman untuk menampilkan konten baru.

Asynchronous request => Model request ini jauh lebih fleksibel. Ketika browser mengirim permintaan ke server, ia tidak perlu menunggu. Pengguna bisa terus berinteraksi dengan halaman (men-scroll page, mengklik, atau mengetik) sementara permintaan tersebut diproses di latar belakang. Saat server mengirimkan respons, hanya bagian tertentu dari halaman yang akan diperbarui, tanpa perlu memuat ulang seluruhnya. Ini seperti memesan makanan di restoran dengan buzzer: pelanggan bisa duduk santai sambil menunggu buzzer berbunyi, alih-alih berdiri di depan konter.

Alur kerja asynchronous request:
1. Pengguna melakukan aksi.
2. Sebuah fungsi JavaScript di browser mengirim request ke server di latar belakang.
3. Pengguna tetap bisa menggunakan halaman web seperti biasa.
4. Server memproses dan mengirimkan kembali data (biasanya dalam format JSON, XML, atau HTML).
5. JavaScript menerima data tersebut dan memperbarui hanya elemen yang relevan di halaman (misalnya, sebuah div, tabel, atau teks).


## Bagaimana AJAX bekerja di Django (alur request–response)?
AJAX bukan bahasa pemrograman atau framework, melainkan teknik yang menggabungkan JavaScript, objek XMLHttpRequest, atau Fetch API modern untuk memungkinkan komunikasi asinkron antara klien dan server.
Berikut alur kerjanya dalam konteks Django:

1. Sisi Klien (Client-Side / Browser)
  - Pemicu: Aksi pengguna seperti klik tombol, isi form secara real-time, atau pilih opsi dropdown akan memanggil fungsi JavaScript.

  - Pengiriman request: Fungsi JavaScript membuat objek XMLHttpRequest atau menggunakan fetch() untuk mengirim data ke URL Django tertentu, baik dengan metode GET maupun POST.

2. Sisi Server (Server-Side / Django)
  - Penerimaan request: Django menerima permintaan tersebut melalui sistem routing (urls.py). Biasanya URL untuk AJAX dibuat khusus agar terpisah dari request yang merender halaman penuh.

  - Pemrosesan di view: View yang sesuai akan dijalankan—bisa mengambil data dari database, memvalidasi form, atau menjalankan logika bisnis.

  - Menyusun respons: Alih-alih merender template HTML, view akan mengirim data dalam format ringan seperti JSON menggunakan JsonResponse.

3. Kembali ke Sisi Klien
  - Penerimaan respons: JavaScript yang mengirim request akan menerima data dari server.

  - Pembaruan DOM: Data tersebut digunakan untuk memperbarui tampilan halaman secara dinamis—misalnya menambahkan komentar baru, memperbarui jumlah “like”, atau menampilkan pesan sukses—tanpa perlu me-refresh halaman.


## Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
Penerapan AJAX (Asynchronous JavaScript and XML) memberikan berbagai keunggulan dibandingkan metode konvensional yang mengharuskan pemuatan ulang (reload) seluruh halaman setiap kali terjadi perubahan data. Berikut beberapa di antaranya:

1. Peningkatan Kecepatan dan Responsivitas
  AJAX memungkinkan pertukaran data dalam jumlah kecil antara klien dan server karena hanya bagian tertentu dari halaman yang diperbarui. Dengan demikian, waktu pemrosesan menjadi lebih singkat dan tampilan aplikasi terasa lebih responsif. Pengguna tidak lagi harus menunggu halaman dimuat ulang secara penuh, sehingga proses interaksi berlangsung lebih cepat dan efisien.

2. Peningkatan Pengalaman Pengguna (User Experience / UX)
  Interaksi yang dihasilkan oleh AJAX bersifat lebih halus dan tidak terputus. Pengguna dapat merasakan pengalaman yang lebih interaktif melalui fitur-fitur seperti:
  - Infinite scroll, yang memungkinkan konten baru muncul secara otomatis tanpa memuat ulang halaman (misalnya seperti pada Instagram).
  - Validasi formulir secara real-time, misalnya ketika sistem menampilkan peringatan “username sudah digunakan” tanpa perlu mengirim formulir terlebih dahulu.
  - Pembaruan notifikasi otomatis, di mana data baru muncul tanpa memerlukan penyegaran halaman.
  Kombinasi fitur-fitur ini berkontribusi pada peningkatan kepuasan dan kenyamanan pengguna.

3. Pengurangan Beban pada Server
  Dalam pendekatan tradisional, setiap perubahan kecil pada data memerlukan pengiriman ulang seluruh halaman HTML dari server. Dengan AJAX, server hanya mengirimkan data mentah (biasanya dalam format JSON), bukan keseluruhan template halaman. Hal ini secara signifikan mengurangi beban kerja server, karena proses rendering halaman penuh tidak lagi diperlukan.

4. Efisiensi Penggunaan Bandwidth
  Ukuran data yang ditransfer melalui AJAX relatif kecil, sehingga konsumsi bandwidth menjadi lebih hemat. Efisiensi ini sangat bermanfaat bagi pengguna dengan koneksi internet terbatas atau kecepatan jaringan yang rendah, karena proses pertukaran data tetap dapat berlangsung dengan lancar tanpa mengorbankan performa aplikasi.


## Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
Meskipun AJAX memberikan banyak kemudahan dalam pengembangan aplikasi web interaktif, penerapannya juga dapat menimbulkan risiko keamanan apabila tidak dikonfigurasi dengan benar. Oleh karena itu, diperlukan langkah-langkah khusus untuk memastikan keamanan data dan mencegah potensi serangan, terutama pada fitur-fitur sensitif seperti login dan registrasi.

1. Gunakan CSRF Token
  Framework Django menyediakan perlindungan bawaan terhadap serangan Cross-Site Request Forgery (CSRF). Saat mengirimkan permintaan AJAX menggunakan metode POST, pastikan token CSRF disertakan di dalam header atau body permintaan. Tanpa token ini, Django secara otomatis akan menolak request tersebut untuk mencegah manipulasi data oleh pihak tidak berwenang.

2. Selalu Gunakan HTTPS
  Seluruh komunikasi antara klien dan server sebaiknya dienkripsi menggunakan protokol HTTPS (SSL/TLS). Dengan demikian, data sensitif seperti kata sandi atau informasi pribadi tidak dapat disadap (eavesdropped) oleh pihak ketiga selama proses transmisi.

3. Lakukan Validasi di Sisi Server
  Data yang dikirim dari sisi klien tidak boleh sepenuhnya dipercaya. Walaupun sudah dilakukan validasi melalui JavaScript di browser, proses validasi ulang tetap wajib dilakukan di view Django. Hal ini penting karena penyerang dapat memanipulasi request AJAX secara langsung tanpa melalui antarmuka web yang sah.

4. Gunakan Metode POST untuk Data Sensitif
  Apabila data yang dikirim bersifat rahasia—seperti password atau informasi pribadi—gunakan metode HTTP POST, bukan GET. Hal ini dikarenakan data dalam permintaan GET akan tercatat di URL, log server, dan riwayat browser, yang berpotensi membocorkan informasi pengguna.

5. Terapkan Pembatasan Akses (Rate Limiting)
  Untuk mencegah serangan brute-force pada formulir login, batasi jumlah percobaan login dari satu alamat IP dalam jangka waktu tertentu. Django menyediakan paket seperti django-ratelimit yang dapat digunakan untuk menerapkan kebijakan pembatasan ini secara efektif.

6. Hindari Mengirimkan Password dalam Respons
  Setelah proses login atau registrasi berhasil, jangan pernah mengirimkan kembali password pengguna di dalam respons AJAX, baik dalam bentuk teks biasa maupun terenkripsi. Server cukup memberikan respons berupa pesan keberhasilan atau token sesi untuk autentikasi lanjutan.


## Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
Penerapan AJAX (Asynchronous JavaScript and XML) memberikan pengaruh yang sangat besar dan positif terhadap pengalaman pengguna (user experience). Teknologi ini mengubah pola interaksi pengguna dengan web dari yang semula bersifat statis menjadi lebih dinamis, interaktif, dan responsif.

1. Interaksi yang Lebih Halus dan Tanpa Gangguan
  Dengan AJAX, pengguna dapat melakukan berbagai aktivitas tanpa perlu memuat ulang halaman. Misalnya, ketika pengguna menambahkan produk ke keranjang belanja, ikon keranjang dapat diperbarui secara otomatis tanpa meninggalkan halaman produk. Hal ini menciptakan alur interaksi yang lebih lancar dan efisien.

2. Pemberian Umpan Balik Secara Langsung (Real-Time Feedback)
  AJAX memungkinkan aplikasi memberikan tanggapan secara instan terhadap tindakan pengguna. Contohnya, saat pengguna mengisi formulir pendaftaran, sistem dapat langsung menampilkan pesan bahwa “username sudah digunakan” atau bahwa “password terlalu lemah,” bahkan sebelum tombol Submit ditekan. Respons cepat seperti ini membantu pengguna memperbaiki kesalahan dengan segera.

3. Meningkatkan Rasa Kontrol dan Kepuasan Pengguna
  Aplikasi yang cepat dan responsif memberikan kesan bahwa pengguna memiliki kendali penuh atas interaksi yang dilakukan. Hal ini secara psikologis menurunkan tingkat frustrasi dan meningkatkan rasa puas terhadap kinerja situs atau aplikasi.

4. Mendekatkan Pengalaman Web dengan Aplikasi Desktop
  AJAX juga menjadi komponen utama dalam pengembangan Single Page Application (SPA) seperti Gmail, Google Maps, dan Facebook, yang mampu beroperasi layaknya aplikasi desktop. Dengan hampir tidak adanya proses reload halaman penuh, seluruh interaksi dapat terjadi secara cepat di satu halaman yang sama, menciptakan pengalaman yang lebih intuitif dan menyenangkan.

Secara keseluruhan, AJAX berperan sebagai jembatan penting yang menjadikan aplikasi web berbasis Django lebih modern, cepat, dan user-friendly. Teknologi ini tidak hanya meningkatkan efisiensi sistem, tetapi juga memberikan pengalaman interaksi yang lebih natural bagi pengguna.


