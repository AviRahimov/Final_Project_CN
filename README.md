# WhatsApp Web Packet Analysis (Final Project in Communication Networks)

Welcome to the WhatsApp Web Packet Analysis project repository! This repository contains code and resources for analyzing packets from WhatsApp web group messages. The project involves sniffing packets, identifying message-related packets, and generating helpful plots to facilitate packet identification. The analysis is conducted in two distinct parts: one involving packet filtering, and the other simulating real-world noise with YouTube music playing in the background.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Packet Analysis](#packet-analysis)
  - [Part 1: With Filtering](#part-1-with-filtering)
  - [Part 2: Without Filtering and Background Music](#part-2-without-filtering-and-background-music)
- [Plots](#plots)
- [Resources](#resources)
- [Source Code](#source-code)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The goal of the WhatsApp Web Packet Analysis project is to dissect and interpret packets generated by WhatsApp web group messages. By applying various analysis techniques and filtering methods, the project aims to identify packets that correspond to sent messages. Visualization plots are employed to assist in the identification process.

## Project Structure

The project is organized into three main directories:

- `res`: This directory houses the plots generated during the analysis, including plots depicting functions of time as functions of packet size, PDF (probability density function) plots, and CCDF (Complementary CDF) plots.
- `resources`: This directory contains eight pcapng files and, eight CSV files, with four corresponding to filtered packets and four to unfiltered packets. These resources serve as the basis for the analysis.
- `src`: Within this directory, you'll find four Python files. Each file contains code for a different type of plot: the CCDF plot, the PDF plot, and the time as a function of the size plot.

## Packet Analysis

### Part 1: With Filtering

In this phase, the packet analysis is conducted while applying a filter specifically targeting `tcp.port 443`. This filtering helps reduce noise and concentrate on the most pertinent packets. The focus is on isolating the packets associated with the sent messages and creating visualization plots to aid in their identification.

### Part 2: Without Filtering and Background Music

The second phase of the analysis is conducted without any packet filtering, and it introduces a realistic element of background noise. The simulated background noise is akin to having YouTube music playing in the background. The objective here is to assess real-world noise's impact on packet analysis accuracy.

## Plots

The `res` directory hosts a variety of plots that provide valuable insights into the packet analysis process:

- **Functions of Time vs. Packet Size**: These plots showcase the relationship between time and packet size, shedding light on trends and patterns.
- **PDF (Probability Density Function) Plots**: PDF plots graphically represent the probability distribution of packet sizes. Separate plots are generated for each packet, totaling eight plots (four filtered and four unfiltered).
- **CCDF (Complementary CDF) Plots**: CCDF plots illustrate the complementary cumulative distribution function of packet sizes. CCDF plots are generated for the four filtered packets.

## Resources

The `resources` directory encompasses the raw materials necessary for the analysis, consisting of eight CSV files representing both filtered and unfiltered packets.

## Source Code

The `src` directory contains the Python code required for generating different types of plots. The four Python files are dedicated to the CCDF plot, the PDF plots, and the time as a function of the size plot.

## Contributing

Contributions to the project are greatly appreciated! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Implement your changes and commit them: `git commit -m 'Add some feature'`.
4. Push your changes to the branch: `git push origin feature-name`.
5. Open a pull request describing your changes.

Please adhere to the project's coding standards and guidelines.

Thank you for your interest in the WhatsApp Web Packet Analysis project!
