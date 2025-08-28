CREATE TABLE IF NOT EXISTS Layout1
(

    Name TEXT PRIMARY KEY,
    Age REAL,
    Average_Fraud TEXT,
    Total_Fraud TEXT
);

INSERT INTO Layout1
    (Name, Age, Average_Fraud, Total_Fraud)
VALUES
    ('Albert', 22, 'USD 200', 'USD 30,000'),
    ('Lucas', 19, 'USD 570', 'USD 55,000'),
    ('Timothy', 28, 'USD 17,000', 'USD 250,000'),
    ('Cyril', 24, 'USD 27,000', 'USD 170,000')
,

SELECT *FROM Layout1