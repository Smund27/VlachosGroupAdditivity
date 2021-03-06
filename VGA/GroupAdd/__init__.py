# 2016. Vlachos Group Geun Ho Gu. University of Delaware.
"""
=============================
Group-additivity computations
=============================

This module is used for using Group additivity method to compute energies

--------
Examples
--------

>>> from VGA.GroupAdd.Library import GroupLibrary
>>> import VGA.ThermoChem
>>> lib = GroupLibrary.Load('benson')
>>> groups = lib.GetDescriptors('CC')
>>> print groups
>>> thermochem = lib.Estimate(groups,'thermochem')
>>> print thermochem.eval_ND_H(298.15)
defaultdict(<type 'int'>, {'C(C)(H)3': 2})
-34.4280812417

"""

from . Library import GroupLibrary
from . Scheme import GroupAdditivityScheme

__all__ = ['GroupLibrary','GroupAdditivityScheme']
