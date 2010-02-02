#!/usr/bin/python
# =============================================================================
# Standard Python modules
# =============================================================================
import os, sys, string, pdb, copy, time

# =============================================================================
# External Python modules
# =============================================================================
from numpy import linspace, cos, pi, hstack, zeros, ones, sqrt, imag, interp, \
    array, real, reshape, meshgrid, dot, cross, vstack, arctan2, tan

# =============================================================================
# Extension modules
# =============================================================================

# mdo_lab import utility
from mdo_import_helper import *
exec(import_modules('pyGeo'))

# ==============================================================================
# Start of Script
# ==============================================================================

# This script reads a surfaced-based plot3d file as typically
# outputted by aerosurf. It then creates a b-spline surfaces for each
# surface patch.
aircraft = pyGeo.pyGeo('plot3d',file_name='./geo_input/full_aircraft.xyz')
aircraft.calcEdgeConnectivity(1e-6,1e-6)
aircraft.writeEdgeConnectivity('./geo_input/aircraft.con')
aircraft.propagateKnotVectors()
aircraft.writeTecplot('./geo_output/full_aircraft.dat',orig=True)