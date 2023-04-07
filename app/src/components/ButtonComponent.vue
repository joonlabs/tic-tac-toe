<template>
  <button>
    <slot/>
  </button>
</template>

<script lang="ts">
import {defineComponent} from "vue";

export default defineComponent({
})
</script>

<style lang="scss" scoped>
button {
  outline: none;
  background: var(--color-accent);
  border-radius: var(--border-radius);
  border: none;
  padding: .85rem 1.9rem;
  font-size: .95rem;
  color: white;
  font-weight: bold;
  cursor: pointer;

  &:active {
    transform: scale(.975);
  }
}
</style>