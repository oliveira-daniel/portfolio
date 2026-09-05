<script setup lang="ts">
import { computed } from 'vue'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, BarElement, CategoryScale, LinearScale, Tooltip } from 'chart.js'

ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip)

const props = defineProps<{ counts: Record<string, number> }>()

const labels = computed(() => Object.keys(props.counts).sort())
const data = computed(() => ({
  labels: labels.value,
  datasets: [{
    data: labels.value.map((l) => props.counts[l]),
    backgroundColor: ['#518E45', '#F1CA30', '#20372F', '#6bcf5a'],
    borderRadius: 8,
  }],
}))

const options = {
  responsive: true,
  plugins: { legend: { display: false } },
  scales: {
    x: { grid: { display: false } },
    y: { beginAtZero: true, ticks: { stepSize: 1 } },
  },
}
</script>

<template>
  <div class="glass rounded-2xl p-4 max-w-md">
    <Bar :data="data" :options="options" />
  </div>
</template>