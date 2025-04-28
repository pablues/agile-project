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

Bengisu Testing -> 1- projeyi başlatıp sizi ekledim 4-dbyi postresqle çevirdim 5- İlk modelleri oluşturdum

Tuğçe Frontend -> 6- proje için bir base.html oluşturuldu 7-tuğçe base.htmle ekstra özellikler ekledi 8-modelleri htmlde kullılabilir hale getirdi

Aslı Veri Tabanı
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

2. Proje Kapsamı
Kullanıcı kaydı ve giriş sistemi

Proje oluşturma

Sprint oluşturma

User Story ve Task ekleme

Task'ları durumlara göre (To Do, In Progress, Done) yönetme

3. İş Kırılımı (WBS)

Modül	Yapılacak İş	Açıklama
Kullanıcı Yönetimi	Kullanıcı kaydı	Kullanıcı e-posta ve şifre ile kayıt olabilir.
Kullanıcı Yönetimi	Kullanıcı girişi	Kullanıcı sisteme giriş yapabilir.
Proje Yönetimi	Proje oluşturma	Kullanıcı yeni bir proje başlatabilir.
Sprint Yönetimi	Sprint ekleme	Projeye sprint ekleyebilir (başlangıç-bitiş tarihi).
User Story Yönetimi	User Story ekleme	Sprint içine user story ekleyebilir.
Task Yönetimi	Task ekleme	User story altına görev ekleyebilir.
Task Yönetimi	Task durum değiştirme	Görevler To Do, In Progress, Done durumlarına alınabilir.
Task Yönetimi	Task kişiye atama (Opsiyonel)	Görevler kullanıcıya atanabilir.

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

Timeline:

1-7 Mayıs: Backend API geliştir

8-14 Mayıs: Frontend tasarım

15-20 Mayıs: Test ve düzeltmeler

21 Mayıs: Deployment

Our team: Melisa Backend, Tuğçe Frontend, 

Tools we use:
Django for framework, PostgreSQL for database, Docker.

Risks:

problems with Docker ve AWS.

API speed problems


Aşama	                      Yapılacak İş	               Tarih	                      Sorumlu
Backend API geliştirme	   User register,login 	           1-3 Mayıs	                   Melisa
Frontend tasarım	       User register,login	           1-3 Mayıs	                   Tuğçe
Database                   User register,login             1-3 Mayıs                        Aslı
Testing                    User register,login             1-3 Mayıs                       Bengisu
Backend API geliştirme	   feature to add new project      4-7 Mayıs	                   Melisa
Frontend tasarım	       feature to add new project 	   4-7 Mayıs	                   Tuğçe
Database                   feature to add new project      4-7 Mayıs                        Aslı
Testing                    feature to add new project      4-7 Mayıs                       Bengisu
Backend API geliştirme	   add sprint, user story 	       7-14 Mayıs	                   Melisa
Frontend tasarım	       add sprint, user story 	       7-14 Mayıs	                   Tuğçe
Database                   add sprint, user story 	       7-14 Mayıs                        Aslı
Testing                    add sprint, user story 	       7-14 Mayıs                      Bengisu
Backend API geliştirme	   User register,login 	           1-7 Mayıs	                   Melisa
Frontend tasarım	       User register,login	           1-7 Mayıs	                   Tuğçe
Database                   User register,login             1-7 Mayıs                        Aslı
Testing                    User register,login             1-7 Mayıs                       Bengisu
Deployment	Dockerize et ve AWS EC2'ye kur	15-20 Mayıs	Bengisu
Test ve Sunum	Testler ve küçük düzeltmeler	21 Mayıs	Tuğçe