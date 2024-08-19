+++
title = "Release 0.2"
date = 2015-04-03

[links]
    "Class Documentation" = "/class_documentation/v_02"
    "OpenFCST Tutorial" = "/examples/v_02"
+++
* New graphical user interface (GUI)
* Non-isothermal membrane electrode assembly model (see M. Bhaiya, A. Putz and M. Secanell, "Analysis of non-isothermal effects on polymer electrolyte fuel cell electrode assemblies", Electrochimica Acta, 147C:294-309, 2014. DOI: [10.1016/j.electacta.2014.09.051](http://dx.doi.org/10.1016/j.electacta.2014.09.051)
* Double-trap kinetic model available (see M. Moore, A. Putz and M. Secanell, "Investigation of the ORR Using the Double-Trap Intrinsic Kinetic Model", Journal of the Electrochemical Society 160(6): F670-F681. DOI: [10.1149/2.123306jes](http://dx.doi.org/10.1149/2.123306jes)
* Multi-scale framework for analysis of complex agglomerate structures available (see M. Moore, P. Wardlaw, P. Dobson, J.J. Boisvert, A. Putz, R.J. Spiteri, M. Secanell, "Understanding the Effect of Kinetic and Mass Transport Processes in Cathode Agglomerates", Journal of The Electrochemical Society, 161(8):E3125-E3137 DOI: [10.1149/2.010408jes](http://dx.doi.org/10.1149/2.010408jes)
* Improved compilation script and transition to CMake: OpenFCST will automatically look for all dependent libraries and will automatically download any missing libraries if necessary. (Installation tested nightly in OpenSUSE 12.3 and Ubuntu 14.04)
* Improved documentation: Improved user guide and folder with input files for several of the articles above.
* Improved post-processing capabilities: New classes developed to be able to output oxide coverage, agglomerate effectiveness, relative humidity, overpotentials and more.
* Improved post-processing capabilities: New classes to compute functionals such as overall current density and all types of heat losses.

List of packaged required to be installed, before the installation of OpenFCST:

* gcc (compiler for C/C++ and Fortran)
* boost
* make
* cmake
* openmpi
* mpich
* BLAS
* Lapack
* python, python-matplotlib, python-tk, numpy, scipy
* flex
* doxygen
* valgrind (For developers, not a pre-requisite)
