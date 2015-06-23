#! /usr/bin/env python
"""
VoNDA - Visualization of Network Data (http://vonda.sourceforge.net)

Copyright (C) 2013-2015 T.R Maarlveld all rights reserved.

Timo R. Maarleveld (tmd200@users.sourceforge.net)
Centrum Wiskunde & informatica, Life Sciences, Amsterdam

Permission to use, modify, and distribute this software is given under the
terms of the VoNDA (BSD style) license. 

NO WARRANTY IS EXPRESSED OR IMPLIED.  USE AT YOUR OWN RISK.
"""
from __future__ import division, print_function, absolute_import


__doc__ =   """        
            VoNDA (Visualization of Network DAta) allows for interactive visualization of heterogeneous data
            """

__version__ = '0.6.0'
import os,shutil,sys

try:
    from numpy.distutils.core import setup
except Exception as ex:
    print(ex)
    os.sys.exit(-1)
    
def InitiateSVGfiles(directory):
    """
    Build SVG files for visualization
    
    Input:
     - *directory* (string)
    """   
    import vonda.networks.metabolic_map_synechocystis as metabolic_map_synechocystis
    import vonda.networks.core_model as core_model
    D_models = {}
    D_models['Synechocystis'] = metabolic_map_synechocystis.SVG
    D_models['core_model'] = core_model.SVG
    prefix = '.svg'
    model_names = list(D_models)
    model_dir = os.listdir(directory)
    for mod_name in model_names:                
        if (mod_name + prefix) not in model_dir: 
            print("Model {0:s} copied to {1:s}".format(mod_name + prefix,directory))
            file_in = open(os.path.join(directory,mod_name + prefix),'w')            
            file_in.write(D_models[mod_name])
            file_in.close()
    del metabolic_map_synechocystis
    
    
def InitiateModelfiles(directory):
    """
    Build Model files

    
    Input:
     - *directory* (string)
    """   
    import vonda.models.core_model_sbml3 as core_model
    import vonda.models.iTM686_sbml3 as iTM686
    import vonda.models.Ecoli_Carlson2003_sbml3 as Ecoli_Carlson2003
    D_models = {}
    D_models['iTM686_sbml3'] = iTM686
    D_models['core_model_sbml3'] = core_model
    D_models['Ecoli_Carlson2003_sbml3'] = Ecoli_Carlson2003
    prefix = '.xml'
    model_names = list(D_models)
    model_dir = os.listdir(directory)    
    for mod_name in model_names:                      
        if (mod_name + prefix) not in model_dir: 
            print("Model {0:s} copied to {1:s}".format(mod_name + prefix,directory))
            file_in = open(os.path.join(directory,mod_name + prefix),'w')            
            file_in.write(D_models[mod_name].data)
            file_in.close()  
    

def InitiateDatafiles(directory):
    """
    Build data files for visualization
    
    Input:
     - *directory* (string)
    """   
    import vonda.data_examples.CyanoEXpress_cluster as CyanoEXpress_cluster    
    import vonda.data_examples.iTM686_FBA as iTM686_FBA
    import vonda.data_examples.iTM686_GPRs as iTM686_GPRs
    import vonda.data_examples.iTM686_blocked_reactions_LLS as iTM686_blocked_reactions_LLS
    import vonda.data_examples.reaction_associations_example as reaction_associations_example
    import vonda.data_examples.associations_example as associations_example
    D_data_examples = {}
    D_data_examples['CyanoEXpress_cluster'] = CyanoEXpress_cluster   
    D_data_examples['iTM686_FBA'] = iTM686_FBA
    D_data_examples['iTM686_GPRs'] = iTM686_GPRs
    D_data_examples['iTM686_blocked_reactions_LLS'] = iTM686_blocked_reactions_LLS
    D_data_examples['reaction_associations_example'] = reaction_associations_example
    D_data_examples['associations_example'] = associations_example    
    
    prefix = '.txt'    
    data_dir = os.listdir(directory)
    for data_file in sorted(D_data_examples):               
        if (data_file + prefix) not in data_dir:
            print("Data file {0:s} copied to {1:s}".format(data_file+prefix,directory))
            file = open(os.path.join(directory,data_file+prefix),'w')            
            file.write(D_data_examples[data_file].data)
            file.close()
    del CyanoEXpress_cluster
    
