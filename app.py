from flask import Flask, render_template
import instaloader
import matplotlib.pyplot as plt
import matplotlib as mp
import numpy as np

import os
os.remove('static/plot.png') 

L = instaloader.Instaloader()

f = open('input.txt','r')
accounts = f.read()
p = accounts.split('\n')

PROFILE = p[:]
#print(PROFILE)
followers_count=[]
for ind in range(len(PROFILE)):
    pro = PROFILE[ind]
    profile = instaloader.Profile.from_username(L.context, pro)
    followers_count.append(profile.followers)


likeability_scores = np.array(followers_count)
 
data_normalizer = mp.colors.Normalize()
color_map = mp.colors.LinearSegmentedColormap(
    "my_map",
    {
        "red": [(0, 1.0, 1.0),
                (1.0, .5, .5)],
        "green": [(0, 0.5, 0.5),
                  (1.0, 0, 0)],
        "blue": [(0, 0.50, 0.5),
                 (1.0, 0, 0)]
        
        
    }
)

fig, ax = plt.subplots()
#plt.bar(usernames,followers_count)
bars = ax.bar(p,followers_count,color=color_map(data_normalizer(likeability_scores)))
plt.xticks(rotation=25, fontname='dejavu sans')

# Axis formatting.
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)

# Add text annotations to the top of the bars.
bar_color = bars[0].get_facecolor()
for bar in bars:
    ax.text(
      bar.get_x() + bar.get_width() / 2,
      bar.get_height() + 14.0,
      round(bar.get_height()),
      horizontalalignment='center',
      color='red'
  )
    
ax.set_xlabel('Daur Insta handles', labelpad=25, color='#333333', fontsize=12, weight='bold')
ax.set_ylabel('Followers Count', labelpad=25, color='#333333', fontsize=12, weight='bold')
ax.set_title('Daurs Verticals on Insta', pad=35, color='#333333', fontsize=15,
             weight='bold')

fig.tight_layout()

plt.savefig('static/plot.png')

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('display.html')


if __name__ == "__main__":
    app.run(debug=True)