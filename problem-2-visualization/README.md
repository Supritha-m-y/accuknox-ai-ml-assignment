# Problem 2 - Data Processing and Visualization

## Overview

This project retrieves student examination scores from a public REST API, processes the data using Python, calculates the average score for each student, and visualizes the results using a bar chart.

## API

API endpoint:

https://sainformatics.org/data/exams.json

The API contains examination information including participants and their scores.

## Assumption

For this problem, I selected the `intensive_2_exam_3_2026` examination.

Each participant has scores for multiple problems. I calculated the average score for each student by taking the mean of their available problem scores.

## Technologies Used

- Python
- Requests
- Matplotlib

## Processing

1. Retrieve JSON data from the API.
2. Select the required examination.
3. Extract participant scores.
4. Calculate the average score for each student.
5. Create a bar chart showing the average score for each student.

## Output

The program prints the calculated average score for every student and generates:

`student_average_scores.png`
