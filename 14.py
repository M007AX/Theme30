textvalue = 1  # объём книги
time = textvalue * 1024 * 60 / 1.5  # время записи книги
audiovalue = 2 * 48000 * 24 * time  # объём аудио дорожки
audiovalue = audiovalue * 0.16
print(audiovalue / 8 / 1024 / 1024 / 15)
