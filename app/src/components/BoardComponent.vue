<template>
  <div :class="{'game-container': true, 'active': active}">
    <div
        class="cell"
        v-for="(cell, cellIndex) in cells"
        :key="`cell_${cellIndex}`">
      <div
          class="cell-content"
          @click="emitClick(cellIndex)">
        <span v-if="cell === 1">✗</span>
        <span v-if="cell === 2">○</span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">

import {defineComponent} from "vue";

export default defineComponent({
  props: {
    cells: {
      type: Array,
      required: true
    },
    active: {
      type: Boolean,
      required: true
    }
  },
  methods: {
    /**
     * Emits a click event with the cell index.
     * @param cellIndex
     */
    emitClick(cellIndex: number) {
      if (!this.active)
        return;
      this.$emit('cellClick', cellIndex);
    }
  }
})
</script>

<style lang="scss" scoped>
div.game-container {
  --border-width: 5px;
  --border-color: #2d2d2d;

  display: grid;
  grid-template-columns: repeat(3, 1fr);
  margin-left: auto;
  margin-right: auto;
  border: var(--border-width) solid var(--border-color);
  border-radius: var(--border-radius);
  overflow: hidden;
  transition: all .5s;

  &:not(.active) {
    opacity: 0.15;
    transform: scale(0.95);

    div.cell {
      &:hover {
        cursor: not-allowed;
      }
    }
  }

  &.active {
    div.cell {
      cursor: pointer;

      &:hover {
        background-color: rgba(255, 255, 255, 0.05);
      }
    }
  }

  div.cell {
    aspect-ratio: 1;
    border-bottom: var(--border-width) solid var(--border-color);
    border-right: var(--border-width) solid var(--border-color);
    overflow: hidden;
    transition: all .1s;

    &:nth-last-of-type(-n+3) {
      border-bottom: none;
    }

    &:nth-of-type(3n) {
      border-right: none;
    }

    div.cell-content {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100%;
      font-size: 2rem;
      font-weight: bold;
      color: #fff;
    }
  }
}
</style>