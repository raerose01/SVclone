import numpy as np

# PREPROCESSING PARAMETERS
tr      = 5    # threshold by how much read has to overlap breakpoint
window  = 500  # base-pairs considered to the left and right of the break

# parameters extracted for each read from BAMs
read_dtype = [('query_name', 'S150'), ('chrom', 'S50'), ('ref_start', int), ('ref_end', int), \
              ('align_start', int), ('align_end', int), ('len', int), ('ins_len', int), ('is_reverse', np.bool)]

# PHYL constant parameters
subclone_threshold      = 0.05 # throw out any subclones with frequency lower than this value
subclone_sv_prop        = 0.10 # remove any cluster groups with fewer than this proportion of SVs clustering together
subclone_diff           = 0.10 # merge any clusters within this range
init_iters              = 100000 # inital clustering mcmc iterations
reclus_iters            = 50000 # reclustering iterations
burn                    = 5000 # burn-in period
thin                    = 10 # thinning parameter for sampling
