### RPM external python_tools 2.0
## INITENV +PATH PYTHON27PATH %{i}/${PYTHON_LIB_SITE_PACKAGES}
## INITENV +PATH PYTHON3PATH %{i}/${PYTHON3_LIB_SITE_PACKAGES}
Source: none

Requires: root curl python python3 xrootd llvm hdf5 mxnet-predict yoda opencv

#needed for cmssw until python2-> python3 switch of framework
Requires: py2-configparser
Requires: py2-enum34

Requires: py3-scipy
Requires: py3-Keras
Requires: py3-Theano
Requires: py3-scikit-learn
#save for the end
Requires: py3-tensorflow
Requires: py2-googlePackages
Requires: py3-cmsml
Requires: py3-law

Requires: py3-cloudpickle
Requires: py3-tables
Requires: py3-numexpr
Requires: py3-histogrammar
Requires: py3-pandas
Requires: py3-Bottleneck
Requires: py3-downhill
Requires: py3-theanets
Requires: py3-xgboost
Requires: py3-llvmlite
Requires: py3-numba
Requires: py3-hep_ml
Requires: py3-rep
Requires: py3-uncertainties
Requires: py3-hyperas
Requires: py3-hyperopt
Requires: py3-seaborn
Requires: py3-h5py
Requires: py3-h5py-cache
Requires: py3-uproot
Requires: py3-uproot4
Requires: py3-opt-einsum
Requires: py3-joblib

#this DOES NOT depend on numpy..
Requires: py3-xrootdpyfs

Requires: root curl python openldap

Requires: py3-entrypoints
Requires: py3-psutil
Requires: py3-repoze-lru
Requires: py3-Pygments
Requires: py3-appdirs
Requires: py3-argparse
Requires: py3-bleach
Requires: py3-certifi
Requires: py3-decorator
Requires: py3-html5lib
Requires: py3-ipykernel
Requires: py3-ipython
Requires: py3-ipython_genutils
Requires: py3-ipywidgets
Requires: py3-jsonschema
Requires: py3-jupyter
Requires: py3-jupyter_client
Requires: py3-jupyter_console
Requires: py3-jupyter_core
Requires: py3-mistune
Requires: py3-nbconvert
Requires: py3-nbformat
Requires: py3-notebook
Requires: py3-packaging
Requires: py3-pandocfilters
Requires: py3-pathlib2
Requires: py3-pexpect
Requires: py3-pickleshare
Requires: py3-prompt_toolkit
Requires: py3-ptyprocess
Requires: py3-pyparsing
Requires: py3-pyzmq
Requires: py3-qtconsole
Requires: py3-scandir
Requires: py2-setuptools
Requires: py3-setuptools
Requires: py3-simplegeneric
Requires: py3-singledispatch
Requires: py2-six
Requires: py3-terminado
Requires: py3-testpath
Requires: py3-tornado
Requires: py3-traitlets
Requires: py2-wcwidth
Requires: py3-webencodings
Requires: py3-widgetsnbextension
Requires: py3-cycler
Requires: py3-docopt
Requires: py3-networkx
Requires: py2-prettytable
Requires: py2-pycurl
Requires: py3-pytz
Requires: py3-requests
Requires: py3-schema
Requires: py3-python-dateutil
Requires: py3-mock
Requires: py3-pbr
Requires: py3-mpmath
Requires: py3-sympy
Requires: py3-tqdm
Requires: py3-funcsigs
Requires: py3-nose
Requires: py3-pkgconfig
Requires: py3-Click
Requires: py3-jsonpickle
Requires: py3-prwlock
Requires: py3-virtualenv
Requires: py3-virtualenvwrapper
Requires: py3-urllib3
Requires: py3-chardet
Requires: py3-idna
Requires: py3-Werkzeug
Requires: py3-pytest
Requires: py3-avro
Requires: py3-fs
Requires: py3-lizard
Requires: py3-flawfinder
Requires: py3-python-ldap
Requires: py3-plac

Requires: py3-matplotlib
Requires: py2-numpy-toolfile
Requires: py2-sqlalchemy
Requires: py2-pygithub
Requires: py3-dxr-toolfile
Requires: py2-PyYAML
Requires: py3-pylint
Requires: py2-pip
Requires: py3-pip
%ifarch x86_64
Requires: py3-cx-Oracle
%endif
Requires: py2-cython
Requires: py2-future
Requires: py3-pybind11-toolfile
Requires: py3-histbook
Requires: py3-flake8
Requires: py3-autopep8
Requires: py3-pycodestyle
Requires: py3-lz4
Requires: py3-ply
Requires: py3-py
Requires: py3-typing
Requires: py3-defusedxml
Requires: py3-atomicwrites
Requires: py3-attrs
Requires: py3-nbdime
Requires: py3-onnx
Requires: py3-onnxmltools
Requires: py2-backports
Requires: py3-colorama
Requires: py3-lxml
Requires: py3-beautifulsoup4
Requires: py3-GitPython py3-GitPython
Requires: py3-Send2Trash
Requires: py3-ipaddress
Requires: py3-mccabe
Requires: py3-more-itertools
Requires: py3-pluggy
Requires: py3-prometheus_client
Requires: py3-pyasn1-modules
Requires: py3-pyasn1
Requires: py3-pyflakes
Requires: py3-smmap2
Requires: py3-stevedore
Requires: py3-typing_extensions
Requires: py3-virtualenv-clone
Requires: py3-asn1crypto
Requires: py3-backcall
Requires: py3-cffi
Requires: py3-google-common
Requires: py3-jedi
Requires: py3-parso
Requires: py3-pycparser
Requires: py3-absl-py
Requires: py3-gast
Requires: py3-grpcio
Requires: py3-grpcio-tools
Requires: py3-Markdown
Requires: py3-subprocess32
Requires: py3-kiwisolver
Requires: py3-bokeh py3-bokeh
Requires: py3-climate
Requires: py3-mpld3
Requires: py3-neurolab
Requires: py3-nose-parameterized
Requires: py3-pillow
Requires: py3-pybrain
Requires: py3-pymongo
Requires: py3-pydot

Requires: py3-astroid
Requires: py3-hepdata-lib
Requires: py3-isort
Requires: py3-lazy-object-proxy
Requires: py3-pytest-cov
Requires: py3-wrapt

Requires: py3-distlib
Requires: py3-filelock
Requires: py3-gitdb
Requires: py3-importlib-resources
Requires: py3-smmap
Requires: py3-zipp

Requires: py3-pycuda
Requires: onnxruntime

Requires: py3-boost-histogram
Requires: py3-hist
Requires: py3-histoprint
Requires: py3-mplhep
Requires: py3-correctionlib

%prep

%build

%install
mkdir -p %{i}/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/python_tools.xml
<tool name="%{n}" version="%{v}">
</tool>
EOF_TOOLFILE

