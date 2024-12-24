import gym
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

# CartPole ortamını yükle
env = gym.make("CartPole-v1", render_mode="rgb_array")  # render_mode eklenmiş

# Durum ve aksiyon boyutlarını al
state_size = env.observation_space.shape[0]
action_size = env.action_space.n

# Modeli oluştur
model = Sequential([
    Input(shape=(state_size,)),  # Input katmanı güncellenmiş
    Dense(64, activation='relu'),  # Katman sayısı arttırıldı
    Dense(64, activation='relu'),
    Dense(action_size, activation='linear')
])
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')

# Q-öğrenme parametreleri
total_episodes = 100
max_timesteps = 200
gamma = 0.95
epsilon = 1.0
epsilon_decay = 0.995
epsilon_min = 0.01

# Performans verilerini kaydetmek için listeler
total_rewards = []
successes_list = []
failures_list = []
successes = 0  # Başarı sayısını tutacak değişkeni döngü dışında tanımla
failures = 0  # Başarısızlık sayısını tutacak değişkeni döngü dışında tanımla

# Eğitim döngüsü
for episode in range(total_episodes):
    state = env.reset(seed=42)[0]  # reset() fonksiyonu güncellendi
    state = np.reshape(state, [1, state_size])
    total_reward = 0
    episode_successes = 0 # o bölümdeki başarı sayısını tutacak değişkeni tanımla
    episode_failures = 0 # o bölümdeki başarısızlık sayısını tutacak değişkeni tanımla
    
    for t in range(max_timesteps):
        if np.random.rand() <= epsilon:
            action = env.action_space.sample()  # Rastgele aksiyon
        else:
            action = np.argmax(model.predict(state, verbose=0)[0])  # Model tahminine göre aksiyon

        next_state, reward, done, _, info = env.step(action)
        next_state = np.reshape(next_state, [1, state_size])

        # Başarıyı ve hatayı hesapla
        total_reward += reward
        if reward == 1:  # Başarıyı kontrol et
            successes += 1
            episode_successes += 1
        else:  # Başarısızlık
            failures += 1
            episode_failures += 1

        # Q-değerini güncelle
        target = reward
        if not done:
            target = reward + gamma * np.amax(model.predict(next_state, verbose=0)[0])

        target_f = model.predict(state, verbose=0)
        target_f[0][action] = target
        model.fit(state, target_f, epochs=1, verbose=0)  # Hızlı öğrenme

        state = next_state

        # Oyun bittiğinde ekranı güncelle
        if done:
            total_rewards.append(total_reward)
            successes_list.append(successes)  # Toplam başarı sayısını listeye ekle
            failures_list.append(failures) # Toplam başarısızlık sayısını listeye ekle
            print(f"Episode: {episode+1}/{total_episodes}, Total Reward: {total_reward}, Successes: {successes}, Failures: {failures}")
            break

    # Epsilon'ı yavaşça güncelle
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay
        if epsilon < 0.1:  # epsilon'ın çok hızlı düşmemesi için küçük bir alt limit koyduk
            epsilon = 0.1

# Eğitimin sonunda görselleştirme
if (episode + 1) % 10 == 0:
    plt.plot(total_rewards, label='Total Reward', color='b')  # Total Reward için mavi renk
    plt.plot(successes_list, label='Successes', color='orange')  # Successes için turuncu renk
    plt.plot(failures_list, label='Failures', color='red')  # Failures için kırmızı renk
    plt.xlabel('Episode')
    plt.ylabel('Value')
    plt.title(f'Total Rewards, Successes and Failures for Episodes (Up to {episode+1})')
    
    # Legend ekleyerek iki veri kümesi için etiket ekliyoruz
    plt.legend()

    # Grafiği göster
    plt.show()

env.close()