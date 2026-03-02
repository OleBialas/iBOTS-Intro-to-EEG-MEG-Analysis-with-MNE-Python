from pathlib import Path
import mne
import numpy as np

root = Path(__file__).parent
N_EPOCHS = 100

raw_fname = mne.datasets.eegbci.load_data(subjects=1, runs=[6])[0]
raw = mne.io.read_raw_edf(raw_fname, preload=True)
montage = mne.channels.make_standard_montage("standard_1005")
mne.datasets.eegbci.standardize(raw)
raw.set_montage(montage)
fs_dir = mne.datasets.fetch_fsaverage(verbose=True)
src = fs_dir / "bem" / "fsaverage-ico-5-src.fif"
bem = fs_dir / "bem" / "fsaverage-5120-5120-5120-bem-sol.fif"
fwd = mne.make_forward_solution(
    raw.info,
    trans="fsaverage",
    src=src,
    bem=bem,
    meg=False,
    eeg=True,
    mindist=5.0,
    n_jobs=None,
)
raw.info["dev_head_t"] = fwd["info"]["dev_head_t"]

labels = mne.read_labels_from_annot(
    "fsaverage", parc="aparc", subjects_dir=fs_dir.parent
)
label_names = ["transversetemporal-lh", "parsopercularis-lh"]
labels = [l for l in labels if l.name in label_names]

times = np.arange(0, 1, 1 / raw.info["sfreq"])
stc_a1 = mne.simulation.simulate_sparse_stc(
    fwd["src"],
    n_dipoles=1,
    times=times,
    labels=[labels[1]],
    location="center",
    data_fun=lambda t: 0.1e-7 * np.sin(2 * np.pi * 8 * t),
)
stc_broca = mne.simulation.simulate_sparse_stc(
    fwd["src"],
    n_dipoles=1,
    times=times,
    labels=[labels[0]],
    location="center",
    data_fun=lambda t: 0.1e-7 * np.sin(2 * np.pi * 8 * t - np.pi / 4),
)


# Get all vertices from both STCs
all_vertices = [
    np.union1d(stc_a1.vertices[0], stc_broca.vertices[0]),  # left hemi
    np.union1d(stc_a1.vertices[1], stc_broca.vertices[1]),  # right hemi
]

# Expand both to have the same vertices
stc_a1_expanded = stc_a1.expand(all_vertices)
stc_broca_expanded = stc_broca.expand(all_vertices)

# Now you can add them
stc = stc_a1_expanded + stc_broca_expanded

raw_sim = mne.simulation.simulate_raw(
    raw.info, [stc] * N_EPOCHS, forward=fwd, verbose=False
)


cov = mne.make_ad_hoc_cov(raw_sim.info)
mne.simulation.add_noise(raw_sim, cov, iir_filter=[0.2, -0.2, 0.04])

n_samples_per_epoch = len(stc.times)
events = np.array([[i * n_samples_per_epoch, 0, 1] for i in range(N_EPOCHS)])
epochs = mne.epochs.Epochs(
    raw_sim, events, tmin=-1, tmax=2, baseline=None, preload=True
)

stc.save(root / "sim", overwrite=True)
epochs.save(root / "sim-epo.fif", overwrite=True)
