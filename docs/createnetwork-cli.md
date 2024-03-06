# Networking Scenarios 

## Managing Network for Greenfield Workflow
   - [Create Network](#create-network)
   - [Use an existing DRG in OCI while creating the network](#use-an-existing-drg-in-oci-while-creating-the-network)
   - [Modify Network](#modify-network)
   - [Modify Security Rules, Route Rules and DRG Route Rules](#modify-security-rules-route-rules-and-drg-route-rules)
   - [Sync manual changes done in OCI of Security Rules, Route Rules and DRG Route Rules with CD3 Excel Sheet and Terraform](#sync-manual-changes-done-in-	oci-of-security-rules-route-rules-and-drg-route-rules-with-cd3-excel-sheet-and-terraform)
   - [Add/Modify/Delete NSGs](#addmodifydelete-nsgs)
   - [Add/Modify/Delete VLANs](#addmodifydelete-vlans)
   - [RPCs](#rpcs)


!!! note
      Before you start with Network Creation, make sure you have run 'Fetch Compartments OCIDs to variables file'.

### Create Network
Creation of Networking components using Automation Toolkit involves four simple steps.
 - Add the networking resource details to appropriate Excel Sheets.
 - Running the toolkit to generate auto.tfvars.
 - Executing Terraform commands to provision the resources in OCI.
 - Exporting the automatically generated Security Rules and Route Rules by the toolkit to CD3 Excel Sheet.
 
Below are the steps in detail to create Network that includes VCNs, Subnets, DHCP, DRG, Security List, Route Tables, DRG Route Tables, NSGs, etc.

1. Choose appropriate excel sheet from [Excel Templates](excel-templates.md) and fill the required Network details in the Networking Tabs - VCNs, DRGs, VCN Info, DHCP, Subnets, NSGs tabs. <br>
   <br>
2. Execute the _setupOCI.py_ file with _workflow_type_ parameter value to _create_resources_:
   ```python setUpOCI.py /cd3user/tenancies/<customer_name>/<customer_name>_setUpOCI.properties``` <br>
   <br> 
3. Choose option _'Validate CD3'_ and then _'Validate Network(VCNs, Subnets, DHCP, DRGs)'_ to check for syntax errors in Excel sheet. Examine the log file generated at ```/cd3user/tenancies/<customer_name>/<customer_name>_cd3validator.log.``` If there are errors, please rectify them accordingly and proceed to the next step. <br>
   <br>
4. Choose option to _'Create Network'_ under _'Network'_ from the displayed menu. Once the execution is successful, multiple .tfvars related to networking like _<customer\_name>\_major-objects.auto.tfvars_ and more will be generated under the folder ```/cd3user/tenancies/<customer_name>/terraform_files/<region_dir>/<service_dir>``` <br>
   <br>
5. Navigate to the above path and execute the terraform commands:
       <br>_terraform init_
       <br>_terraform plan_
       <br>_terraform apply_
   <br>
   <br>This completes the creation of Networking components in OCI. Verify the components in console. However the details of the default security lists and default route tables may not be available in the CD3 Excel sheet yet. Inorder to export that data please follow the below steps: <br>
<br>
6. Execute the _setupOCI.py_ file with _workflow_type_ parameter value to _create_resources_:
   ```python setUpOCI.py /cd3user/tenancies/<customer_name>/<customer_name>_setUpOCI.properties``` <br>
  <br>    
7. Choose _'Network'_ from the displayed menu. Choose below sub-options: (Make sure to choose all the three options for the first time)
   - Security Rules
      <br>-Export Security Rules (From OCI into SecRulesinOCI sheet)
   - Route Rules
      <br> -Export Route Rules (From OCI into RouteRulesinOCI sheet)
   - DRG Route Rules
      <br> -Export DRG Route Rules (From OCI into DRGRouteRulesinOCI sheet)

This completes the steps for Creating the Network in OCI and exporting the default rules to the CD3 Excel Sheet using the Automation Toolkit.


### Use an existing DRG in OCI while creating the network
In some scenarios, a DRG has already been created in the tenancy and rest of the Network components still need to be created. In such cases, generate the networking related tfvars using same process mentioned above till Step 4. Use same name for DRG in DRGs tab as present in OCI console.

 - For Step 5, Navigate to the outdir path and execute the terraform commands:<br>
       <br>_terraform init_
       <br>_terraform import "module.drgs[\\"&lt;&lt;drgs terraform variable name&gt;&gt;\\"].oci_core_drg.drg" &lt;&lt;drg-ocid&gt;&gt;_
       <br>&nbsp;&nbsp;→ This will Import the DRG into your state file.       
       _terraform plan_
       <br>&nbsp;&nbsp;→ Terraform Plan will indicate to add all the other components except DRG.
       <br>_terraform apply_

   Continue executing the remaining steps (from Step 6) of [Create Network](#create-network).

### Modify Network 
Modifying the Networking components using Automation Toolkit involves three simple steps.
 - Add/modify the details of networking components like the VCNs, Subnets, DHCP and DRG in Excel Sheet.
 - Running the toolkit to generate auto.tfvars.
 - Executing Terraform commands to provision/modify the resources in OCI.

!!! note 
   Follow [these steps](#modify-security-rules-route-rules-and-drg-route-rules) to modify Security Rules, Route Rules and DRG Route Rules

_Steps in detail_:

1. Modify your excel sheet to update required data in the Tabs - VCNs, DRGs, VCN Info, DHCP and Subnets. <br>
<br>   
2. Execute the _setupOCI.py_ file with _workflow_type_ parameter value to _create_resources_:
   ```python setUpOCI.py /cd3user/tenancies/<customer_name>/<customer_name>_setUpOCI.properties``` <br>
<br>   
3. To Validate the CD3 excel Tabs - Choose option _'Validate CD3'_ and _'Validate Network(VCNs, Subnets, DHCP, DRGs)'_ from sub-menu to check for syntax errors in Excel sheet. Examine the log file generated at ```/cd3user/tenancies/<customer_name>/<customer_name>\_cd3validator.logs_.``` If there are errors, please rectify them accordingly and proceed to the next step. <br>
<br>
4. Choose option to _'Modify Network'_ under _'Network'_ from the displayed menu. Once the execution is successful, multiple .tfvars related to networking like _<customer_name>\_major-objects.auto.tfvars_ and more will be generated under the folder ```/cd3user/tenancies/<customer_name>/terraform_files/<region_dir>/<service_dir>_```. Existing files will move into respective backup folders.
   **Note-**: Make sure to export Sec Rules, Route Rules, DRG Route Rules to CD3 Excel Sheet before executing this option. <br>
<br>
5. Navigate to the above path and execute the terraform commands:
       <br>_terraform init_
       <br>_terraform plan_
       <br>_terraform apply_
   
This completes the modification of Networking components in OCI. Verify the components in console.

### Modify Security Rules, Route Rules and DRG Route Rules

Follow the below steps to add, update or delete the following components:
- Security Lists and Security Rules
- Route Table and Route Rules
- DRG Route Table and DRG Route Rules

1. Modify your excel sheet to update required data in the Tabs - RouteRulesInOCI, SecRulesInOCI, DRGRouteRulesInOCI tabs. <br>
<br>
2. Execute the _setupOCI.py_ file with _workflow_type_ parameter value to _create_resources_:
   ```python setUpOCI.py /cd3user/tenancies/<customer_name>/<customer_name>_setUpOCI.properties``` <br>
<br>   
4. Choose _'Network'_ from the displayed menu. Choose below sub-options:
   - Security Rules
      <br> - Add/Modify/Delete Security Rules (Reads SecRulesinOCI sheet)
   - Route Rules
      <br> - Add/Modify/Delete Route Rules (Reads RouteRulesinOCI sheet)
   - DRG Route Rules
      <br> - Add/Modify/Delete DRG Route Rules (Reads DRGRouteRulesinOCI sheet)

   Once the execution is successful, _<customer\_name>\_seclists.auto.tfvars_, _<customer\_name>\_routetables.auto.tfvars_ and _<customer\_name>\_drg-routetables.auto.tfvars_ file will be generated under the folder ```/cd3user/tenancies/<customer_name>/terraform_files/<region_dir>.``` Existing files will move into respective backup folders.

!!! note 
      This will create TF for only those Security Lists and Route Tables in VCNs which are part of cd3 and skip any VCNs that have been created outside of cd3 execution.

```
Navigate to the above path and execute the terraform commands:

       terraform init
       terraform plan
       terraform apply
```

   This completes the modification of Security Rules, Route Rules and DRG Route Rules in OCI. Verify the components in console.<br>

### Sync manual changes done in OCI of Security Rules, Route Rules and DRG Route Rules with CD3 Excel Sheet and Terraform
Follow the below process to export the rules to the same CD3 Excel Sheet as the one used to Create Network, and to sync the Terraform files with OCI whenever an user adds, modifies or deletes rules in OCI Console manually.

!!! note 
      Make sure to close your Excel sheet during the export process.
                       
1. Execute the _setupOCI.py_ file with _workflow_type_ parameter value to _create_resources_: <br>
   ```python setUpOCI.py /cd3user/tenancies/<customer_name>/<customer_name>_setUpOCI.properties``` <br>
   <br>
2. Choose _'Network'_ from the displayed menu. Choose below sub-options:
   - Security Rules
      <br> -Export Security Rules (From OCI into SecRulesinOCI sheet)
   - Route Rules
      <br> -Export Route Rules (From OCI into RouteRulesinOCI sheet)
   - DRG Route Rules
      <br> -Export DRG Route Rules (From OCI into DRGRouteRulesinOCI sheet)
 
    Once the execution is successful, 'RouteRulesInOCI', 'SecRulesInOCI', 'DRGRouteRulesInOCI' tabs of the excel sheet will be updated with the rules exported from OCI. At this point, we only have our Excel sheet Tabs updated, proceed to the next step to create the Terraform Files for the same.
 
3. Choose _'Network'_ from the displayed menu. Choose below sub-options:
   - Security Rules
      <br> -Add/Modify/Delete Security Rules (Reads SecRulesinOCI sheet)
   - Route Rules
      <br> - Add/Modify/Delete Route Rules (Reads RouteRulesinOCI sheet)
   - DRG Route Rules
      <br> - Add/Modify/Delete DRG Route Rules (Reads DRGRouteRulesinOCI sheet)

   Once the execution is successful, ```<customer_name>_seclists.auto.tfvars,  <customer_name>_routetables.auto.tfvars and  <customer_name>drg-routetables.auto.tfvars``` file will be generated under the folder ```/cd3user/tenancies/<customer_name>/terraform_files/<region_dir>/<service_dir>```
    
   Navigate to the above path and execute the terraform commands:<br>
       <br>_terraform init_
       <br>_terraform plan_
       <br>_terraform apply_
   
   This completes the export of Security Rules, Route Rules and DRG Route Rules from OCI. Terraform plan/apply should be in sync with OCI.
    

### Add/Modify/Delete NSGs
Follow the below steps to update NSGs.

1.  Modify your excel sheet to update required data in the Tabs - NSGs. <br>
   <br>
2. Execute the _setupOCI.py_ file with _workflow_type_ parameter value to _create_resources_:
   ```python setUpOCI.py /cd3user/tenancies/<customer_name>/<customer_name>_setUpOCI.properties``` <br>
   <br>
3. Choose _'Network'_ from the displayed menu. Choose below sub-option:
   - Network Security Groups
      <br> -Add/Modify/Delete NSGs (Reads NSGs sheet)
    
     Once the execution is successful,  ```<customer_name>_nsgs.auto.tfvars``` will be generated under the folder ```/cd3user/tenancies/<customer_name>/terraform_files/<region_dir>/<service_dir>```. Existing files will move into respective backup folders.
    
4. Navigate to the above path and execute the terraform commands:<br>
       <br>_terraform init_
       <br>_terraform plan_
       <br>_terraform apply_
   
This completes the modification of NSGs in OCI. Verify the components in console.


### Add/Modify/Delete VLANs
Follow the below steps to update VLANs.

1.  Modify your excel sheet to update required data in the Tabs - SubnetsVLANs. <br>
<br>
2.  Make sure that the RouteRulesinOCI sheet and corresponing terraform is in synch with route rules in OCI console. If not, please follow procedure specified in [Sync manual changes done in OCI of Security Rules, Route Rules and DRG Route Rules with CD3 Excel Sheet and Terraform](#sync-manual-changes-done-in-oci-of-security-rules-route-rules-and-drg-route-rules-with-cd3-excel-sheet-and-terraform) <br>
<br>   
3. Execute the _setupOCI.py_ file with _workflow_type_ parameter value to _create_resources_: <br>
   ```python setUpOCI.py /cd3user/tenancies/<customer_name>/<customer_name>_setUpOCI.properties``` <br>
<br>   
4. Choose _'Network'_ from the displayed menu. Choose below sub-option: <br>
   >- Add/Modify/Delete VLANs (Reads SubnetsVLANs sheet)
    
      >Once the execution is successful, ```<customer_name>\_vlans.auto.tfvars``` will be generated under the folder   ```/cd3user/tenancies/<customer_name>/terraform_files/<region_dir>/<service_dir>.``` Existing files will move into respective backup folders.```<customer_name>_routetables.auto.tfvars``` file will also be updated with the route table information specified for each VLAN.
    
5. Navigate to the above path and execute the terraform commands:<br>
       <br>_terraform init_
       <br>_terraform plan_
       <br>_terraform apply_   <br>
<br>
6.  Again make sure to export the Route Rules in OCI into excel and terraform. Please follow procedure specified in [Sync manual changes done in OCI of Security Rules, Route Rules and DRG Route Rules with CD3 Excel Sheet and Terraform](#sync-manual-changes-done-in-oci-of-security-rules-route-rules-and-drg-route-rules-with-cd3-excel-sheet-and-terraform) 

This completes the modification of VLANs in OCI. Verify the components in console.

### RPCs
Remote VCN peering is the process of connecting two VCNs in different regions (but the same tenancy). The peering allows the VCNs' resources to communicate using private IP addresses without routing the traffic over the internet or through your on-premises network.
 
   - Modify your excel sheet to update required data in the Tabs - DRGs.
   - The source and target RPC details to be entered in DRG sheet for establishing a connection. Please check the example in excel file for reference.
   - Make sure that the DRGRouteRulesinOCI sheet and corresponding to terraform is in synch with DRG route rules in OCI console. If not, please follow procedure specified in [Sync manual changes done in OCI of Security Rules, Route Rules and DRG Route Rules with CD3 Excel Sheet and Terraform](#sync-manual-changes-done-in-oci-of-security-rules-route-rules-and-drg-route-rules-with-cd3-excel-sheet-and-terraform)
   - Global directory which is inside the customer outdir will have all RPC related files and scripts.
   - The RPC resources(modules,provider configurations etc) are generated dynamically for the tenancy and can work along only with CD3 automation toolkit.
   - Choose option 'Network' and then 'Customer Connectivity' for creating RPC in GreenField workflow.
   - Output files are created under ```/cd3user/tenancies/<customer_name>/terraform_files/global/rpc``` directory


<br><br>
<div align='center'>  
</div>