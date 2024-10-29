# tissue_data.py

tissue_list = [
    "AIR", "BRAIN", "FAT", "HEART", "KIDNEY", "LUNG", "MUSCLE", "BONE",
    "SKIN", "TENDON", "TUMOR", "LSO", "TOP", "UNDEF"
]
# Comment out if all tissues are needed
tissue_list = [
    "SKIN"
]

# Define tissue properties (Density and Anisotropy)
tissue_properties_2 = {
    "AIR":    {"density": 0.0        ,  "anisotropy": 0.0,   "refractive_index": 1.0},
    "BRAIN":  {"density": 0.947384674,  "anisotropy": 0.9,   "refractive_index": 1.33},
    "FAT":    {"density": 1.0        ,  "anisotropy": 0.9,   "refractive_index": 1.33},
    "HEART":  {"density": 0.873847566,  "anisotropy": 0.9,   "refractive_index": 1.33},
    "KIDNEY": {"density": 0.915925965,  "anisotropy": 0.9,   "refractive_index": 1.33},
    "LUNG":   {"density": 0.919293730,  "anisotropy": 0.9,   "refractive_index": 1.33},
    "MUSCLE": {"density": 0.914010849,  "anisotropy": 0.9,   "refractive_index": 1.33},
    "BONE":   {"density": 0.941679476,  "anisotropy": 0.9,   "refractive_index": 1.33},
    "SKIN":   {"density": 0.980770079,  "anisotropy": 0.9,   "refractive_index": 1.45},
    "TENDON": {"density": 0.975501448,  "anisotropy": 0.9,   "refractive_index": 1.33},
    "TUMOR":  {"density": 0.914010849,  "anisotropy": 0.9,   "refractive_index": 1.33},
    "LSO":    {"density": 0.761966035,  "anisotropy": 0.624, "refractive_index": 1.82},
    "TOP":    {"density": 0.0        ,  "anisotropy": 0.9,   "refractive_index": 1.33},
    "UNDEF":  {"density": 0.914010849,  "anisotropy": 0.0,   "refractive_index": 1.33}
}


tissue_properties = {
    "AIR": {"density": 0.0, "anisotropy": 0.0, "refractive_index": 1.0},
    "BRAIN": {"density": 0.6096, "anisotropy": 0.9, "refractive_index": 1.33},
    "FAT": {"density": 0.0941, "anisotropy": 0.9, "refractive_index": 1.33},
    "HEART": {"density": 2.3221, "anisotropy": 0.9, "refractive_index": 1.33},
    "KIDNEY": {"density": 0.9483, "anisotropy": 0.9, "refractive_index": 1.33},
    "LUNG": {"density": 1.1389, "anisotropy": 0.9, "refractive_index": 1.33},
    "MUSCLE": {"density": 1.3434, "anisotropy": 0.9, "refractive_index": 1.33},
    "BONE": {"density": 0.5194, "anisotropy": 0.9, "refractive_index": 1.33},
    "SKIN": {"density":  0.2271, "anisotropy": 0.9, "refractive_index": 1.45},
    "TENDON": {"density":0.2164, "anisotropy": 0.9, "refractive_index": 1.33},
    "TUMOR": {"density":1.3434, "anisotropy": 0.9, "refractive_index": 1.33, "emission": 1.0},
    "LSO": {"density": 0.048, "anisotropy": 0.624, "refractive_index": 1.82},
    "TOP": {"density":  0. , "anisotropy": 0.9, "refractive_index": 1.33},
    "UNDEF": {"density": 1.0, "anisotropy": 0.0, "refractive_index": 1.33}
}
tissue_properties = {
    "SKIN": {"density": 0.1, "anisotropy": 0.9, "refractive_index": 1.45}
}

meshes = {
    "caliper-xfm-2-fluorescent-mouse-phantom": "SKIN",
    "01-skin-128": "SKIN",
    "02-masseter-muscle-L-24": "MUSCLE",
    "03-masseter-muscle-R-24": "MUSCLE",
    "04-lacrimal-gland-L-16": "MUSCLE",  # Closest match: Muscle
    "05-lacrimal-gland-R-16": "MUSCLE",  # Closest match: Muscle
    "06-eye-L-8": "BRAIN",  # Closest match: Brain (nervous tissue)
    "07-eye-R-8": "BRAIN",  # Closest match: Brain (nervous tissue)
    "08-brain-misc-48": "BRAIN",
    "09-brain-cerebrum-48": "BRAIN",
    "10-brain-olfactory-bulb-24": "BRAIN",
    "11-brain-striatum-32": "BRAIN",
    "12-brain-medulla-32": "BRAIN",
    "13-brain-cerebellum-32": "BRAIN",
    "14-liver-64": "FAT",  # Closest match: FAT (soft tissue)
    "15-lung-64": "LUNG",
    "16-heart-24": "HEART",
    "17-stomach-32": "FAT",  # Closest match: FAT (smooth muscle tissue)
    "18-pancreas-32": "FAT",  #
    "19-spleen-32": "FAT",  # Closest match: FAT (soft tissue)
    "20-adrenal-gland-L-8": "FAT",  # Closest match: FAT (soft tissue)
    "21-adrenal-gland-R-8": "FAT",  # Closest match: FAT (soft tissue)
    "22-kidney-L-24": "KIDNEY",
    "23-kidney-R-24": "KIDNEY",
    "24-bladder-16": "AIR",  # Closest match: AIR if empty (smooth muscle tissue)
    "25-testis-L-16": "MUSCLE",  # Closest match: Muscle (soft tissue)
    "26-testis-R-16": "MUSCLE",  # Closest match: Muscle (soft tissue)
    "27-skeleton-head-128": "BONE",
    "28-skeleton-ribs-and-spine-156": "BONE",
    "29-skeleton-upper-extremity-L-128": "BONE",
    "30-skeleton-upper-extremity-R-128": "BONE",
    "31-skeleton-lower-extremities-128": "BONE"
}

