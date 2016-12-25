# Remove strings starting from numerics

LANG=C sed -i 's/^[.0-9].*//g' ma_raw_book_3.txt

# Remove non-ascii characters 
1. Variant 1
tr '\0-\10\13\14\16-\37' '[ *]' < infile  > outfile

2. Variant 2
In UTF-8 locales, you could use GNU sed which doesn't have the problem GNU tr has:
sed 's/[^[:print:]\r\t]/ /g' < infile > outfile

(note that those \r, \t are not standard, and GNU sed won't recognize them if POSIXLY_CORRECT is in the environment (will treat them as backslash, r and t being part of the set as POSIX requires)).

# Remove string containing pattern

sed '/About/d' infile

Make it inline with backup file
sed -i.bak '/pattern to match/d' infile

# Remove lines shorter than 12 characters including empty lines
sed -r '/^.{,12}$/d' infile

# Remove lines with word count less than 5
awk 'NF>5' infile  >  outfile
sed -n 's/\([^ ]\+ \)\{5,\}/&/p' infile

# Remove empty lines
sed '/^\s*$/d'

# Remove string between patterns
We want to delete some of the lines from the file using the command line stream editor, sed.
1. Use the following command to delete the lines lying between PATTERN-1 and PATTERN-2 , excluding the lines containing these patterns:
sed '/PATTERN-1/,/PATTERN-2/{//!d}' input.txt

If you want to modify the file itself, instead of just the file stream, include the “-i” flag after sed.
2. Use the following command to delete the lines lying between PATTERN-1 and PATTERN-2 , including the lines containing these patterns:
sed '/PATTERN-1/,/PATTERN-2/d'

3. To delete all the lines after PATTERN-2, use this
sed '/PATTERN-1/,$d' input

4. To delete lines, say 2 through 4 (if you know the correct line numbers, of course!), use this
sed '2,4d' input

# Remove string between two empty strings
Should test it!!!!!
sed '/^\s*$/,/^\s*$/d' input

# Remove certain character

## Remove paranthesis
sed 's/[()]//g' input

# Add point to the end of line
sed "s/$/./" input

# Remove quates
sed "s/['\"]//g" input

# Change characters at the end of the file
; -> .
sed "s/\;$/./" input

# Remove strings starting from digits
sed 's/^[0-9].*[0-9]//g' test_sed.txt | less

# Remove empty spaces from the left 
sed 's/^\s*//g' test_sed.txt | less

# Remove empty spaces from left end right of the string
sed 's/^\s*//;s/\s*$//' test_sed.txt > test_sed_1.txt

# Remove lists like
a). Foo
b. Soo
c.Koop
1.
sed -r 's/^[a-zA-Z0-9].?\.//' test_sed.txt | less



DealRoom requests template
sed 's/^Cat:.*//' 19_7_Sample_Tracker | sed 's/^-.*//' | sed '/^\s*$/d' > Sample_Tracker_0.txt

### Find word starting from 'symbols' and replace it with a word
echo 'hello 1worlZamoos man' | sed  -e 's/1worl.\w*/{PLANET}/g'
hello {PLANET} man

### Removes all empty strings
sed  -e '/^$/d' sed_test.txt

### Substitute set of sympols to word
p123 to {PLANET}
sed  -e 's/p[0-9].\w*/{PLANET}/g' sed_test.txt

at the planet p123_67_90_$78 with serious atmosphere
sed  -e 's/p[0-9].\w*$.\w*/{PLANET}/g' sed_test.txt

### Currency 
Change $ numbers to {DOLLARS} 
echo 'he bought it for $ 120.000.23 well' | sed  -e 's/\$.[0-9.,]*/{DOLLARS}/g'
echo 'he bought it for $120.000.23,9 well' | sed  -e 's/\$.[0-9.,]*/{DOLLARS}/g'

## Remove BULLET

sed 's/•//' infile
sed -i 's/■//'

## Remove brackets
sed 's/[][]//g'

