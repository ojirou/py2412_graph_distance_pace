import matplotlib.pyplot as plt
import numpy as np
import webbrowser
base_folder='D:\\00b_ドキュメント2023年4月\\30ランニング\\【RUN-SKL-CAL001】ペースから走行距離計算\\'
a0=np.loadtxt(base_folder+'241014走行距離（10時間）.csv', delimiter=',', encoding='shift-jis', skiprows=1)
fig_1, ax=plt.subplots(figsize=(6,4))
ax.plot(a0[:,0]/60, a0[:,1], color="red", lw=1, ls='-', marker='o', markersize=0, label='10:00/km')
ax.plot(a0[:,0]/60, a0[:,4], color="orange", lw=1, ls='-', marker='o', markersize=0, label='8:00/km')
ax.plot(a0[:,0]/60, a0[:,6], color="green", lw=1, ls='-', marker='o', markersize=0, label='7:04/km')
ax.plot(a0[:,0]/60, a0[:,9], color="purple", lw=1, ls='-', marker='o', markersize=0, label='6:00/km')
ax.plot(a0[:,0]/60, a0[:,13], color="blue", lw=1, ls='-', marker='o', markersize=0, label='5:00/km')
# ax.plot(a0[:,0], a0[:,2], color="red", lw=1, ls='-', marker='o', markersize=6.5, label='B')
# ax.plot(a0[:,0], a0[:,1], color="blue", lw=1, ls='-', marker='o', markersize=6.5, label='A')
# ax.plot(a0[:,0], a0[:,2], color="red", lw=1, ls='-', marker='o', markersize=6.5, label='B')
# ax.plot(a0[:,0], a0[:,1], color="blue", lw=1, ls='-', marker='o', markersize=6.5, label='A')
# ax.plot(a0[:,0], a0[:,2], color="red", lw=1, ls='-', marker='o', markersize=6.5, label='B')
ax.set_xscale('linear')
ax.set_xlim([0, 10])
ax.set_ylim([0, 120])
ax.set_xlabel('Running Time [h]', fontsize=11)
ax.set_ylabel('Distance [km]', fontsize=11)
ax.legend(loc='upper left') 
plt.title('Ruuning Distance accoding to Pace', fontsize=11)
ax.grid(ls=':')
PngFile=base_folder+'241014走行距離（10時間）.png'
PdfFile=base_folder+'241014走行距離（10時間）.pdf'
fig_1.subplots_adjust(left=0.13, right=0.95, bottom=0.13, top=0.93)
fig_1.savefig(PngFile, facecolor='white')
fig_1.savefig(PdfFile, facecolor='white')
# webbrowser.open_new(PngFile)
# webbrowser.open_new(PdfFile)