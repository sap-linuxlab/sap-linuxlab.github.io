# Projects Functionality

Projects within the SAP LinuxLab initiative have various functionality for Day 0/1/2 of SAP. The initiative overall seeks to assist SAP-run enterprises to achieve various business-focused outcomes, such as:

- **SAP S/4HANA Greenfield/Re-Implementation**, *e.g. install from SAP Maintenance Planner*
- **SAP S/4HANA Brownfield/Conversion**, *e.g. System Copy and DMO for SUM*
- **SAP S/4HANA Selective Data Transition**, *e.g. System Copy and Shell Conversion or Mix&Match*
- **Datacenter Exit / Cloud Service Provider switch Compute Re-locate**, *e.g. System Copy to new Infrastructure*
- **Enterprise re-structures with Spin-offs and Divestitures**, *e.g. System Copy and carve-out*
- **Enterprise re-structures with Mergers and Acquisitions**, *e.g. System Copy and merge*
- **Daily SAP Operations / Maintenance**, *e.g. Start/Stop SAP Systems, RFC / BAPI / Task List runs, Backup scheduled runs, SAP Kernel patching*

<br/>

As a high-level summary, the following functionality is currently available (as of writing, Apr-2022):

| Activity | Functionality | Project/s within SAP LinuxLab open-source initiative |
| --- | --- | --- |
| End-to-End Automated Infrastructure and SAP Software scenario installations (Day 0) | <ul><li>:white_check_mark: SAP HANA single-node installation</li><li>:white_check_mark: SAP S/4HANA single-node installation, using SAP Maintenance Planner</li><li>:white_check_mark: SAP S/4HANA single-node System Copy (Homogeneous)</li><li>:white_check_mark: SAP ECC on SAP HANA single-node System Copy (Homogeneous)</li> | [terraform.templates_for_sap](https://github.com/sap-linuxlab/terraform.templates_for_sap) |
| Automated Provisioning to Cloud Infrastructure (Day 0)<br/><sub>*Includes Account Bootstrap (aka. minimal landing zone)*</sub> | <ul><li>:white_check_mark: AWS EC2</li><li>:x: GCP VM</li><li>:white_check_mark: IBM Cloud, Intel VS</li><li>:white_check_mark: IBM Cloud, Power VS</li><li>:white_check_mark: Microsoft Azure</li></ul> | [terraform.modules_for_sap](https://github.com/sap-linuxlab/terraform.modules_for_sap) |
| Automated Provisioning to Hypervisor Infrastructure (Day 0) | <ul><li>:white_check_mark: IBM PowerVM LPAR</li><li>:x: OVirt VM</li><li>:x: VMware vSphere VM</li></ul> | [terraform.modules_for_sap](https://github.com/sap-linuxlab/terraform.modules_for_sap) |
| Automated SAP Installations (Day 1) | <ul><li>:white_check_mark: Preconfigure host for SAP HANA and SAP NetWeaver</li><li>:white_check_mark: Install SAP HANA via HDBLCM, any combination</li><li>:white_check_mark: Install SAP Software via SWPM, any combination (includes Templates)</li><li>:warning: Install Linux Pacemaker and setup SAP HA/DR `[WIP]`</li></ul> | [community.sap_install](https://github.com/sap-linuxlab/community.sap_install) |
| Automated SAP Operations (Day 2) | <ul><li>:white_check_mark: Post-Install of SAP Software OS configuration</li><li>:white_check_mark: SAP Systems Start/Stop</li><li>:white_check_mark: SAP Profile updates</li><li>:white_check_mark: SAP basic monitoring</li><li>:white_check_mark: SAP HANA Backint backup scheduling and execution</li><li>:white_check_mark: SAP RFC / BAPI / Task List runs</li><li>:warning: SAP Kernel patching `[WIP]`</li></ul> | [community.sap_operations](https://github.com/sap-linuxlab/community.sap_operations) |
| Automated SAP Software Downloads | <ul><li>:white_check_mark: SAP User ID SSO login</li><li>:white_check_mark: Search and download by filename</li><li>:white_check_mark: Maintenance Planner stack download</li></ul> | [community.sap_launchpad](https://github.com/sap-linuxlab/community.sap_launchpad) |
| Hardware sizing and specifications calculators | <ul><li>:white_check_mark: Benchmark records extraction and compare in CSV</li><li>:white_check_mark: Calculate storage requirements for SAP HANA (scale-up/scale-out) and SAP NetWeaver</li></ul> | [tool.sap_sizing_calculators](https://github.com/sap-linuxlab/tool.sap_sizing_calculators) |
