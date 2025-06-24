<script setup>
import Card from './Card.vue'
import Task from './Task.vue'
import { ref, onMounted } from 'vue';

const tasks = ref([]);

async function fetchTasks() {
  try {
    const res = await fetch(
      `${import.meta.env.VITE_API_URL}/tasks/`
    )
    if (!res.ok) throw new Error(res.statusText);
    tasks.value = await res.json();
  } catch (e) {
    console.log(e)
  }
}

onMounted(async () => {
  fetchTasks();
  intervalId = setInterval(fetchTasks, 2_000);
})

function addTaskBtnClick () {
  alert('Coming soon...')
}

function updateTask(task) {
  const i = tasks.value.findIndex(e => e.pk === task.pk)
  if (i !== -1) {
    tasks.value[i] = task;
  }
}
</script>

<template>
  <div class="tasks-container">
    <Task v-for="task in tasks" :key="task" :task="task" :updateTask="updateTask" />
    <Card @click="addTaskBtnClick">+</Card>
  </div>
</template>

<style scoped>
.tasks-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: stretch;

  padding: 12px 72px;
  gap: 8px;
}
</style>
