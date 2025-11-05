def preprocess_ecg(df, fs):
    """
    TODO: bandpass filter, R-peak detection...
    df: pandas DataFrame with columns like ['timestamp','ecg']
    fs: sampling rate (Hz)
    """
    return df  

def extract_hrv_features(df, fs):
    """
    TODO: compute RMSSD, SDNN, MeanNN, LF/HF...
    Return a dict of features.
    """
    return {"RMSSD": None, "SDNN": None, "MeanNN": None, "LF_HF": None}