import numpy as np
import matplotlib.pyplot as plt

# データの作成
x = np.linspace(0, 2 * np.pi, 1000)  # 0から2πまでの範囲で1000点
y = np.sin(x)

# Sine波のプロット
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)

# 軸ラベルとタイトルの設定
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Wave')
plt.legend()

# グリッドの表示
plt.grid(True)

# 保存するファイル形式のリスト
formats = ['eps', 'svg', 'pdf', 'png']

# 各ファイル形式で保存
# for fmt in formats:
#     plt.savefig(f'sine_wave.{fmt}', format=fmt)  # 他の形式で保存

[plt.savefig(f'sine_wave.{fmt}', format=fmt) for fmt in formats]

# 描画をクリア
plt.clf()
