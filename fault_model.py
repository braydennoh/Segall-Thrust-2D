import numpy as np

def gaussian_slip(x, amp, mean, std):
    return amp * np.exp(-((x - mean)**2) / (2 * std**2))

def calculate_uplift_from_slip(x_obs, slip, delta, d_start, x_start):
    if d_start == 0:
        arcterm = np.arctan2((x_obs - x_start), 1e-12)
        uplift = -(slip / np.pi) * (np.sin(delta) * arcterm)
    else:
        zeta = (x_obs - x_start) / d_start
        uplift = -(slip / np.pi) * (np.sin(delta) * np.arctan(zeta) +
                                 (np.cos(delta) + zeta * np.sin(delta)) / (1.0 + zeta**2))
    return uplift

def forward_model(params, fault_geom, segment_lengths, cumulative_lengths, x_obs_pts):
    slip_amp, slip_mean, slip_std = params
    uplift_model = np.zeros_like(x_obs_pts)
    N_PHYSICAL_PATCHES = 100
    for i, f_geom in enumerate(fault_geom):
        x1_major, z1_major = f_geom['start']
        x2_major, z2_major = f_geom['end']
        x_points = np.linspace(x1_major, x2_major, N_PHYSICAL_PATCHES + 1)
        z_points = np.linspace(z1_major, z2_major, N_PHYSICAL_PATCHES + 1)
        start_len = cumulative_lengths[i]
        end_len = cumulative_lengths[i+1]
        len_points = np.linspace(start_len, end_len, N_PHYSICAL_PATCHES + 1)
        for j in range(N_PHYSICAL_PATCHES):
            x1_patch, z1_patch = x_points[j], z_points[j]
            x2_patch, z2_patch = x_points[j+1], z_points[j+1]
            mid_len = (len_points[j] + len_points[j+1]) / 2.0
            slip = gaussian_slip(mid_len, slip_amp, slip_mean, slip_std)
            if abs(slip) < 1e-9:
                continue
            delta = np.arctan2(-(z2_patch - z1_patch), x2_patch - x1_patch)
            uplift_top = calculate_uplift_from_slip(x_obs_pts, slip, delta, -z1_patch, x1_patch)
            uplift_bot = calculate_uplift_from_slip(x_obs_pts, -slip, delta, -z2_patch, x2_patch)
            uplift_model += (uplift_top + uplift_bot)
    return uplift_model

def log_prior(params, total_model_fault_length):
    slip_amp, slip_mean, slip_std = params
    if -30 < slip_amp < 30 and 0.0 < slip_mean < total_model_fault_length and 1 < slip_std < 20:
        return 0.0
    return -np.inf

def log_likelihood(params, x, y, yerr, fault_geom, segment_lengths, cumulative_lengths):
    model_y = forward_model(params, fault_geom, segment_lengths, cumulative_lengths, x)
    sigma2 = yerr**2
    return -0.5 * np.sum((y - model_y)**2 / sigma2)

def log_probability(params, x, y, yerr, fault_geom, segment_lengths, cumulative_lengths, total_model_fault_length):
    # Note: total_model_fault_length is added as an argument to be passed here
    lp = log_prior(params, total_model_fault_length)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(params, x, y, yerr, fault_geom, segment_lengths, cumulative_lengths)