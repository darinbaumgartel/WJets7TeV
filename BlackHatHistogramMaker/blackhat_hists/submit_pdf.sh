#!/bin/sh

exe=./runList_batch.sh

#list=`ls lists/split/Wp2*list_??`
#list=`ls lists/split/Wm3j*real*list_??`
#list=`ls lists/split/Wp2*real*list_00`
list=`ls lists/split/*list_??`

ren=1.0
fac=1.0
nmem=0
pdf=CT10.LHgrid
case $1 in
    0 ) pdf=CT10.LHgrid ;nmem=52;;
    1 ) pdf=cteq6m.LHpdf ;nmem=40;;
    2 ) pdf=MSTW2008nlo68cl.LHgrid ;nmem=40;;
    3 ) pdf=NNPDF21_100.LHgrid ;nmem=99;;
    4 ) pdf=cteq6ll.LHpdf ;nmem=0;;
esac

# case $1 in
#     0 ) pdf=CT10.LHgrid ;nmem=10;;
#     1 ) pdf=cteq6m.LHpdf ;nmem=1;;
#     2 ) pdf=MSTW2008nlo68cl.LHgrid ;nmem=1;;
#     3 ) pdf=NNPDF21_100.LHgrid ;nmem=1;;
#     4 ) pdf=cteq6ll.LHpdf ;nmem=1;;
# esac

echo "pdf = $pdf"

for l in $list ; do

    job=`basename $l`
    echo ./submitBatch.perl $job $exe $l $pdf $ren $fac $nmem
    ./submitBatch.perl $job $exe $l $pdf $ren $fac $nmem
    #sleep 1
    python wait_bjobs.py

done

exit 0