output_dir = None
model_dir = None
map_dir = None
if os.sys.platform != 'win32':
    if not os.path.exists(os.path.join(os.path.expanduser('~'),'Vonda')):
        os.makedirs(os.path.join(os.path.expanduser('~'),'Vonda'))
    if not os.path.exists(os.path.join(os.path.expanduser('~'),'Vonda', 'interactive_map')):
        os.makedirs(os.path.join(os.path.expanduser('~'),'Vonda','interactive_map')) 
    if not os.path.exists(os.path.join(os.path.expanduser('~'),'Vonda', 'data_examples')):
        os.makedirs(os.path.join(os.path.expanduser('~'),'Vonda','data_examples')) 
    if not os.path.exists(os.path.join(os.path.expanduser('~'),'Vonda', 'models')):
        os.makedirs(os.path.join(os.path.expanduser('~'),'Vonda','models'))     
    output_dir = os.path.join(os.path.expanduser('~'),'Vonda')
    map_dir = os.path.join(os.path.expanduser('~'),'Vonda','interactive_map')
    data_dir = os.path.join(os.path.expanduser('~'),'Vonda','data_examples')
    model_dir = os.path.join(os.path.expanduser('~'),'Vonda','models')
    InitiateSVGfiles(map_dir)
    InitiateDatafiles(data_dir)
    InitiateModelfiles(model_dir)
   
else:
    if not os.path.exists(os.path.join(os.getenv('HOMEDRIVE')+os.path.sep,'Vonda')):
        os.makedirs(os.path.join(os.getenv('HOMEDRIVE')+os.path.sep,'Vonda'))
    if not os.path.exists(os.path.join(os.getenv('HOMEDRIVE')+os.path.sep,'Vonda','interactive_map')):
        os.makedirs(os.path.join(os.getenv('HOMEDRIVE')+os.path.sep,'Vonda','interactive_map'))
    if not os.path.exists(os.path.join(os.getenv('HOMEDRIVE')+os.path.sep,'Vonda','data_examples')):
        os.makedirs(os.path.join(os.getenv('HOMEDRIVE')+os.path.sep,'Vonda','data_examples'))
    if not os.path.exists(os.path.join(os.getenv('HOMEDRIVE')+os.path.sep,'Vonda','models')):
        os.makedirs(os.path.join(os.getenv('HOMEDRIVE')+os.path.sep,'Vonda','models'))
    output_dir = os.path.join(os.getenv('HOMEDRIVE')+os.path.sep,'Vonda',)
    map_dir = os.path.join(os.getenv('HOMEDRIVE')+os.path.sep,'Vonda','interactive_map')
    data_dir = os.path.join(os.getenv('HOMEDRIVE')+os.path.sep,'Vonda','data_examples')
    model_dir = os.path.join(os.getenv('HOMEDRIVE')+os.path.sep,'Vonda','models')
    InitiateSVGfiles(map_dir)
    InitiateDatafiles(data_dir)
    InitiateModelfiles(model_dir)
    
from .modules.Map2SVG import PVisualizer
#from modules.Map2SVG import PMaker
#from modules.Maker import Pmaker

print("""
########################################################################
#                                                                      #
#            Welcome to the interactive VoNDA environment              #
#                                                                      #
########################################################################
#  VoNDA: Visualization of Network DAta (2013-2015)                    #
#  http://vonda.sf.net                                                 #
#  Copyright (C) T.R Maarleveld, J. Boele, F.J. Bruggeman, B. Teusink  #
#  Email: tmd200@users.sourceforge.net                                 #
#  Centrum Wiskunde Informatica, Amsterdam, Netherlands                #
#  VU University, Amsterdam, Netherlands                               #
#  VoNDA is distributed under the BSD licence.                         #
########################################################################
""")
print("Version {0}".format(__version__) )
print("Output Directory: {0:s}".format(output_dir) )
print("Map Directory: {0:s}".format(map_dir) )
print("Model Directory: {0:s}".format(model_dir) )
