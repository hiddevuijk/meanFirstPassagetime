import scipy.integrate as integrate


def v(r,c):
	return c/(r*r)


def Iy(y,c,dr,dt):
	return y*y

def Ix(x,c,a,R,dr,dt):
	A = integrate.quad(lambda y: Iy(y,c,dr,dt),x,R)[0]
	D = dt + v(x,c)*v(x,c)/(6*dr)
	return A/(x*x*D)

def T(r,c,a,R,dr,dt):
	A = integrate.quad(lambda x: Ix(x,c,a,R,dr,dt),a,r)[0]
	return A



