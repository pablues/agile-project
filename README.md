# agile-project

Aslı Tuğçe Melisa Bengisu

Agile Developmentı takip edebileceğimiz bir uygulama

Django üzerinden gerçekleştirilecek, Postgresql bağlanacak 
Kullanıcılar login olabilir 
Proje oluşturabilirler

Projenin içinde Sprints oluşturabilirler.

Her Sprint'in içinde User Story ve Task ekleyebilirler.

Tasklar için durumlar:

To Do

In Progress

Done

Tasklara atanan kişiler olabilir.

Burndown Chart ekleyebilirsin. 

Melisa Backend -> 2-django ile projeyi başlattı 3-userlar için ilk appi ekledi 6-modeller için gereken kodu oluşturdu

Bengisu Veri Tabanı -> 1- projeyi başlatıp sizi ekledim 4-dbyi postresqle çevirdim 5- İlk modelleri oluşturdum

Aslı ve Tuğçe Frontend -> 6- proje için bir base.html oluşturuldu 7-tuğçe base.htmle ekstra özellikler ekledi 8-modelleri htmlde kullılabilir hale getirdi

Task

Bengisu doküman oluşturdu. Push (p)

D1 d2 d3 d4 d5 d6 d7 d8 d9 d10 görevler

Tracability nedensellik zinciri problemin root cause

📋 Project Plan Nasıl Oluşturulur?
1. Projenin Amacını Belirle
Öncelikle neden bu projeyi yapıyorsun?

Hedef kitlen kim? Hangi sorunu çözecek?

Örnek:

Kullanıcıların günlük yedikleri yiyecekleri takip etmelerine ve kalori/makro değerlerini yönetmelerine yardımcı olacak bir web uygulaması geliştirmek.

2. Kapsamı (Scope) Tanımla
Proje neleri kapsıyor, neleri kapsamıyor?

Başlangıçta hangi özellikler olacak? (MVP: Minimum Viable Product)

Örnek:

Kullanıcı kaydı ve girişi

Yiyecek ekleme ve listeleme

Günlük toplam kalori/makro gösterimi
(İlk aşamada mesela sosyal özellikler yok)

3. İş Kırılımı (Work Breakdown Structure - WBS) Yap
Projeyi küçük adımlara böl.

Hangi adımda neler yapılacak?

Örnek WBS:

Backend Geliştirme:

Kullanıcı modeli oluştur

Yiyecek modeli oluştur

API endpoint'leri yaz

Frontend Geliştirme:

Login/Register sayfası

Dashboard ekranı

Deploy:

Dockerize et

AWS EC2 üzerine taşı

4. Zaman Çizelgesi (Timeline) Oluştur
Hangi işi hangi tarihe kadar bitirmek istiyorsun?

Sprint Sprint ayırabilirsin (Agile yapıyorsan).

Örnek Timeline:

1-7 Mayıs: Backend API geliştir

8-14 Mayıs: Frontend tasarım

15-20 Mayıs: Test ve düzeltmeler

21 Mayıs: Deployment

5. Kaynakları Belirle
Kim çalışacak? (Sen tek başına mı yapıyorsun? Ekip var mı?)

Hangi araçları kullanacaksın? (örneğin Django, PostgreSQL, Docker)

6. Riskleri Önceden Düşün
Nerelerde sorun çıkabilir?

Mesela AWS'de deploy zorlukları, veri tabanı problemleri, vs.

Örnek Riskler:

Docker kurulumu ve AWS yapılandırması gecikebilir.

API hız problemleri yaşanabilir.

7. Teslimatları (Deliverables) Tanımla
Hangi somut çıktıları teslim edeceksin?

Örnek:

Çalışan web uygulaması

API dökümantasyonu

Kullanım kılavuzu

🎯 Kısacası Bir Project Plan Böyle Oluyor:

Aşama	Yapılacak İş	Tarih	Sorumlu
Backend API geliştirme	Kullanıcı ve yiyecek CRUD işlemleri	1-7 Mayıs	Bengisu
Frontend tasarım	Login ve dashboard	8-14 Mayıs	Bengisu
Deployment	Dockerize et ve AWS EC2'ye kur	15-20 Mayıs	Bengisu
Test ve Sunum	Testler ve küçük düzeltmeler	21 Mayıs	Bengisu