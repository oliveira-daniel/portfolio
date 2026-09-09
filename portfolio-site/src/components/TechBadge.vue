<script setup lang="ts">
import { computed } from 'vue'

export type BadgePath = { d: string; fillRule?: string }

const props = withDefaults(
  defineProps<{
    path?: string
    paths?: BadgePath[]
    viewBox?: string
    hex?: string
    label: string
  }>(),
  { viewBox: '0 0 24 24' },
)

const color = computed(() => (props.hex ? `#${props.hex}` : '#518E45'))

const allPaths = computed<BadgePath[]>(() => {
  if (props.paths?.length) return props.paths
  if (props.path) return [{ d: props.path }]
  return []
})
</script>

<template>
  <span
    class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full glass text-xs font-medium text-brand-dark/80"
    :title="label"
  >
    <svg
      v-if="allPaths.length"
      :viewBox="viewBox"
      class="h-4 w-auto max-w-12 shrink-0"
      fill="currentColor"
      :style="{ color }"
    >
      <path v-for="(p, i) in allPaths" :key="i" :d="p.d" :fill-rule="p.fillRule ?? undefined" />
    </svg>
    <span>{{ label }}</span>
  </span>
</template>
