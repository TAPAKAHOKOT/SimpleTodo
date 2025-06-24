<script setup>
import Card from './Card.vue'
import { defineProps } from 'vue'

const props = defineProps({
  task: {
    type: Object,
    required: true
  },
  updateTask: {
    type: Function,
    required: true
  }
})

async function setCompletion(task_id, is_completed) {
  const action = is_completed ? 'completed' : 'uncompleted';
  
  try {
    const res = await fetch(
      `${import.meta.env.VITE_API_URL}/tasks/${task_id}/${action}/`,
      {
        method: 'POST',
      }
    )
    if (!res.ok) throw new Error(res.statusText);
    props.updateTask(await res.json())
  } catch (e) {
    console.log(e)
  }
}
</script>

<template>
  <Card>
    <div class="task-header">
        Name: {{ task.title }} ({{ task.pk }})
    </div>
    <ul class="task-body">
      <li>
        <span class="muted-reverse">Priority: </span>{{ task.priority }}
      </li>
      <li v-if="task.repeat_after_seconds">
        <span class="muted-reverse">Repeat in: </span>
        {{ task.repeat_after_seconds }} sec.
      </li>
      <button v-if="task.is_completed" @click="() => setCompletion(task.pk, false)">Uncomplete</button>
      <button v-if="!task.is_completed" @click="() => setCompletion(task.pk, true)">Complete</button>
    </ul>
  </Card>
</template>

<style scoped>
  .task-body {
    padding: 0;
    margin: 0;
    margin-top: 8px;
    list-style: none;

    button {
      border: unset;
      border-radius: 4px;
      box-shadow: 2px 2px black;
      background-color: #f5f5f5;
      margin-top: 8px;
      cursor: pointer;

      transition: box-shadow .2s ease-in-out;

      &:hover {
        box-shadow: 0 0 0 4px black;
      }
    }
  }
</style>
