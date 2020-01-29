MuonSC8 Simulation   
====================

[1] Setup

1.1 Untar the MuonSC8 simulation package by

1.2 Modify the environments in 
muonSetupMac.sh for Mac
muonSetupHPCC.sh  for HPCC

[2] build and run Simulation in "sim" directory

2.0  set environmnet by
. muonSetupMac.sh

2.1  build the simulation program
make

2.2  set the executable in runG4CRY_batch.sh

2.3  run the program
. runG4CRY_batch.sh

The number of events to simulate is set by 
/run/beamOn 1000
in runG4CRYbatch_run01.mac

The output root nuple file is
muonTree01.root

The geometry of the detector is defined in
src/B4DetectorConstruction.cc

The output data is in the root ntuple format and defined in
src/B4aEventAction.cc
src/MuonTree.cc

The cosmic muons are gerated by CRY and transfered to GEANT4 via
src/PrimaryGeneratorAction.cc


[3] analysis of simulated events in "ana" directory

3.0  set the environment by
. muonSetupMac.sh  in the "sim" directory

3.1  copy nutple file from the "sim" directory

3.2  compile and run the analysis program
. runana.sh

The output histogram file is "hist_muon01.root".
The analysis code is "muonAnalysis3.cc"

