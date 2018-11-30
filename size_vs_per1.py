import pandas as pd

data = pd.read_csv("/home/chaithanya/Downloads/planets.csv", skiprows=71)
df1 = data[['pl_name','pl_pnum', 'pl_orbper', 'pl_radj']]
grp=df1.groupby('pl_pnum')

pl_1  =grp.get_group(1)
pl_2  =grp.get_group(2)
pl_3  =grp.get_group(3)
pl_4  =grp.get_group(4)
pl_5  =grp.get_group(5)
pl_6  =grp.get_group(6)
pl_7  =grp.get_group(7)

ax1 = pl_1.plot(x='pl_orbper', y='pl_radj' , color='r', kind='scatter', label='pnum=1', logx =True)
ax2 = pl_2.plot(x='pl_orbper', y='pl_radj' , color='b' , kind='scatter', label='pnum=2', ax=ax1, logx=True)
ax3 = pl_3.plot(x='pl_orbper', y='pl_radj' , color='g' , kind='scatter', label='pnum=3', ax=ax1, logx =True)
ax4 = pl_4.plot(x='pl_orbper', y='pl_radj' , color='c' , kind='scatter', label='pnum=4', ax=ax1, logx =True)
ax5 = pl_5.plot(x='pl_orbper', y='pl_radj' , color='k' , kind='scatter', label='pnum=5', ax=ax1, logx =True)
ax6 = pl_6.plot(x='pl_orbper', y='pl_radj' , color='m' , kind='scatter', label='pnum=6', ax=ax1, logx =True)
ax7 = pl_7.plot(x='pl_orbper', y='pl_radj' , color='y' , kind='scatter', label='pnum=7', ax=ax1, logx =True)
ax1.set_xlabel("orbital period in days")
ax1.set_ylabel("planet radius compared to jupiter")
