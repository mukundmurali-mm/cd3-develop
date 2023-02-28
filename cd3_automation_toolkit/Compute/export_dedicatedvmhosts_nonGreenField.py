#!/usr/bin/python3
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.
#
# This script will produce a Terraform file that will be used to export OCI core components
# Export Dedicated VM Hosts Components
#
# Author: Suruchi
# Oracle Consulting
#

import argparse
import oci
import os

from oci.config import DEFAULT_LOCATION
from commonTools import *

importCommands = {}
oci_obj_names = {}


def print_dedicatedvmhosts(region, dedicatedvmhost, values_for_column, ntk_compartment_name):
    dedicatedvmhost_tf_name = commonTools.check_tf_variable(dedicatedvmhost.display_name)
    importCommands[region.lower()].write("\nterraform import \"module.dedicated-hosts[\\\"" +dedicatedvmhost_tf_name+ "\\\"].oci_core_dedicated_vm_host.dedicated_vm_host\" " + str(dedicatedvmhost.id))

    for col_header in values_for_column:
        if col_header == 'Region':
            values_for_column[col_header].append(region)
        elif col_header == 'Compartment Name':
            values_for_column[col_header].append(ntk_compartment_name)
        elif ("Availability Domain" in col_header):
            value = dedicatedvmhost.__getattribute__(sheet_dict[col_header])
            ad = ""
            if ("AD-1" in value or "ad-1" in value):
                ad = "AD1"
            elif ("AD-2" in value or "ad-2" in value):
                ad = "AD2"
            elif ("AD-3" in value or "ad-3" in value):
                ad = "AD3"
            values_for_column[col_header].append(ad)
        elif col_header.lower() in commonTools.tagColumns:
            values_for_column = commonTools.export_tags(dedicatedvmhost, col_header, values_for_column)
        else:
            oci_objs = [dedicatedvmhost]
            values_for_column = commonTools.export_extra_columns(oci_objs, col_header, sheet_dict, values_for_column)


def parse_args():
    # Read the arguments
    parser = argparse.ArgumentParser(description="Export Block Volumes on OCI to CD3")
    parser.add_argument("inputfile", help="path of CD3 excel file to export Block Volume objects to")
    parser.add_argument("outdir", help="path to out directory containing script for TF import commands")
    parser.add_argument("service_dir",help="subdirectory under region directory in case of separate out directory structure")
    parser.add_argument("--config", default=DEFAULT_LOCATION, help="Config file name")
    parser.add_argument("--export-compartments", nargs='*', required=False, help="comma seperated Compartments for which to export Block Volume Objects")
    parser.add_argument("--export-regions", nargs='*', help="comma seperated Regions for which to export Networking Objects",
                        required=False)
    return parser.parse_args()


def export_dedicatedvmhosts(inputfile, _outdir, service_dir, _config, ct, export_compartments=[], export_regions=[]):
    global tf_import_cmd
    global sheet_dict
    global importCommands
    global config
    global cd3file
    global reg
    global outdir
    global values_for_column


    cd3file = inputfile
    if ('.xls' not in cd3file):
        print("\nAcceptable cd3 format: .xlsx")
        exit()


    outdir = _outdir
    configFileName = _config
    config = oci.config.from_file(file_location=configFileName)

    sheetName="DedicatedVMHosts"
    if ct==None:
        ct = commonTools()
        ct.get_subscribedregions(configFileName)
        ct.get_network_compartment_ids(config['tenancy'],"root",configFileName)

    # Read CD3
    df, values_for_column= commonTools.read_cd3(cd3file,sheetName)

    # Get dict for columns from Excel_Columns
    sheet_dict=ct.sheet_dict[sheetName]

    print("\nCD3 excel file should not be opened during export process!!!")
    print("Tabs- DedicatedVMHosts  will be overwritten during export process!!!\n")

    # Create backups
    resource = 'tf_import_' + sheetName.lower()
    file_name = 'tf_import_commands_' + sheetName.lower() + '_nonGF.sh'
    for reg in export_regions:
        script_file = f'{outdir}/{reg}/{service_dir}/'+file_name
        if (os.path.exists(script_file)):
            commonTools.backup_file(outdir + "/" + reg+"/"+service_dir, resource, file_name)
        importCommands[reg] = open(script_file, "w")
        importCommands[reg].write("#!/bin/bash")
        importCommands[reg].write("\n")
        importCommands[reg].write("terraform init")

    # Fetch Block Volume Details
    print("\nFetching details of Dedicated VM Hosts...")

    for reg in export_regions:
        importCommands[reg].write("\n\n######### Writing import for Dedicated VM Hosts #########\n\n")
        config.__setitem__("region", ct.region_dict[reg])
        region = reg.capitalize()

        compute_client = oci.core.ComputeClient(config,retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)

        for ntk_compartment_name in export_compartments:
            dedicatedvmhosts = oci.pagination.list_call_get_all_results(compute_client.list_dedicated_vm_hosts,compartment_id=ct.ntk_compartment_ids[ntk_compartment_name], lifecycle_state="ACTIVE")
            for dedicatedvmhost in dedicatedvmhosts.data:
                dedicatedvmhost=compute_client.get_dedicated_vm_host(dedicatedvmhost.id).data
                print_dedicatedvmhosts(region, dedicatedvmhost,values_for_column, ntk_compartment_name)

    commonTools.write_to_cd3(values_for_column, cd3file, "DedicatedVMHosts")

    print("Dedicated VM Hosts exported to CD3\n")


if __name__ == '__main__':
    args = parse_args()
    # Execution of the code begins here
    export_dedicatedvmhosts(args.inputfile, args.outdir, args.service_dir,args.config, args.export_compartments, args.export_regions)
