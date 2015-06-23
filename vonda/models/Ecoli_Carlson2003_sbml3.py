data = """<?xml version="1.0" encoding="utf-8"?>
<!-- Created with PySCeS CBM (0.7.0) on Thu, 20 Feb 2014 14:43:49 by timo -->
<sbml xmlns="http://www.sbml.org/sbml/level3/version1/core" xmlns:fbc="http://www.sbml.org/sbml/level3/version1/fbc/version1" xmlns:html="http://www.w3.org/1999/xhtml" level="3" version="1" fbc:required="false">
  <model metaid="meta_carlson_model" id="carlson_model">
    <notes>
      <html:p>
        <html:br/>
        <html:span size="small">Model &quot;<html:strong>carlson_model</html:strong>&quot; (CBMPY_CB_MODEL) generated with <html:a href="http://pysces.sourceforge.net">PySCeS CBM</html:a> (0.7.0) on Thu, 20 Feb 2014 14:43:49.</html:span>
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
    <species metaid="meta_ACETATE" id="ACETATE" name="acetate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_ACETATE_ext" id="ACETATE_ext" name="extracellular acetate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_ACETYL_CoA" id="ACETYL_CoA" name="acetyl-coenzyme A" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_ADP" id="ADP" name="adenosine diphosphate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_AKG" id="AKG" name="alpha-ketoglutarate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_ATP" id="ATP" name="adenosine triphosphate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_ATP_main" id="ATP_main" name="maintenance energy" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_BIOMASS" id="BIOMASS" name="biomass" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_CITRATE" id="CITRATE" name="citrate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_CO2" id="CO2" name="carbon dioxyde" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_CO2_ext" id="CO2_ext" name="extracellular carbon dioxyde" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_CoASH" id="CoASH" name="coenzyme A" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_DHAP" id="DHAP" name="dihydroxyacetone phosphate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_ERYTH_4_P" id="ERYTH_4_P" name="erythrose-4-phosphate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_ETOH" id="ETOH" name="ethanol" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_ETOH_ext" id="ETOH_ext" name="extracellular ethanol" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_FAD" id="FAD" name="flavin adenine dinucleotide" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_FADH" id="FADH" name="flavin adenine dinucleotide" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_FORMATE" id="FORMATE" name="formate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_FORMATE_ext" id="FORMATE_ext" name="extracellular formate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_FRU_6_P" id="FRU_6_P" name="fructose-6-phosphate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_FRU_BIS_P" id="FRU_BIS_P" name="fructose bi-phosphate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_FUMARATE" id="FUMARATE" name="fumarate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_GA_3P" id="GA_3P" name="glyceraldehyde-3-phosphate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_GLU_6_P" id="GLU_6_P" name="glucose-6-phosphate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_GLU_ext" id="GLU_ext" name="extracellular glucose" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_ISOCIT" id="ISOCIT" name="isocitrate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_LACTATE" id="LACTATE" name="lactate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_LACTATE_ext" id="LACTATE_ext" name="extracellular lactate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_MALATE" id="MALATE" name="malate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_NAD" id="NAD" name="nicotinamide adenine dinucleotide" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_NADH" id="NADH" name="nicotinamide adenine dinucleotide" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_NH3" id="NH3" name="ammonium" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_NH3_ext" id="NH3_ext" name="extracellular ammonium" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_OXALO" id="OXALO" name="oxaloacetate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_OXY_ext" id="OXY_ext" name="extracellular monooxygen" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_PEP" id="PEP" name="phosphoenolpyruvate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_PG" id="PG" name="phosphoglycerate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_PYR" id="PYR" name="pyruvate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_RIBOSE_5_P" id="RIBOSE_5_P" name="ribose-5-phosphate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_RIBULOSE_5_P" id="RIBULOSE_5_P" name="ribulose-5-phosphate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_SED_7_P" id="SED_7_P" name="sedoheptulose-7-phosphate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_SUCC" id="SUCC" name="succinate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_SUCC_CoA" id="SUCC_CoA" name="succinyl-coenzyme A" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_SUCC_ext" id="SUCC_ext" name="extracellular succinate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
    <species metaid="meta_XYL_5_P" id="XYL_5_P" name="xylulose-5-phosphate" compartment="Cell" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
      <notes>
        <html:p>SUBSYSTEM: metabolism</html:p>
      </notes>
      <annotation>
        <listOfKeyValueData xmlns="http://pysces.sourceforge.net/KeyValueData">
          <data id="SUBSYSTEM" type="string" value="metabolism"/>
        </listOfKeyValueData>
      </annotation>
    </species>
  </listOfSpecies>
  <listOfReactions>
    <reaction metaid="meta_R54r" id="R54r" name="R54r" reversible="true" fast="false">
      <listOfReactants>
        <speciesReference species="ACETYL_CoA" stoichiometry="1" constant="false"/>
        <speciesReference species="NADH" stoichiometry="2" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="ETOH" stoichiometry="1" constant="false"/>
        <speciesReference species="NAD" stoichiometry="2" constant="false"/>
        <speciesReference species="CoASH" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R13r" id="R13r" name="R13r" reversible="true" fast="false">
      <listOfReactants>
        <speciesReference species="RIBOSE_5_P" stoichiometry="1" constant="false"/>
        <speciesReference species="XYL_5_P" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="SED_7_P" stoichiometry="1" constant="false"/>
        <speciesReference species="GA_3P" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R26r" id="R26r" name="R26r" reversible="true" fast="false">
      <listOfReactants>
        <speciesReference species="SUCC_CoA" stoichiometry="1" constant="false"/>
        <speciesReference species="ADP" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="SUCC" stoichiometry="1" constant="false"/>
        <speciesReference species="ATP" stoichiometry="1" constant="false"/>
        <speciesReference species="CoASH" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R15r" id="R15r" name="R15r" reversible="true" fast="false">
      <listOfReactants>
        <speciesReference species="ERYTH_4_P" stoichiometry="1" constant="false"/>
        <speciesReference species="XYL_5_P" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="GA_3P" stoichiometry="1" constant="false"/>
        <speciesReference species="FRU_6_P" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R96" id="R96" name="R96" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="FORMATE" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="FORMATE_ext" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R94" id="R94" name="R94" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="LACTATE" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="LACTATE_ext" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R95" id="R95" name="R95" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="SUCC" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="SUCC_ext" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R93" id="R93" name="R93" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="NH3_ext" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="NH3" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R90" id="R90" name="R90" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="ETOH" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="ETOH_ext" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R91" id="R91" name="R91" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="ACETATE" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="ACETATE_ext" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R8r" id="R8r" name="R8r" reversible="true" fast="false">
      <listOfReactants>
        <speciesReference species="PG" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="PEP" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R10" id="R10" name="R10" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="GLU_6_P" stoichiometry="1" constant="false"/>
        <speciesReference species="NAD" stoichiometry="2" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="RIBULOSE_5_P" stoichiometry="1" constant="false"/>
        <speciesReference species="NADH" stoichiometry="2" constant="false"/>
        <speciesReference species="CO2" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R28r" id="R28r" name="R28r" reversible="true" fast="false">
      <listOfReactants>
        <speciesReference species="FUMARATE" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="MALATE" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R3" id="R3" name="R3" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="FRU_6_P" stoichiometry="1" constant="false"/>
        <speciesReference species="ATP" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="FRU_BIS_P" stoichiometry="1" constant="false"/>
        <speciesReference species="ADP" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R70" id="R70" name="R70" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="GLU_6_P" stoichiometry="4" constant="false"/>
        <speciesReference species="RIBOSE_5_P" stoichiometry="13" constant="false"/>
        <speciesReference species="ERYTH_4_P" stoichiometry="5" constant="false"/>
        <speciesReference species="PEP" stoichiometry="32" constant="false"/>
        <speciesReference species="PYR" stoichiometry="38" constant="false"/>
        <speciesReference species="ACETYL_CoA" stoichiometry="41" constant="false"/>
        <speciesReference species="AKG" stoichiometry="14" constant="false"/>
        <speciesReference species="OXALO" stoichiometry="24" constant="false"/>
        <speciesReference species="ATP" stoichiometry="547" constant="false"/>
        <speciesReference species="NADH" stoichiometry="178" constant="false"/>
        <speciesReference species="NH3" stoichiometry="139" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="BIOMASS" stoichiometry="1" constant="false"/>
        <speciesReference species="CoASH" stoichiometry="41" constant="false"/>
        <speciesReference species="ADP" stoichiometry="547" constant="false"/>
        <speciesReference species="NAD" stoichiometry="178" constant="false"/>
        <speciesReference species="CO2" stoichiometry="2" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R6r" id="R6r" name="R6r" reversible="true" fast="false">
      <listOfReactants>
        <speciesReference species="GA_3P" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="DHAP" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R97r" id="R97r" name="R97r" reversible="true" fast="false">
      <listOfReactants>
        <speciesReference species="CO2" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="CO2_ext" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R2r" id="R2r" name="R2r" reversible="true" fast="false">
      <listOfReactants>
        <speciesReference species="GLU_6_P" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="FRU_6_P" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R55" id="R55" name="R55" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="ACETYL_CoA" stoichiometry="1" constant="false"/>
        <speciesReference species="ADP" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="ACETATE" stoichiometry="1" constant="false"/>
        <speciesReference species="CoASH" stoichiometry="1" constant="false"/>
        <speciesReference species="ATP" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R4" id="R4" name="R4" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="FRU_BIS_P" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="FRU_6_P" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R12r" id="R12r" name="R12r" reversible="true" fast="false">
      <listOfReactants>
        <speciesReference species="RIBULOSE_5_P" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="RIBOSE_5_P" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R1" id="R1" name="R1" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="GLU_ext" stoichiometry="1" constant="false"/>
        <speciesReference species="PEP" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="GLU_6_P" stoichiometry="1" constant="false"/>
        <speciesReference species="PYR" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R27r" id="R27r" name="R27r" reversible="true" fast="false">
      <listOfReactants>
        <speciesReference species="SUCC" stoichiometry="1" constant="false"/>
        <speciesReference species="FAD" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="FUMARATE" stoichiometry="1" constant="false"/>
        <speciesReference species="FADH" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R81" id="R81" name="R81" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="FADH" stoichiometry="1" constant="false"/>
        <speciesReference species="ADP" stoichiometry="1" constant="false"/>
        <speciesReference species="OXY_ext" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="FAD" stoichiometry="1" constant="false"/>
        <speciesReference species="ATP" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R23r" id="R23r" name="R23r" reversible="true" fast="false">
      <listOfReactants>
        <speciesReference species="CITRATE" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="ISOCIT" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R9" id="R9" name="R9" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="PEP" stoichiometry="1" constant="false"/>
        <speciesReference species="ADP" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="PYR" stoichiometry="1" constant="false"/>
        <speciesReference species="ATP" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R14r" id="R14r" name="R14r" reversible="true" fast="false">
      <listOfReactants>
        <speciesReference species="GA_3P" stoichiometry="1" constant="false"/>
        <speciesReference species="SED_7_P" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="ERYTH_4_P" stoichiometry="1" constant="false"/>
        <speciesReference species="FRU_6_P" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_RR9" id="RR9" name="RR9" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="PYR" stoichiometry="1" constant="false"/>
        <speciesReference species="ATP" stoichiometry="2" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="PEP" stoichiometry="1" constant="false"/>
        <speciesReference species="ADP" stoichiometry="2" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R53r" id="R53r" name="R53r" reversible="true" fast="false">
      <listOfReactants>
        <speciesReference species="PYR" stoichiometry="1" constant="false"/>
        <speciesReference species="NADH" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="LACTATE" stoichiometry="1" constant="false"/>
        <speciesReference species="NAD" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R80" id="R80" name="R80" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="NADH" stoichiometry="1" constant="false"/>
        <speciesReference species="ADP" stoichiometry="2" constant="false"/>
        <speciesReference species="OXY_ext" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="NAD" stoichiometry="1" constant="false"/>
        <speciesReference species="ATP" stoichiometry="2" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R83" id="R83" name="R83" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="NADH" stoichiometry="1" constant="false"/>
        <speciesReference species="FAD" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="NAD" stoichiometry="1" constant="false"/>
        <speciesReference species="FADH" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R82" id="R82" name="R82" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="ATP" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="ADP" stoichiometry="1" constant="false"/>
        <speciesReference species="ATP_main" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R29r" id="R29r" name="R29r" reversible="true" fast="false">
      <listOfReactants>
        <speciesReference species="MALATE" stoichiometry="1" constant="false"/>
        <speciesReference species="NAD" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="OXALO" stoichiometry="1" constant="false"/>
        <speciesReference species="NADH" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R7r" id="R7r" name="R7r" reversible="true" fast="false">
      <listOfReactants>
        <speciesReference species="GA_3P" stoichiometry="1" constant="false"/>
        <speciesReference species="ADP" stoichiometry="1" constant="false"/>
        <speciesReference species="NAD" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="PG" stoichiometry="1" constant="false"/>
        <speciesReference species="ATP" stoichiometry="1" constant="false"/>
        <speciesReference species="NADH" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R41" id="R41" name="R41" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="MALATE" stoichiometry="1" constant="false"/>
        <speciesReference species="NAD" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="PYR" stoichiometry="1" constant="false"/>
        <speciesReference species="NADH" stoichiometry="1" constant="false"/>
        <speciesReference species="CO2" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R40" id="R40" name="R40" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="PEP" stoichiometry="1" constant="false"/>
        <speciesReference species="CO2" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="OXALO" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R11r" id="R11r" name="R11r" reversible="true" fast="false">
      <listOfReactants>
        <speciesReference species="RIBULOSE_5_P" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="XYL_5_P" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R42" id="R42" name="R42" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="OXALO" stoichiometry="1" constant="false"/>
        <speciesReference species="ATP" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="PEP" stoichiometry="1" constant="false"/>
        <speciesReference species="ADP" stoichiometry="1" constant="false"/>
        <speciesReference species="CO2" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R5r" id="R5r" name="R5r" reversible="true" fast="false">
      <listOfReactants>
        <speciesReference species="FRU_BIS_P" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="DHAP" stoichiometry="1" constant="false"/>
        <speciesReference species="GA_3P" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R25" id="R25" name="R25" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="AKG" stoichiometry="1" constant="false"/>
        <speciesReference species="NAD" stoichiometry="1" constant="false"/>
        <speciesReference species="CoASH" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="NADH" stoichiometry="1" constant="false"/>
        <speciesReference species="SUCC_CoA" stoichiometry="1" constant="false"/>
        <speciesReference species="CO2" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R24" id="R24" name="R24" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="ISOCIT" stoichiometry="1" constant="false"/>
        <speciesReference species="NAD" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="AKG" stoichiometry="1" constant="false"/>
        <speciesReference species="NADH" stoichiometry="1" constant="false"/>
        <speciesReference species="CO2" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R22" id="R22" name="R22" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="OXALO" stoichiometry="1" constant="false"/>
        <speciesReference species="ACETYL_CoA" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="CITRATE" stoichiometry="1" constant="false"/>
        <speciesReference species="CoASH" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R21" id="R21" name="R21" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="PYR" stoichiometry="1" constant="false"/>
        <speciesReference species="NAD" stoichiometry="1" constant="false"/>
        <speciesReference species="CoASH" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="ACETYL_CoA" stoichiometry="1" constant="false"/>
        <speciesReference species="CO2" stoichiometry="1" constant="false"/>
        <speciesReference species="NADH" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
    <reaction metaid="meta_R20" id="R20" name="R20" reversible="false" fast="false">
      <listOfReactants>
        <speciesReference species="PYR" stoichiometry="1" constant="false"/>
        <speciesReference species="CoASH" stoichiometry="1" constant="false"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference species="ACETYL_CoA" stoichiometry="1" constant="false"/>
        <speciesReference species="FORMATE" stoichiometry="1" constant="false"/>
      </listOfProducts>
    </reaction>
  </listOfReactions>
  <fbc:listOfFluxBounds>
    <fbc:fluxBound fbc:id="R54r_lb" fbc:reaction="R54r" fbc:operation="greaterEqual" fbc:value="-999999"/>
    <fbc:fluxBound fbc:id="R54r_ub" fbc:reaction="R54r" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R13r_lb" fbc:reaction="R13r" fbc:operation="greaterEqual" fbc:value="-999999"/>
    <fbc:fluxBound fbc:id="R13r_ub" fbc:reaction="R13r" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R81_lb" fbc:reaction="R81" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R81_ub" fbc:reaction="R81" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R15r_lb" fbc:reaction="R15r" fbc:operation="greaterEqual" fbc:value="-999999"/>
    <fbc:fluxBound fbc:id="R15r_ub" fbc:reaction="R15r" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R26r_lb" fbc:reaction="R26r" fbc:operation="greaterEqual" fbc:value="-999999"/>
    <fbc:fluxBound fbc:id="R26r_ub" fbc:reaction="R26r" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R94_lb" fbc:reaction="R94" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R94_ub" fbc:reaction="R94" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R95_lb" fbc:reaction="R95" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R95_ub" fbc:reaction="R95" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R11r_lb" fbc:reaction="R11r" fbc:operation="greaterEqual" fbc:value="-999999"/>
    <fbc:fluxBound fbc:id="R11r_ub" fbc:reaction="R11r" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R90_lb" fbc:reaction="R90" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R90_ub" fbc:reaction="R90" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R91_lb" fbc:reaction="R91" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R91_ub" fbc:reaction="R91" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R8r_lb" fbc:reaction="R8r" fbc:operation="greaterEqual" fbc:value="-999999"/>
    <fbc:fluxBound fbc:id="R8r_ub" fbc:reaction="R8r" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R10_lb" fbc:reaction="R10" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R10_ub" fbc:reaction="R10" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R28r_lb" fbc:reaction="R28r" fbc:operation="greaterEqual" fbc:value="-999999"/>
    <fbc:fluxBound fbc:id="R28r_ub" fbc:reaction="R28r" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R27r_lb" fbc:reaction="R27r" fbc:operation="greaterEqual" fbc:value="-999999"/>
    <fbc:fluxBound fbc:id="R27r_ub" fbc:reaction="R27r" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R93_lb" fbc:reaction="R93" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R93_ub" fbc:reaction="R93" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R70_lb" fbc:reaction="R70" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R70_ub" fbc:reaction="R70" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R6r_lb" fbc:reaction="R6r" fbc:operation="greaterEqual" fbc:value="-999999"/>
    <fbc:fluxBound fbc:id="R6r_ub" fbc:reaction="R6r" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R97r_lb" fbc:reaction="R97r" fbc:operation="greaterEqual" fbc:value="-999999"/>
    <fbc:fluxBound fbc:id="R97r_ub" fbc:reaction="R97r" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R2r_lb" fbc:reaction="R2r" fbc:operation="greaterEqual" fbc:value="-999999"/>
    <fbc:fluxBound fbc:id="R2r_ub" fbc:reaction="R2r" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R55_lb" fbc:reaction="R55" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R55_ub" fbc:reaction="R55" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R4_lb" fbc:reaction="R4" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R4_ub" fbc:reaction="R4" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R12r_lb" fbc:reaction="R12r" fbc:operation="greaterEqual" fbc:value="-999999"/>
    <fbc:fluxBound fbc:id="R12r_ub" fbc:reaction="R12r" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R1_lb" fbc:reaction="R1" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R1_ub" fbc:reaction="R1" fbc:operation="lessEqual" fbc:value="10"/>
    <fbc:fluxBound fbc:id="R3_lb" fbc:reaction="R3" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R3_ub" fbc:reaction="R3" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R23r_lb" fbc:reaction="R23r" fbc:operation="greaterEqual" fbc:value="-999999"/>
    <fbc:fluxBound fbc:id="R23r_ub" fbc:reaction="R23r" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R9_lb" fbc:reaction="R9" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R9_ub" fbc:reaction="R9" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R14r_lb" fbc:reaction="R14r" fbc:operation="greaterEqual" fbc:value="-999999"/>
    <fbc:fluxBound fbc:id="R14r_ub" fbc:reaction="R14r" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="RR9_lb" fbc:reaction="RR9" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="RR9_ub" fbc:reaction="RR9" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R53r_lb" fbc:reaction="R53r" fbc:operation="greaterEqual" fbc:value="-999999"/>
    <fbc:fluxBound fbc:id="R53r_ub" fbc:reaction="R53r" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R80_lb" fbc:reaction="R80" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R80_ub" fbc:reaction="R80" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R83_lb" fbc:reaction="R83" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R83_ub" fbc:reaction="R83" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R82_lb" fbc:reaction="R82" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R82_ub" fbc:reaction="R82" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R96_lb" fbc:reaction="R96" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R96_ub" fbc:reaction="R96" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R29r_lb" fbc:reaction="R29r" fbc:operation="greaterEqual" fbc:value="-999999"/>
    <fbc:fluxBound fbc:id="R29r_ub" fbc:reaction="R29r" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R7r_lb" fbc:reaction="R7r" fbc:operation="greaterEqual" fbc:value="-999999"/>
    <fbc:fluxBound fbc:id="R7r_ub" fbc:reaction="R7r" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R41_lb" fbc:reaction="R41" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R41_ub" fbc:reaction="R41" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R40_lb" fbc:reaction="R40" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R40_ub" fbc:reaction="R40" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R42_lb" fbc:reaction="R42" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R42_ub" fbc:reaction="R42" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R5r_lb" fbc:reaction="R5r" fbc:operation="greaterEqual" fbc:value="-999999"/>
    <fbc:fluxBound fbc:id="R5r_ub" fbc:reaction="R5r" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R25_lb" fbc:reaction="R25" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R25_ub" fbc:reaction="R25" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R24_lb" fbc:reaction="R24" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R24_ub" fbc:reaction="R24" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R22_lb" fbc:reaction="R22" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R22_ub" fbc:reaction="R22" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R21_lb" fbc:reaction="R21" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R21_ub" fbc:reaction="R21" fbc:operation="lessEqual" fbc:value="999999"/>
    <fbc:fluxBound fbc:id="R20_lb" fbc:reaction="R20" fbc:operation="greaterEqual" fbc:value="0"/>
    <fbc:fluxBound fbc:id="R20_ub" fbc:reaction="R20" fbc:operation="lessEqual" fbc:value="999999"/>
  </fbc:listOfFluxBounds>
  <fbc:listOfObjectives fbc:activeObjective="objMaxJ70">
    <fbc:objective fbc:id="objMaxJ70" fbc:type="maximize">
      <fbc:listOfFluxObjectives>
        <fbc:fluxObjective fbc:reaction="R70" fbc:coefficient="1"/>
      </fbc:listOfFluxObjectives>
    </fbc:objective>
  </fbc:listOfObjectives>
</model>
</sbml>"""
