"""
ModifyData
==========

Modifies data 

Written by TR Maarleveld, Amsterdam, The Netherlands
E-mail: t.r.maarleveld@cwi.nl
Last Change: Augustus 28, 2014
"""

from __future__ import division, print_function, absolute_import

import math,numpy as np,os,re,sys,copy
file_dir = os.path.dirname(__file__)

class ModifyData:
    def __init__(self):
        """
        Initialize Modify data class                      
        """
        pass      
       
    def ValuesHigherThan(self,lb,D_values,IsAbsoluteValues):
        """
        *** Remove values lower than lb ***
        
        Input:
         - *lb* (float)
         - *D_values* (dict)
         - *IsAbsoluteValues* (boolean)
        """       
        for key in list(D_values):
            key_value = D_values[key]
            temp = copy.deepcopy(key_value)            
            if type(temp) == list:  # probably squares data that can contain multiple values per reaction      
                if temp != []:
                    for key_value_pair in D_values[key]:
                        value = key_value_pair[1]  
                        if IsAbsoluteValues:
                            value = abs(value)                      
                        if (value < lb):                                      
                            temp.remove(key_value_pair)                    
                if temp == []:
                    D_values.pop(key)
                else:
                    D_values[key] = temp           
            else:
                if IsAbsoluteValues:
                    key_value = abs(key_value)
                if key_value < lb :   
                    D_values.pop(key)       
        return D_values
                 
    def ValuesLowerThan(self,ub,D_values,IsAbsoluteValues):
        """
        *** Remove values higher than ub ***
        
        Input:
         - *ub* (float)
         - *D_values* (dict)
         - *IsAbsoluteValues* (boolean)
        """
        for key in list(D_values):  
            key_value = D_values[key]   
            temp = copy.deepcopy(key_value)
            if type(temp) == list:  # probably squares data that can contain multiple values per reaction                
                if temp != []:                    
                    for key_value_pair in D_values[key]:
                        value = key_value_pair[1]    
                        if IsAbsoluteValues:
                            value = abs(value) 
                        if (value > ub):                                      
                            temp.remove(key_value_pair)                    
                if temp == []:
                    D_values.pop(key)
                else:
                    D_values[key] = temp
            else:
                if IsAbsoluteValues:
                    key_value = abs(key_value)
                if key_value > ub:
                    D_values.pop(key)             
        return D_values  
         
    def ValuesBetween(self,lb,ub,D_values,IsAbsoluteValues):
        """
        *** Remove values outside lb and ub ***
        
        Input:
         - *lb* (float)
         - *ub* (float) 
         - *D_values* (dict)
        """        
        for key in list(D_values):
            key_value = D_values[key]            
            temp = copy.deepcopy(key_value)
            if type(temp) == list:  # probably squares data that can contain multiple values per reaction                  
                if temp != []:                    
                    for key_value_pair in D_values[key]:
                        value = key_value_pair[1]
                        if IsAbsoluteValues:
                            value = abs(value)       
                        if IsAbsoluteValues:
                            value = abs(value)                  
                        if (value < lb) or (value > ub):                                      
                            temp.remove(key_value_pair)
                if temp == []:
                    D_values.pop(key)
                else:
                    D_values[key] = temp
            else:
                if IsAbsoluteValues:
                    key_value = abs(key_value)
                if (key_value < lb) or (key_value > ub):                    
                    D_values.pop(key)
       
        return D_values         

    def ValuesOutside(self,lb,ub,D_values,IsAbsoluteValues):
        """
        *** Remove values between lb and ub ***
        
        Input:
         - *lb* (float)
         - *ub* (float)
         - *D_values* (dict)
        """
        for key in list(D_values): 
            key_value = D_values[key] 
            temp = copy.deepcopy(key_value)
            if type(temp) == list: 
                if temp != []:                    
                    for key_value_pair in D_values[key]:
                        value = key_value_pair[1]    
                        if IsAbsoluteValues:
                            value = abs(value)                          
                        if (value > lb) and (value < ub):                                      
                            temp.remove(key_value_pair)
                if temp == []:
                    D_values.pop(key)
                else:
                    D_values[key] = temp                
                   
            else:
                if IsAbsoluteValues:
                    key_value = abs(key_value)
                if (key_value > lb) and (key_value < ub):                
                    D_values.pop(key)               
        return D_values        
