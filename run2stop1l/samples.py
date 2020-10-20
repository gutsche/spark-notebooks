LUMI = 35900 # in pb

###
SAMPLES_PREFIX = 'root://eospublic.cern.ch//eos/user/g/gutsche/data/'
SAMPLES_BASE   = 'run2data/'

####
samples = {    
    'TTbar' : {
        'filenames' : ['ttbar_powheg_pythia8_25ns.root', \
                      ],
        'xsec'      : None,   
        'eff'       : 1.,   
        'kfactor'   : 1.,   
        'weight'    : 1.,   
        'color'     : 'black',   
    },
    'WZ' : {
        'filenames' : ['WZ_pythia8_25ns.root', \
                      ],
        'xsec'      : None,   
        'eff'       : 1.,   
        'kfactor'   : 1.,   
        'weight'    : 1.,   
        'color'     : 'green',   
    },

}
