from __future__ import absolute_import
from .advection_1d import advection_1d
from .acoustics_1d_homogeneous import acoustics_1d
from .acoustics_2d_homogeneous import acoustics_2d
from .acoustics_2d_variable import acoustics_2d_interface
from .acoustics_3d_variable import acoustics_3d_interface
from .advection_1d_variable import variable_coefficient_advection
from .advection_2d import advection_2d
from .advection_2d_annulus import advection_annulus
from .burgers_1d import burgers_1d
from .euler_1d import woodward_colella_blast
from .euler_1d import shocktube
from .euler_2d import shock_bubble_interaction
from .kpp import kpp
from .psystem_2d import psystem_2d
from .shallow_1d import dam_break
from .shallow_1d import sill
from .shallow_2d import radial_dam_break
from .shallow_sphere import Rossby_wave
from .stegoton_1d import stegoton
from .traffic import traffic
