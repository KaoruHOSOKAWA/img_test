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
plt.grid(True)

# 文字をパスに変換する設定
plt.rcParams['svg.fonttype'] = 'path'
# パスに変換されたSVGとして保存
plt.savefig('sine_wave_vector_text_as_path.svg', format='svg')

# テキスト情報を保持したSVGとして保存
plt.rcParams['svg.fonttype'] = 'none'
plt.savefig('sine_wave_vector_text_as_text.svg', format='svg')
