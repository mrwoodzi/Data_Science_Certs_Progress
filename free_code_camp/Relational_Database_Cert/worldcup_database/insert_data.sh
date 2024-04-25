# Do not change code above this line. Use the PSQL variable above to query your database.
echo $($PSQL "TRUNCATE teams, games;")
cat games.csv | while IFS="," read  YEAR ROUND WINNER OPPONENT WINNER_GOALS OPPONENT_GOALS
do 
  # check if 'year' is == to YEAR
  if [[ $YEAR != 'year' ]]
  then # inserting all data from games.csv into respective tables
    #Get the WINNER_ID ID None Make NEW Winner ID
    WINNER_NAME=$($PSQL "SELECT team_id FROM teams WHERE name='$WINNER';")
    #If no WINNER_ID is found insert new winner into winners table
    if [[ -z $WINNER_NAME ]]
    then
      INSERT_WINNER=$($PSQL "INSERT INTO teams(name) VALUES('$WINNER')")
      #echo $WINNER Inserted
    fi
    WINNER_NAME=$($PSQL "SELECT team_id FROM teams WHERE name='$WINNER';")
    fi


    if [[ $OPPONENT != 'opponent' ]]
    then
    # Get Opponent ID and if None Make new Opponent ID
      OPPONENT_NAME=$($PSQL "SELECT team_id FROM teams WHERE name='$OPPONENT';")
      #IF opponent_id not found
      if [[ -z $OPPONENT_NAME ]]
        then
        #INSERT OPPONENT
        INSERT_OPPONENT=$($PSQL "INSERT INTO teams(name) VALUES('$OPPONENT')")
        #echo $OPPONENT Inserted
      fi
      #Getting NEW Opponent_ID
    OPPONENT_NAME=$($PSQL "SELECT team_id FROM teams WHERE name='$OPPONENT';")

    # Get winner_id
    WINNER_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$WINNER_NAME';")
    # Get opponent_id
    OPPONENT_ID=$($PSQL "SELECT team_id FROM teams WHERE name='$OPPONENT_NAME';")
    #INSERT data into games table
    INSERT_GAMES=$($PSQL "INSERT INTO games(year, round, winner_id, opponent_id, winner_goals, opponent_goals) VALUES('$YEAR', '$ROUND', '$WINNER_NAME', '$OPPONENT_NAME', '$WINNER_GOALS', '$OPPONENT_GOALS')")
  fi
done