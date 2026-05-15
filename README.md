# Mqam (Digital) Audio Transmission System

## Project Overview
This project implements a complete digital communication chain using GNU Radio Companion. The system facilitates the transmission of analog audio (WAV) over a simulated AWGN channel using various MQAM modulation schemes.

A primary component of this project is the development of custom Embedded Python Blocks to handle non-linear speech coding via the mu-law algorithm.

## Technical Features
* Custom Python Blocks: Implementation of mu-law compression, 8-bit quantization, and expansion.
* Modulation Support: BPSK, QPSK, 8-PSK, and 16-QAM.
* Signal Processing: Root Raised Cosine (RRC) filtering and Polyphase symbol synchronization.
* Performance Analysis: Real-time monitoring of constellation diagrams and Symbol Error Rate (SER).

## Technologies Used
* GNU Radio Companion (GRC)
* Python 3
* Digital Signal Processing (DSP) Principles

## Repository Structure
* audio_transmission_system.grc: The main flowgraph.
* mu_law_encoder.py: Python block for mu-law companding.
* mu_law_decoder.py: Python block for mu-law decoding.

---
Developed by Danai Chalkidou as part of the Digital Communications course.
