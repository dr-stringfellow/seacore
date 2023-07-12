import ROOT as root 
ROOT.gInterpreter.ProcessLine("#include <SeaCore/Utils/interface/Logger.h>")
root.gSystem.Load("libSeaCoreUtils.so")

Logger = root.Logger
logger = Logger()

# for backwards-compatibility
def PInfo(*args):
    logger.info(*args)
def PDebug(*args):
    logger.debug(*args)
def PWarning(*args):
    logger.warning(*args)
def PError(*args):
    logger.error(*args)
