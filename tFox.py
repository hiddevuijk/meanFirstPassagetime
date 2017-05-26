import numpy as np
import scipy.integrate as integrate




def v(r,c):
	return c/(r*r)


def Iy(y,c,dr,dt):
	A = np.sqrt(6*dr*dt+v(y,c)*v(y,c))
	return y*y/A

def Iz(z,c,a,R,dr,dt):
	A = integrate.quad(lambda y: Iy(y,c,dr,dt),z,R)[0]
	B = np.sqrt(6*dr*dt + v(z,c)*v(z,c))
	return A/(B*z*z)
def T(r,c,a,R,dr,dt):
	A = integrate.quad(lambda z: Iz(z,c,a,R,dr,dt),a,r)[0]
	return 6*dr*A



