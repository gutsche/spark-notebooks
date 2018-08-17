LUMI = 35900 # in pb

###
SAMPLES_PREFIX = 'root://eospublic.cern.ch//eos/user/g/gutsche/data/'
SAMPLES_BASE   = 'stopRun2/'

####
samples = {    
    'TTbar' : {
        'filenames' : ['ttbar_singleLeptFromT_madgraph_pythia8_25ns.root', \
#                        'ttbar_singleLeptFromT_madgraph_pythia8_25ns_1.root', \
#                        'ttbar_singleLeptFromT_madgraph_pythia8_25ns_2.root' \
                      ],
        'xsec'      : None,   
        'eff'       : 1.,   
        'kfactor'   : 1.,   
        'weight'    : 1.,   
        'color'     : 'black',   
    },
    'W3JetsToLNu' : {
        'filenames' : ['W3JetsToLNu_madgraph_pythia8_25ns.root', \
                      ],
        'xsec'      : None,   
        'eff'       : 1.,   
        'kfactor'   : 1.,   
        'weight'    : 1.,   
        'color'     : 'green',   
    },

}
