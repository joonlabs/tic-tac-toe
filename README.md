# Tic Tac Toe

This repository contains a web based Tic Tac Toe game.
It contains a simple AI trained with Tensorflow that plays against the user.

The AI is a simple neural network that is trained using random moves.
The game is written with Vue3 and Typescript.

A demo is available at https://dev.joonlabs.com/tic-tac-toe/.

## Train the AI

To train the AI, go into the `ai` folder and follow these steps:


1. Generate rnadom training data using `generate_training_data.py`
2. Train the model using `train.py`

This will produce a `model.h5` file (and some files for TensorflowJS) in the `models` folder which contain the trained model.

You can test the model using `try.py` or evaluate it on 1000 games with the `evaluate.py` script.

## Play the game

To play the game, go into the `app` folder and follow these steps:

1. Install the dependencies using `npm install`
2. Copy the TensorflowJS model files from the `ai/models` folder into the `app/public/model` folder.
3. Start the development server using `npm run dev`

## Build the game

To build the game, go into the `app` folder and follow these steps:

1. Install the dependencies using `npm install`
2. Copy the TensorflowJS model files from the `ai/models` folder into the `app/public/model` folder.
3. Build the game using `npm run build`

This will produce a `dist` folder which contains the game.