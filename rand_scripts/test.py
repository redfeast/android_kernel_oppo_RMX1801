f=open('h.txt')
o=open('cmd1.sh','w')
for each in f:
		a=each.split('rm2pk')
		b=a[1].split('/')
		n=0
		pt='\.\.\/\.\.'
		while n<(len(b)-1):
			if n==len(b)-2:
				pt=pt+str(b[n])
			else:
				pt=pt+str(b[n])+'\/'
			n+=1
		print(pt)
		o.write('sed -i.bakkk "s/.*\#define *TRACE_INCLUDE_PATH.*/\#define TRACE_INCLUDE_PATH '+pt+'/g" '+each)
o.close()



