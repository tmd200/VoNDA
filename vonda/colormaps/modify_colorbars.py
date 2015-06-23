from __future__ import division, print_function, absolute_import

import re
filename = 'cyanyellow_white.py'
file_in = open(filename,'r')
file_out = open(filename.replace('.py','.svg'),'w')

file_out.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')
file_out.write("<svg version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>\n")
file_out.write('<g id="colorbar" transform="translate(0,0)">\n')
rect_str = ''
IsRect=False
for line in file_in:
    if IsRect and '/>' in line:
        IsRect = False
        file_out.write(rect_str+line.strip()+'\n')
        print(rect_str)
        rect_str = ''
    elif IsRect:
        if "x=" in line:
            m = re.search('x="\d+"',line)
            new= int(m.group(0)[3:-1])-2434            
            line = line.replace(m.group(0),'x="%s"' % new)
        rect_str += ' '+line.strip()
    elif '<rect' in line:
        IsRect=True
        rect_str = line.strip()
        
file_out.write('''
   <path id="indication_0" style="fill:none;stroke:#000000;stroke-width:1.0;stroke-dasharray:none" d="m 0,48 0,3"/>
   <path id="indication_1" style="fill:none;stroke:#000000;stroke-width:1.0;stroke-dasharray:none" d="m 40,48 0,3"/>
   <path id="indication_2" style="fill:none;stroke:#000000;stroke-width:1.0;stroke-dasharray:none" d="m 80,48 0,3"/>
   <path id="indication_3" style="fill:none;stroke:#000000;stroke-width:1.0;stroke-dasharray:none" d="m 120,48 0,3"/>
   <path id="indication_4" style="fill:none;stroke:#000000;stroke-width:1.0;stroke-dasharray:none" d="m 160,48 0,3"/>
   <path id="indication_5" style="fill:none;stroke:#000000;stroke-width:1.0;stroke-dasharray:none" d="m 200,48 0,3"/>
   <path id="indication_6" style="fill:none;stroke:#000000;stroke-width:1.0;stroke-dasharray:none" d="m 240,48 0,3"/>
   <path id="indication_7" style="fill:none;stroke:#000000;stroke-width:1.0;stroke-dasharray:none" d="m 280,48 0,3"/>
   <path id="indication_8" style="fill:none;stroke:#000000;stroke-width:1.0;stroke-dasharray:none" d="m 320,48 0,3"/>
   <path id="indication_9" style="fill:none;stroke:#000000;stroke-width:1.0;stroke-dasharray:none" d="m 360,48 0,3"/>
   <path id="indication_10" style="fill:none;stroke:#000000;stroke-width:1.0;stroke-dasharray:none" d="m 400,48 0,3"/>
   <text x="0" y="58" font-family = "times" font-size="8" style="fill:black">value_indication</text>      
   <text x="40" y="58" font-family = "times" font-size="8" style="fill:black">value_indication</text>    
   <text x="80" y="58" font-family = "times" font-size="8" style="fill:black">value_indication</text>    
   <text x="120" y="58" font-family = "times" font-size="8" style="fill:black">value_indication</text>      
   <text x="160" y="58" font-family = "times" font-size="8" style="fill:black">value_indication</text>    
   <text x="200" y="58" font-family = "times" font-size="8" style="fill:black">value_indication</text>    
   <text x="240" y="58" font-family = "times" font-size="8" style="fill:black">value_indication</text>      
   <text x="280" y="58" font-family = "times" font-size="8" style="fill:black">value_indication</text>    
   <text x="320" y="58" font-family = "times" font-size="8" style="fill:black">value_indication</text>  
   <text x="360" y="58" font-family = "times" font-size="8" style="fill:black">value_indication</text>   
   <text x="400" y="58" font-family = "times" font-size="8" style="fill:black">value_indication</text>
   </g>
   <script type="text/javascript"><![CDATA[
    var KEY = { w:87, a:65, s:83, d:68, i:73, j:74, k:75, l:76 };
    var moveSpeed = 10;
    var colorbar1 = document.getElementById("colorbar");   
    
    var xforms1 = colorbar1.transform.baseVal;  // An SVGTransformList
    var firstXForm1 = xforms1.getItem(0);     // An SVGTransform
    if (firstXForm1.type == SVGTransform.SVG_TRANSFORM_TRANSLATE){
     var firstX1 = firstXForm1.matrix.e,
         firstY1 = firstXForm1.matrix.f;
    } 

    document.documentElement.addEventListener('keydown',function(evt){
      switch (evt.keyCode){
        case KEY.w:          
          colorbar1.transform.baseVal.getItem(0).setTranslate(firstX1,firstY1-=moveSpeed);         
        break;
        case KEY.s:
          colorbar1.transform.baseVal.getItem(0).setTranslate(firstX1,firstY1+=moveSpeed);       
        break;
        case KEY.a:
          colorbar1.transform.baseVal.getItem(0).setTranslate(firstX1-=moveSpeed,firstY1);            
        break;
        case KEY.d:
          colorbar1.transform.baseVal.getItem(0).setTranslate(firstX1+=moveSpeed,firstY1);               
        break;
      }
    },false);
  ]]></script>  
  ''')   
file_out.write('</svg>')
file_out.close()   
