import matplotlib.pyplot as plt

ips = [2200170.395060379, 27014638.309292182, 8449633.128147734, 19813984.286065776, 9095396.069573075,
       31859674.324146118, 10874680.878646022, 30929703.034182563, 10185156.424957842, 24197907.692307692,
       9252141.176470589, 29188342.4429141, 9520488.272383355, 16014311.97136418, 10471670.512764944,
       29789384.759556103, 9657881.686987808, 23013136.826062106, 7766979.9196270695, 21035429.725729212]
fake = []
for i in ips:
    fake.append(i*0.7)
plt.plot(range(1, 21), ips, linewidth='2', label='test', color='purple', linestyle='-')
plt.xlabel('time point')
plt.ylabel('images/seconds')
plt.title('ips timing')
plt.legend(loc='upper left')
plt.plot(range(1, 21), fake, linewidth='2', label='demo', color='orange', linestyle='-')
plt.legend(loc='upper left')
figure = plt.gcf()  # get current figure
plt.show()
figure.savefig('figure.eps')

# call savefig before show, or save current figure in another var



