#!/bin/sh

echo "==============================="
echo -n "START: "
date

if [ $# -lt 1 ] ; then
    echo "Need a list file"
    exit 1
fi
listfile=$1

pdf=cteq6ll.LHpdf
if [ $# -gt 1 ] ; then
    pdf=$2
fi

ren=1.0
if [ $# -gt 2 ] ; then
    ren=$3
fi

fac=1.0
if [ $# -gt 3 ] ; then
    fac=$4
fi

NPDFMEMBERS=0
if [ $# -gt 4 ] ; then
    NPDFMEMBERS=$5
fi


source rc.bash
. ./setup.sh

#dir=BHSNtuples_mnt
dir=$BATCHDIR
histsdir=hists
logsdir=logs

echo $dir

echo -n "COPY: "
date

echo "Concatenating List Files "

list=" "
for f in `cat $listfile` ; do
    # to=$dir/`basename $f`
    # echo xrdcp root://eoscms//eos/cms/store/group/phys_smp/WPlusJets/$f $to
    # xrdcp root://eoscms//eos/cms/store/group/phys_smp/WPlusJets/$f $to
    # ls -l $to
    list="$list  root://eoscms//eos/cms/store/group/phys_smp/WPlusJets/$f"
done

echo "HERE HERE HERE"
echo $list

if ! [ -d $histsdir ] ; then 
    echo "mkdir -p $histsdir"
    mkdir -p $histsdir
fi
if ! [ -d $logsdir ] ; then 
    echo "mkdir -p $logsdir"
    mkdir -p $logsdir
fi

touch $log
for i in $(seq 0 $NPDFMEMBERS); do
    outname=$histsdir/`basename $listfile`_${pdf}_r${ren}_f${fac}_m$i.root
    log=$logsdir/`basename $listfile`_${pdf}_r${ren}_f${fac}_m$i.log

    echo -n "RUN: "
    date

    # run the list
    echo ./makeHistograms.exe -outfile $outname -pdf $pdf -ren $ren -fac $fac -member $i $list
    ./makeHistograms.exe -outfile $outname -pdf $pdf -ren $ren -fac $fac -member $i $list >> $log 
done


echo -n "DONE: "
date
echo "==============================="

exit 0
