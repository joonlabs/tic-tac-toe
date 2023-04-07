<template>
  <div class="app-container">
    <main>

      <div class="header">
        <h1>Tic Tac Toe</h1>

        <div :class="{'message-holder': true, 'active': winner !== null}">
          <h2 v-if="winner === 0">Draw! 🤝🏽</h2>
          <h2 v-else-if="winner === 1">🤖 wins!</h2>
          <h2 v-else-if="winner === 2">You win! 🎉</h2>
          <h2 v-else>Let's gooooo...</h2>
        </div>
      </div>

      <GameComponent :cells="cells" :active="!isGameOver && initiated" @cell-click="cellClick"/>

      <div class="button-holder" v-if="isGameOver || !initiated">
        <ButtonComponent @click="restartGame(2)">🙋🏽‍♂️ Begins</ButtonComponent>
        <ButtonComponent @click="restartGame(1)">🤖 Begins</ButtonComponent>
      </div>
    </main>
  </div>
</template>

<script lang="ts">
import {defineComponent} from "vue";
import GameComponent from "@/components/BoardComponent.vue";
import ButtonComponent from "@/components/ButtonComponent.vue";
import * as tf from '@tensorflow/tfjs';
import type {LayersModel} from "@tensorflow/tfjs";


export default defineComponent({
  components: {
    ButtonComponent,
    GameComponent
  },
  data() {
    return {
      cells: Array(9).fill(0),
      winner: null as number | null,
      initiated: false,
      model: null as object | null
    }
  },
  methods: {
    /**
     * Handles a cell click.
     * @param cellIndex
     */
    async cellClick(cellIndex: number) {
      // check if the cell is empty
      if (this.cells[cellIndex] === 0) {
        // make the player's move
        this.cells[cellIndex] = 2;

        if(!this.isGameOver)
          // make the computer's move
          this.cells[await this.getComputerMove()] = 1;
      }
    },

    /**
     * Gets the computer's move.
     */
    async getComputerMove() {
      // load the model
      // @ts-ignore
      let model = window.tfModel as LayersModel | undefined;
      if(!model) {
        // @ts-ignore
        window.tfModel = model = await tf.loadLayersModel('./model/model.json');
      }

      // predict the next move
      const prediction = await model.predict(
          [tf.tensor([this.cells])],
          {
            batchSize: 1,
            verbose: true
          }) as tf.Tensor;
      const predictionArray = await prediction.dataSync() as Float32Array;

      // get the empty cells
      const emptyCells = this.cells.map((cell, index) => cell === 0 ? index : null).filter(cell => cell !== null);

      // choose the best available move
      let foundBestValidMove = false;
      let bestMove = 0;
      while(!foundBestValidMove){
        // get the best move from the prediction
        bestMove = predictionArray.indexOf(Math.max(...predictionArray));

        // check if the best move is valid
        if(emptyCells.includes(bestMove)){
          foundBestValidMove = true
        } else {
          // remove the best move from the prediction
          predictionArray[bestMove] = 0
        }
      }

      return bestMove!
    },

    /**
     * Restarts the game.
     */
    async restartGame(player: number) {
      this.cells = Array(9).fill(0)
      this.winner = null
      this.initiated = true

      if (player === 1)
        this.cells[await this.getComputerMove()] = 1
    }
  },
  computed: {
    /**
     * Checks if the game is over.
     */
    isGameOver(): boolean {
      // check if there is a row or column with the same value
      for (let i = 0; i < 3; i++) {
        if (this.cells[i] !== 0 && this.cells[i] === this.cells[i + 3] && this.cells[i] === this.cells[i + 6]) {
          this.winner = this.cells[i]
          return true;
        }
        if (this.cells[i * 3] !== 0 && this.cells[i * 3] === this.cells[i * 3 + 1] && this.cells[i * 3] === this.cells[i * 3 + 2]) {
          this.winner = this.cells[i * 3]
          return true;
        }
      }

      // check if there is a diagonal with the same value
      if (this.cells[0] !== 0 && this.cells[0] === this.cells[4] && this.cells[0] === this.cells[8]) {
        this.winner = this.cells[0]
        return true;
      }
      if (this.cells[2] !== 0 && this.cells[2] === this.cells[4] && this.cells[2] === this.cells[6]) {
        this.winner = this.cells[2]
        return true;
      }

      // check if there are no empty cells
      if (this.cells.every(cell => cell !== 0)) {
        this.winner = 0;
        return true;
      }

      return false;
    }
  }
});
</script>

<style lang="scss" scoped>
div.app-container {
  padding: min(5vh, 3rem);
  width: 400px;
  max-width: 100%;
  margin: auto;
  text-align: center;

  div.header {
    margin-bottom: 2rem;

    div.message-holder {
      margin-top: 1rem;
      background: rgba(255, 255, 255, .1);
      border-radius: var(--border-radius);
      max-height: 0;
      padding: 0;
      transition: all 1s;
      overflow: hidden;

      &.active {
        max-height: 100px;
        padding: .05rem .5rem;
      }

    }
  }

  div.button-holder {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 1rem;
    margin-top: 3rem;
  }
}
</style>