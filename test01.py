import numpy as np
import matplotlib.pyplot as plt

# 論文用の設定
plt.rcParams['svg.fonttype'] = 'none'  # テキスト情報を保持する設定
plt.rcParams['font.family'] = 'sans-serif'  # サンセリフ系フォントを指定
# plt.rcParams['font.sans-serif'] = ['Arial']  # Helveticaを指定

# データの作成
x = np.linspace(0, 2 * np.pi, 1000)  # 0から2πまでの範囲で1000点
y = np.sin(x)

# Sine波のプロット
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)

# 軸ラベルとタイトルの設定
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Wave. it is very important for me !!')
plt.legend()

# グリッドの表示
plt.grid(True)

# SVG形式で保存
plt.savefig('sine_wave.svg', format='svg')

