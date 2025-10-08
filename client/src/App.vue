<script setup>
import Chart from "./components/Charts.vue";
import Chat from "./components/Chat.vue";
const message = "LLM Chat Summarizer";

</script>

<template>
  <div class="container">

    <div class="row">
      <div class="col">
        <h1>{{ message }}</h1>
      </div>
    </div>

    <hr />

    <div class="row">
      <div class="col-lg-6">
        <Chat />
      </div>
      <div class="col-lg-6">
        <Chart />
      </div>
    </div>

    <hr />
  </div>
</template>

