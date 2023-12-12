w = "A 11.105 B 2.96226 C 5.20256 D 3.45627 E 14.6267 F 1.39484 G 2.64619 H 1.32054 I 8.0974 J 0.377811 K 0.411214 L 4.44086 M 3.38385 N 5.82441 O 6.04346 P 2.63182 Q 0.223954 R 6.67458 S 4.41009 T 5.86733 U 5.97792 V 1.00012 W 0.11428 X 0.403724 Y 0.40256 Z 0.847835".split()
v = "A 2.13677 B 2.83065 C 5.07117 D 4.41296 E 2.79822 F 2.26971 G 4.54265 H 2.3151 I 1.81901 J 3.79365 K 2.23728 L 3.91686 M 5.06793 N 6.23196 O 1.5661 P 4.73396 Q 5.42784 R 5.28517 S 1.02461 T 5.40838 U 2.36049 V 7.37979 W 6.69239 X 3.19056 Y 2.59071 Z 4.89608".split()

WORDS = dict()
VRAC = dict()

for i in range(len(w)//2):
    WORDS[w[2*i]] = float(w[2*i+1])
    VRAC[v[2*i]] = float(v[2*i+1])

# Sort the dict based on the values
WORDS = dict(sorted(WORDS.items(), key=lambda item: item[1], reverse=True))
VRAC = dict(sorted(VRAC.items(), key=lambda item: item[1], reverse=True))

print(WORDS)
print(VRAC)