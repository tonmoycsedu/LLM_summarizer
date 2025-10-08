<template>
  <div ref="chart"></div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import * as d3 from "d3";

const chart = ref(null);
const data = ref([])

onMounted(async() => {
  drawChart();
});

function drawChart(data) {
  const width = 600;
  const height = 300;
  const padding = 28;
  const margin = { top: 20, right: 20, bottom: 30, left: 40 };

  const svg = d3.select(chart.value)
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .attr("viewBox", [-padding, 0, width, height]);

  svg.append("g")
      .style("font", "bold 20px sans-serif")
      .style("pointer-events", "none")
    .selectAll("text")
    .data(["Your visual summary should go here"])
    .join("text")
      // .attr("transform", (d, i) => `translate(${i * size},${i * size})`)
      .attr("x", padding)
      .attr("y", padding)
      .attr("dy", ".71em")
      .text(d => d);
}
</script>

<style scoped>
svg {
  font-family: sans-serif;
}
</style>
