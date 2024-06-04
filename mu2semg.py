#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:27:33 2024

@author: root
"""

from MU import MotorUnit
from sEMG import SurfaceEMG


if __name__=='__main__':
    simulation_time=10 # s
    ramp=[2, 6, 2] # s
    sampling_rate=2048 # Hz
    maximum_excitation_level=50
    signal_to_noise_ratio= float('inf')
    signal_amplitude_offset=0
    number_of_motor_units=100
    recruitment_range=30
    excitatory_gain=3
    minimum_firing_rate=2 
    peak_firing_rate_first_unit=35
    peak_firing_rate_difference=10
    inter_spike_interval_coefficient_variation=0.20
    conduction_velocity_min_value=4.0
    conduction_velocity_max_value=4.5
    twitch_force_range=100
    motor_unit_density=20
    smallest_motor_unit_number_of_fibres=20
    largest_motor_unit_number_of_fibres=2000
    muscle_fibre_diameter=46e-3
    muscle_cross_sectional_diameter=15 
    maximum_number_of_motor_units=200
    motor_unit_depth = 10
    electrodes_in_z=14
    electrodes_in_x=9
    
    ### Create a SurfaceEMG object.
    surface_emg = SurfaceEMG(simulation_time, ramp, sampling_rate, maximum_excitation_level, signal_to_noise_ratio, signal_amplitude_offset, number_of_motor_units, recruitment_range, 
                             excitatory_gain, minimum_firing_rate, peak_firing_rate_first_unit, peak_firing_rate_difference, inter_spike_interval_coefficient_variation, 
                             conduction_velocity_min_value, conduction_velocity_max_value, twitch_force_range, motor_unit_density, smallest_motor_unit_number_of_fibres, 
                             largest_motor_unit_number_of_fibres, muscle_fibre_diameter, muscle_cross_sectional_diameter, maximum_number_of_motor_units, motor_unit_depth, 
                             electrodes_in_z, electrodes_in_x)

    # Simulate the motor unit recruitment firing pattern. -> MUSTs
    spikes = surface_emg.simulate_recruitment_model()
    
    # Plot the motor unit recruitment firing pattern.  
    y_limit_minimum=-1
    y_limit_maximum=1
    simulations=[]
    time_start=0
    time_end=10
    amplitude_start=-20
    amplitude_end=60
    surface_emg.init_plot_parameters(y_limit_minimum, y_limit_maximum, simulations, time_start, time_end, amplitude_start, amplitude_end)
    surface_emg.plot_recruitment_model()
    
    # Simulate the surface EMG signal.
    muaps, emg=surface_emg.caculate_surface_emg()
    emg_with_noise = surface_emg.simulate_surface_emg()
    
    # Plot the surface EMG signal only for first electrode in the array.
    
    # Plot the surface EMG signal for electrode's array.
    surface_emg.plot_suface_emg_array_no_noise()
    
    surface_emg.plot_muap_array()
    
    # ### Create a SaveData object
    # save_data = SaveData()
    
    # # Save the saved motor unit data to a file.
    # motot_unit_data = MotorUnit().simulate_motor_unit()
    # save_data.save_output_data(motot_unit_data, 'simulate_motor_unit')
    
    # # Load the saved motor unit data from a file.
    # motor_unit_data = save_data.open_and_load_saved_data('simulate_motor_unit.npy')
    
    # # Plot the saved motor unit data.
    # save_data.plot_saved_motor_unit(motor_unit_data)
    
    # # Save the surface EMG signal to a file.
    # surface_emg_data = surface_emg.simulate_surface_emg()
    # save_data.save_output_data(surface_emg_data, 'simulate_surface_emg')
    
    # # Load the saved surface EMG signal data to a file.
    # semg_data = save_data.open_and_load_saved_data('simulate_surface_emg.npy')
    
    # # Plot the saved surface EMG signal data.
    # save_data.plot_saved_surface_emg_array(semg_data)
