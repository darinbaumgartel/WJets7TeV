import os
import sys
from glob import glob
import math

def round_sigfigs(num, sig_figs):
    sig_figs=2
    if num != 0:
        return round(num, -int(math.floor(math.log10(abs(num))) - (sig_figs - 1)))
    else:
        return 0  # Can't take the log of 0
def BeautifiedEntry(entry):
	# print '---------------------------------'
	# print entry
	entry = [format(float(u), '.66f') for u in entry]
	# print entry
	# print ' --------------'
	# print ' entry:',entry
	# print ' flent:',float(entry[0])
	if float(entry[0])==0.0:
		return '--'
	rentry =  [str(round_sigfigs(float(e),2)) for e in entry]

	# print rentry
	# print 'clean rentry:',rentry
	newrentry = []
	for u in rentry:
		newu = u
		if 'e' in u:
			# print rentry
			# print ' *',(u.split('e')[-1])
			# print ' **',int(u.split('e')[-1])
			dim = int(u.split('e')[-1])
			# print dim
			newu = u.split('e')[0]
			if dim<0:
				nzeros = abs(dim)-1
				newu = '0.'+'0'*nzeros+newu.replace('.','')
			if dim>0:
				nzeros = abs(dim) - len(newmu.split('.')[-1])
				newu =  newu.replace('.','') + '0'*nzeros

		newrentry.append(newu)


	# print ' !! ',newrentry
	rentry = newrentry

	# print ' zmod:',rentry

	# print rentry
	uncertainties = rentry[1:]
	# print uncertainties
	NL = 999
	NR = 0
	for u in uncertainties:
		# u = format(float(u), '.66f')

		nl = len(u.split('.')[0])
		nr = 0
		if (len(u.split('.')) > 1):
			if float('.'+u.split('.')[1]) == float(u):
				nl = 0
			nr = len(u.split('.')[1])
		if nl < NL:
			NL = nl
		if nr > NR:
			NR = nr
	rplace = 9999
	# print 'nl', NL
	if NL <rplace:
		rplace = -NL+2
	# print 'rplace', rplace
	if NL <= 0:
		rplace = 1*NR
	# print 'rplace', rplace


	decimal = 10**rplace
	# print 'd', decimal

	entry = [str(round(float(e) * 1.0*decimal) / (1.0*decimal)) for e in entry]

	# print 'sigmod:', entry

	newentry = []
	for u in entry:
		newu = u
		if 'e' in u:
			# print ' -- '
			# print entry
			# print u
			# print u.split('e')
			dim = int(u.split('e')[-1])
			# print dim
			newu = u.split('e')[0]
			if dim<0:
				nzeros = abs(dim)-1
				newu = '0.'+'0'*nzeros+newu.replace('.','')
			if dim>0:
				nzeros = abs(dim) - len(newmu.split('.')[-1])
				newu =  newu.replace('.','') + '0'*nzeros

		newentry.append(newu)
	entry = newentry

	# print 'dimmod ', entry
	outentry = []

	ap0 = True

	for e in entry:
		rhs = e.split('.')[1]
		while len(rhs) <NR:
			rhs+='0'
		e = e.split('.')[0]+'.'+rhs
		outentry.append(e)
		if e[-1] !='0' or e[-2]!='.':
			ap0 = False
		
	if ap0==True:
		outentry = [e[:-2] for e in outentry]

	# print 'outent', outentry
	outtex = ''
	if len(outentry)==3:
		if outentry[1]!=outentry[2]:
			outtex = outentry[0] +'$^{+'+outentry[1]+'}_{-'+outentry[2]+'}$'
		else:
			outtex = outentry[0] +' $\\pm$ '+outentry[1]
	elif len(outentry)==2:
		outtex = outentry[0] +' $\\pm$ '+outentry[1]
	elif len(outentry)==1:
		outtex = outentry[0]
	else:
		print ' Too many uncertaities to parse for TeX!'
		sys.exit()

	# print outtex
	return outtex




def HArrayFromHlog(hlog):
	harray = []
	for line in open(hlog,'r'):
		line = line.replace(';',',')
		line = line.split(',')
		for x in range(len(line)):
			if 'ROOT' in line[x]:
				line[x] = '100'
		fline = [float(x) for x in line]
		harray.append(fline)
	harray = harray[0:-1]
	return harray

def GetFiles(adir):
	bfiles = allfiles = glob(adir+'/pyplotsTCHEM/PF*standard_s*.hlog')
	nfiles = allfiles = glob(adir+'/pyplotsTCHEMBTagOff/PF*standard_s*.hlog')
	bvfiles = allfiles = glob(adir+'/pyplotsTCHEM/PF*btag*s_simp*.hlog')

	# print bvfiles
	centraldata = HArrayFromHlog(bfiles[0])
	downdata = HArrayFromHlog(bvfiles[0])
	downmdata = HArrayFromHlog(bvfiles[1])
	upmdata = HArrayFromHlog(bvfiles[2])
	updata = HArrayFromHlog(bvfiles[3])

	nobdata = HArrayFromHlog(nfiles[0])

	# print 'C', centraldata
	# print 'U', updata
	# print 'D', downdata
	# print 'N', nobdata

	return [centraldata, updata, downdata,upmdata,downmdata, nobdata]


