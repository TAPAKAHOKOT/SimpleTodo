<template>
  <div class="card">
    <slot></slot>
  </div>
</template>

<style scoped>
  .card {
    background-color: #7277D8;
    color: #f5f5f5;
    border-radius: 8px;
    padding: 8px;

    width: fit-content;
    box-shadow: 4px 4px black;
    transition: box-shadow .2s ease-in-out;

    min-width: 32px;
    min-height: 32px;
    box-sizing: border-box;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    &:hover {
      box-shadow: 2px 2px black;
      cursor: pointer;
    }
  }
</style>
