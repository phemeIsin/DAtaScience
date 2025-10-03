import matplotlib.pyplot as plt
import numpy as np

months = ['07/2019', '08/2019', '09/2019', '10/2019', '11/2019']
searches = [50, 53, 59, 56, 62]
direct = [39, 47, 42, 51, 51]
social = [70, 80, 90, 87, 92]

x = np.arange(len(months))
width = 0.22

fig, ax = plt.subplots(figsize=(11,6.5))
bars1 = ax.bar(x - width, searches, width=width, label='Searches', color='#2E9AFE')
bars2 = ax.bar(x, direct, width=width, label='Direct', color='#F781BE')
bars3 = ax.bar(x + width, social, width=width, label='Social Media', color='#F39C12')

def autolabel(bars):
    for bar in bars:
        h = bar.get_height()
        ax.annotate(f'{h}', xy=(bar.get_x() + bar.get_width() / 2, h),
                    xytext=(0, 4), textcoords='offset points', ha='center', va='bottom', fontsize=9)

autolabel(bars1)
autolabel(bars2)
autolabel(bars3)

ax.set_ylabel('visitors\nin thousands', fontsize=11, labelpad=12, rotation=0)
ax.yaxis.set_label_coords(-0.07, 0.95)
ax.set_xlabel('months', fontsize=11)
ax.set_title('Visitors by web traffic sources', fontsize=14, pad=14)
ax.set_xticks(x)
ax.set_xticklabels(months)
ax.set_ylim(0, 110)
ax.set_yticks(range(0,111,20))
ax.legend(loc='lower left', bbox_to_anchor=(0.02, -0.16), ncol=3, frameon=False)
plt.tight_layout(rect=[0,0.02,1,1])

# Show the plot window
plt.show()
