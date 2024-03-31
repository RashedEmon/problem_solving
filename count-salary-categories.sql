SELECT
    COALESCE(main.category, hardcoded_table.category) AS category,
    COALESCE(accounts_count, 0) AS accounts_count
FROM (
    SELECT category, count(*) AS accounts_count
    FROM (
        SELECT
            account_id,
            income,
            CASE
                WHEN income > 50000 THEN 'High Salary'
                WHEN income >= 20000 AND income <= 50000 THEN 'Average Salary'
                ELSE 'Low Salary'
            END AS category
        FROM Accounts
    ) AS combined
    GROUP BY category
) AS main
RIGHT JOIN (
    SELECT
        category,
        salary
    FROM
    (
        VALUES
            ('High Salary', 0),
            ('Average Salary', 0),
            ('Low Salary', 0)
    ) AS hardcoded_table (category, salary)
) AS hardcoded_table ON main.category = hardcoded_table.category;
