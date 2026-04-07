import matplotlib.pyplot as plt
import numpy as np

class QuickViz:
    def radar(self, name, stats):
        cats = ['Damage', 'Dex', 'Intel', 'Con', 'Cha']
        values = stats + [stats[0]]
        angles = np.linspace(0, 2*np.pi, 5, endpoint=False).tolist()
        angles += angles[:1]
        
        plt.figure(figsize=(6,6))
        ax = plt.subplot(111, projection='polar')
        ax.plot(angles, values, 'o-', linewidth=2)
        ax.fill(angles, values, alpha=0.25)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(cats)
        ax.set_title(f"{name}'s Stats")
        plt.savefig(f"{name}_radar.png")
        plt.show()
    
    def compare(self, name1, stats1, name2, stats2):
        cats = ['Damage', 'Dex', 'Intel', 'Con', 'Cha']
        x = [0,1,2,3,4]
        plt.figure(figsize=(10,6))
        plt.bar([i-0.2 for i in x], stats1, 0.4, label=name1)
        plt.bar([i+0.2 for i in x], stats2, 0.4, label=name2)
        plt.xticks(x, cats)
        plt.legend()
        plt.title("Character Comparison")
        plt.savefig("compare.png")
        plt.show()