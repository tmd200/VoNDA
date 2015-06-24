from __future__ import division, print_function, absolute_import

import numpy as np

colorbar_template = \
    '    <rect width="$width$" height="48" x="$x$" y="0" id="rect11" style="fill:rgb($RGB$);stroke:rgb($RGB$);"/>\n'

indicatoin_template = \
    '    <path id="indication_$i$" style="fill:none;stroke:#000000;stroke-width:1.0;stroke-dasharray:none" d="m $x$,48 0,3"/>\n'

tick_template = \
    '    <text x="$x$" y="58" font-family="times" font-size="8" style="fill:black">value_indication</text>\n'

def CreateColorGradient(c0, c1, num):
    """
        Creates a RGB color gradient between two given colors.
    
        Arguments:
            c0    - 3-tuple with RGB values of starting color
            c1    - 3-tuple with RGB values of ending color
            num   - number of samples to generate
    """
    return [tuple(map(lambda (x0,x1): int(x0*(1-j) + x1*j), zip(c0, c1)))
            for j in np.linspace(0.0, 1.0, num)]
    

N_colors = 100
fixed_points = [(230, 230, 150), (180, 80, 120), (90, 0, 90)]
colormap = []
for i in xrange(1, len(fixed_points)):
    if colormap != []:
        colormap.pop()
    colormap += CreateColorGradient(fixed_points[i-1], fixed_points[i], N_colors)

colormap_size = 400
N_ticks = 11

with open('custom.svg' ,'w') as file_out:
    
    file_out.write(
    '''<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>
  <g id="colorbar" transform="translate(0,0)">''')
    
    rect_x_pos = np.linspace(0, colormap_size, len(colormap)+1)[0:-1]
    width = colormap_size / (len(colormap))
    for x, color in zip(rect_x_pos, colormap):
        line = colorbar_template.replace('$x$', '%d' % x)
        line = line.replace('$width$', '%g' % width)
        line = line.replace('$RGB$', "%d,%d,%d" % color)
        file_out.write(line)
    
    tick_x_pos = np.linspace(0.0, colormap_size, N_ticks)
    for i in xrange(11):
        file_out.write(indicatoin_template.replace('$i$', '%d' % i).replace('$x$', '%d' % tick_x_pos[i]))

    for i in np.arange(10, -1, -1):
        file_out.write(tick_template.replace('$x$', '%d' % tick_x_pos[i]))

    file_out.write('''  </g>
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
  ]]>
  </script>  
</svg>''')   
