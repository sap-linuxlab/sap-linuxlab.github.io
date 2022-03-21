# Demos

This page contains several demo recordings, to demonstrate the functionality of the open-source projects within the SAP LinuxLab initiative.

## Terraform end-to-end automated deployments

### SAP HANA installation

- SAP solution scenario: **SAP HANA 2.0 SPS06, single-node**
- Operating System: **RHEL for SAP Solutions 8.4**
- Infrastructure: **Azure VM (ARM only, not Classic/ASM)**
- Terraform Template name: <sub style="vertical-align: baseline;">**/terraform.sap_infrastructure/templates_for_sap/sap_hana_single_node_install/msazure_vm**</sub>

<div id="terraform-demo1-wrapper" style="z-index: 1; position: relative; max-width: 80%;"></div>

<!--
### SAP S/4HANA installation using SAP Maintanence Planner

- SAP solution scenario: **SAP S/4HANA 2021, One Host**
- Operating System: **RHEL for SAP Solutions 8.4**
- Infrastructure: **AWS EC2 instance (VPC platform only, not Classic)**
- Terraform Template name: <sub style="vertical-align: baseline;">**/terraform.sap_infrastructure/templates_for_sap/sap_s4hana_single_node_install/aws_ec2_instance**</sub>

<div id="terraform-demo2-wrapper" style="z-index: 1; position: relative; max-width: 80%;"></div>


### SAP S/4HANA System Copy (Homogeneous with SAP HANA Backup / Recovery)

- SAP solution scenario: **SAP S/4HANA 2021, One Host System Copy (Homogeneous) using SAP HANA complete data backup file)**
- Operating System: **RHEL for SAP Solutions 8.4**
- Infrastructure: **IBM Cloud Virtual Server (VPC environment only, not Classic)**
- Terraform Template name: <sub style="vertical-align: baseline;">**/terraform.sap_infrastructure/templates_for_sap/sap_s4hana_single_node_system_copy_homogeneous_hdb/ibmcloud_vs**</sub>

<div id="terraform-demo3-wrapper" style="z-index: 1; position: relative; max-width: 80%;"></div>


### SAP ECC on SAP HANA System Copy (Homogeneous with SAP HANA Backup / Recovery)

- SAP solution scenario: **SAP S/4HANA 2021, One Host System Copy (Homogeneous) using SAP HANA complete data backup file)**
- Operating System: **RHEL for SAP Solutions 8.4**
- Infrastructure: **IBM Cloud Virtual Server (VPC environment only, not Classic)**
- Terraform Template name: <sub style="vertical-align: baseline;">**/terraform.sap_infrastructure/templates_for_sap/sap_ecc_hana_single_node_system_copy_homogeneous_hdb/ibmcloud_vs**</sub>

<div id="terraform-demo4-wrapper" style="z-index: 1; position: relative; max-width: 80%;"></div>



## Ansible automated SAP installations

### SAP HANA installation

- SAP solution scenario: **SAP HANA, scale-out cluster**
- Operating System: **RHEL for SAP Solutions 8.4**
- Ansible Collection: <sub style="vertical-align: baseline;">**/community.sap_install/roles/**</sub>

<div id="ansible-demo1-wrapper" style="z-index: 1; position: relative; max-width: 80%;"></div>

-->

<script>
  window.onload = function(){
    AsciinemaPlayer.create('/assets/asciicast/sap_01-ascii.cast', document.getElementById('terraform-demo1-wrapper'));
    AsciinemaPlayer.create('/assets/asciicast/example.cast', document.getElementById('terraform-demo2-wrapper'));
    AsciinemaPlayer.create('/assets/asciicast/example.cast', document.getElementById('terraform-demo3-wrapper'));
    AsciinemaPlayer.create('/assets/asciicast/example.cast', document.getElementById('terraform-demo4-wrapper'));
    AsciinemaPlayer.create('/assets/asciicast/example.cast', document.getElementById('ansible-demo1-wrapper'));
  }
</script>
