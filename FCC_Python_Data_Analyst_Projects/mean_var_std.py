import numpy as np

def calculate(list):
    calculations = {}
    if len(list) < 9 or len(list) > 9:
      raise ValueError("List must contain nine numbers.")
    else:
      list_numpy = np.array(list) # turns list into numpy array
      list_array = list_numpy.reshape(3, 3) # reshapes list into numpy matrix
      axis0_stat = np.mean(list_array[:, 0])
      axis1_stat = np.mean(list_array[:, 1])
      axis2_stat = np.mean(list_array[:, -1])
      axis0 = np.mean(list_array[0])
      axis1 = np.mean(list_array[1])
      axis2 = np.mean(list_array[-1])
      flattened_stat = np.mean(list) # how do I flatten it
      axis0_var = np.var(list_array[:, 0])
      axis1_var = np.var(list_array[:, 1])
      axis2_var = np.var(list_array[:, -1])
      axis0var = np.var(list_array[0])
      axis1var = np.var(list_array[1])
      axis2var = np.var(list_array[-1])
      flattened_var = np.var(list)
      axis0_std = np.std(list_array[:, 0])
      axis1_std = np.std(list_array[:, 1])
      axis2_std = np.std(list_array[:, -1])
      axis0std = np.std(list_array[0])
      axis1std = np.std(list_array[1])
      axis2std = np.std(list_array[-1])
      flattened_std = np.std(list)
      axis0_max = np.max(list_array[:, 0])
      axis1_max = np.max(list_array[:, 1])
      axis2_max = np.max(list_array[:, -1])
      axis0max = np.max(list_array[0])
      axis1max = np.max(list_array[1])
      axis2max = np.max(list_array[-1])
      flattened_max = np.max(list)
      axis0_min = np.min(list_array[:, 0])
      axis1_min = np.min(list_array[:, 1])
      axis2_min = np.min(list_array[:, -1])
      axis0min = np.min(list_array[0])
      axis1min = np.min(list_array[1])
      axis2min = np.min(list_array[-1])
      flattened_min = np.min(list)
      axis0_sum = np.sum(list_array[:, 0])
      axis1_sum = np.sum(list_array[:, 1])
      axis2_sum = np.sum(list_array[:, -1])
      axis0sum = np.sum(list_array[0])
      axis1sum = np.sum(list_array[1])
      axis2sum = np.sum(list_array[-1])
      flattened_sum = np.sum(list)
      calculations['mean'] = [[axis0_stat, axis1_stat, axis2_stat], [axis0, axis1, axis2], flattened_stat]
      calculations['variance'] = [[axis0_var, axis1_var, axis2_var], [axis0var, axis1var, axis2var], flattened_var]
      calculations['stdandard deviation'] = [[axis0_std, axis1_std, axis2_std], [axis0std, axis1std, axis2std], flattened_std]
      calculations['max'] = [[axis0_max, axis1_max, axis2_max], [axis0max, axis1max, axis2max], flattened_max]
      calculations['min'] = [[axis0_min, axis1_min, axis2_min], [axis0min, axis1min, axis2min], flattened_min]
      calculations['sum'] = [[axis0_sum, axis1_sum, axis2_sum], [axis0sum, axis1sum, axis2sum], flattened_sum]


    return calculations

stat_var_std = [2,6,2,8,4,0,1,5,7]
print(calculate(stat_var_std))

