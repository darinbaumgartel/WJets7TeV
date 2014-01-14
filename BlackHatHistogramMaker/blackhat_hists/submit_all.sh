#!/bin/sh

./submit_pdf.sh 0
./submit_pdf.sh 2
./submit_pdf.sh 3

./submit_scales.sh 0.5
./submit_scales.sh 2.0

python wait_bjobs.py --done

exit 0
