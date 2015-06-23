data = """<?xml version="1.0" encoding="utf-8"?>
<!-- Created with PySCeS CBM (0.7.0) on Fri, 29 Nov 2013 10:39:21 by timo -->
<sbml xmlns="http://www.sbml.org/sbml/level3/version1/core" xmlns:fbc="http://www.sbml.org/sbml/level3/version1/fbc/version1" xmlns:html="http://www.w3.org/1999/xhtml" level="3" version="1" fbc:required="false">
  <model metaid="meta_core_memesa_model" id="core_memesa_model">
    <notes>
      <html:p>
        <html:span style="font-family: Courier New,Courier,monospace;">Model core_memesa_model (None) generated with PySCeS CBM (0.4.2 [r973]) on Thu, 02 Feb 2012 12:06:35.</html:span>
      </html:p>
    </notes>
    <listOfUnitDefinitions>
      <unitDefinition id="substance" name="substance">
        <listOfUnits>
          <unit kind="mole" exponent="1" scale="0" multiplier="1"/>
        </listOfUnits>
      </unitDefinition>
      <unitDefinition id="area" name="area">
        <listOfUnits>
          <unit kind="metre" exponent="2" scale="0" multiplier="1"/>
        </listOfUnits>
      </unitDefinition>
      <unitDefinition id="volume" name="volume">
        <listOfUnits>
          <unit kind="litre" exponent="1" scale="0" multiplier="1"/>
        </listOfUnits>
      </unitDefinition>
      <unitDefinition id="length" name="length">
        <listOfUnits>
          <unit kind="metre" exponent="1" scale="0" multiplier="1"/>
        </listOfUnits>
      </unitDefinition>
      <unitDefinition id="time" name="time">
        <listOfUnits>
          <unit kind="second" exponent="1" scale="0" multiplier="1"/>
        </listOfUnits>
      </unitDefinition>
      <unitDefinition id="mmol_per_gDW_per_hr" name="mmol_per_gDW_per_hr">
        <listOfUnits>
          <unit kind="mole" exponent="1" scale="-3" multiplier="1"/>
          <unit kind="gram" exponent="-1" scale="0" multiplier="1"/>
          <unit kind="second" exponent="-1" scale="0" multiplier="0.00027777"/>
        </listOfUnits>
      </unitDefinition>
    </listOfUnitDefinitions>
    <listOfCompartments>
      <compartment id="Cell" name="Cell" size="1" constant="false"/>
    </listOfCompartments>
    <listOfSpecies>
      <species metaid="meta_A" id="A" name="A" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_B" id="B" name="B" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_C" id="C" name="C" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_D" id="D" name="D" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_E" id="E" name="E" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_F" id="F" name="F" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_G" id="G" name="G" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_H" id="H" name="H" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_I" id="I" name="I" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_J" id="J" name="J" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_K" id="K" name="K" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_L" id="L" name="L" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_M" id="M" name="M" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_N" id="N" name="N" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_O" id="O" name="O" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_P" id="P" name="P" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_Q" id="Q" name="Q" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_R" id="R" name="R" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_S" id="S" name="S" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species metaid="meta_T" id="T" name="T" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false"/>
      <species metaid="meta_U" id="U" name="U" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false"/>
      <species metaid="meta_X" id="X" name="X" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false"/>
      <species metaid="meta_Y" id="Y" name="Y" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false"/>
    </listOfSpecies>
    <listOfReactions>
      <reaction metaid="meta_R01" id="R01" name="R01" reversible="false" fast="false">
        <notes>
          <html:p>SUBSYSTEM: L</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="L"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="X" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="A" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R10" id="R10" name="R10" reversible="false" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C2</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C2"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="G" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="H" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R03" id="R03" name="R03" reversible="true" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C1</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C1"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="A" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="C" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R02" id="R02" name="R02" reversible="true" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C1</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C1"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="A" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="B" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R05" id="R05" name="R05" reversible="false" fast="false">
        <notes>
          <html:p>SUBSYSTEM: L</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="L"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="B" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="D" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R04" id="R04" name="R04" reversible="true" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C1</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C1"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="C" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="B" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R16" id="R16" name="R16" reversible="false" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C3</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C3"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="J" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="M" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R17" id="R17" name="R17" reversible="false" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C3</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C3"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="M" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="N" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R14" id="R14" name="R14" reversible="true" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C3</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C3"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="K" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="L" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R15" id="R15" name="R15" reversible="false" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C3</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C3"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="L" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="Q" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R12" id="R12" name="R12" reversible="false" fast="false">
        <notes>
          <html:p>SUBSYSTEM: L</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="L"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="I" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="J" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R13" id="R13" name="R13" reversible="false" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C3</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C3"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="J" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="K" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R07" id="R07" name="R07" reversible="false" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C2</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C2"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="E" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="F" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R06" id="R06" name="R06" reversible="false" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C2</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C2"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="D" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="E" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R09" id="R09" name="R09" reversible="false" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C2</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C2"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="D" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="G" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R08" id="R08" name="R08" reversible="false" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C2</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C2"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="F" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="I" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R11" id="R11" name="R11" reversible="false" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C2</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C2"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="H" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="I" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R18" id="R18" name="R18" reversible="false" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C3</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C3"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="N" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="Q" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R19" id="R19" name="R19" reversible="true" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C3</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C3"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="K" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="O" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R26" id="R26" name="R26" reversible="false" fast="false">
        <notes>
          <html:p>SUBSYSTEM: L</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="L"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="S" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="Y" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R25" id="R25" name="R25" reversible="false" fast="false">
        <notes>
          <html:p>SUBSYSTEM: L</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="L"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="A" stoichiometry="1" constant="false"/>
          <speciesReference species="T" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S" stoichiometry="0.5" constant="false"/>
          <speciesReference species="U" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R24" id="R24" name="R24" reversible="false" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C4</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C4"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="R" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R23" id="R23" name="R23" reversible="true" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C4</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C4"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="R" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R22" id="R22" name="R22" reversible="false" fast="false">
        <notes>
          <html:p>SUBSYSTEM: L</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="L"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="Q" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="R" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R21" id="R21" name="R21" reversible="true" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C3</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C3"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="P" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="L" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
      <reaction metaid="meta_R20" id="R20" name="R20" reversible="true" fast="false">
        <notes>
          <html:p>SUBSYSTEM: C3</html:p>
        </notes>
        <annotation>
          <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
            <data id="SUBSYSTEM" type="string" value="C3"/>
          </listOfKeyValueData>
        </annotation>
        <listOfReactants>
          <speciesReference species="O" stoichiometry="1" constant="false"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="P" stoichiometry="1" constant="false"/>
        </listOfProducts>
      </reaction>
    </listOfReactions>
    <fbc:listOfFluxBounds>
      <fbc:fluxBound fbc:id="c0" fbc:reaction="R16" fbc:operation="greaterEqual" fbc:value="0"/>
      <fbc:fluxBound fbc:id="c1" fbc:reaction="R16" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c2" fbc:reaction="R03" fbc:operation="greaterEqual" fbc:value="-1000"/>
      <fbc:fluxBound fbc:id="c3" fbc:reaction="R03" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c4" fbc:reaction="R02" fbc:operation="greaterEqual" fbc:value="-1000"/>
      <fbc:fluxBound fbc:id="c5" fbc:reaction="R02" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c6" fbc:reaction="R05" fbc:operation="greaterEqual" fbc:value="0"/>
      <fbc:fluxBound fbc:id="c7" fbc:reaction="R05" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c8" fbc:reaction="R07" fbc:operation="greaterEqual" fbc:value="0"/>
      <fbc:fluxBound fbc:id="c9" fbc:reaction="R07" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c10" fbc:reaction="R04" fbc:operation="greaterEqual" fbc:value="-1000"/>
      <fbc:fluxBound fbc:id="c11" fbc:reaction="R04" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c12" fbc:reaction="R01" fbc:operation="greaterEqual" fbc:value="0"/>
      <fbc:fluxBound fbc:id="c13" fbc:reaction="R01" fbc:operation="lessEqual" fbc:value="1"/>
      <fbc:fluxBound fbc:id="c14" fbc:reaction="R17" fbc:operation="greaterEqual" fbc:value="0"/>
      <fbc:fluxBound fbc:id="c15" fbc:reaction="R17" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c16" fbc:reaction="R14" fbc:operation="greaterEqual" fbc:value="-1000"/>
      <fbc:fluxBound fbc:id="c17" fbc:reaction="R14" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c18" fbc:reaction="R15" fbc:operation="greaterEqual" fbc:value="0"/>
      <fbc:fluxBound fbc:id="c19" fbc:reaction="R15" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c20" fbc:reaction="R12" fbc:operation="greaterEqual" fbc:value="0"/>
      <fbc:fluxBound fbc:id="c21" fbc:reaction="R12" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c22" fbc:reaction="R13" fbc:operation="greaterEqual" fbc:value="0"/>
      <fbc:fluxBound fbc:id="c23" fbc:reaction="R13" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c24" fbc:reaction="R10" fbc:operation="greaterEqual" fbc:value="0"/>
      <fbc:fluxBound fbc:id="c25" fbc:reaction="R10" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c26" fbc:reaction="R11" fbc:operation="greaterEqual" fbc:value="0"/>
      <fbc:fluxBound fbc:id="c27" fbc:reaction="R11" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c28" fbc:reaction="R09" fbc:operation="greaterEqual" fbc:value="0"/>
      <fbc:fluxBound fbc:id="c29" fbc:reaction="R09" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c30" fbc:reaction="R08" fbc:operation="greaterEqual" fbc:value="0"/>
      <fbc:fluxBound fbc:id="c31" fbc:reaction="R08" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c32" fbc:reaction="R06" fbc:operation="greaterEqual" fbc:value="0"/>
      <fbc:fluxBound fbc:id="c33" fbc:reaction="R06" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c34" fbc:reaction="R18" fbc:operation="greaterEqual" fbc:value="0"/>
      <fbc:fluxBound fbc:id="c35" fbc:reaction="R18" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c36" fbc:reaction="R19" fbc:operation="greaterEqual" fbc:value="-1000"/>
      <fbc:fluxBound fbc:id="c37" fbc:reaction="R19" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c38" fbc:reaction="R26" fbc:operation="greaterEqual" fbc:value="0"/>
      <fbc:fluxBound fbc:id="c39" fbc:reaction="R26" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c40" fbc:reaction="R25" fbc:operation="greaterEqual" fbc:value="0"/>
      <fbc:fluxBound fbc:id="c41" fbc:reaction="R25" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c42" fbc:reaction="R24" fbc:operation="greaterEqual" fbc:value="0"/>
      <fbc:fluxBound fbc:id="c43" fbc:reaction="R24" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c44" fbc:reaction="R23" fbc:operation="greaterEqual" fbc:value="-1000"/>
      <fbc:fluxBound fbc:id="c45" fbc:reaction="R23" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c46" fbc:reaction="R22" fbc:operation="greaterEqual" fbc:value="0"/>
      <fbc:fluxBound fbc:id="c47" fbc:reaction="R22" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c48" fbc:reaction="R21" fbc:operation="greaterEqual" fbc:value="-1000"/>
      <fbc:fluxBound fbc:id="c49" fbc:reaction="R21" fbc:operation="lessEqual" fbc:value="1000"/>
      <fbc:fluxBound fbc:id="c50" fbc:reaction="R20" fbc:operation="greaterEqual" fbc:value="-1000"/>
      <fbc:fluxBound fbc:id="c51" fbc:reaction="R20" fbc:operation="lessEqual" fbc:value="1000"/>
    </fbc:listOfFluxBounds>
    <fbc:listOfObjectives fbc:activeObjective="objMaxJ25">
      <fbc:objective fbc:id="objMaxJ25" fbc:type="maximize">
        <fbc:listOfFluxObjectives>
          <fbc:fluxObjective fbc:reaction="R26" fbc:coefficient="1"/>
        </fbc:listOfFluxObjectives>
      </fbc:objective>
    </fbc:listOfObjectives>
  </model>
</sbml>"""
