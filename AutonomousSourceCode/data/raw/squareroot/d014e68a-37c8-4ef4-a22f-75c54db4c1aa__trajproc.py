# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:40:51 2012

@author: esteban
"""
import numpy as np
from scipy.signal import lfilter

def trajVelocity(traj):
    "Compute trajectory velocities"
    data = np.array(traj.pointData)
    return data[1:,:] - data[:-1,:]

def trajEnergy(traj):
    "Compute trajectory energy by taking square of velocity vector length."
    vel = trajVelocity(traj)
    return np.sum(vel**2, 1)
    
def trajSpeed(traj):
    "Compute trajectory speed by taking square root of energy"
    e = trajEnergy(traj)
    return e**.5
    
def smooth(data, alpha):
    return  lfilter([alpha], [1.0, 1.0-alpha], data)