<template>
    <div class="card p-4 shadow-sm">
      <div class="mb-3">
        <label for="inputText" class="form-label">What do you want to chat about?</label>
        <input
          id="inputText"
          v-model="inputText"
          class="form-control"
          placeholder="Type something..."
        />
      </div>

      <div class="d-flex gap-2">
        <button class="btn btn-success" @click="sendData">
          <i class="bi bi-arrow-right"></i>
        </button>
      </div>

      <div class="mt-4">
        <h5>Response:</h5>
        <p class="border rounded p-3 bg-light">{{ reply }}</p>
      </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const reply = ref('')
const inputText = ref('')

async function sendData() {
  const res = await fetch('http://localhost:5001/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: inputText.value })
  })
  const data = await res.json()
  reply.value = JSON.stringify(data["message"])
}
</script>
