### RPM cms cmssw CMSSW_12_0_0

Requires: cmssw-tool-conf python

%define runGlimpse      yes
%define saveDeps        yes
%define branch          master
%define gitcommit       %{realversion}
# build with debug symbols, and package them in a separate rpm
%define subpackageDebug yes

## INCLUDE cmssw-queue-override

%define source1         git://github.com/cms-sw/cmssw.git?protocol=https&obj=%{branch}/%{gitcommit}&module=%{cvssrc}&export=%{srctree}&output=/src.tar.gz

## IMPORT scram-project-build
## SUBPACKAGE debug IF %subpackageDebug
