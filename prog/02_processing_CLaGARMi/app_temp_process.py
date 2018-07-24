# this script
# processes monthly means for the CORDEX input data
# processes monthly means for the total length of the IMAGE data
# processes monthly means for each of the 30-year ensembles of IMAGE data

from prog.functions.data.process_clag_stats_functions import *
import sys

# get total number of arguments
total = len(sys.argv)

# get the arguments list
cmdargs = str(sys.argv)

# variables for processing CLaGARMi output
slice = sys.argv[1]                             # slice = '01'
years_sim = int(float((sys.argv[2])))           # years_sim = 4000
continent = sys.argv[3]                         # continent = 'euro'
scen = sys.argv[4]                              # scen = 'hist'
year_start = int(float((sys.argv[5])))          # year_start = 1971
year_end = int(float((sys.argv[6])))            # year_end = 2000
#
# # loading data for both observations and simulations
# tas_obs_data,  tas_sim_data = load_clag_output(slice, years_sim, continent, scen, year_start, year_end, 'tasmax')
# wind_obs_data, wind_sim_data = load_clag_output(slice, years_sim, continent, scen, year_start, year_end, 'sfcWindmax')
#
# windchill_obs_data = wind_chill_creator(tas_obs_data, wind_obs_data)
#
# # output to merged obs and sim values to csv
# obs_sim_data_processed.to_csv('~/git/IMAGE/output/CLaGARMi/' + continent + '_cordex/figures_processing/' + metric + '_' + continent + '_' + scen + '_' + str(year_start) + '_' + str(year_end) + '_' + str(years_sim) + 'yrs_' + '_obs_sim_merged.csv')
# sim_data_processed_ens.to_csv('~/git/IMAGE/output/CLaGARMi/' + continent + '_cordex/figures_processing/' + metric + '_' + continent + '_' + scen + '_' + str(year_start) + '_' + str(year_end) + '_' + str(years_sim) + 'yrs_' + '_sim_ens.csv')