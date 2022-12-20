#!/usr/bin/env python3
"""
"""
import re
import operator
from collections import defaultdict
import pandas as pd
from pyparsing import col

def get_all_animal_ids(animal_string):
    """
    Converts a string that contains the ID of animals, and only gets the IDs. 
    This usually removes extra characters that were added. (i.e. "1.1 v 2.2" to ("1.1", "2.2"))

    Args:
        animal_string(str): This is the first param.

    Returns:
        tuple: Of IDs of animals as strings
    """
    # Splitting by space so that we have a list of just the words
    all_words = animal_string.split()
    # Removing all words that are not numbers
    all_numbers = [num for num in all_words if re.match(r'^-?\d+(?:\.\d+)$', num)]
    return tuple(all_numbers)

def add_session_number_column(dataframe, indexes, session_number_column="session_number"):
    """
    Add a column to Pandas DataFrame that contains the session number. 
    This will only add session numbers to the rows specified by indexes. 
    You can fill in the empty cells with method: DataFrame.fillna(method='ffill')
    
    Args:
        dataframe(Pandas DataFrame): The DataFrame to add the session number column
        indexes(list): List of indexes for which rows to add the session numbers
        session_number_column(str): Name of the column to add
        
    Returns:
        Pandas DataFrame: DataFrame with the session numbers added
    """
    # Using a copy so that original is not changed
    copy_dataframe = dataframe.copy()
    session_number = 1
    for index in indexes:
        # Changing the session number one cell at a time where the index is
        copy_dataframe.at[index, session_number_column] = session_number
        session_number += 1
    return copy_dataframe

def update_elo_rating(winner_id, loser_id, id_to_elo_rating=None, default_elo_rating=1000, \
    winner_score=1, loser_score=0, **calculate_elo_rating_params):
    """
    Updates the Elo rating in a dictionary that contains the ID of the subject as keys, 
    and the Elo rating as the values. You can also adjust how the Elo rating is calculated with 'calculate_elo_rating_params'.
    
    Args:
        winner_id(str): ID of the winner
        loser_id(str): ID of the loser
        id_to_elo_rating(dict): Dict that has the ID of the subjects as keys to the Elo Score as values
        default_elo_rating(int): The default Elo rating to be used if there is not elo score for the specified ID
        **calculate_elo_rating_params(kwargs): Other params for the calculate_elo_rating to change how the Elo rating is calculated
        
    Returns:
        Dict: Dict that has the ID of the subjects as keys to the Elo Score as values
    """
    if id_to_elo_rating is None:
        id_to_elo_rating = defaultdict(lambda:default_elo_rating)
    
    # Getting the current Elo Score
    current_winner_rating = id_to_elo_rating[winner_id] 
    current_loser_rating = id_to_elo_rating[loser_id] 
    
    # Calculating Elo rating            
    id_to_elo_rating[winner_id] = calculate_elo_rating(subject_elo_rating=current_winner_rating, \
        agent_elo_rating=current_loser_rating, score=winner_score, **calculate_elo_rating_params)
    id_to_elo_rating[loser_id] = calculate_elo_rating(subject_elo_rating=current_loser_rating, \
        agent_elo_rating=current_winner_rating, score=loser_score, **calculate_elo_rating_params)

    return id_to_elo_rating

def get_ranking_from_elo_rating_dictionary(input_dict, subject_id):
    """
    Orders a dictionary of subject ID keys to ELO score values by ELO score. 
    And then gets the rank of the subject with the inputted ID.
    Lower ranks like 1 would represent those subjects with higher ELO scores and vice versa.

    Args:
        input_dict(dict): 
            Dictionary of subject ID keys to ELO score values
        subject_id(str, int, or any value that's a key in input dict): 
            The ID of the subject that you want the ranking of

    Returns:
        int:
            Ranking of the subject with the ID inputted
    """
    # Sorting the subject ID's by ELO score
    sorted_subject_to_elo_rating = sorted(input_dict.items(), key=operator.itemgetter(1), reverse=True)
    # Getting the rank of the subject based on ELO score
    return [subject_tuple[0] for subject_tuple in sorted_subject_to_elo_rating].index(subject_id) + 1