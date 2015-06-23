"""
MAP2SVG
=======

This script contains a class with functions that can map fluxes of for instance a FBA simulation on a SVG file.

Written by TR Maarleveld, Amsterdam, The Netherlands
E-mail: t.r.maarleveld@cwi.nl
Last Change: Augustus 28, 2014
"""

from __future__ import division, print_function, absolute_import

import copy,sys,re,os,operator,numpy as np
file_dir = os.path.dirname(__file__)

from .ModifySVG import ModifySVGfile
from .ModifyData import ModifyData
from .Operations import PerformOperations

class PVisualizer:
    """
    This class allows for the visualization of heterogenous biological data, such as (computational) flux, metabolics, or transcriptomics data.        
   
    Input:
     - *SVG_file* (string) [default = 'Synechocystis.svg']
     - *SVG_dir* (string) [default = None]   
     - *colormap* (string) [default= 'rainbow.svg']     
     - *start_marker* (string) [default = 'se_marker_start_svg_1']
     - *end_marker* (string) [default = 'se_marker_end_svg_1']
     - *reaction_suffix* (string) [default = 'R_']
     - *species_suffix* (string) [default = 'M_']
    """
    def __init__(self, SVG_file = 'Synechocystis.svg',SVG_dir = None,colormap = 'rainbow.svg',start_marker='se_marker_start_svg_1',end_marker='se_marker_end_svg_1',reaction_suffix = 'R_',species_suffix='M_',IsPrintStatements = True):
        if os.sys.platform != 'win32':
            self.output_dir = os.path.join(os.path.expanduser('~'),'Vonda',)
            self.data_dir = os.path.join(os.path.expanduser('~'),'Vonda','data_examples')
            if SVG_dir == None:
                self.SVG_dir = os.path.join(os.path.expanduser('~'),'Vonda','interactive_map')                
            else:
               self.SVG_dir = SVG_dir
        else:
            self.output_dir = os.path.join(os.getenv('HOMEDRIVE') + os.path.sep,'Vonda',)
            self.data_dir = os.path.join(os.getenv('HOMEDRIVE') + os.path.sep,'Vonda','data_examples')            
            if SVG_dir == None:
                self.SVG_dir = os.path.join(os.getenv('HOMEDRIVE') + os.path.sep,'Vonda','interactive_map')
            else:
               self.SVG_dir = SVG_dir
               
        self.SVG_file = SVG_file        
        self.L_species_in_svg = None
        self.L_reactions_in_svg = None
        self.D_expression_data = None  
        self.colormap = colormap  
        self.start_marker = start_marker
        self.end_marker = end_marker        
        self.reaction_suffix = reaction_suffix
        self.species_suffix = species_suffix
        self.parseSVGfile()
        if IsPrintStatements:
            print("Info: The reaction suffix is {0}. Make sure this is correct. If not modify the reaction suffix via (1) setReactionSuffix() or (2) by re-using this functionality with as additonal argument reaction_suffix".format(self.reaction_suffix))
            print("Info: The species suffix is {0}. Make sure this is correct. If not modify the species suffix via (1) setSpeciesSuffix() or (2) by re-using this functionality with as additonal argument species_suffix".format(self.species_suffix))
    
    def setReactionSuffix(r_suffix):
        self.reaction_suffix = str(reaction_suffix)

    def setSpeciesSuffix(s_suffix):
        self.species_suffix = str(species_suffix)
    
    def parseSVGfile(self,colorbar = None):  
        """ Parses SVG files and initiates different classes for modification of the SVG file """
        try:  
            file_in = open(os.path.join(self.SVG_dir,self.SVG_file), 'r')    
        except Exception as er:
            print(er)
            sys.exit()
                        
        L_metabolic_map = [line for line in file_in]  # parse metabolic map to list
        if not colorbar:
            self.ModifySVG = ModifySVGfile(L_metabolic_map,self.colormap,self.start_marker,self.end_marker) 
        else:
            try:
                self.ModifySVG = ModifySVGfile(L_metabolic_map,colorbar,self.start_marker,self.end_marker) 
            except:
                self.ModifySVG = ModifySVGfile(L_metabolic_map,self.colormap,self.start_marker,self.end_marker) 
        self.ModifyData = ModifyData()
        self.PerformOperations = PerformOperations(self.ModifySVG)
        self.output_filename = None

    def doMapReactions(self,D_reactions,scaling_mode ='log',IsAbsoluteValues = True,maxValue=None,minValue=None,objective_reaction=None,objective=None,D_yields = None,filename_out = None,reaction_suffix=None,valuesRange=None,IsAddReactionValue=True,old_width = 1.0,new_width=2.0):
        """        
        doMapReactions(self,D_reactions,scaling_mode ='log',IsAbsoluteValues = True,maxValue=None,minValue=None,objective_reaction=None,objective=None,D_yields = None,filename_out = None,reaction_suffix=None,valuesRange=None,IsAddReactionValue=True,old_width = 1.0,new_width=2.0)
        
        Map reaction values (e.g. fluxes) on the metabolic map for a given colorbar.       
         
        Input:
         - *D_reactions*: (dictionary)         
         - *scaling_mode*: (string)  [default = 'log']
         - *IsAbsoluteValues*: (boolean) [default = True] 
         - *maxValue*: maximum abs reaction value (float) [default = None]
         - *minValue*: minimum abs reaction value (float) [default = None]
         - *objective_reaction* (string) [default = None]
         - *objective* (string)     [default = None]         
         - *filename_out* (string)  [default = None]
         - *reaction_suffix* (string) [default = 'R_']
         - *valuesRange* (list) [default = None]    
         - *IsAddReactionValue* (boolean) [default = True]    
         - *old_width* (float) [default = 1.0]
         - *new_width* (float) [default = 2.0]
         
        Options: 
         - valuesRange = ['outside',-1,1]
         - valuesRange = ['between',-1,1] 
         - valuesRange = ['higher',1]
         - valuesRange = ['lower',1]
        """
        if reaction_suffix == None:
            reaction_suffix = self.reaction_suffix
        self.parseSVGfile()
        style_element = 'style="fill:none;stroke:#000000' # hard coded in current version              
        D_r_ids = copy.deepcopy(D_reactions)        
        if maxValue == None and minValue == None:
            (maxValue, minValue) = extractAbsBoundaryValues(D_r_ids)
                
        ### Modify values to visualize ###    
        if valuesRange == None:
            pass
        elif (type(valuesRange) == list) and (len(valuesRange) == 3):
            if valuesRange[0].lower() == 'outside':
                D_r_ids = self.ModifyData.ValuesOutside(valuesRange[1],valuesRange[2],D_r_ids,IsAbsoluteValues)
            elif valuesRange[0].lower() == 'between':
                D_r_ids = self.ModifyData.ValuesBetween(valuesRange[1],valuesRange[2],D_r_ids,IsAbsoluteValues)
        elif (type(valuesRange) == list) and (len(valuesRange) == 2):
            if valuesRange[0].lower() == 'higher':                
                D_r_ids = self.ModifyData.ValuesHigherThan(valuesRange[1],D_r_ids,IsAbsoluteValues)
            elif valuesRange[0].lower() == 'lower':
                D_r_ids = self.ModifyData.ValuesLowerThan(valuesRange[1],D_r_ids,IsAbsoluteValues)        
                
        L_input_r_ids = list(D_r_ids) # reaction identifiers specified by the user    
        self.ModifySVG.Arr_data_scale = self.ModifySVG.createDataScale(minValue,maxValue,scaling_mode)
        
        ### open file path for visualization ###
        if filename_out == None:
            file_path = os.path.join(self.output_dir, "{0:s}_reactions.svg".format(self.SVG_file[:-4]) )
            self.output_filename = "{0:s}_reactions.svg".format(self.SVG_file[:-4])
        else:
            file_path = os.path.join(self.output_dir,"{0:s}.svg".format(filename_out) )
            self.output_filename = "{0:s}.svg".format(filename_out)
        file_out = open(file_path, 'w')
       
        yield_index = 0
        N_maximum_yields = 5
        for self.ModifySVG.svg_line in self.ModifySVG.L_metabolic_map:           
            if ('id="{0}'.format(reaction_suffix)) in self.ModifySVG.svg_line:
                self.PerformOperations.findReaction(reaction_suffix)
            elif (style_element in self.ModifySVG.svg_line) and (self.PerformOperations.IsDoMapping == True) and (self.PerformOperations.r_id in L_input_r_ids):
                r_value = D_r_ids[self.PerformOperations.r_id]
                self.ModifySVG.dashedLine2solidLine() 
                if r_value:
                    self.ModifySVG.changeLineWidth(r_value,old_width,new_width)
                else:
                    self.ModifySVG.changeLineWidth(r_value,old_width,old_width)                
                self.ModifySVG.colorReactions(r_value)
                if IsAbsoluteValues or (not r_value):
                    self.ModifySVG.adaptArrowDirection(r_value)
                elif not IsAbsoluteValues or (not r_value):
                    self.ModifySVG.adaptArrowDirection(abs(r_value))             # show negative numbers, so make all arrows in the default direction
                self.PerformOperations.IsDoMapping = False                
            elif ('ReactionValue' in self.ModifySVG.svg_line) or "<title>{0}".format(reaction_suffix):
                self.ModifySVG.addReactionValue(D_r_ids,IsAbsoluteValues,IsAddReactionValue)                
            if ('<!--Objective' in self.ModifySVG.svg_line):    
                try:
                    objective_value = D_r_ids[objective_reaction]
                    self.ModifySVG.svg_line = self.ModifySVG.svg_line.replace('<!--Objective-->', 'Objective: {0:s} {1:s} = {2:0.1e}'.format (objective,objective_reaction,objective_value))
                except KeyError: 
                    if type(objective) == str and type(objective_reaction) == str: # if objective is given, but no value is available
                        self.ModifySVG.svg_line = self.ModifySVG.svg_line.replace('<!--Objective-->', 'Objective: {0:s} {1:s}'.format(objective,objective_reaction))
            
            elif ('<!--Yield' in self.ModifySVG.svg_line) and (type(D_yields) == dict):      
                i=0
                yield_description = sorted(D_yields)[0]
                try:
                    L_locations = re.findall('\d+', self.ModifySVG.svg_line) # get x="...", y="...", and font=size="..."
                    r_yield = D_yields[yield_description]      
                    yield_value = D_r_ids[objective_reaction]/abs(D_r_ids[r_yield])                   
                    self.ModifySVG.svg_line = self.ModifySVG.svg_line.replace('<!--Yield-->', 'Yield ({0:s}): {1:0.1e}'.format(yield_description,yield_value)) 
                    i+=1
                except KeyError as er:                   
                    print(er)
                except ZeroDivisionError as er:                   
                    print(er,r_yield)
                                                   
                for yield_description in sorted(D_yields)[1:]:  
                    if i==N_maximum_yields: # up to 5 (existing) yields fit in the visualization map
                       break                
                    try:
                        r_yield = D_yields[yield_description] 
                        yield_value = D_r_ids[objective_reaction]/abs(D_r_ids[r_yield])                           
                        line_to_add = '<text x="{0}" y="{1}" font-size="{2}" font-family = "times" style="fill:black;font-weight:bold">Yield ({3:s}): {4:0.1e}</text>'.format (L_locations[0],int(L_locations[1]) +int(L_locations[-1])*i,L_locations[-1],yield_description,yield_value)                       
                        self.ModifySVG.svg_line += line_to_add
                        i+=1
                    except KeyError as er:
                        print(er)
                    except ZeroDivisionError as er:
                        print(er,r_yield)
            if '</svg>' in self.ModifySVG.svg_line:            
                self.ModifySVG.addColorbar()  
            file_out.write(self.ModifySVG.svg_line)
        file_out.close()    
        print("Visualization results can be found at {0:s}".format(file_path) )
        
    def doMapReactionGroups(self,D_modules,filename_out = None,reaction_suffix=None,old_width = 1.0,new_width=2.0,L_module_colors = ['#0000FF','#00CC00','#FF0033','#FF00CC','#6600FF','#FFA500','#FFFF00','#000000','#00CCFF','#FF6666','#FF99CC','#CC6600','#003300','#CCFFFF','#9900FF','#CC6633']):
        """           
        Input:
         - *D_modules* (dict)
         - *filename_out* (string) [default = None]   
         - *reaction_suffix* (string) [default = "R_"]
         - *old_width* (float) [default = 1.0]
         - *new_width* (float) [default = 2.0]
         - *L_module_colors* (list) [default = ['#0000FF','#00CC00','#FF0033','#FF00CC','#6600FF','#FFA500','#FFFF00','#000000','#00CCFF','#FF6666','#FF99CC','#CC6600','#003300','#CCFFFF','#9900FF','#CC6633']]
        """
        if reaction_suffix == None:
            reaction_suffix = self.reaction_suffix
        style_element = 'style="fill:none;stroke:#000000' # hard coded in current version 
        L_modules = list(D_modules.values())
        L_input_r_ids = [item for sublist in L_modules for item in sublist]
        
        self.parseSVGfile()
        if filename_out == None:
            file_path = os.path.join(self.output_dir, "{0:s}_reaction_groups.svg".format(self.SVG_file[:-4]) )
            self.output_filename = "{0:s}_reaction_groups.svg".format(self.SVG_file[:-4])
        else:
            file_path = os.path.join(self.output_dir,"{0:s}.svg".format(filename_out) )
            self.output_filename = "{0:s}.svg".format(filename_out)
        file_out = open(file_path, 'w')     
           
        for self.ModifySVG.svg_line in self.ModifySVG.L_metabolic_map:
            if ('id="{0}'.format(reaction_suffix)) in self.ModifySVG.svg_line:
                self.PerformOperations.findReaction(reaction_suffix)
            elif (style_element in self.ModifySVG.svg_line) and (self.PerformOperations.IsDoMapping == True) and (self.PerformOperations.r_id in L_input_r_ids):                
                N_modules = len(L_modules)
                for i in range(N_modules):
                    if self.PerformOperations.r_id in L_modules[i]:                                                
                        self.ModifySVG.svg_line = self.ModifySVG.svg_line.replace('stroke:#000000', 'stroke:{0}'.format(L_module_colors[i]) )
                        self.ModifySVG.dashedLine2solidLine()
                        self.ModifySVG.changeLineWidth(1,old_width,new_width) # should give it some value (except 0) to modifty the line width
                        break
                    
            file_out.write(self.ModifySVG.svg_line)
        file_out.close()      
        print("Mapping is done to {0:s}".format(file_path) )

    def doMapSquares(self,D_squares,colorbar = 'cyanyellow_white.svg',maxValue=None,minValue=None,filename_out = None,kegg_prefix = 'syn',reaction_suffix=None,valuesRange = None,IsAbsoluteValues=False):
        """
        *** Map data to reaction squares (genes) ***
        
        Example of input format:
        ------------------------
        ['R_DXPRIi': [['sll0019', -0.243417846]],
        'R_G3PAT181': [['sll1973', 0.308248907], ['sll1510', -0.932184797]], 
        'R_G3PAT180': [['sll1973', 0.308248907], ['sll1510', -0.932184797]]    
        ]
        
        User can user different colorbars: 'cyanyellow_white','yellowcyan', 'yellowblue','and 'redgreen'        
         
        Input:
         - *D_squares*: (dictionary)
         - *colorbar* (string) [default = 'yellowcyan']
         - *maxValue*: (float) [default = None]
         - *minValue*: (float) [default = None]    
         - *filename_out* (string)  [default = None]
         - *kegg_prefix* (string) [default = 'syn']
         - *reaction_suffix* (string) [default = "R_"]
         - *valuesRange* (list) [default = None]
         
        Options: 
         valuesRange = ['outside',-1,1]
         valuesRange = ['between',-1,1]         
        """
        if reaction_suffix == None:
            reaction_suffix = self.reaction_suffix        
        style_element = 'style="fill:white;stroke:black;' # hard coded                         
        self.parseSVGfile(colorbar)        
        D_square_indices = {}
        D_r_ids = copy.copy(D_squares)                
        if maxValue == None and minValue == None:            
            L_values_nested = list(D_r_ids.values())
            L_values = [item[-1] for sublist in L_values_nested for item in sublist]
            maxValue = max(L_values)
            minValue = min(L_values) 
        colorbarBoundary = max(abs(maxValue),abs(minValue)) # symmetric colorbar
        self.ModifySVG.Arr_data_scale = self.ModifySVG.createDataScale(-colorbarBoundary,colorbarBoundary,mode='normal') # max = - min (symmetric colorbar)
        
        ### Modify values to visualize ###
        if valuesRange == None:
            pass
        elif (type(valuesRange) == list) and (len(valuesRange) == 3):
            if valuesRange[0].lower() == 'outside':
                D_r_ids = self.ModifyData.ValuesOutside(valuesRange[1],valuesRange[2],D_r_ids,IsAbsoluteValues)
            elif valuesRange[0].lower() == 'between':
                D_r_ids = self.ModifyData.ValuesBetween(valuesRange[1],valuesRange[2],D_r_ids,IsAbsoluteValues)
        elif (type(valuesRange) == list) and (len(valuesRange) == 2):
            if valuesRange[0].lower() == 'higher':                
                D_r_ids = self.ModifyData.ValuesHigherThan(valuesRange[1],D_r_ids,IsAbsoluteValues)
            elif valuesRange[0].lower() == 'lower':
                D_r_ids = self.ModifyData.ValuesLowerThan(valuesRange[1],D_r_ids,IsAbsoluteValues)                
        
        L_input_r_ids = list(D_r_ids) # reaction identifiers specified by the user
        
        if filename_out == None:
            file_path = os.path.join(self.output_dir, "{0:s}_squares.svg".format(self.SVG_file[:-4]))
            self.output_filename = "{0:s}_squares.svg".format(self.SVG_file[:-4])
        else:
            file_path = os.path.join(self.output_dir,"{0:s}.svg".format(filename_out) )
            self.output_filename = "{0:s}.svg".format(filename_out)
        file_out = open(file_path, 'w')
        
        IscolormapSquares = False
        IsLink = False
        for self.ModifySVG.svg_line in self.ModifySVG.L_metabolic_map:
            if '<a' in self.ModifySVG.svg_line.replace(" ",""):  
                IsLink = True
            elif '</a>' in self.ModifySVG.svg_line.replace(" ",""):  
                IsLink = False
            if ('id="{0}'.format(reaction_suffix)) in self.ModifySVG.svg_line:                
                self.PerformOperations.findReaction(reaction_suffix)               
            if (style_element in self.ModifySVG.svg_line) and (self.PerformOperations.IsDoMapping == True)  and (self.PerformOperations.r_id in L_input_r_ids):   
                r_id = self.PerformOperations.r_id                
                if not r_id in D_square_indices:                                               # first square
                    D_square_indices[r_id] = {}
                    D_square_indices[r_id]['index'] = 0
                    ### order data for squares ###           
                    L_values_ordered = []
                    for vect in D_r_ids[r_id]:                    
                        L_values_ordered.append(vect+[abs(vect[-1])])                          # add absolute value to vect which will be used for abs. sorting                        
                    L_values_ordered.sort(key=operator.itemgetter(2),reverse=True)             # sort on absolute value                    
                    D_square_indices[r_id]['values'] = L_values_ordered                   
                else: 
                    D_square_indices[r_id]['index'] += 1                                       # second or third square               
                if D_square_indices[r_id]['index'] < len(D_square_indices[r_id]['values']): 
                    index = D_square_indices[r_id]['index']
                    gene_id = D_square_indices[r_id]['values'][index][0]
                    value = D_square_indices[r_id]['values'][index][1]
                    ### Replace link to reaction identifier to gene identifier
                    if IsLink:
                        self.ModifySVG.svg_line = '    </a>\n    <a xlink:href="http://www.genome.jp/dbget-bin/www_bget?{0}:{1:s}" target="_blank">\n{2}'.format(kegg_prefix,gene_id,self.ModifySVG.svg_line)                    
                    else:                     
                        self.ModifySVG.svg_line = '<a xlink:href="http://www.genome.jp/dbget-bin/www_bget?{0}:{1}" target="_blank">\n{2}</a>'.format (kegg_prefix,gene_id,self.ModifySVG.svg_line)  
                    self.ModifySVG.colorSquares(value)
            if '</svg>' in self.ModifySVG.svg_line:            
                self.ModifySVG.addColorbar()  
            file_out.write(self.ModifySVG.svg_line)        
        file_out.close() 
        print("Mapping results can be found at {0:s}".format(file_path) )
        
    def doMapSpecies(self,D_species,scaling_mode ='log',maxValue=None,minValue=None,objective_reaction=None,objective=None,filename_out = None,species_suffix=None,valuesRange=None):
        """
        *** Species ***
        Map all the metabolite values on the metabolic map for a given heat map.       
         
        Input:
         - *D_species*: (dict)         
         - *scaling_mode* (string)  [default = 'log']
         - *maxValue*: maximum abs metabolite value (float) [default = None]
         - *minValue*: minimum abs metabolite value (float) [default = None]
         - *objective_reaction* (string) [default = None]
         - *objective* (string)     [default = None]         
         - *filename_out* (string)  [default = None]
        """ 
        if species_suffix == None:
            species_suffix = self.species_suffix             
        self.parseSVGfile()
        L_input_s_ids = list(D_species)       
        D_s_ids = copy.deepcopy(D_species)
        
        if maxValue == None and minValue == None:
            (maxValue, minValue) = extractAbsBoundaryValues(D_species) 
            
        ### Modify values to visualize ###
        if valuesRange == None:
            pass
        elif (type(valuesRange) == list) and (len(valuesRange) == 3):
            if valuesRange[0].lower() == 'outside':
                D_s_ids = self.ModifyData.ValuesOutside(valuesRange[1],valuesRange[2],D_s_ids,IsAbsoluteValues)
            elif valuesRange[0].lower() == 'between':
                D_s_ids = self.ModifyData.ValuesBetween(valuesRange[1],valuesRange[2],D_s_ids,IsAbsoluteValues)
        elif (type(valuesRange) == list) and (len(valuesRange) == 2):
            if valuesRange[0].lower() == 'higher':                
                D_s_ids = self.ModifyData.ValuesHigherThan(valuesRange[1],D_s_ids,IsAbsoluteValues)
            elif valuesRange[0].lower() == 'lower':
                D_s_ids = self.ModifyData.ValuesLowerThan(valuesRange[1],D_s_ids,IsAbsoluteValues)
        
        self.ModifySVG.Arr_data_scale = self.ModifySVG.createDataScale(minValue,maxValue,scaling_mode)
        
        if filename_out == None:
            file_path = os.path.join(self.output_dir, "{0:s}_species.svg".format(self.SVG_file[:-4]) )
            self.output_filename = "{0:s}_species.svg".format(self.SVG_file[:-4])
        else:
            file_path = os.path.join(self.output_dir,"{0:s}.svg".format(filename_out) )
            self.output_filename = "{0:s}.svg".format(filename_out)
        file_out = open(file_path, 'w')               
  
        for self.ModifySVG.svg_line in self.ModifySVG.L_metabolic_map:
            if ('<text id="{0}'.format(species_suffix)) in self.ModifySVG.svg_line:
                self.PerformOperations.findSpecies(species_suffix)               
                if (self.PerformOperations.IsDoMapping == True) and (self.PerformOperations.s_id in L_input_s_ids):
                    s_value = D_species[self.PerformOperations.s_id]
                    self.ModifySVG.colorSpecies(s_value)
                    self.PerformOperations.IsDoMapping = False
            if ('<title>{0}'.format(species_suffix)) in self.ModifySVG.svg_line:
                self.ModifySVG.addSpeciesValue(D_s_ids)                    
            elif "</svg>" in self.ModifySVG.svg_line:
                self.ModifySVG.addColorbar()    
            file_out.write(self.ModifySVG.svg_line)
        file_out.close()
        print("Mapping results can be found at {0:s}".format(file_path) )
        
    def doMapSpeciesGroups(self,D_modules,species_suffix=None,filename_out = None,L_module_colors = ['#0000FF','#00CC00','#FF0033','#FF00CC','#6600FF','#FFA500','#FFFF00','#000000','#00CCFF','#FF6666','#FF99CC','#CC6600','#003300','#CCFFFF','#9900FF','#CC6633']):
        """       
        doMapSpeciesGroups(D_modules,species_suffix=None,filename_out = None,L_module_colors = ['#0000FF','#00CC00','#FF0033','#FF00CC','#6600FF','#FFA500','#FFFF00','#000000','#00CCFF','#FF6666','#FF99CC','#CC6600','#003300','#CCFFFF','#9900FF','#CC6633'])
                            
        Input:
         - *D_modules* (dict)
         - *species_suffix* (string) [default = 'M_']
         - *filename_out* (string) [default = None]   
         - *L_module_colors* (list) [default = ['#0000FF','#00CC00','#FF0033','#FF00CC','#6600FF','#FFA500','#FFFF00','#000000','#00CCFF','#FF6666','#FF99CC','#CC6600','#003300','#CCFFFF','#9900FF','#CC6633']]
        """
        if species_suffix == None:
            species_suffix = self.species_suffix     
        L_modules = list(D_modules.values())
        L_input_s_ids = [item for sublist in L_modules for item in sublist]
        self.parseSVGfile()
        if filename_out == None:
            file_path = os.path.join(self.output_dir, "{0:s}_species_groups.svg".format(self.SVG_file[:-4]) )
            self.output_filename = "{0:s}_species_groups.svg".format(self.SVG_file[:-4])
        else:
            file_path = os.path.join(self.output_dir,"{0:s}.svg".format(filename_out))
            self.output_filename = "{0:s}.svg".format(filename_out)
        
        file_out = open(file_path,'w')
        for self.ModifySVG.svg_line in self.ModifySVG.L_metabolic_map:
            if ('<text id="{0}'.format(species_suffix)) in self.ModifySVG.svg_line:
                self.PerformOperations.findSpecies(species_suffix)
                if (self.PerformOperations.IsDoMapping == True) and (self.PerformOperations.s_id in L_input_s_ids):              
                    N_modules = len(L_modules)
                    for i in range(N_modules):
                        if self.PerformOperations.s_id in L_modules[i]:                            
                            self.ModifySVG.colorSpeciesGroups(L_module_colors[i])
                            break
            file_out.write(self.ModifySVG.svg_line)
        file_out.close()
        print("Mapping is done to {0:s}".format(file_path) )
        
    def getSVGspecies(self,species_suffix=None):
        """
        Get metabolite identifiers of all species (species) in the SVG map.
        
        Metabolite identifiers are written to L_species_in_svg

        Input:
         - *species_suffix* (string) [default = "M_"]
        """
        if species_suffix == None:
            species_suffix = self.species_suffix     
        self.L_species_in_svg = []
        for svg_line in self.ModifySVG.L_metabolic_map:
            if ('<text id="{0}'.format(species_suffix)) in svg_line:
                prefix = 'id="'
                species_regex = "{0}.+?".format(species_suffix)
                suffix = '"'       
                s_id = re.findall('{0:s}{1:s}{{2:s}'.format(prefix,species_regex,suffix),svg_line)[0][len(prefix):-len(suffix)].strip()  
                if s_id != [] and s_id not in self.L_species_in_svg:
                    self.L_species_in_svg.append(s_id)
    
    def getSVGreactions(self,reaction_suffix = None):
        """
        Get reaction identifiers of all reactions in the SVG map.
        
        Reaction identifiers are written to L_reactions_in_svg.
        
        Input:
         - *reaction_suffix* (string) [default = "R_"]
        """
        if reaction_suffix == None:
            reaction_suffix = self.reaction_suffix  
        self.L_reactions_in_svg = []
        for svg_line in self.ModifySVG.L_metabolic_map:
            if ('id="{0}'.format(reaction_suffix)) in svg_line:
                prefix = 'id="'
                reaction_regex = "{0}.+?".format(reaction_suffix)
                suffix = '"'    
                r_id = re.findall('{0:s}{1:s}{2:s}'.format(prefix,reaction_regex,suffix),svg_line)[0][len(prefix):-len(suffix)].strip()  
                if r_id != [] and r_id not in self.L_reactions_in_svg:
                    self.L_reactions_in_svg.append(r_id)    
                    
    def importKeyValueData(self,filename_in,file_dir = None,IsHeader = True,delimiter='\t'):
        """
        Imports key-value pair data from a text file. Keys can be 1) reaction identifiers or 2) metabolite identifiers and values can be for instance fluxes, reduced costs, concentrations.
        
        Example (tab delimited):
        ------------------------
        ID	FluxValue
        R_UREA	0.0
        R_USHD	0.002424
        R_PFK	0.05
        
        Input:
         - *filename_in* (string)
         - *file_dir* (string)  [default = None]
         - *IsHeader* (boolean) [default = True]
         - *delimiter* (string) [default = '\t']
        """
        D_parsed_data = {}
        try:
            if file_dir == None:
                file_in = open(os.path.join(self.data_dir,filename_in),'r')
            else:                  
                file_in = open(os.path.join(file_dir,filename_in),'r')                
            IsFileParsed = True
        except :           
            print("Error: file {0:s} does not exist in {1:s}".format(filename_in,file_dir))
            IsFileParsed = False
        if IsFileParsed:
            for line in file_in:
                if IsHeader:
                    IsHeader = False                
                else:
                    line = line.rstrip()                                        
                    sline = line.split(delimiter) 
                    identifier = sline[0].strip()                   
                    try:              
                        value = float(sline[1])
                    except Exception as er:
                        print(er)
                    if identifier not in D_parsed_data:
                        D_parsed_data[identifier] = value
                    else:
                        print("Warning: {0:s} is detected multiple times. {0:s} is neglected.".format(group_identifier))     
            return D_parsed_data  
        
    def importKeyMembersData(self,filename_in,file_dir = None,IsHeader = False,delimiter='\t'): 
        """
        Imports key-values pair data from a text file. Keys are group identifiers and values are group members
        
        Example (tab delimited):
        ------------------------
        Exchange	R_EX_h2o_e	R_EX_o2_e	R_EX_co2_e
        Glycolysis	R_PGK	R_PGN	R_ENO	R_PYK       
        
        Input:
         - *filename_in* (string)
         - *file_dir* (string)  [default = None]
         - *IsHeader* (boolean) [default = False]
         - *delimiter* (string) [default = '\t']
        """        
        try:
            if file_dir == None:
                file_in = open(os.path.join(self.data_dir,filename_in),'r')
            else:                  
                file_in = open(os.path.join(file_dir,filename_in),'r')
            IsFileParsed = True
        except:           
            IsFileParsed = False
            print("Error: file {0:s} does not exist in {1:s}".format(filename_in,file_dir))            
         
        if IsFileParsed:    
            D_parsed_data = {}           
            for line in file_in:
                if IsHeader:
                    IsHeader = False
                else:
                    line = line.rstrip() 
                    sline = line.split(delimiter) 
                    group_identifier = sline[0].strip() # group identifier has index=0
                    try: 
                        group_members = sline[1:]       # group members have index=1:n
                    except Exception as er:
                        print(er)
                    if group_identifier not in D_parsed_data:   # each group identifier can exist only once
                        D_parsed_data[group_identifier] = group_members
                    else:
                        print("Warning: {0:s} is detected multiple times. {0:s} is neglected.".format(group_identifier))
            return D_parsed_data
        
    def importCoPE_FBA_Data(self,filename_in,file_dir=None):
        """
        Import module data from CoPE-FBA        

        Example:
        --------
        Unique vertices: 5
        Module fluxes: R_NDPK9,R_PYK,R_NDPK3,R_NDPK2,R_NDPK1,R_PYK5,R_PYK4,R_PYK3,R_PYK2
        
        Input:
         - *filename_in* (string)
         - *file_dir* (string)        
        """
        try:
            if file_dir == None:
                file_in = open(filename_in,'r')                 
            else:                  
                file_in = open(os.path.join(file_dir,filename_in),'r')
            IsFileParsed = True
        except:           
            IsFileParsed = False
            print("Error: file {0:s} does not exist in {1:s}".format(filename,file_dir))  
                   
        if IsFileParsed:
            D_parsed_data = {} 
            for line in file_in:
                if line.startswith('Module:'):
                    module_number = int(line.split(':')[1])
                if line.startswith('Module fluxes:'):                # Module fluxes: R_CBFC2pp,R_CYO1bpp_syn\n
                    reactions_str = line.split(':')[1]               # R_CBFC2pp,R_CYO1bpp_syn\n
                    reactions_str = reactions_str.strip()            # R_CBFC2pp,R_CYO1bpp_syn
                    L_module_reactions = reactions_str.split(',')    # [R_CBFC2pp, R_CYO1bpp_syn]                
                    D_parsed_data[module_number]  = L_module_reactions
            return D_parsed_data
                    

    def importExpressionData(self,D_associations,growth_condition,filename_in = 'CyanoEXpress_cluster.txt',file_dir=None,delimiter = "\t",IsHeader= True):
        """
        get gene expression data (e.g. microarrays)
    
        creates a dictionary of gene expression data per experimental condition (e.g. wt_growth_stage_1h)    
    
        Example:
        --------
        Genes	NAME	wt_growth_stage_1h	wt_growth_stage_2.5h	...	...

        Input:
        - *D_associations* (dictionary)
        - *growth_condition* (string)
        - *filename_in* (string) [default = "CyanoEXpress_cluster.txt"]
        - *file_dir* (string) [default = None]
        - *delimiter* (string) [default = "\t"]
        - *IsHeader* (boolean) [default = True] 
        """
        if not self.D_expression_data: # parse data file only once     
            try:
                if file_dir:
                    file_in = open(os.path.join(file_dir,filename_in),'r')
                else:
                    file_in = open(os.path.join(self.data_dir,filename_in),'r')
                IsParsed = True
            except Exception as er:
                print(er)
                IsParsed = False
                
            if IsParsed:        
                FirstFloat = None
                self.D_expression_data = {}
                for line in file_in:                    
                    sline = line.strip().split(delimiter)    
                    if (not IsHeader) and (len(sline) == len(first_line)):                
                        g_id = sline[0]
                        ### Get the first float ###
                        if not FirstFloat:                            
                            for i,element in enumerate(sline):
                                try:
                                   float(element)
                                   FirstFloat = i
                                   L_conditions = first_line[FirstFloat:]    
                                   break
                                except:
                                   pass                                
                        ###########################            
                        self.D_expression_data[g_id] = {}
                       
                        for i,expression_level in enumerate(sline[FirstFloat:]):
                            try:
                                self.D_expression_data[g_id][L_conditions[i]] = float(expression_level)
                            except Exception:
                                pass                     # N.A                            
                    else:
                        first_line = copy.deepcopy(sline)
                        IsHeader = False                        
                   
        D_squares = {}        
        for r_id in D_associations:
            L_g_ids = D_associations[r_id]    # get gene identifiers belonging to a reaction identifier
            L_r_associated_data = []          # list of expression values belonging to a reaction identifier
            for g_id in L_g_ids:  
                try:
                    g_expression = self.D_expression_data[g_id][growth_condition]                
                    L_r_associated_data.append([g_id,g_expression])
                except Exception as er:
                    pass                      # not available for this growth_condition                    
            D_squares[r_id] = L_r_associated_data
        return D_squares   
                    

    def coupleAssociatioData2Reactions(self,D_associations,D_values):
        """
        couple Associations data to reactions
    
        Input:
         - *D_values* (dictionary)
        """
        if (D_associations) and (D_values):
            D_squares = {}        
            for r_id in D_associations:
                L_square_ids = D_associations[r_id]
                L_r_associated_data = []          # list of values belonging to a reaction identifier
                for square_id in L_square_ids:                      
                    square_value = D_values[square_id]
                    L_r_associated_data.append([square_id,square_value])
                D_squares[r_id] = L_r_associated_data
            return D_squares    

  
    def getReactionModelId(self,search_key,reaction_suffix=None,link_regex='R\d{5}'): 
        """
        get model reaction identifiers from the metabolic map
        
        Input:
         - *search_key* (string)
         - *reaction_suffix* (string) [default = "R_"]        
         - *link_regex* (string) [default = "R\d{5}"] 
        """         
        if reaction_suffix == None:
            reaction_suffix = self.reaction_suffix  
        regex_str = '"{0}.*?"'.format(reaction_suffix)
        L_model_ids = []
        if re.search(link_regex,search_key):
            for i in range(len(self.ModifySVG.L_metabolic_map)):
                if ("<a xlink:href=" in self.ModifySVG.L_metabolic_map[i]):                 # search in reference line that gives the links in a browser
                    if search_key in self.ModifySVG.L_metabolic_map[i]:                      
                        for j in range(i+1,len(self.ModifySVG.L_metabolic_map)):           # start search for species identifier
                            if "</a>" in self.ModifySVG.L_metabolic_map[j]:                 # quit search 
                                break
                            else:
                                m = re.search(regex_str,self.ModifySVG.L_metabolic_map[j])
                                if m:
                                    L_model_ids.append(m.group(0)[1:-1])                    # reaction found
                                    break
            if not len(L_model_ids):
                print("Nothing matches {0}".format(search_key) )
            elif len(L_model_ids) == 1:
                return L_model_ids[0]
            else:
                return L_model_ids
        else:
            print("Error: Not a valid search key; search key {0} does not correspond to the default 'link_regex' {1}".format(search_key,link_regex))
            
    def getSpeciesModelId(self,search_key,species_suffix=None,link_regex =  "C\d{5}"): 
        """
        get SBML reaction identifiers        
        
        Input:
         - *search_key* (string)   
         - *species_suffix* (string) default = ['M_']
         - *link_regex* (string) [default = "C\d{5}"] 
        """
        if species_suffix == None:
            species_suffix = self.species_suffix     
        L_model_ids = []         
        prefix = '"'
        suffix = '" x='
        s_regex = '{0:s}{1}.*?{2:s}'.format(prefix,species_suffix,suffix)  
        if re.search(link_regex,search_key):
            for i in range(len(self.ModifySVG.L_metabolic_map)):                
                if "<a xlink:href=" in self.ModifySVG.L_metabolic_map[i]:                   # search in reference line that gives the links in a browser
                    if search_key in self.ModifySVG.L_metabolic_map[i]:                          
                        for j in range(i+1,len(self.ModifySVG.L_metabolic_map)):           # start search for species identifier
                            if "</a>" in self.ModifySVG.L_metabolic_map[j]:                 # quit search 
                                break
                            else:  
                                m = re.search(s_regex, self.ModifySVG.L_metabolic_map[j])                     
                                if m:
                                    species_id = m.group(0)[len(prefix):-len(suffix)]
                                    if species_id not in L_model_ids:
                                        L_model_ids.append(species_id)                      # species found
            if not len(L_model_ids): 
                print("Nothing matches {0}".format(search_key))
            elif len(L_model_ids) == 1:
                return L_model_ids[0]
            else:
                return L_model_ids
        else:            
            print("Error: Not a valid search key; search key {0} does not correspond to the default 'link_regex' {1}".format(search_key,link_regex))
              
    def getSpeciesLinkId(self,search_key,link_regex =  "C\d{5}"): 
        """
        get species link identifier (works only if <a> </a>  is used
        
        Input:
         *search_key* (string)  
         *link_regex* (string) [default = "C\d{5}"]
        """        
        for i in range(len(self.ModifySVG.L_metabolic_map)):            
            if "<a xlink:href=" in self.ModifySVG.L_metabolic_map[i]:                       # search in reference line that gives the links in a browser 
                m_regex = re.search(link_regex,self.ModifySVG.L_metabolic_map[i])                
                if m_regex:                    
                    for j in range(i+1,len(self.ModifySVG.L_metabolic_map)):               # start search for species identifier
                        if "</a>" in self.ModifySVG.L_metabolic_map[j]:                     # quit search 
                            break
                        else:
                            if 'id="{0}"'.format(search_key) in self.ModifySVG.L_metabolic_map[j]:
                               link_id = m_regex.group(0)                                   # species found
                               return link_id
        
    def getReactionsWithSpecies(self,species,IsSubstrate=True,IsProduct = True,reaction_suffix = None,species_suffix=None,link_regex =  'C\d{5}'):
        """        
        get all reactions that have a certain species as substrate and/or product. Works only if the right information is provided in the SVG file

        <!-- substrate : M_atp_c --> 
        <!-- substrate : M_glc_DASH_D_c -->
        <!-- product : M_adp_c -->
        <!-- product : M_g6p_c -->
        <!-- product : M_h_c -->
        <!-- substrate : M_atp_c -->
        <!-- substrate : M_glc_D_c -->
        <!-- product : M_adp_c -->
        <!-- product : M_g6p_c -->
        <!-- product : M_h_c -->
        <!-- gene association (R_HEX1) : sll0593 -->
        
        Input:
         - *species* (string) 
         - *IsSubstrate* (boolean) [default = True]
         - *IsProduct* (boolean) [default = True]
         - *reaction_suffix* (string) [default = 'R_']
         - *species_suffix*  (string) [default = 'M_']
         - *link_regex* (string) [default = 'C\d{5}']
        """  
        if reaction_suffix == None:
            reaction_suffix = self.reaction_suffix             
        if species_suffix == None:
            species_suffix = self.species_suffix           
        substrate_prefix = '<!-- substrate'
        product_prefix = '<!-- product'
        self.parseSVGfile()
        D_reactions = {'Substrate':[],'Product':[]}
        if re.search(link_regex, species):
            species = self.getSpeciesModelId(species,species_suffix,link_regex)
            print("Species Model Identifier(s): {0}".format(species) )
        
        prefix = 'id="'
        reaction_regex = "{0}.+?".format(reaction_suffix)
        suffix = '"'    
        for svg_line in self.ModifySVG.L_metabolic_map:
            if ('id="{0}'.format(reaction_suffix)) in svg_line:      # reaction detected
                IsReaction = False
                m = re.search('{0:s}{1}{2:s}'.format(prefix,reaction_regex,suffix), svg_line)
                if m:
                    r_id = m.group(0)[len(prefix):-len(suffix)].strip()
                    IsReaction = True
            elif (IsSubstrate == True) and (substrate_prefix in svg_line) and (IsReaction == True):
                if (type(species) == str) and (species in svg_line):
                     if r_id not in D_reactions['Substrate']:
                         D_reactions['Substrate'].append(r_id)
                elif type(species) == list:                   # species (e.g. C00073) is located in different compartments
                    for s_id in species:
                        if s_id in svg_line:
                            if r_id not in D_reactions['Substrate']:
                                D_reactions['Substrate'].append(r_id)
            elif (IsProduct == True) and (product_prefix in svg_line) and (IsReaction == True):
                if (type(species) == str) and (species in svg_line):
                    if r_id not in D_reactions['Product']:
                        D_reactions['Product'].append(r_id)
                elif type(species) == list:                   # species (e.g. C00073) is located in different compartments
                    for s_id in species:
                        if s_id in svg_line:
                            if r_id not in D_reactions['Product']:
                                D_reactions['Product'].append(r_id)
        return D_reactions            
            
    def colorReactionsWithSpecies(self,species,IsSubstrate=True,IsProduct = True,reaction_suffix = None,species_suffix=None,link_regex =  'C\d{5}'): 
        """
        color all reactions that have a certain species as substrate or produt.  Works only if the right information is provided in the SVG file.
        
        Input:
         - *species* (string) 
         - *IsSubstrate* (boolean) [default = True]
         - *IsProduct* (boolean) [default = True]
         - *reaction_suffix* (string) [default = 'R_']
         - *species_suffix*  (string) [default = 'M_']
         - *link_regex* (string) [default = 'C\d{5}']
        """   
        if reaction_suffix == None:
            reaction_suffix = self.reaction_suffix             
        if species_suffix == None:
            species_suffix = self.species_suffix          
        D_reactions = self.getReactionsWithSpecies(species,IsSubstrate,IsProduct,reaction_suffix,species_suffix,link_regex)        
        L_reactions = [item for sublist in D_reactions.values() for item in sublist]        
        self.doMapReactionGroups({"both":L_reactions},filename_out = "{0}_combined".format(species),L_module_colors = ['#0000FF','#00CC00'],reaction_suffix=reaction_suffix)        
        self.doMapReactionGroups(D_reactions,filename_out = "{0}_separated".format(species), L_module_colors = ['#0000FF','#00CC00'],reaction_suffix=reaction_suffix)    
        
    def getReagentsFromReaction(self,r_id,reaction_suffix=None):
        """
        Get all reagents from a specific reaction (r_id). Works only if the right information is provided in the SVG file
        
        Example:
        --------
        <!-- substrate : M_atp_c --> 
        <!-- substrate : M_glc_DASH_D_c -->
        <!-- product : M_adp_c -->
        <!-- product : M_g6p_c -->
        <!-- product : M_h_c -->
        <!-- substrate : M_atp_c -->
        <!-- substrate : M_glc_D_c -->
        <!-- product : M_adp_c -->
        <!-- product : M_g6p_c -->
        <!-- product : M_h_c -->
        <!-- gene association (R_HEX1) : sll0593 -->
        
        Can be exploited for determining e.g. reaction directionallity       
        
        Input:
         - *r_id* (string) which can be model identifier or link identifier
         - *reaction_suffix* (string) [default = "R_"]
        """
        if reaction_suffix == None:
            reaction_suffix = self.reaction_suffix            
         
        substrate_prefix = "<!-- substrate"
        product_prefix = "<!-- product"  
        D_reactions = {"Substrate":[],"Product":[]} 
        IsReactionId = True
        if not r_id.startswith(reaction_suffix): 
            r_id_ori = copy.copy(r_id)
            r_id = self.getReactionModelId(r_id)  # convert potential link identifier into model identifier
            if type(r_id) == list:                # multiple hits
                print("{0:s} matches {1:s}, determine the reagents of these identifiers separately".format(r_id_ori,r_id))
                IsReactionId = False
            elif r_id == None:                    # no hits
                IsReactionId = False
        
        if IsReactionId:
            IsReaction = False
            for svg_line in self.ModifySVG.L_metabolic_map:
                if ('id="{0}"'.format(r_id) ) in svg_line:
                    IsReaction = True                                               
                elif substrate_prefix in svg_line and IsReaction == True:
                    sline = svg_line.split(':')
                    species_id = sline[1].strip().replace('-->','').strip()  
                    if species_id not in D_reactions["Substrate"]:       
                        D_reactions["Substrate"].append(species_id)                             
                elif product_prefix in svg_line and IsReaction == True:
                    sline = svg_line.split(':')
                    species_id = sline[1].strip().replace('-->','').strip()        
                    if species_id not in D_reactions["Product"]:       
                        D_reactions["Product"].append(species_id)   
                elif '</a>' in svg_line:
                    IsReaction = False                             
            return D_reactions          


def extractAbsBoundaryValues(D_values):
    """ 
    Get minimal and maximal *absolute* values
    
    Input:
     - *D_values* (dictionary)   
    """  
    maxValue = 0
    minValue = 999999     
    for key in D_values:
        key_value = D_values[key]    
        if abs(key_value) > maxValue:
            maxValue = abs(key_value)
        if abs(key_value) and abs(key_value) < minValue:            
            minValue = abs(key_value)        
    return (maxValue,minValue)
        
def extractBoundaryValues(D_values):
    """ 
    Get minimal and maximal values
    
    Input:
     - *D_values* (dictionary)   
    """      
    L_values_nested = list(D_values.values())
    L_values = [item for sublist in L_values_nested for item in sublist]    
    return (max(L_values),min(L_values))
