# This is my solution to the FreeCodeCamp Machine Learning Certification project Rock Paper Scissors.

# Project requirements can be found here : https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors


def player(last_move, history=[], sequences={}):

  # This function plays Rock paper scissors using a Markov chain.
  # The length of the Markov chain is set by the sequence_length variable.

  choices = ['R', 'P', 'S']
  counter = {'R': 'P', 'P': 'S', 'S': 'R'}
  sequence_length = 5

  # First the function defines default start parameters.
  # It also stores the opponent's moves in the history list.

  if not last_move:
    last_move = choices[0]

  history.append(last_move)
  next_move = choices[1]

  # Once enough moves are known, the function starts predicting the opponent's next move.

  if len(history) > sequence_length:

    next_sequence = []
    sequence_frequency = {}

    # First it identifies all sequences equal in length to the Markov chain length and stores them in the sequences dictionary, along with the number of times they appear.

    last_sequence = ''.join(history[-sequence_length:])
    sequences[last_sequence] = sequences.get(last_sequence, 0) + 1

    # Then it calculates each possible sequence that may appear next by taking the last known sequence, removing the most ancient move, and adding each potential new move.

    for choice in choices:
      next_sequence.append("".join([*history[-(sequence_length - 1):],
                                    choice]))

    # If the newly created sequences have appeared previously, they are already stored in the sequences dictionary.
    # The function counts the number of times each has appeared and stores the total in the sequence_frequency dictionary.

    for sequence in next_sequence:
      if sequence in sequences:
        sequence_frequency[sequence] = sequences[sequence]

    # Finally, the function predicts the opponent's next move by taking the sequence with the highest frequency.
    # It then returns the counter to the last move of the sequence.

    if sequence_frequency:
      next_move = max(sequence_frequency, key=sequence_frequency.get)[-1:]

  return counter[next_move]
