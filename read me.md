# Denge Ustası Uygulaması

## Temel Amaç

"Denge Ustası", yapay zeka kullanarak "CartPole" ortamında bir direğin dengede durmasını öğrenen bir uygulamadır. Bu uygulama, bir vagonun üzerinde duran bir direği dengede tutmayı amaçlayan bir problem olan "CartPole" oyununu çözmek için takviyeli öğrenme (reinforcement learning) tekniklerini kullanır.
![best](https://github.com/user-attachments/assets/b99a6f61-06d5-4b98-904c-859842faf899)

## Çalışma Prensibi

1.  **CartPole Ortamı:**
    *   Uygulamamız, OpenAI'nin `gym` kütüphanesiyle sağlanan "CartPole-v1" ortamını kullanır.
    *   Bu ortamda, bir vagon yatay bir çizgi üzerinde hareket edebilir ve bu vagonun üzerinde de bir direk durur.
    *   Uygulamanın amacı, vagonu sağa veya sola hareket ettirerek direğin düşmesini engellemektir.

2.  **Yapay Zeka Modeli:**
    *   Uygulamamızda, bu denge problemini çözmek için bir yapay sinir ağı (neural network) modeli kullanılır. Bu model, TensorFlow/Keras kütüphaneleriyle oluşturulur.
    *   Model, vagon ve direğin durumunu (pozisyon, hız gibi) girdi olarak alır ve vagonu hangi yöne hareket ettireceğine dair karar verir.
    *   Modelimiz, girdi olarak durum bilgilerini alır.
    *   Modelimiz, çıktı olarak iki aksiyon (sola git veya sağa git) için bir skor üretir.

3.  **Q-Öğrenme Algoritması:**
    *   Modeli eğitmek için Q-öğrenme (Q-learning) algoritması kullanılır.
    *   Q-öğrenme, bir ajanın (bizim modelimiz) etkileşimde bulunduğu ortamdan (CartPole) deneyimler yoluyla öğrenmesini sağlar.
    *   Model, attığı her adımda bir ödül (reward) alır. Direği dengede tuttuğu sürece +1 ödül alır. Direk düştüğünde oyun biter.
    *   Model, bu ödülleri kullanarak doğru aksiyonları öğrenir ve daha iyi denge performansı gösterir.

4.  **Eğitim Süreci:**
    *   Uygulama, belirli sayıda bölüm (episode) boyunca CartPole oyununu oynar.
    *   Her bölüm sonunda, modelin performansı güncellenir ve model yeni deneyimlerden öğrenir.
    *   Model, başlangıçta rastgele aksiyonlar seçerken, zamanla daha iyi bir strateji geliştirir ve direği daha uzun süre dengede tutmayı öğrenir.
    *   `epsilon` parametresi ile rastgele aksiyon yapma ihtimali değiştirilerek öğrenmenin keşif ve sömürü aşaması dengelenir.

5.  **Performans Değerlendirmesi:**
    *   Eğitim boyunca, uygulamanın performansı birkaç farklı metrikle takip edilir:
        *   **Total Reward (Toplam Ödül):** Her bölüm sonunda alınan toplam ödül.
        *   **Successes (Başarılar):** Direğin dengede tutulduğu adımların toplam sayısı.
        *   **Failures (Başarısızlıklar):** Direğin düştüğü bölüm sayısı.
    *   Bu metrikler, eğitim sürecinin ilerlemesini ve modelin ne kadar başarılı olduğunu görmemizi sağlar.
    *   Bu metrikler, çizdirilen grafik ile görselleştirilir.
    *   Tablo formatında her bölümdeki bu değerler aynı zamanda görülür.

## Uygulamanın Temel Özellikleri

*   **Yapay Zeka ile Takviyeli Öğrenme:** CartPole oyununu çözmek için takviyeli öğrenme yöntemleri kullanır.
*   **Yapay Sinir Ağı:** Karar mekanizması için derin öğrenme modelini kullanır.
*   **Q-Öğrenme:** Modeli eğitmek için Q-öğrenme algoritmasını kullanır.
*   **Performans Takibi:** Eğitim sürecini görselleştirmek ve değerlendirmek için grafik ve tablo kullanır.

## Uygulamanın Kullanım Alanları

*   **Takviyeli Öğrenme Eğitimi:** Takviyeli öğrenme algoritmalarını anlamak ve uygulamak için pratik bir araçtır.
*   **Yapay Zeka Deneyleri:** Yapay zeka modelleriyle deneyler yapmak ve farklı parametrelerin etkilerini görmek için kullanılabilir.
*   **Oyun Geliştirme:** Oyunlarda yapay zeka davranışlarını modellemek için kullanılabilir.

## Özet

"Denge Ustası", basit bir oyun ortamında takviyeli öğrenme prensiplerini gösteren eğitici bir uygulamadır. Hem yeni başlayanlar hem de bu alanda deneyimi olan kişiler için pratik bir öğrenme aracıdır.
