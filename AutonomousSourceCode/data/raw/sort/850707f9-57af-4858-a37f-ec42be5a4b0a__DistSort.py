from mDist import mDist

def DistSort(p,C):
	dists=[ (mDist(p,c),c) for c in C]
	return [p for d,p in sorted(dists,key=lambda x: x[0])]
