import abc
import numpy as np
from scipy.integrate._ode import IntegratorBase


class Rk4Integrator(IntegratorBase):
    #
    #     runner = <odeint function> or None
    #
    def __init__(self, dt):  # required
        self.dt = dt
        self.success = 1

    def run(self, f, jac, y0, t0, t1, f_params, jac_params):  # required
        #         # this method is called to integrate from t=t0 to t=t1
        #         # with initial condition y0. f and jac are user-supplied functions
        #         # that define the problem. f_params,jac_params are additional
        #         # arguments
        #         # to these functions.
        #         <calculate y1>
        #         if <calculation was unsuccessful>:
        #             self.success = 0

        self.y = y0.copy()
        K1 = self.dt*f(t0,self.y)
        K2 = self.dt*f(t0 + 0.5 * self.dt, self.y + 0.5 * K1)
        K3 = self.dt*f(t0 + 0.5 * self.dt, self.y + 0.5 * K2)
        K4 = self.dt*f(t0 + self.dt, self.y + K3)

        self.y += (1 / 6.0) * (K1 + 2 * K2 + 2 * K3 + K4)
        return self.y, t1


if Rk4Integrator not in IntegratorBase.integrator_classes:
    IntegratorBase.integrator_classes.append(Rk4Integrator)
