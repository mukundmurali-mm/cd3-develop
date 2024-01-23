# Networking Scenarios

## Managing Network for Non-Greenfield Workflow
- [Export Network](#non-greenfield-tenancies)
- [Add a new or modify the existing networking components](#add-a-new-or-modify-the-existing-networking-components)


**NOTE-**
Before you start with Network Export, make sure you have run 'Fetch Compartments OCIDs to variables file'.

### Export Network

Follow the below steps to export the Networking components that includes VCNs, Subnets, DHCP, DRG, Security List, Route Tables, DRG Route Tables, NSGs, etc to CD3 Excel Sheet and create the Terraform state.

1. Use the [CD3-Blank-Template.xlsx](/cd3_automation_toolkit/example) to export the networking resources into the Tabs - VCNs, DRGs, VCN Info, DHCP, Subnets, NSGs, RouteRulesInOCI, SecRulesInOCI,DRGRouteRulesInOCI tabs.
   
2. Execute the _setupOCI.py_ file with _workflow_type_ parameter value to _export_resources_:
   
   ```python setUpOCI.py /cd3user/tenancies/<customer_name>/<customer_name>_setUpOCI.properties```
   
3. Choose one of the below available sub-options from _'Export Network'_ of the main menu. 
   - Export all Network Components
   - Export Network components for VCNs, DRGs and DRGRouteRulesinOCI Tabs
   - Export Network components for DHCP Tab
   - Export Network components for SecRulesinOCI Tab
   - Export Network components for RouteRulesinOCI Tab
   - Export Network components for SubnetsVLANs Tab
   - Export Network components for NSGs Tab
   
   Once the execution is successful, networking related .tfvars files and .sh files containing import statements will be generated under the folder _/cd3user/tenancies/<customer\_name>/terraform_files/<region_dir>_
   
   Also,The RPC related .tfvars and .sh files containing import statements will be generated in global directory which is inside the /cd3user/tenancies/<customer\_name>/terraform_files/ folder. 

   **NOTE:** The **oci_core_drg_attachment_management** for RPC resources will be shown as created at the end of import process, but it doesn't actually create any resources and can be safely ignored.

<img width="870" alt="rpc" src="https://github.com/oracle-devrel/cd3-automation-toolkit/assets/103548537/1a5d94a8-3309-4edf-84b4-f0e824e0c7d7">
    
   Navigate to the above path and execute the terraform commands:<br>
       <br>_terraform init_
       <br>_Execute the shell scirpts of networking components_
       <br>_terraform plan_
       <br>&nbsp;&nbsp;→ Terraform Plan must show that all the components are in sync.
   
This completes the export of Networking components from OCI.

**Sample of CD3 Excel after export:**
<br>(DO NOT Modify the highlighted columns)

(Showing old images below)
<br>VCNs tab:
![image](https://user-images.githubusercontent.com/115973871/214372501-65e68d60-bedd-4df9-bf84-a2316d0f6c62.png)

Subnets tab:
![image](https://user-images.githubusercontent.com/115973871/214372535-69714cbc-1980-4dd5-ae52-e20441903d8a.png)

<br>[Go back to Networking Scenarios](#networking-scenarios)
### Add a new or modify the existing networking components
1. Export the Networking components by following the steps [above](#1-export-network). (Note that here _workflow_type_ flag is set to create_resources)
2. Follow the [process](/cd3_automation_toolkit/documentation/user_guide/NetworkingScenariosGF.md#modify-network) to add new components such as VCN/DHCP/DRG/IGW/NGW/SGW/LPG/Subnet etc. (Note that here _workflow_type_ flag is set to create_resources)

<br>[Go back to Networking Scenarios](#networking-scenarios)


<br><br>
<div align='center'>

| <a href="/cd3_automation_toolkit/documentation/user_guide/NonGreenField.md">:arrow_backward: Prev</a> | <a href="/cd3_automation_toolkit/documentation/user_guide/ComputeNGF.md">Next :arrow_forward:</a> |
| :---- | -------: |
  
</div>
