#!/usr/bin/env python
# * coding: utf8 *
'''
pallet.py
A module that contains the pallet for daily sgid data
'''
from os import path

import arcpy
from forklift import core
from forklift.models import Pallet


class SgidDailyPallet(Pallet):
    def __init__(self):
        super(SgidDailyPallet, self).__init__()
        self.destination_coordinate_system = 26912
        self.geographic_transformation = None
    
    def build(self, target):

        self.sgid = path.join(self.garage, 'SGID10.sde')
        self.cloud_port = r'C:\CloudPort'

        self.bioscience = path.join(self.cloud_port, 'bioscience.gdb')
        self.boundaries = path.join(self.cloud_port, 'boundaries.gdb')
        self.cadastre = path.join(self.cloud_port, 'cadastre.gdb')
        self.economy = path.join(self.cloud_port, 'economy.gdb')
        self.energy = path.join(self.cloud_port, 'energy.gdb')
        self.environment = path.join(self.cloud_port, 'environment.gdb')
        self.geoscience = path.join(self.cloud_port, 'geoscience.gdb')
        self.history = path.join(self.cloud_port, 'history.gdb')
        self.location = path.join(self.cloud_port, 'location.gdb')
        self.recreation = path.join(self.cloud_port, 'recreation.gdb')
        
        self.copy_data = [self.bioscience,
                          self.boundaries,
                          self.cadastre,
                          self.economy,
                          self.energy,
                          self.environment,
                          self.geoscience,
                          self.history,
                          self.location,
                          self.recreation]

        self.add_crates([
            'BeaverRestorationAssessment'],
        {'source_workspace': self.sgid,
        'destination_workspace': self.bioscience})

        self.add_crates([
            'Municipalities',
            'Municipalities_Carto',
            'Municipalities_Modifications'],
        {'source_workspace': self.sgid,
        'destination_workspace': self.boundaries})

        self.add_crates([
            'LandOwnership'],
        {'source_workspace': self.sgid,
        'destination_workspace': self.cadastre})

        self.add_crates([
            'EnterpriseZones'],
        {'source_workspace': self.sgid,
        'destination_workspace': self.economy})

        self.add_crates([
            'OilGasWells',
            'OilGasWells_DownHoles',
            'OilGasWells_Paths'],
        {'source_workspace': self.sgid,
        'destination_workspace': self.energy})

        self.add_crates([
            'BFNONTARGETED',
            'BFTARGETED',
            'DAQAirEmissionsInventory',
            'DWMRCHazWasteUsedOilFacilities',
            'DWMRCLLRWUMillFacilities',
            'DWMRCSolidWasteFacilities',
            'DWQAssessmentUnits',
            'DWQGroundWaterPermits',
            'DWQMonitoredLakes132',
            'EWA',
            'FACILITYUST',
            'FUD',
            'ICBUFFERZONES',
            'LakeMonitoring',
            'MMRP',
            'NPL',
            'SITEREM',
            'StreamMonitorSites',
            'TIER2',
            'TRI',
            'UPDESSites',
            'VCP'],
        {'source_workspace': self.sgid,
        'destination_workspace': self.environment})

        self.add_crates([
            'GeologicFormationsLine'],
        {'source_workspace': self.sgid,
        'destination_workspace': self.geoscience})

        self.add_crates([
            'ArchaeologySites'],
        {'source_workspace': self.sgid,
        'destination_workspace': self.history})

        self.add_crates([
            'Buildings',
            'PlaceNamesGNIS2010'],
        {'source_workspace': self.sgid,
        'destination_workspace': self.location})

        self.add_crates([
            'Trails'],
        {'source_workspace': self.sgid,
        'destination_workspace': self.recreation})

