# StashDataPull

The Account Statement PDF from Stash does not come well formatted.
To make use of specific data held in each month's report, the file needs
to be converted into a csv or tsv file. After this is done, the file is formatted
and adjusted to make the data useable. This includes the cutting of pages that
hold no data, or irrelevant data.

From here the resulting csv and tsv can be used in SQL to form a database where
an algorithm may be applied for multiple purpouses.

Tasks completed:
-CSV conversion
-Data parsing and cutting
-Formatted CSV

To Do:
-Integrate SQL database
-VBA interface(?)
-Predictive algorithm