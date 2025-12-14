# Multi-Agent System for University Query Resolution

## Project Overview
This project implements a Multi-Agent System (MAS) designed to resolve university-related queries. It utilizes a text-based retrieval system where user queries are matched against a knowledge base using Cosine Similarity. The system identifies the most relevant agent to handle a specific request based on predefined intent categories.

## Project Details
* **Course:** Knowledge Representation and Reasoning (KRR)
* **Class:** BSAI-5A
* **Instructor:** Mr. Adil Sheraz

## Team Members
| Name | Roll Number |
| :--- | :--- |
| **Muhammad Maaz Akram** | 231192 |
| **Muhammad Umar** | 231200 |

## Technical Specifications
* **Language:** Python 3.14.0
* **Similarity Metric:** Cosine Similarity
* **Key Libraries:** `utils` (for similarity calculation), `numpy` (if applicable for vector handling)

## How It Works
1.  **Input Processing:** The system accepts a natural language query from the user.
2.  **Vectorization:** The query and the predefined agent competencies are converted into vector representations.
3.  **Similarity Matching:** The system calculates the Cosine Similarity between the user query and agent descriptions using the `utils` library.
4.  **Agent Selection:** The agent with the highest similarity score is selected to respond to the query.

## Setup and Usage
1.  Ensure Python 3.14.0 is installed.
2.  Install necessary dependencies.
3.  Run the main script to initiate the query resolution process.