"""
Operations
==========

This script contains a class with functions to operate on SVG files

Written by TR Maarleveld, Amsterdam, The Netherlands
E-mail: t.r.maarleveld@cwi.nl
Last Change: Augustus 28, 2014
"""

from __future__ import division, print_function, absolute_import

import re

class PerformOperations():
    def __init__(self,ModifySVG):
        self.ModifySVG = ModifySVG
        self.s_id = None
        self.r_id = None
        self.IsDoMapping = False

    def findSpecies(self,species_suffix):
        """ Search for species identifier in SVG line """
        self.IsDoMapping = False           
        prefix = 'id="'
        metabolite_regex = "{0}.+?".format(species_suffix)
        suffix = '"'
        m = re.search('{0}{1}{2}'.format(prefix,metabolite_regex,suffix),self.ModifySVG.svg_line) # use REGEX for finding species identifiers        
        if m:
            self.s_id = m.group(0)[len(prefix):-len(suffix)].strip()           
            self.IsDoMapping = True
        
    def findReaction(self,reaction_suffix):
        """
        Search for the reaction ID in the SVG file
        
        id="R_PPC" extract stuff between "..."   with REGEX
        """        
        self.IsDoMapping = False
        prefix = 'id="'
        reaction_regex = "{0}.+?".format(reaction_suffix        )
        suffix = '"'       
        m = re.search('{0}{1}{2}'.format(prefix,reaction_regex,suffix),self.ModifySVG.svg_line)  # use REGEX for finding reaction identifiers
        if m:
            self.r_id = m.group(0)[len(prefix):-len(suffix)].strip()            
            self.IsDoMapping = True              

