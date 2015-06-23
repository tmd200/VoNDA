"""
ModifySVG
=========

This script contains a class with functions that can modify SVG files

Written by TR Maarleveld, Amsterdam, The Netherlands
E-mail: t.r.maarleveld@cwi.nl
Last Change: Augustus 28, 2014
"""

from __future__ import division, print_function, absolute_import

import math,numpy as np,os,re,sys
file_dir = os.path.dirname(__file__)

class ModifySVGfile:
    def __init__(self,L_metabolic_map,colormap_file,start_marker,end_marker):
        """
        Modifies a svg file
        
        Input:
         - *L_metabolic_map* (list)
         - *colormap_file* (string)        
         - *start_marker* (string)
         - *end_marker* (string)
        """
        self.L_metabolic_map = L_metabolic_map
        self.L_rgb_colors = self.getRGBcolors(os.path.join(file_dir.replace('modules',''),'colormaps', colormap_file))
        self.N_colors = len(self.L_rgb_colors)
        self.colormap = colormap_file
        self.start_marker = start_marker
        self.end_marker = end_marker
        
        ### Initial settings ###    
        self.no_value_color = '#808080' # grey HEX-code
        self.data_scale_index = 0
        self.colorbar_index = 0
        
    
    def addColorbar(self):
        """ Adds the color bar """
        file_in = open(os.path.join(file_dir.replace('modules',''),'colormaps', self.colormap),'r')
        L_dat = file_in.readlines()
        for line in L_dat[::-1]:    
            if '<text' in line and 'value_indication' in line:
                N_indications = 11 # number of values
                index = int(math.floor(np.linspace(0,self.N_colors-1,N_indications)[self.colorbar_index]))                
                if self.scale_mode == 'log':
                    line = line.replace('value_indication',"{0:0.1e}".format(np.exp(self.Arr_data_scale[index])) )   
                else:
                    line = line.replace('value_indication',"{0:0.1e}".format(self.Arr_data_scale[index]) )  
                
                self.colorbar_index += 1
                self.svg_line = line + self.svg_line
            elif not "<svg" in line and not "</svg" in line and not "DOCTYPE" in line:                
                self.svg_line = line + self.svg_line  
        
    def getRGBcolors(self,SVG_filepath):
        """
        Use REGEX to extract all rgb color codes from a color map made in SVG format
    
        Example: rgb(44.7059%,10.9804%,54.902%)
    
        Input: 
         - *SVG_filepath* (string)
        """
        try:
            file_in = open(SVG_filepath, 'r')
        except Exception as er:
            print(er)
            sys.exit()
      
        L_rgb_colors = []
        for line in file_in:            
            m = re.search('rgb\\(\\d+.+\\%,\\d+.+\\%,\\d+.+\\%\\)', line)
            if m:
                L_rgb_colors.append(m.group(0))
            n = re.search('rgb\\(\\d+,\\d+,\\d+\\)',line)  # rgb(255,0,0)
            if n:
                L_rgb_colors.append(n.group(0))
        return L_rgb_colors
 

    def createDataScale(self,value_min,value_max,mode): 
        """
        Make the log scale that is necessary for coloring the reactions according to their value
        
        Input:
         - *value_min* (float)
         - *value_max* (float)
         - *mode* (string)
        
        Output:
         - *Arr_data_scale* (array)
        """        
        self.scale_mode = mode
        if self.scale_mode == 'log':
            Arr_data_scale = np.linspace(np.log(value_min), np.log(value_max), self.N_colors)       
        else:
            Arr_data_scale = np.linspace(value_min,value_max, self.N_colors) 
        return Arr_data_scale    
    
    def changeLineWidth(self,value,old_width = 1.0,new_width = 2.0):
        """
        Change the line width of every reaction (arrow) found in the model 
        
        By default the line width is set to 2 pt for every reaction.
                
        Input:
         - *value* (float)
         - *old_width* (float)
         - *new_width* (float)        
        """        
        self.svg_line = self.svg_line.replace('stroke-width:{0}'.format(old_width), 'stroke-width:{0}'.format(new_width)  )
            
    def colorSquares(self,value,additional_colorbar = 'yellowcyan'):
        """
        Change the color of the reactions according to the chosen heatmap
        
        Input:
         - *value* (float)
        """        
        if value:
            if self.scale_mode == 'log':            
                value = np.log(value)  
            if value == self.Arr_data_scale[0]: # value is first color of colorbar
                index = 0                    
            else:
                for index in range(self.N_colors-1):
                    # if value is higher than color[i] and lower or equal than color[i+1]
                    if (self.Arr_data_scale[index] < value) and (value <= self.Arr_data_scale[(index+1)]):
                        break                   # index found
            self.svg_line = self.svg_line.replace('stroke-opacity:0;fill-opacity:0;','stroke-opacity:1;fill-opacity:1;') # make them visible
            self.svg_line = self.svg_line.replace('style="fill:white;stroke:black;','style="fill:{0};stroke:black;'.format(self.L_rgb_colors[index])) # coloring
            
    def colorReactions(self,value):
        """
        Change the color of the reactions according to the chosen heatmap
        
        Makes reactions without a value grey
        
        Input:
         - *value* (float)
        """
        value = np.abs(value)
        if value:
            if self.scale_mode == 'log':           
                value = np.log(value)           
            if value == self.Arr_data_scale[0]: # value is first color of colorbar
                index = 0
            else:
                for index in range(self.N_colors-1):
                    # if value is higher than color[i] and lower or equal than color[i+1]
                    if (self.Arr_data_scale[index] < value) and (value <= self.Arr_data_scale[(index+1)]):                      
                        break                  # index found                
            self.svg_line = self.svg_line.replace('stroke:#000000', 'stroke:{0}'.format(self.L_rgb_colors[index]) ) # coloring
        else:
            self.svg_line = self.svg_line.replace('stroke:#000000', 'stroke:{0}'.format(self.no_value_color) )
           
           
    def colorSpecies(self,value):
        """
        Change the color of species according to the chosen heatmap
        
        Makes species without a value grey
        
        Input:
         - *value* (float)
        """        
        if value:
            if self.scale_mode == 'log':
                value = np.log(value)
            if value == self.Arr_data_scale[0]: # value is first color of colorbar
                index = 0
            else:
                for index in range(self.N_colors-1):
                    # if value is higher than color[i] and lower or equal than color[i+1]
                    if (self.Arr_data_scale[index] < value) and (value <= self.Arr_data_scale[(index+1)]):
                        break                   # index found
            self.svg_line = self.svg_line.replace('style="fill:black', 'style="fill:{0}'.format(self.L_rgb_colors[index]) )
        else:
            self.svg_line = self.svg_line.replace('style="fill:black', 'style="fill:{0}'.format(self.no_value_color) )

    def colorSquareGroups(self,hex_code):
        """        
        Change the color of square groups
        
        Input:
         - *hex_code* (string)
        """        
        self.svg_line = self.svg_line.replace('style="fill:white;stroke:black;"','style="fill:{0:s};stroke:black"'.format(hex_code) ) # coloring
        self.svg_line = self.svg_line.replace('visibility="hidden"','visibility="visible"') # make them visible
            
    def colorSpeciesGroups(self,hex_code):
        """
        Change the color of the reactions 
        
        Input:
         - *hex_code* (string)
        """                                          
        self.svg_line = self.svg_line.replace('style="fill:black"', 'style="fill:{0}"'.format(hex_code) )

    def adaptArrowDirection(self,value):       
        """
        Remove one or both markers to indicate the direction of the reaction
        
        Currently hardcoded for a specific start and end-marker
        
        Input:
         - *value* (float)
        """
        if value > 0:           
            self.svg_line = self.svg_line.replace(';marker-start:url(#{0:s})'.format(self.start_marker), '')
        elif value < 0:           
            self.svg_line = self.svg_line.replace(';marker-end:url(#{0:s})'.format(self.end_marker), '')
        else:
            self.svg_line = self.svg_line.replace(';marker-start:url(#{0:s})'.format(self.start_marker), '')           
            self.svg_line = self.svg_line.replace(';marker-end:url(#{0:s})'.format(self.end_marker), '')
    
    def dashedLine2solidLine(self):
        """ Dashed to solid line """
        m = re.search('stroke-dasharray:.+?;',self.svg_line)
        if m:
            self.svg_line = self.svg_line.replace(m.group(0), 'stroke-dasharray:none;')
        
    def addReactionValue(self,D_reactions,IsAbsolute = True,IsAddReactionValue = True):
        """
        Show value of reaction
        
        Input:
         - *D_reactions* (dict)
         - *IsAbsolute* (boolean) [default=True]
         - *IsAddReactionValue* (boolean) [default=True]
        """        
        prefix = 'ReactionValue'      # hard coded            
        suffix = '</text>'
        m = re.search('{0:s}.*{1:s}'.format(prefix,suffix),self.svg_line)
        if m and IsAddReactionValue:
            r_id = m.group(0)[len(prefix):-len(suffix)]  
            if r_id in D_reactions:
                if D_reactions[r_id]: # Do only if reaction has a value
                    temp = '{0:s}{1:s}'.format(prefix,r_id)
                    if IsAbsolute:     
                        self.svg_line = self.svg_line.replace(temp, '{0:0.1e}'.format(np.abs(D_reactions[r_id])) )
                    else:                 
                        self.svg_line = self.svg_line.replace(temp, '{0:0.1e}'.format(D_reactions[r_id]) )
                    self.svg_line = self.svg_line.replace('fill-opacity:0','fill-opacity:1')
        prefix ='<title>'
        suffix = '</title>'
        n = re.search('{0:s}.*{1:s}'.format(prefix,suffix),self.svg_line)
        if n:
            r_id = n.group(0)[len(prefix):-len(suffix)]  
            if r_id in D_reactions:
                if IsAbsolute:     
                    self.svg_line = self.svg_line.replace(r_id, '{0:s}:{1:0.1e}'.format(r_id,np.abs(D_reactions[r_id])))
                else:                 
                    self.svg_line = self.svg_line.replace(r_id, '{0:s}:{1:0.1e}'.format(r_id,D_reactions[r_id]))

    def addSpeciesValue(self,D_species):
        """
        Show value of species in title object
        
        Input:
         - *D_species* (dict)
        """                
        prefix = '<title>'
        suffix = '</title>'
        m = re.search('{0:s}.*{1:s}'.format(prefix,suffix),self.svg_line)
        if m:            
            s_id = m.group(0)[len(prefix):-len(suffix)]             
            if s_id in D_species:  
                self.svg_line = self.svg_line.replace('<title>{0:s}</title>'.format(s_id),'<title>{0:s}:{1:0.1e}</title>'.format (s_id,D_species[s_id]))

    def showcolorMapWithValues(self):
        """ Show chosen color map values below the color bar """
        if self.scale_mode == 'log':
            self.svg_line = self.svg_line.replace('value_between_lb_and_ub','{0:0.1e}---{1:0.1e}'.format(np.exp(self.Arr_data_scale[self.data_scale_index]), np.exp(self.Arr_data_scale[(self.data_scale_index + 1)])))
        else:
            self.svg_line = self.svg_line.replace('value_between_lb_and_ub','{0:0.1e}---{1:0.1e}'.format(self.Arr_data_scale[self.data_scale_index], self.Arr_data_scale[(self.data_scale_index+1)]))
        self.data_scale_index += 1
