
Trouver les k tels que 3^k = 2^k mod 37

- Par démonstration:
```
    3^k = 2^k [37]
<=> 3^k x 19^k = 2^k x 19^k [37]
<=> (3 x 19)^k = 38^k [37]
<=> 57^k = 1 [37]    car 38 = 1 [37]
<=> 20^k = 1 [37]    car 57 = 20 [37]
<=> 20^k - 1 = 0 [37]
<=> k = 36 (petit théorème de Fermat)
```

- Méthode calculatoire
https://docs.google.com/spreadsheets/d/1EvLSKDoTeza1JMohK0UrueMsyyRA9BCgwv_4zhf2j7Y/edit?usp=sharing

Approche itérative en gardant a_i, b_i < 37 à chaque itération.

```
a_i = 3^i [37]
b_i = 2^i [37]
c_i = (3^i - 2^i) [37]

a_i+1 = 3 * a_i [37]
b_i+1 = 2 * b_i [37]
c_i+1 = b_(i+1) - a_(i+1) [37]

i	a_i b_i c_i
1	3	2	1
2	9	4	5
3	27	8	19
4	7	16	-9
5	21	32	-11
6	26	27	-1
7	4	17	-13
8	12	34	-22
9	36	31	5
10	34	25	9
11	28	13	15
12	10	26	-16
13	30	15	15
14	16	30	-14
15	11	23	-12
16	33	9	24
17	25	18	7
18	1	36	-35
19	3	35	-32
20	9	33	-24
21	27	29	-2
22	7	21	-14
23	21	5	16
24	26	10	16
25	4	20	-16
26	12	3	9
27	36	6	30
28	34	12	22
29	28	24	4
30	10	11	-1
31	30	22	8
32	16	7	9
33	11	14	-3
34	33	28	5
35	25	19	6
36	1	1	0
```