[centraldata, updata, downdata,upmdata,downmdata, nobdata] = GetFiles(sys.argv[1])

for bin in range(len(centraldata)):
	C = centraldata[bin]
	# print ' '
	# print C
	U = updata[bin]
	D = downdata[bin]
	UM = upmdata[bin]
	DM = downmdata[bin]	

	N = nobdata[bin]

	[lhsC,rhsC,qC,eqC,sC,esC,vC,evC,zC,ezC,tC,etC,wC,ewC,TC,eTC,datC] = C
	[lhsU,rhsU,qU,eqU,sU,esU,vU,evU,zU,ezU,tU,etU,wU,ewU,TU,eTU,datU] = U
	[lhsD,rhsD,qD,eqD,sD,esD,vD,evD,zD,ezD,tD,etD,wD,ewD,TD,eTD,datD] = D
	[lhsUM,rhsUM,qUM,eqUM,sUM,esUM,vUM,evUM,zUM,ezUM,tUM,etUM,wUM,ewUM,TUM,eTUM,datUM] = UM
	[lhsDM,rhsDM,qDM,eqDM,sDM,esDM,vDM,evDM,zDM,ezDM,tDM,etDM,wDM,ewDM,TDM,eTDM,datDM] = DM
	[lhsN,rhsN,qN,eqN,sN,esN,vN,evN,zN,ezN,tN,etN,wN,ewN,TN,eTN,datN] = N



	bin_tex = int(0.5*(rhsC + lhsC))
	
	#print wC,wU,wD,wUM,wDM

	wpurC = 100.0*wC/TC
	wpurD = (100.0*wD/TD - wpurC)
	wpurU = (100.0*wU/TU - wpurC)
	wpurDM = (100.0*wDM/TDM - wpurC)
	wpurUM = (100.0*wUM/TUM - wpurC)

	wpurUs = []
	wpurDs = []

	for x in [wpurU,wpurUM,wpurD,wpurDM]:
		if x > 0 and len(wpurUs)<2:
			wpurUs.append(x)
		if x < 0 and len(wpurDs)<2:
			wpurDs.append(x)


	wpurUt = math.sqrt(sum([z*z for z in wpurUs]))
	wpurDt = math.sqrt(sum([z*z for z in wpurDs]))

	WpurErrs = [wpurUt,wpurDt]
	# sys.exit()

	wpurN = 100.0*wN/TN

	wpur_central = str(round(wpurC,9))
	# print wpurD
	# print wpurU
	wpur_err = max(WpurErrs)
	wpur_nom = str(round(wpurN,9))
	wpur_err = str(round(wpur_err,9))

	new_wpur = BeautifiedEntry([wpur_central, wpur_err])

	wpur_dig = new_wpur.split(' ')[0]
	# print wpur_dig

	wpur_diglhs = (len(wpur_dig.split('.')[1]))
	# print wpur_diglhs
	# wpur_nom = str(round(float(wpur_nom), wpur_diglhs))


	wredCN = 100.0*(wN - wC)/wN
	wredDN = abs(100.0*(wN - wD)/wN - wredCN)
	wredUN = abs(100.0*(wN - wU)/wN - wredCN)
	wredDNM = abs(100.0*(wN - wDM)/wN - wredCN)
	wredUNM = abs(100.0*(wN - wUM)/wN - wredCN)	

	# print wredCN,wredDN,wredUN,wredDNM,wredUNM
	wredUs = []
	wredDs = []

	for x in [wredUN,wredUNM,wredDN,wredDNM]:
		if x > 0 and len(wredUs)<2:
			wredUs.append(x)
		if x < 0 and len(wredDs)<2:
			wredDs.append(x)



	wredUt = math.sqrt(sum([z*z for z in wredUs]))
	wredDt = math.sqrt(sum([z*z for z in wredDs]))

	WredErrs = [wredUt,wredDt]


	wrederr = max(WredErrs)



	wredCN = str(round(wredCN,9))
	wrederr = str(round(wrederr,9))

	wreduction = BeautifiedEntry([wredCN, wrederr])


	tredCN = 100.0*(tN - tC)/tN
	tredDN = abs(100.0*(tN - tD)/tN - tredCN)
	tredUN = abs(100.0*(tN - tU)/tN - tredCN)
	tredDNM = abs(100.0*(tN - tDM)/tN - tredCN)
	tredUNM = abs(100.0*(tN - tUM)/tN - tredCN)
	trederr = max([tredDN, tredUN])

	tredCN = str(round(tredCN,9))



	tredUs = []
	tredDs = []

	for x in [tredUN,tredUNM,tredDN,tredDNM]:
		if x > 0 and len(tredUs)<2:
			tredUs.append(x)
		if x < 0 and len(tredDs)<2:
			tredDs.append(x)



	tredUt = math.sqrt(sum([z*z for z in tredUs]))
	tredDt = math.sqrt(sum([z*z for z in tredDs]))

	TredErrs = [tredUt,tredDt]


	trederr = max(TredErrs)





	trederr = str(round(trederr,9))

	treduction = BeautifiedEntry([tredCN, trederr])

	print str(bin_tex) + ' & '+wreduction+' & '+treduction+' & '+wpur_nom+' $\\rightarrow$ '+ new_wpur + ' \\\\'



# for pair in ff: 
# 	print pair
