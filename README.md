## Day 1 - From Raw data to Evoked Responses

### 1. Working with Raw data Objects
 - [] Lecture: What is EEG and MEG?
 - [x] Raw Class: loading, plotting, info
 - [x] Selecting data: copying, picking, cropping
 - [x] Loading data from different formats
 - [x] Creating a RawArray from Scratch

 ### 2. Filtering Raw Data
 - [x] Lecture: Fourier transform and the frequency domain
 - [x] Filtering data to remove artifacts and plotting PSD
 - [x] Filter parameter2s and transfer functions
 - [x] Common filterin artifacts, time-frequency tradeoffs
 - [x]: Putting it together: filter a new dataset

 ### 3. Epoching Event-Related Data
 - [] Lecture: Evoked reponse potentials and their components
 - [x] Workign with events: extracting from stimulus channel, merging events
 - [x] Epoching raw data and visualizing ERPs
 - [x] Topoplots and re-rereferencing
 - [x] Removing bad epochs, autoreject

 ### 4. Statistical Comparison of ERPs
 - [] #Lecture: Null hypothesis and the multiple comparisons problem
 - [] Comparing evoked responses (difference topography)
 - [] Statistical comparison: 1-way F-test
 - [] Correting for Multiple Comparisons
 - [] Permutation cluster test

## Day 2. Source Separation in Space and Time. 

### 5. Simulating Data with a Forward Model
- [] Lecture:  source-vs sensor space, forward model, volume conductance
- [x] Selecting and visualizing sources in the brain
- [x] Simulate source activity using a forward model
- [x] Adding noise and artifacts for realism
- [] Putting it together: Simulate data from a source at a specific location

### 6. Dimensionality Reduction and Source Separation

- [] Lecture: ?
- ?

### 7. Time-Frequency Analysis with Wavelets
- [] Lecture: Wavelet convolution
  

### 8. Phase-based Connectivity Analysis

- [] Lecture: What is a phase time series?

## Day 3. Encoding Decoding Models

### 9. Linear Regression and Regularization

- [] Lecture: Regression as matrix multiplication
- [x] OLS regression with one and multiple features
- [x] Regularization to improve predictions
- [] Cross validation for optimization
- [x] Demo: Colinearity

### 10. Regression for Time-Series Data

- [] Lecture: Intro to time-lagged regression

### 11. Modeling Neural Responses to Naturalistics Speech

- [] Lecture Encoding/Decoding models for EEG and speech
- [] Predicting neural responses from different speech features and visualizing weights (exporting to MNE)
- [] Decoding selective attention in cocktail party task
- [] Segmentation and Cross-validation
- [] Musall Lab: Demo on applying encoding models to wide-field imaging data

### 12. Significance Testing and Variance Partitioning

- [] Lecture: Causality vs. Correlation
- [] Permutation based significance testing
- [] Nested cross-validation
- [] Model comparison with feature shuffling
- [] Variance partitioning


