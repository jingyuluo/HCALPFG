# -----------------------------------------------------------------------------------------------------------------------------
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial  #**Up-to-date**
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile #
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3CheatSheet        #
#
# Environment setup:
#    cmsenv
#    source /cvmfs/cms.cern.ch/crab3/crab.sh
# To submit:
#    crab submit -c crabConfig_noiseAnalysis_CollisionData_RECO_cfg.py
# To check status:
#    crab status -d <CRAB-project-directory> [--jobids <comma-separated-list-of-jobs-and/or-job-ranges>]
# To kill jobs:
#    crab kill -d <CRAB-project-directory> [--jobids <comma-separated-list-of-jobs-and/or-job-ranges>]
# To retrieve output:
#    crab getoutput -d <CRAB-project-directory> [--jobids <comma-separated-list-of-jobs-and/or-job-ranges>]
# -----------------------------------------------------------------------------------------------------------------------------
from CRABClient.UserUtilities import config
#from CRABClient.UserUtilities import getUsernameFromSiteDB


# Select dataset to crab over
number = 0 # starting at 0

# List of datasets
datasetnames = [
'/HFSim_Phase2/jingyu-SingleNeutrino_forHF_RAWSIM_PU0p4_phase2_noaging-8c521043f3b2bee20209ffe954752d75/USER'
#'/HFSim_Phase2/jingyu-SingleNeutrino_forHF_RAWSIM_PU10_phase2-087191e991a9fdaf18256a3e51d888f6/USER',
#'/HFSim_Run3/jingyu-SingleNeutrino_forHF_FEVT-7993cd197b6322fa27f61dc5c977a715/USER',
#'/NoBPTX/Commissioning2016-PromptReco-v1/RECO',
#'/MinimumBias/Commissioning2016-PromptReco-v1/RECO',
#'/HcalHPDNoise/Commissioning2016-PromptReco-v1/RECO',
#'/HcalNZS/Commissioning2016-PromptReco-v1/RECO',
#'/Cosmics/Commissioning2016-PromptReco-v1/RECO'
#'/JetHT/Run2017A-v1/RAW'
#'/HLTPhysics1/Run2017A-v1/RAW'
#'/MET/Run2017B-v1/RAW'
#'/JetHT/Run2017B-v1/RAW'
#'/ZeroBias/Commissioning2018-v1/RAW',
#'/IsolatedBunch/Run2018A-v1/RAW',
#'/MinimumBias/Commissioning2018-v1/RAW'
]

# Storage path for output files - EOS specific
#storagepath = '/store/user/'+getUsernameFromSiteDB()+'/HCALnoise2016'
#storagepath = '/store/group/dpg_hcal/comm_hcal/Noise/2017/' # DO NOT USE

# cmsRun file
psetname = 'pfg_Global_RAW_Phase2_cfg.py'

# Output filename
OutputFilename = 'results.root'

# Storage site of output files
#storageSite = 'T2_CH_CERN'
storageSite = 'T3_US_FNALLPC'#'T2_US_UCSD' 

# White list sites

# ['T2_US_UCSD']

# Black list sites
blackList = ['']

# -----------------------------------------------------------------------------------------------------------------------------
# No modifications below this line are necessary

import datetime
timestamp = datetime.datetime.now().strftime("_%Y%m%d_%H%M%S")


dataset = filter(None, datasetnames[number].split('/'))

config = config()

config.General.workArea        = "out_crab"
config.General.instance = 'preprod'
config.General.requestName     = 'HFSim_Phase2_PU0p4_Ntuple_noaging'#dataset[0]+'_'+dataset[1]+'_'+dataset[2]+timestamp
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = psetname
config.JobType.outputFiles = [OutputFilename]
config.JobType.pyCfgParams = ['outputFile='+OutputFilename]


# DATA specific:
config.Data.inputDataset     = datasetnames[number]
config.Data.inputDBS         = 'phys03'#'global'
config.Data.splitting       = 'FileBased'
config.Data.unitsPerJob     = 100
#config.Data.splitting        = 'LumiBased'
#config.Data.unitsPerJob      = 3
#config.Data.ignoreLocality   = True
config.Data.outLFNDirBase    = '/store/group/lpcbril/MC_test/HFSim_Ntuple'  
config.Data.publication      = False
config.Data.outputDatasetTag = 'HFSim_Phase2_PU0p4_Ntuple_noaging'#dataset[1]+'_'+dataset[2]+timestamp
#config.Data.lumiMask         = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Reprocessing/Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON.txt'
#config.Data.runRange         = '254231-260627'
#config.Data.runRange        = '260577-260578' #for test
#config.Data.lumiMask        = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Reprocessing/Cert_13TeV_16Dec2015ReReco_Collisions15_50ns_JSON.txt'
#config.Data.runRange        = '295606-295606'
#config.Data.runRange        = '295436-296174'

#config.Data.lumiMask        = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-297723_13TeV_PromptReco_Collisions17_JSON.txt'
#config.Data.runRange        = '297723-297723'

#config.Data.runRange        =  '315149-315173'#'314470-314505'

# -----------------------------------------------------------------------------------------------------------------------------
# JSON files are available at: /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/
# -----------------------------------------------------------------------------------------------------------------------------

config.Site.storageSite = storageSite

#if not whiteList:
#config.Site.whitelist = whiteList
#config.Site.whitelist = ["T2_US_UCSD"]

if not blackList:
    config.Site.blacklist = blackList
