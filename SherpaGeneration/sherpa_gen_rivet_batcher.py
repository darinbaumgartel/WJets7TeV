import os
import sys
import random

if len(sys.argv) < 3:
	print 'Must specify number of jobs and events. i.e. 50 jobs and 100 events\n\n   python sherpa_gen_rivet_batcher.py 50 100\n\n'

njobs = int(sys.argv[1])
nevents = int(sys.argv[2])
print '\nCreating and running',njobs,'jobs','with',nevents,'events per job.\n' 

if nevents <= 6000:
	q = '2nw'
if nevents < 2600:
	q = '2nd'
if nevents < 1100:
	q = '1nd'
if nevents < 400:
	q = '8nh'


if nevents > 6000:
	print 'Must use less than 6000 events per job. Try again.'

print "Using Queue: ",q

for x in range(njobs):
	jobtag = str(random.randint(1,100000000))
	N = str(nevents)
	script = 'RivetBatch/scripts/batchrun_'+jobtag+'.csh'
	os.system('cat batchrun.csh | sed \'s/RANDTAG/'+jobtag+'/g\' | sed \'s/NUMEVENT/'+N+'/g\' > '+script)
	os.system('chmod +x '+script)
	if '--break' not in sys.argv:
		os.system('bsub -q '+q+' -e /dev/null -J job_sherpabatch_'+jobtag +' < '+script)
	if '--break' in sys.argv:
		print('bsub -q '+q+' -e /dev/null -J job_sherpabatch_'+jobtag +' < '+script)
print '\n'