# このアプリはテスト音声ファイルを数値化するためのものです
# 音声ファイルを数値配列にし、そのデータを波形にして表示します
from pydub import AudioSegment
from pydub.playback import play
import numpy as np
import matplotlib.pyplot as plt

# 音楽データの読み込み
sound = AudioSegment.from_file("./voice/test1.wav", "wav")

# NumPy配列に返還
data = np.array(sound.get_array_of_samples())

# ステレオ音声から片方を抽出
x = data[::sound.channels]

# グラフ化
plt.plot(x[::10])
plt.grid()
plt.show()

# 再生
play(sound)
