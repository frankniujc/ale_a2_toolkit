rm -f input
echo "compile('ale.pl')."  > input
echo "compile_gram('$1')." >> input

if [ $# -eq 2 ]
then
    sentence=`python utils.py -t "$2"`
    echo "rec$sentence." >> input
fi

if [ $# -eq 3 ]
then
    sentences=`python utils.py -tf "$2"`
    echo "$sentences" >> input
fi

/h/u2/csc485h/fall/pub/sicstus < input
rm -f input