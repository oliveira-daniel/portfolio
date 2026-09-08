<script setup lang="ts">
import { computed, ref, onMounted } from 'vue'
import { Doughnut } from 'vue-chartjs'
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import ChartDataLabels from 'chartjs-plugin-datalabels'

ChartJS.register(ArcElement, Tooltip, Legend, ChartDataLabels)

const props = defineProps<{
  title: string
  labels: string[]
  values: number[]
  colors: string[]
}>()

const data = computed(() => ({
  labels: props.labels,
  datasets: [
    {
      data: props.values,
      backgroundColor: props.colors,
      borderWidth: 2,
      borderColor: '#20372F',
      hoverOffset: 6,
    },
  ],
}))

const isDark = ref(false)
onMounted(() => {
  const update = () => (isDark.value = document.documentElement.classList.contains('dark'))
  update()
  new MutationObserver(update).observe(document.documentElement, { attributes: true, attributeFilter: ['class'] })
})

const options = computed(() => ({
  responsive: true,
  cutout: '62%',
  plugins: {
    legend: {
      position: 'bottom' as const,
      labels: {
        usePointStyle: true,
        pointStyle: 'circle',
        padding: 14,
        font: { size: 11 },
        color: isDark.value ? '#e5e7eb' : '#20372F',
      },
    },
    tooltip: {
      callbacks: {
        label: (ctx: any) => ` ${ctx.label}: ${ctx.parsed}`,
      },
    },
    datalabels: { display: false },
  },
}))
</script>

<template>
  <div class="rounded-2xl border border-brand-green/15 overflow-hidden bg-white/40 backdrop-blur-sm dark:bg-white/[0.04] dark:border-white/10 p-4 flex flex-col items-center">
    <h3 class="font-bold text-brand-dark text-sm mb-2 text-center flex items-center justify-center gap-2 flex-wrap">
      {{ title }}
      <span class="badge badge-yellow">{{ values.reduce((a, b) => a + b, 0) }}</span>
    </h3>
    <div class="w-full max-w-[260px]">
      <Doughnut :data="data" :options="(options as any)" />
    </div>
  </div>
</template>
