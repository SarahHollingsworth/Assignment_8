## CONTENTS

* Introduction
* Description
* Requirements
* Installation
* Credits
* License

### INTRODUCTION
* The purpose of this module is to take a function provided by the instructor and identify how to apply the function with the groupby method to a data set provided by the instructor.  
* After running this module, the user will be able to identify how to apply functions to a data set using the groupby method.  This includes:
   * Using groupby to apply a function to a data set with calculations for quantitative data
   * Using groupby to apply a function to a data set with calculations for qualitative data

### DESCRIPTION

* This module allows the user to use attributes of the pandas library to explore the data set.

1. Import the pandas library
   * Using the import statement will allow the user to access all functions and attributes of the pandas library. A nickname is also applied to allow the user to call pandas functions and attributes without having to write the full name of the library.
2. Create the homegames dataframe
   * The homegames dataframe is created using the pandas read_csv function to upload the data set into the homegames_df variable. 
3. Create the parks dataframe
   * The parks dataframe is created using the pandas read_csv function to upload the data set into the parks_df variable.
4. Merge the two dataframes
   * A new combined_df variable is created using the pandas library, the merge function is called on the “left” dataframe homegames_df.  It takes the arguments for the “right” dataframe and “on” parameters.  The “right” dataframe parameter is assigned with the parks_df variable, the left_on variable is assigned with the ‘park.key’ variable from the homegames_df and the right_on variable is assigned with the ‘park.key’ variable from the parks_df.
5. Apply the fillna function with the fill forward method
   * The missing values are replaced by calling the fillna function from the pandas library on the combined_df variable.  The fill forward method replaces values by replacing the next missing value with the last known value and if any of the columns starts with a missing value these will not be replaced.  The fillna function takes an argument for method, which is assigned with the ‘ffill’ variable.  The combined_df variable is assigned with the new values which are filled forward from the last known value.
6. Apply the fillna function with the fill backward method
   * The fill backward method replaces values by replacing the missing value with the newest value. The fillna function from the pandas library is called on the combined_df variable.  The fillna function takes an argument for method, which is assigned with the ‘bfill’ variable.  The combined_df variable is assigned with the new values which are filled backward from the last known value.
7. Apply the rename function
   * Using the rename function will allow the user to rename the columns of the combined_df dataframe to remove any periods from our column names.  The rename function takes a dictionary which includes the old column name and the new column name.  
8. Create the summarize_data function
   * The summarize_data function passes one argument into the function, ‘x’. 
   *  The return statement returns a Panda series which performs the below calculations:
      * The column ‘avg_games’ is created, the pandas function mean is called on the ‘team’ column and returns the calculated mean for each league.
      * The column ‘min_games’ is created, the pandas function min is called on the ‘team’ column and returns the calculated minimum for each league.
      * The column ‘max_games’ is created, the pandas function max is called on the ‘team’ column and returns the calculated maximum for each league.  
      * The column ‘std_dev_games’ is created, the pandas function std is called on the ‘team’ column and returns the calculated standard deviation for each league.  
      * The column ‘1st_quartile’ is created, the pandas function quantile is called on the ‘team’ column, the variable q is assigned with the value 0.25 and passed into the quantile function.  Returning the calculated first quartile for each league.
      * The column ‘2nd_quartile’ is created, the pandas function quantile is called on the ‘team’ column, the variable q is assigned with the value 0.50 and passed into the quantile function.  Returning the calculated second quartile for each league.
      * The column ‘3rd_quartile’ is created, the pandas function quantile is called on the ‘team’ column, the variable q is assigned with the value 0.75 and passed into the quantile function.  Returning the calculated third quartile for each league.
      * The column ‘sample_count’ is created, the pandas function len is called on the variable ‘x’ and returns the count of observations for each league.
      * The column ‘proportion’ is created and the proportion of observations assigned.  This is done by dividing the values returned by first calling the pandas function count on the ‘team’ column grouped by league with the value returned by calling the pandas function count on the ‘combined_df’ counting all observations of the column.
9. Use the groupby method to apply the summarize_data function
   * Using the groupby method, the ‘league’ column is passed in as the argument by which we want to group our results.  The apply function is then used to apply the summarize_data function to our combined_df dataframe.  This will return the results of our function in the form of a Panda Series.
10. Update the summarize_data function
    * We update the summarize_data function to perform calculations on string data.
    * The summarize_data function passes one argument into the function, ‘x’. 
    * The return statement returns a Panda series which performs the below calculations:
       * The column ‘sample_count’ is created, the pandas function count is called on the ‘park_name’ column and returns the count of observations for each league.
       * The column 'park_name (first alpha)' is created, the pandas function min is called on the ‘park_name’ column and returns the alphabetically first value.
       * The column 'park_name (last alpha)' is created, the pandas function max is called on the ‘park_name’ column and returns the alphabetically last value.
       * The column ‘proportion’ is created and the proportion of observations assigned.  This is done by dividing the values returned by first calling the pandas function count on the ‘team’ column grouped by league with the value returned by calling the pandas function count on the ‘combined_df’ counting all observations of the column.
11. Use the groupby method to apply the summarize_data function
    * Using the groupby method, the ‘league’ column is passed in as the argument by which we want to group our results.  The apply function is then used to apply the summarize_data function to our combined_df dataframe.  This will return the results of our function in the form of a Panda Series.

### REQUIREMENTS

* This module requires the pandas library.

### INSTALLATION

* This module requires no installation.

### CREDITS

* This module has no credits.

### LICENSE

* This module has no license.
