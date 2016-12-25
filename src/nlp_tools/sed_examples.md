## Exmaples of sed

### Find word starting from 'symbols' and replace it with a word
echo 'hello 1worlZamoos man' | sed  -e 's/1worl.\w*/{PLANET}/g'
hello {PLANET} man

### Removes all empty strings
sed  -e '/^$/d' sed_test.txt

### Substitute sest of sympols to word
p123 to {PLANET}
sed  -e 's/p[0-9].\w*/{PLANET}/g' sed_test.txt

at the planet p123_67_90_$78 with serious atmosphere
sed  -e 's/p[0-9].\w*$.\w*/{PLANET}/g' sed_test.txt

### Currency 
Change $ numbers to {DOLLARS} 
echo 'he bought it for $ 120.000.23 well' | sed  -e 's/\$.[0-9.,]*/{DOLLARS}/g'
echo 'he bought it for $120.000.23,9 well' | sed  -e 's/\$.[0-9.,]*/{DOLLARS}/g'
