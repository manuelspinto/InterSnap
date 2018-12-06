# InterSnap
WebApp for mining and displaying statistics of the Internet

The Internet is a ever changing environment, that is why it is so important for related studies to first assess on its current status. The public data sources discussed are automatically updated on a regular basis. Using this material, some websites provide automatically-generated statistics on the state of the Internet. CAIDA has recently unveiled a project aimed at providing a framework for Live BGP Data Analysis. Still, these are very general results that may not apply to all applications. As so, we thought of publicly providing a web platform to show some statistics from this thesis through time as multiple snapshots of the Internet. The project goals include automatic updates, appealing interface and room for future integrations. Taking all of this into account the InterSnap platform was created.

![Alt text](https://raw.githubusercontent.com/manuelspinto/InterSnap/master/images/intersnap_arch.PNG)

The InterSnap web server uses open source software hosted on a free cloud platform. As support, it uses an SQL database with pre-processed data that is automatically updated every year by directly fetching the files from the CAIDA’s directories and applying the statistics algorithms. It currently provides statistics on the Address Space, Prefix type to both IP versions and Network information for IPv4.

![Alt text](https://raw.githubusercontent.com/manuelspinto/InterSnap/master/images/pxtype.PNG)

![Alt text](https://raw.githubusercontent.com/manuelspinto/InterSnap/master/images/evolution.PNG)

More information can be found in the original thesis '[Inter-Domain traffic engineering](https://fenix.tecnico.ulisboa.pt/downloadFile/1126295043834237/dissertacao.pdf)'  

