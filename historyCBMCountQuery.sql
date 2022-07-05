WITH filteredset
AS (
SELECT number, timestamp, TIMESTAMP_DIFF(timestamp, LAG(timestamp) over (order by timestamp), SECOND) AS blockInterval
FROM bigquery-public-data.crypto_bitcoin.blocks
)
SELECT * from filteredset WHERE blockInterval > 7200 ORDER BY timestamp
