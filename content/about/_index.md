+++
title = "About"
+++

**OpenFCST** was conceived by M. Secanell in 2006 while doing his Ph.D. at the University of Victoria. In 2004, M. Secanell developed a small set of routines that were used to setup the governing equations for a fuel cell cathode in two-dimensions. The governing equations were first linearized and then the weak form of the equations was implemented and solved using the [deal.II](http://www.dealii.org/) finite element libraries. In 2006, after attending a deal.II workshop in Heidelberg, Germany, and discussing the idea of creating an open-source code for fuel cells based on deal.II with Dr. Guido Kanschat and Dr. Wolfgang Bangerth, M. Secanell decided to integrate the routines he had developed into AppFrame, an application framework developed by Dr. Guido Kanschat. The integrated package led to the idea of creating a toolbox for fuel cell analysis. From 2006 to 2008, OpenFCST development continued with the implementation of a complete membrane electrode assembly model; however, with M. Secanell as a sole developer the code was too rough and disorganized to result in an open-source fuel cell package that the research community could use. In 2009, once M. Secanell joined the University of Alberta, the idea of developing OpenFCST was solidified. 

Thanks to the funding provided by the [Automotive Fuel Cell Cooperation Corp.](http://www.afcc-auto.com/), [MITACS](http://www.mitacs.ca/) and the [Natural Science and Engineering Research Council of Canada](http://www.nserc-crsng.gc.ca), a group of core developers was established at the [Electrochemical Energy Systems Design Laboratory](https://esdlab.github.io) (ESDLab) at the University of Alberta. Researchers at the ESDLab re-developed the majority of the classes in order to increase the modularity, usability and reliability of the code. Currently, OpenFCST is used by 6-8 researchers at two different laboratories, it is tested nightly for errors and it contains a bug tracking site to report any issues with its performance.

# Supporting OpenFCST

OpenFCST is developed at the University of Alberta by academics and graduate students. Even though OpenFCST is provided free of charge to the fuel cell community, the developers of OpenFCST spend endless hours developing new code. If you like the library and would like to continue to see it being developed please help the developers in the following ways:

* If you are either an industrial or academic researcher using the library, please make sure to cite the OpenFCST libraries in your publications. Please cite all relevant publications by the OpenFCST developers (see a list of publications below) as well as the OpenFCST reference manual and paper. Also, let us know about your publications by contacting M. Secanell. We will add your publication to the OpenFCST related publications.

* If you are either an industrial or academic researcher using the library and you have developed a new physics model or material database entry, please consider submitting the class to the developers so that it can be integrated with the newest version of OpenFCST.

* If you are an industrial researcher that is considering using OpenFCST for research and development in the company, please consider contacting the developers in order to develop a research program with them.

* If you are an industrial researcher that is considering using OpenFCST for research and development in the company, please consider hiring the graduate students that develop OpenFCST, i.e. the graduate students from the [Electrochemical Energy Systems Design Laboratory](https://esdlab.github.io/people) at the University of Alberta.

## Reference Publications

Please cite these articles if your article uses OpenFCST in any way.

* M. Secanell, A. Putz, P. Wardlaw, V. Zingan, M. Bhaiya, M. Moore, J. Zhou, C. Balen and K. Domican, "OpenFCST: An Open-Source Mathematical Modelling Software for Polymer Electrolyte Fuel Cells", ECS Transactions 64(3): 655-680, 2014. [doi:10.1149/06403.0655ecst](http://ecst.ecsdl.org/content/64/3/655.abstract).
* OpenFCST development team. Fuel Cell Simulation Toolbox (OpenFCST): [User and Developer's Reference Guide](pdfs/v_03/User_Guide.pdf).

## Publications using OpenFCST

Please cite these articles if your article uses OpenFCST in any way.

* M. Moore, S. Shukla, S. Voss, K. Karan, A. Weber, I. Zenyuk and M. Secanell, "A Numerical Study on the Impact of Cathode Catalyst Layer Loading on the Open Circuit Voltage in a Proton Exchange Membrane Fuel Cell," Journal of the Electrochemical Society, 168(4): 044519, 2021.
* A. Kosakian and M. Secanell, "Estimating charge-transport properties of fuel-cell and electrolyzer catalyst layers via electrochemical impedance spectroscopy," Electrochimica Acta, 367: 137521, 2021.
* A. Kosakian, L. Padilla Urbina, A. Heaman, and M. Secanell, "Understanding single-phase water-management signatures in fuel-cell impedance spectra: A numerical study," Electrochimica Acta, 350: 136204, 2020.
* A. Jarauta, V. Zingan, P. Minev, and M. Secanell, "A Compressible Fluid Flow Model Coupling Channel and Porous Media Flows and Its Application to Fuel Cell Materials," Transport in Porous Media, 134: 351-386, 2020.
* M. Sabharwal, L. M. Pant, N. Patel, and M. Secanell, "Computational Analysis of Gas Transport in Fuel Cell Catalyst Layer under Dry and Partially Saturated Conditions," Journal of The Electrochemical Society, 166(7): F3065-F3080, 2019.
* J. Zhou, S. Shukla, A. Putz, and M. Secanell, "Analysis of the role of the microporous layer in improving polymer electrolyte fuel cell performance," Electrochimica Acta, 268C: 366-382, 2018.
* M. Sabharwal, J.T. Gostick, and M. Secanell, "Virtual Liquid Water Intrusion in Fuel Cell Gas Diffusion Media," Journal of the Electrochemical Society, 165(7): F553-F563, 2018.
* J. Zhou, D. Stanier, A. Putz, and M. Secanell, "A Mixed Wettability Pore Size Distribution Based Mathematical Model for Analyzing Two-Phase Flow in Porous Electrodes II. Model Validation and Analysis of Micro-Structural Parameters," Journal of the Electrochemical Society, 164(6): F540-F556, 2017.
* J. Zhou, A. Putz, and M. Secanell, "A Mixed Wettability Pore Size Distribution Based Mathematical Model for Analyzing Two-Phase Flow in Porous Electrodes I. Mathematical Model," Journal of the Electrochemical Society, 164(6): F530-F539, 2017.
* D. Novitski, A. Kosakian, T. Weissbach, M. Secanell, S. Holdcroft, "Electrochemical Reduction of Dissolved Oxygen in Alkaline, Solid Polymer Electrolyte Films," Journal of the American Chemical Society, 138(47): 15465-15472, 2016.
* M. Sabharwal, L. M. Pant, A. Putz, D. Susac, J. Jankovic, M. Secanell, "Analysis of Catalyst Layer Microstructures: From Imaging to Performance," Fuel Cells, 2016
* M. Bhaiya, A. Putz and M. Secanell, "Analysis of non-isothermal effects on polymer electrolyte fuel cell electrode assemblies", Electrochimica Acta, 147C:294-309, 2014. DOI: 10.1016/j.electacta.2014.09.051
* M. Moore, P. Wardlaw, P. Dobson, J.J. Boisvert, A. Putz, R.J. Spiteri, M. Secanell, "Understanding the Effect of Kinetic and Mass Transport Processes in Cathode Agglomerates", Journal of The Electrochemical Society, 161(8):E3125-E3137, 2014. DOI: 10.1149/2.010408jes
* M. Moore, A. Putz and M. Secanell, "Investigation of the ORR Using the Double-Trap Intrinsic Kinetic Model", Journal of the Electrochemical Society 160(6): F670-F681, 2013. DOI: 10.1149/2.123306jes
* P. Dobson, C. Lei, T. Navessin, M. Secanell, "Characterization of the PEM Fuel Cell Catalyst Layer Microstructure by Nonlinear Least-Squares Parameter Estimation", Journal of the Electrochemical Society, 159(5), B1-B10, 2012. DOI: 10.1149/2.041205jes
* M. Secanell, R. Songprakorp, A. Suleman and N. Djilali, "Multi-Objective Optimization of a Polymer Electrolyte Fuel Cell Membrane Electrode Assembly", Energy and Environmental Sciences, 1(3) 378 - 388, 2008.
* M. Secanell, K. Karan, A. Suleman and N. Djilali, "Optimal Design of Ultra-Low Platinum PEMFC Anode Electrodes", Journal of the Electrochemical Society, 155(2) B125-B134, 2008.
* M. Secanell, B. Carnes, A. Suleman and N. Djilali, "Numerical optimization of proton exchange membrane fuel cell cathodes", Electrochimica Acta, 52, 2007, 2668-2682
* M. Secanell, K. Karan, A. Suleman and N. Djilali, "Multi-Variable Optimization of PEMFC Cathodes using an Agglomerate Model ", Electrochimica Acta, 52(22):6318-6337, 2007
