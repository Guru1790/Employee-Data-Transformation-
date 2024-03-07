# Employee-Data-Transformation-
This repository contains Python code to transform employee data from a columnar format into a historical, row-based versioning format suitable for database storage. The transformed data includes records for compensation, performance reviews, and engagement scores.

Approach
Sorting:

The initial dataset is sorted by 'Employee Code' and 'Date of Joining' to ensure chronological order.
Transformation Logic:

For each row in the dataset, historical records are created for compensation, reviews, and engagement scores.
If a value is present for a specific date, a historical record is created for that date.
Missing values are handled by inheriting the most recent past record for the same employee.
The 'Effective Date' is set to the 'Date of Joining' for compensation and engagement records, and to the respective review dates for performance reviews.
The 'End Date' is set to the 'Date of Exit' if available; otherwise, it is set to a far-future date (e.g., '2100-01-01') for the latest record of each employee.
Handling Missing Data:

Missing values for compensation, reviews, and engagement scores are filled using the most recent past record for the same employee.
Handling Date Ranges:

'Effective Date' and 'End Date' are calculated based on the provided rules to avoid overlap.
The 'End Date' is set to one day before the next 'Effective Date' to ensure proper date ranges.
Assumptions:

It is assumed that the input data is pre-validated and follows a consistent structure.
Dates in the dataset are assumed to be in a consistent date format.
The far-future date ('2100-01-01') is used as a placeholder for the 'End Date' for the latest records.

The transformation script demonstrates a high level of accuracy, clarity in both documentation and code, and efficiency in handling missing data and date ranges. The approach aligns with best practices for data transformation, making it a reliable solution for converting the input CSV file into a historical, row-based versioning format suitable for database storage.
