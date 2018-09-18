"""
SiEPIC Photonics Package

Author:     Mustafa Hammood
            Mustafa@ece.ubc.ca

Module:     Core functionalities of SiEPIC PP

functions:

calibrate( input_response, reference_response): response correction function to calibrate an input response with respect to a reference response
baseline_correction( input_response ): baseline correction function to flatten a response with respect to it self
cutback( input_data_response, input_data_count):
to_s_params( input_data ):
download_response (url, port): downloads input .mat response from a url and parses it into array
"""

from SiEPIC_Photonics_Package.setup import *

#%% calibration function
def calibrate( input_response, reference_response):
    print("called")
    return

#%% baseline_correction function
# input list format: input_response[wavelength (nm), power (dBm)]
# output list format: [power (dBm) with baseline correction, baseline correction fit]
def baseline_correction( input_response ):
    fitOrder = 4
    wavelength = input_response[0]
    power = input_response[1]
    
    pfit = numpy.polyfit(wavelength-numpy.mean(wavelength), power, fitOrder)
    power_baseline = numpy.polyval(pfit, wavelength-numpy.mean(wavelength))
    
    power_corrected = power - power_baseline
    power_corrected = power_corrected + max(power_baseline) -max(power)
    
    return [power_corrected, power_baseline]

#%% cutback function
def cutback( input_data_response, input_data_count):
    return

#%% to_s_params function
def to_s_params( input_data ):
    return

#%% download_response function
# download input .mat url data
# outputs parsed data array [wavelength (m), power (dBm)]
# data is assumed to be from automated measurement scanResult format
def download_response ( url, port):
    r = requests.get(url,allow_redirects=True)
    file_name = 'downloaded_data'+str(port)
    with open(file_name, 'wb') as f:
        f.write(r.content)
        
    data = scipy.io.loadmat(file_name)

    wavelength = data['scanResults'][0][port][0][:,0]
    power = data['scanResults'][0][port][0][:,1]
    data = [wavelength,power]
    return data